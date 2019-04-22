//#ifdef makeAnalysisNtuple_cxx
//#define makeAnalysisNtuple_cxx
#include "makeAnalysisNtuple.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLorentzVector.h>
#include <iostream>
#include <ctime>
#include "TRandom3.h"
#include"PUReweight.h"
#include "METzCalculator.h"
#include "TopEventCombinatorics.h"
#include "JetResolutions.h"
#include"JEC/JECvariation.h"
//#include"OverlapRemove.cpp"
#include <cmath>

using std::cout;
using std::endl;
using std::flush;


std::string mt_PUfilename = "mt_pileupNominal.root";
std::string mt_PUfilename_up = "mt_pileupUp.root"; 
std::string mt_PUfilename_down = "mt_pileupDown.root"; 

int jecvar012_g = 1;   // 0:down, 1:norm, 2:up
int jervar012_g = 1;   // 0:down, 1:norm, 2:up
int muscale012_g = 1;  // 0:down, 1:norm, 2:up
int elesmear012_g = 1; // 0:down, 1:norm, 2:up
int elescale012_g = 1; // 0:down, 1:norm, 2:up

#include "BTagCalibrationStandalone.h"

// No stochastic scaling or smearing for leptons/jets
bool noScaleSmear = false;

bool overlapRemovalTT(EventTree* tree);
bool overlapRemovalWZ(EventTree* tree);
bool overlapRemoval_Tchannel(EventTree* tree);
double getJetResolution(double, double, double);

std::clock_t startClock;
double duration;

ostream& operator<<(ostream& os, const TLorentzVector& v);
ostream& operator<<(ostream& os, const TLorentzVector& v)
{
    os<<"(pt,eta,phi,E) = ("<<v.Pt()<<","<<v.Eta()<<","<<v.Phi()<<","<<v.E()<<")"<<endl;
}


makeAnalysisNtuple::makeAnalysisNtuple(int ac, char** av)
{
	startClock = clock();
	tree = new EventTree(ac-3, av+3);

    sampleType = av[1];
	systematicType = "";
	
	isSystematicRun = false;
    isTTGamma = false;
    mtAnalysis = true;

    if (mtAnalysis)
    {
        TFile* f = new TFile(eleID_SF_path, "read");
        eleID_SF = (TH1F*)f->Get("EGamma_SF2D");
        eleID_SF->SetDirectory(0);
        f->Close();

        f = new TFile(eleReco_SF_path, "read");
        eleReco_SF = (TH1F*)f->Get("EGamma_SF2D");
        eleReco_SF->SetDirectory(0);
        f->Close();

        f = new TFile(muID_BF_SF_path, "read");
        muID_BF_SF = (TH1F*)f->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio");
        muID_BF_SF->SetDirectory(0);
        f->Close();

        f = new TFile(muID_GH_SF_path, "read");
        muID_GH_SF = (TH1F*)f->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio");
        muID_GH_SF->SetDirectory(0);
        f->Close();
     
        f = new TFile(muIso_BF_SF_path, "read");
        muIso_BF_SF = (TH1F*)f->Get("TightISO_TightID_pt_eta/abseta_pt_ratio");
        muIso_BF_SF->SetDirectory(0);
        f->Close();

        f = new TFile(muIso_GH_SF_path, "read");
        muIso_GH_SF = (TH1F*)f->Get("TightISO_TightID_pt_eta/abseta_pt_ratio");
        muIso_GH_SF->SetDirectory(0);
        f->Close();

        f = new TFile(muTrack_SF_path, "read");
        muTrack_SF = (TGraphAsymmErrors*)f->Get("ratio_eff_eta3_dr030e030_corr")->Clone();
        f->Close();

        f = new TFile(trigger_SF_path, "read");
        trigger_SF = (TH1F*)f->Get("SF");
        trigger_SF->SetDirectory(0);
        f->Close();
    }


	size_t pos = sampleType.find("__");
	if (pos != std::string::npos){
		systematicType = sampleType.substr(pos+2,sampleType.length());
		sampleType = sampleType.substr(0,pos);
	}

    cout << sampleType << "  " << systematicType << endl;

	if (std::end(allowedSampleTypes) == std::find(std::begin(allowedSampleTypes), std::end(allowedSampleTypes), sampleType)){
		cout << "This is not an allowed sample, please specify one from this list (or add to this list in the code):" << endl;
		for (int i =0; i < sizeof(allowedSampleTypes)/sizeof(allowedSampleTypes[0]); i++){
			cout << "    "<<allowedSampleTypes[i] << endl;
		}			
		return;
	}


	selector = new Selector();

	evtPick = new EventPick("nominal");

	selector->looseJetID = true;
	selector->useDeepCSVbTag = true;

    selector->useRoccor = true;	
    selector->fixedSeed = false; 
   
//    evtPick->saveCutflows = true;

    if (noScaleSmear)
    {
        // Don't scale or smear any lepton/jet energies
        selector->smearJetPt = false;
        selector->smearEle = false;
        selector->scaleEle = false;
        selector->useRoccor = false;
    }
   
    if (selector->smearJetPt)
    {
        cout<<"Applying jet pt smearing"<<endl;
    }
    if (selector->scaleEle || selector->smearEle)
    {
        if (selector->scaleEle && selector->smearEle)
            cout<<"Applying electron scale and smear corrections"<<flush<<endl;
        else
            cout<<"Applying electron "<<(selector->scaleEle ? "scale" : "smear")<<" corrections"<<flush<<endl;
    }

    if (selector->useRoccor) { cout<<"Applying Rochester Muon Corrections using "<<((selector->fixedSeed) ? "fixed" : "random")<<" seed"<<endl; }

    if (!selector->fixedSeed) { gRandom->SetSeed(); }
    //	selector->jet_Pt_cut = 40.;
	evtPick->Njet_ge = 2;	
	evtPick->NBjet_ge = 1;	
	BTagCalibration calib;
	if (!selector->useDeepCSVbTag){
		calib = BTagCalibration("csvv2", "CSVv2_Moriond17_B_H.csv");
	} else {
		calib = BTagCalibration("deepcsv", "DeepCSV_Moriond17_B_H.csv");
	}

	BTagCalibrationReader reader(BTagEntry::OP_MEDIUM,  // operating point
								 "central",             // central sys type
								 {"up", "down"});      // other sys types

	if (tree == 0) {
		std::cout <<"Tree not recognized" << endl;
	}

	reader.load(calib,                // calibration instance
				BTagEntry::FLAV_B,    // btag flavour
				"comb");               // measurement type

	reader.load(calib,                // calibration instance
				BTagEntry::FLAV_C,    // btag flavour
				"comb");               // measurement type

	reader.load(calib,                // calibration instance
				BTagEntry::FLAV_UDSG,    // btag flavour
				"incl");               // measurement type

	getGenScaleWeights = false;
	if( sampleType.substr(0,5)=="TTbar"){
		getGenScaleWeights = true;
	}

	
	applypdfweight = false;
	applyqsquare  = false;


    if( sampleType.substr(0,5)=="TTbar"){
         applypdfweight = true; 	
		 applyqsquare = true;
	}
	
	if (applypdfweight||applyqsquare)  std::cout<<"###### Will apply pdfWeights and Q2 weights ######"<< std::endl;

	string JECsystLevel = "";
	if( systematicType.substr(0,3)=="JEC" ){
		int pos = systematicType.find("_");
		JECsystLevel = systematicType.substr(3,pos-3);
		if (std::end(allowedJECUncertainties) == std::find(std::begin(allowedJECUncertainties), std::end(allowedJECUncertainties), JECsystLevel)){
			cout << "The JEC systematic source, " << JECsystLevel << ", is not in the list of allowed sources (found in JEC/UncertaintySourcesList.h" << endl;
			cout << "Exiting" << endl;
			return;
		}
		if (systematicType.substr(pos+1,2)=="up"){ jecvar012_g = 2; }
		if (systematicType.substr(pos+1,2)=="do"){ jecvar012_g = 0; }
		isSystematicRun = true;
	}
		
	if( systematicType=="JER_up")       {jervar012_g = 2; selector->JERsystLevel=2; isSystematicRun = true;}
	if( systematicType=="JER_down")     {jervar012_g = 0; selector->JERsystLevel=0; isSystematicRun = true;}
	if(systematicType=="elesmear_down") {elesmear012_g=0;selector->elesmearLevel=0; isSystematicRun = true;}
	if(systematicType=="elesmear_up") {elesmear012_g=2;selector->elesmearLevel=2; isSystematicRun = true;}
	if(systematicType=="elescale_down") {elescale012_g=0;selector->elescaleLevel=0; isSystematicRun = true;}
	if(systematicType=="elescale_up") {elescale012_g=2;  selector->elescaleLevel=2; isSystematicRun = true;}
	if(systematicType=="muscale_up")   {muscale012_g = 2; selector->muscaleLevel=2; isSystematicRun = true;}
	if(systematicType=="muscale_down") {muscale012_g = 0; selector->muscaleLevel=0; isSystematicRun = true;}
    if(systematicType=="hdamp_up" || systematicType=="hdamp_down" || systematicType=="UE_up" || systematicType=="UE_down") { isSystematicRun = true; }

    if( (sampleType.substr(0,13) == "TTbar_CRerdON") || (sampleType.substr(0,13) == "TTbar_CRGluon") || (sampleType.substr(0,11) == "TTbar_CRQCD") || (sampleType.substr(0,13)=="TTbar_amcanlo") || (sampleType.substr(0,14)=="TTbar_madgraph") || (sampleType.substr(0,14)=="TTbar_herwigpp") || (sampleType.substr(0,9)=="TTbar_isr") || (sampleType.substr(0,9)=="TTbar_fsr") || (sampleType.substr(0,13)=="ST_tW_top_isr") || (sampleType.substr(0,13)=="ST_tW_top_fsr") || (sampleType.substr(0,17)=="ST_tW_antitop_isr") || (sampleType.substr(0,17)=="ST_tW_antitop_fsr") || (sampleType.substr(0,12)=="ST_tW_top_DS") || (sampleType.substr(0,16)=="ST_tW_antitop_DS") ) { isSystematicRun = true; }
	
    std::cout << "JEC: " << jecvar012_g << "  JER: " << jervar012_g << "  eleScale: "<< elescale012_g  
              << "  eleSmear: " << elesmear012_g << "  muScale: " << muscale012_g << endl;

	if (isSystematicRun){
		std::cout << "  Systematic Run : Dropping genMC variables from tree" << endl;
	}
	std::string outputDirectory(av[2]);
	std::string outputFileName = outputDirectory + "/" + sampleType+"_AnalysisNtuple.root";
	// char outputFileName[100];
	//cout << av[2] << " " << sampleType << " " << systematicType << endl;
	//	outputFileName = sprintf("%s_AnalysisNtuple.root",sampleType);
	if (systematicType!=""){
		outputFileName = outputDirectory + "/"+ sampleType + "__" +systematicType+"_AnalysisNtuple.root";
		//		sprintf(outputFileName,"%s/%s_%s_AnalysisNtuple.root",av[2],systematicType,sampleType);
	}
	cout << av[2] << " " << sampleType << " " << systematicType << endl;
	cout << outputFileName << endl;
	TFile *outputFile = new TFile(outputFileName.c_str(),"recreate");
	outputTree = new TTree("AnalysisTree","AnalysisTree");

	InitBranches();
    

	PUReweight* PUweighter = new PUReweight(ac-3, av+3, mt_PUfilename);
	PUReweight* PUweighterUp = new PUReweight(ac-3, av+3, mt_PUfilename_up);
	PUReweight* PUweighterDown = new PUReweight(ac-3, av+3, mt_PUfilename_down);
	bool isMC;

	tree->GetEntry(0);
	isMC = !(tree->isData_);
	std::cout << "isMC: " << isMC << endl;

	JECvariation* jecvar;
	if (isMC && jecvar012_g!=1) {
		//		jecvar = new JECvariation("./jecFiles/Summer16_23Sep2016V4", isMC, "Total");//SubTotalAbsolute");
		cout << "Applying JEC uncertainty variations : " << JECsystLevel << endl;
		jecvar = new JECvariation("./jecFiles/Summer16_23Sep2016V4", isMC, JECsystLevel);//SubTotalAbsolute");
	}


    _lumiWeight = getEvtWeight(sampleType);
	
	_PUweight       = 1.;
	_muEffWeight    = 1.;
	_muEffWeight_Do = 1.;
	_muEffWeight_Up = 1.;
	_muIDEffWeight    = 1.;
	_muIDEffWeight_Do = 1.;
	_muIDEffWeight_Up = 1.;
	_muIsoEffWeight    = 1.;
	_muIsoEffWeight_Do = 1.;
	_muIsoEffWeight_Up = 1.;
	_muTrackEffWeight    = 1.;
	_muTrackEffWeight_Do = 1.;
	_muTrackEffWeight_Up = 1.;
	_eleEffWeight    = 1.;
	_eleEffWeight_Up = 1.;
	_eleEffWeight_Do = 1.;
	_eleIDEffWeight    = 1.;
	_eleIDEffWeight_Up = 1.;
	_eleIDEffWeight_Do = 1.;
	_eleRecoEffWeight    = 1.;
	_eleRecoEffWeight_Up = 1.;
	_eleRecoEffWeight_Do = 1.;

	Long64_t nEntr = tree->GetEntries();

	bool saveAllEntries = false;

	if (sampleType=="Test") nEntr = 10000;
	if (sampleType=="TestAll") {
		nEntr = 1000;
		saveAllEntries = true;
	}
	//nEntr = 10000;

	int dumpFreq = 1;
	if (nEntr >50)     { dumpFreq = 5; }
	if (nEntr >100)     { dumpFreq = 10; }
	if (nEntr >500)     { dumpFreq = 50; }
	if (nEntr >1000)    { dumpFreq = 100; }
	if (nEntr >5000)    { dumpFreq = 500; }
	if (nEntr >10000)   { dumpFreq = 1000; }
	if (nEntr >50000)   { dumpFreq = 5000; }
	if (nEntr >100000)  { dumpFreq = 10000; }
	if (nEntr >500000)  { dumpFreq = 50000; }
	if (nEntr >1000000) { dumpFreq = 100000; }
	if (nEntr >5000000) { dumpFreq = 500000; }
	if (nEntr >10000000){ dumpFreq = 1000000; }
	int count_overlapTchannel=0;
	int count_overlapVJets=0;
	int count_overlapTTbar=0;


	for(Long64_t entry=0; entry<nEntr; entry++){
		if(entry%dumpFreq == 0){
			duration =  ( clock() - startClock ) / (double) CLOCKS_PER_SEC;
			std::cout << "processing entry " << entry << " out of " << nEntr << " : " << duration << " seconds since last progress" << std::endl;
			startClock = clock();

		}
    //    cout <<"=====================================\nEntry "<< entry << endl<<endl;
		tree->GetEntry(entry);
		isMC = !(tree->isData_);

		// //		Apply systematics shifts where needed
		if( isMC ){
			if (jecvar012_g != 1){
				jecvar->applyJEC(tree, jecvar012_g); // 0:down, 1:norm, 2:up
			}
		}

	
				

		//		selector->process_objects(tree);
		selector->clear_vectors();

        if (isMC)
            _PUweight    = PUweighter->getWeight(tree->nPUInfo_, tree->puBX_, tree->puTrue_);
		evtPick->process_event(tree, selector, _lumiWeight * _PUweight * ((tree->genWeight_ >= 0) ? 1 : -1));
//		if (tree->lumis_==225916 && tree->event_==36191688){
//			cout << tree->run_ <<"\t"<<tree->lumis_ << "\t" << tree->event_ << endl;
//			cout << "Pass Event Pick: " << evtPick->passPresel_emu << endl;
//			cout << "    nMu   = "<<selector->Muons.size() << endl;
//			cout << "           pt="<<tree->muPt_->at(selector->Muons.at(0)) << endl;
//			cout << "    nEle  = "<<selector->Electrons.size() << endl;
//			cout << "           pt="<<tree->elePt_->at(selector->Electrons.at(0)) << endl;
//			cout << "    nJets = "<<selector->Jets.size() << endl;
//			cout << "    nBJets= "<<selector->bJets.size() << endl;
//			return;
//		}
		if ( (mtAnalysis && evtPick->passPresel_emu) || saveAllEntries) {
			InitVariables();
			FillEvent();
			//			cout << tree->run_ <<"\t"<<tree->lumis_ << "\t" << tree->event_ << endl;

			if(isMC) {
				_PUweight    = PUweighter->getWeight(tree->nPUInfo_, tree->puBX_, tree->puTrue_);
				_PUweight_Up = PUweighterUp->getWeight(tree->nPUInfo_, tree->puBX_, tree->puTrue_);
				_PUweight_Do = PUweighterDown->getWeight(tree->nPUInfo_, tree->puBX_, tree->puTrue_);

				_btagWeight    = getBtagSF("central", reader, _btagSF);
				_btagWeight_Up = getBtagSF("up", reader, _btagSF_Up);
				_btagWeight_Do = getBtagSF("down", reader, _btagSF_Do);				
			    
                if (mtAnalysis) 
                {
                    int muInd_ = selector->Muons.at(0);
                    _muEffWeight    = muEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),1);
                    _muEffWeight_Do = muEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),0);
                    _muEffWeight_Up = muEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),2);
                    
                    _muIDEffWeight    = muIDEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),1);
                    _muIDEffWeight_Do = muIDEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),0);
                    _muIDEffWeight_Up = muIDEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),2);
                    
                    _muIsoEffWeight    = muIsoEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),1);
                    _muIsoEffWeight_Do = muIsoEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),0);
                    _muIsoEffWeight_Up = muIsoEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),2);
                    
                    _muTrackEffWeight    = muTrackEffSF(tree->muEta_->at(muInd_),1);
                    _muTrackEffWeight_Do = muTrackEffSF(tree->muEta_->at(muInd_),0);
                    _muTrackEffWeight_Up = muTrackEffSF(tree->muEta_->at(muInd_),2);

                    int eleInd_ = selector->Electrons.at(0);
                    _eleEffWeight    = eleEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),1);
                    _eleEffWeight_Do = eleEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),0);
                    _eleEffWeight_Up = eleEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),2);

                    _eleIDEffWeight    = eleIDEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),1);
                    _eleIDEffWeight_Do = eleIDEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),0);
                    _eleIDEffWeight_Up = eleIDEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),2);

                    _eleRecoEffWeight    = eleRecoEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),1);
                    _eleRecoEffWeight_Do = eleRecoEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),0);
                    _eleRecoEffWeight_Up = eleRecoEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),2);

                    _trigEffWeight    = trigEffSF(tree->elePt_->at(eleInd_), tree->muPt_->at(muInd_),1);
                    _trigEffWeight_Do = trigEffSF(tree->elePt_->at(eleInd_), tree->muPt_->at(muInd_),0);
                    _trigEffWeight_Up = trigEffSF(tree->elePt_->at(eleInd_), tree->muPt_->at(muInd_),2);
                }
			}

			if (tree->isData_){
				if (selector->bJets.size() == 0){
					_btagWeight.push_back(1.0);
					_btagWeight.push_back(0.0);
					_btagWeight.push_back(0.0);
				}				
				if (selector->bJets.size() == 1){
					_btagWeight.push_back(0.0);
					_btagWeight.push_back(1.0);
					_btagWeight.push_back(0.0);
				}				
				if (selector->bJets.size() >= 2){
					_btagWeight.push_back(0.0);
					_btagWeight.push_back(0.0);
					_btagWeight.push_back(1.0);
				}				
			}
			outputTree->Fill();
	//		std::cout<<"done with filling"<<std::endl;
		}
	}

    cout<<flush<<"Output tree has "<<outputTree->GetEntriesFast()<<" entries"<<endl;
//	std::cout <<outputFile <<std::endl;		
	outputFile->cd();
	outputTree->Write();
    if (evtPick->saveCutflows)
    {
        cout<<"\nRaw events"<<flush<<endl;
        evtPick->print_cutflow_emu(evtPick->cutFlow_emu);

        cout<<"\nWeighted events"<<flush<<endl;
        evtPick->print_cutflow_emu(evtPick->cutFlowWeight_emu);
        
        std::cout << "Saving cutflow tables" << std::endl;
        evtPick->cutFlow_emu->Write();
        evtPick->cutFlowWeight_emu->Write();
    }


	outputFile->Close();

}


void makeAnalysisNtuple::FillEvent()
{

	_run             = tree->run_;
	_event           = tree->event_;
	_lumis		     = tree->lumis_;
	_isData		     = tree->isData_;
	_nVtx		     = tree->nVtx_;
	_nGoodVtx	     = tree->nGoodVtx;
	_isPVGood	     = tree->isPVGood_;
	_rho		     = tree->rho_;

	_evtWeight       = _lumiWeight *  ((tree->genWeight_ >= 0) ? 1 : -1);  //event weight needs to be positive or negative depending on sign of genWeight (to account for mc@nlo negative weights)

	if (_isData) {_evtWeight= 1.;}
	_genMET		     = tree->genMET_;
	_pfMET		     = tree->pfMET_;
	_pfMETPhi	     = tree->pfMETPhi_;

	_nEle		     = selector->Electrons.size();
	_nEleLoose           = selector->ElectronsLoose.size();
	_nMuLoose            = selector->MuonsLoose.size();
	_nMu		     = selector->Muons.size();
	_nJet            = selector->Jets.size();
	_nBJet           = selector->bJets.size();
	_nMC             = tree->nMC_;
	_pdfWeight       = tree->pdfWeight_;	
    
	double ht = 0.0;
	ht += tree->pfMET_;
	for( int i_jet = 0; i_jet < _nJet; i_jet++)
		ht += tree->jetPt_->at(i_jet);
	
	_HT = ht; 


	for (int i_ele = 0; i_ele <_nEle; i_ele++){
		int eleInd = selector->Electrons.at(i_ele);
		_elePt.push_back(tree->elePt_->at(eleInd));
		_elePhi.push_back(tree->elePhi_->at(eleInd));
		_eleSCEta.push_back(tree->eleSCEta_->at(eleInd));

		_elePFRelIso.push_back(selector->EleRelIso_corr.at(eleInd));
		lepVector.SetPtEtaPhiE(tree->elePt_->at(eleInd),
							   tree->eleSCEta_->at(eleInd),
							   tree->elePhi_->at(eleInd),
							   tree->eleEn_->at(eleInd));

	}


	for (int i_mu = 0; i_mu <_nMu; i_mu++){
		int muInd = selector->Muons.at(i_mu);
		_muPt.push_back(tree->muPt_->at(muInd));
		_muPhi.push_back(tree->muPhi_->at(muInd));
		_muEta.push_back(tree->muEta_->at(muInd));
		_muPFRelIso.push_back(selector->MuRelIso_corr.at(muInd));
		lepVector.SetPtEtaPhiE(tree->muPt_->at(muInd),
							   tree->muEta_->at(muInd),
							   tree->muPhi_->at(muInd),
							   tree->muEn_->at(muInd));
		// lepVector.SetPtEtaPhiM(tree->muPt_->at(muInd),
		// 					   tree->muEta_->at(muInd),
		// 					   tree->muPhi_->at(muInd),
		// 					   0);
	}
	

    int eleInd = selector->Electrons.at(0);
    int muInd = selector->Muons.at(0);

    if (tree->eleCharge_->at(eleInd) * tree->muCharge_->at(muInd) > 0){
        cout<<"Event "<<_event<<" contains leading emu pair with same sign!"<<endl;
    }

    if (tree->muCharge_->at(muInd) > 0) {
        lpVector.SetPtEtaPhiE(tree->muPt_->at(muInd),
                              tree->muEta_->at(muInd),
                              tree->muPhi_->at(muInd),
                              tree->muEn_->at(muInd));

        lmVector.SetPtEtaPhiE(tree->elePt_->at(eleInd),
                              tree->eleEta_->at(eleInd),
                              tree->elePhi_->at(eleInd),
                              tree->eleEn_->at(eleInd));

    }
    else {
        lpVector.SetPtEtaPhiE(tree->elePt_->at(eleInd),
                              tree->eleEta_->at(eleInd),
                              tree->elePhi_->at(eleInd),
                              tree->eleEn_->at(eleInd));
        
        lmVector.SetPtEtaPhiE(tree->muPt_->at(muInd),
                              tree->muEta_->at(muInd),
                              tree->muPhi_->at(muInd),
                              tree->muEn_->at(muInd));
    }


	

	_passPresel_EMu  = evtPick->passPresel_emu;



    for (int i_jet = 0; i_jet <_nJet; i_jet++){
        
        int jetInd = selector->Jets.at(i_jet);
        _jetPt.push_back(tree->jetPt_->at(jetInd));
        _jetEn.push_back(tree->jetEn_->at(jetInd));
        _jetEta.push_back(tree->jetEta_->at(jetInd));
        _jetPhi.push_back(tree->jetPhi_->at(jetInd));
        _jetRawPt.push_back(tree->jetRawPt_->at(jetInd));
        _jetArea.push_back(tree->jetArea_->at(jetInd));
        _jetpfCombinedMVAV2BJetTags.push_back(tree->jetpfCombinedMVAV2BJetTags_->at(jetInd));
        _jetCSV2BJetTags.push_back(tree->jetCSV2BJetTags_->at(jetInd));
        _jetDeepCSVTags_b.push_back(tree->jetDeepCSVTags_b_->at(jetInd));
        _jetDeepCSVTags_bb.push_back(tree->jetDeepCSVTags_bb_->at(jetInd));

        if (!tree->isData_){
            _jetPartonID.push_back(tree->jetPartonID_->at(jetInd));
            _jetGenJetPt.push_back(tree->jetGenJetPt_->at(jetInd));
            _jetGenPartonID.push_back(tree->jetGenPartonID_->at(jetInd));
            _jetGenPt.push_back(tree->jetGenPt_->at(jetInd));
            _jetGenEta.push_back(tree->jetGenEta_->at(jetInd));
            _jetGenPhi.push_back(tree->jetGenPhi_->at(jetInd));
        }
        jetVector.SetPtEtaPhiE(tree->jetPt_->at(jetInd), tree->jetEta_->at(jetInd), tree->jetPhi_->at(jetInd), tree->jetEn_->at(jetInd));
        
        double resolution = getJetResolution(tree->jetPt_->at(jetInd), tree->jetEta_->at(jetInd), tree->rho_);
        if (tree->jetDeepCSVTags_b_->at(jetInd) + tree->jetDeepCSVTags_bb_->at(jetInd) > selector->btag_cut_DeepCSV){
            bjetVectors.push_back(jetVector);
            bjetResVectors.push_back(resolution);
        } else {
            ljetVectors.push_back(jetVector);
            ljetResVectors.push_back(resolution);
        }
    }	

    _pt_ll = (lpVector + lmVector).Pt();
    _m_ll = (lpVector + lmVector).M();
    _pt_pos = lpVector.Pt();
    _E_pos = lpVector.E();
    _ptp_ptm = lpVector.Pt() + lmVector.Pt();
    _Ep_Em = lpVector.E() + lmVector.E();

    if (!tree->isData_) { _topptWeight = topPtWeight(); }



	ljetVectors.clear();
	bjetVectors.clear();

	ljetResVectors.clear();
	bjetResVectors.clear();

	
	if (!tree->isData_){
		if (applyqsquare){
			
			for (int i=0;i<9;i++){
				if(i==5||i==7){continue;}
				if (getGenScaleWeights){
					_genScaleSystWeights.push_back(tree->genScaleSystWeights_->at(i));
				}
				else{
					_genScaleSystWeights.push_back(1.);
				}
			}
		 	_q2weight_Up = *max_element(_genScaleSystWeights.begin(), _genScaleSystWeights.end());		
			_q2weight_Do = *min_element(_genScaleSystWeights.begin(), _genScaleSystWeights.end());
			_q2weight_nominal = tree->genScaleSystWeights_->at(0);
		}

		if(applypdfweight){
			double mean=0.;
			for (int i=9;i<tree->pdfSystWeight_->size();i++){
				_pdfSystWeight.push_back(tree->pdfSystWeight_->at(i));
				if (i<111){
					mean += tree->pdfSystWeight_->at(i);
				}
			}

			mean = mean/102.;

			double sum=0.;
			for (int j=0;j<102;j++){
				sum+=pow((_pdfSystWeight[j]-mean),2.);
			}
			_pdfuncer = sqrt(sum/102.);

			_pdfweight_Up = (_pdfWeight + _pdfuncer)/_pdfWeight;
			_pdfweight_Do = (_pdfWeight - _pdfuncer)/_pdfWeight;
		}

			
		for (int i_mc = 0; i_mc <_nMC; i_mc++){
			_mcPt.push_back(tree->mcPt->at(i_mc));
			_mcPhi.push_back(tree->mcPhi->at(i_mc));
			_mcEta.push_back(tree->mcEta->at(i_mc));
			_mcMass.push_back(tree->mcMass->at(i_mc));
			_mcStatus.push_back(tree->mcStatus->at(i_mc));
			_mcStatusFlag.push_back(tree->mcStatusFlag->at(i_mc));
			_mcPID.push_back(tree->mcPID->at(i_mc));
			_mcMomPID.push_back(tree->mcMomPID->at(i_mc));
			_mcGMomPID.push_back(tree->mcGMomPID->at(i_mc));
			_mcParentage.push_back(tree->mcParentage->at(i_mc));
		}
	}

}

// https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopPtReweighting
double makeAnalysisNtuple::SFtop(double pt){
	return exp(0.0615 - 0.0005*pt); 
}

double makeAnalysisNtuple::topPtWeight(){
	double toppt=0.0;
	double antitoppt=0.0;
	double weight = 1.0;
	for(int mcInd=0; mcInd<tree->nMC_; ++mcInd){
		if(tree->mcPID->at(mcInd)==6) toppt = tree->mcPt->at(mcInd);
		if(tree->mcPID->at(mcInd)==-6) antitoppt = tree->mcPt->at(mcInd);
	}
	if(toppt > 0.001 && antitoppt > 0.001)
		weight = sqrt( SFtop(toppt) * SFtop(antitoppt) );

    return weight;

}

vector<float> makeAnalysisNtuple::getBtagSF(string sysType, BTagCalibrationReader reader, vector<float> &btagSF){

	// Saving weights w(0|n), w(1|n), w(2|n)
	vector<float> btagWeights;

	double weight0tag = 1.0; 		//w(0|n)
	double weight1tag = 0.0;		//w(1|n)

	double jetpt;
	double jeteta;
	int jetflavor;
	double SFb;
	double SFb2;


	for(std::vector<int>::const_iterator bjetInd = selector->bJets.begin(); bjetInd != selector->bJets.end(); bjetInd++){
		jetpt = tree->jetPt_->at(*bjetInd);
		jeteta = fabs(tree->jetEta_->at(*bjetInd));
		jetflavor = abs(tree->jetHadFlvr_->at(*bjetInd));
		
		if (jetflavor == 5) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_B, jeteta, jetpt); 
		else if(jetflavor == 4) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_C, jeteta, jetpt); 
		else {
			SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_UDSG, jeteta, jetpt); 
			//			if (sysType=="central") cout << tree->event_ << " " << *bjetInd << " " << jetpt << " " << jeteta << " " << jetflavor << " " << SFb<<endl;
		}

		// if 
		// if (SFb==0 && sysType=="central"){
		// 	cout << tree->event_ << " " << *bjetInd << " " << jetpt << " " << jeteta << " " << jetflavor << endl;
		// }
		btagSF.push_back(SFb);
	}

	if(selector->bJets.size() == 0) {
		btagWeights.push_back(1.0);
		btagWeights.push_back(0.0);
		btagWeights.push_back(0.0);

		return btagWeights;

	} else if (selector->bJets.size() == 1) {
		btagWeights.push_back(1-btagSF.at(0));
		btagWeights.push_back(btagSF.at(0));
		btagWeights.push_back(0.0);
		
		return btagWeights;

	} else {

		// We are following the method 1SFc from the twiki
		// https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagSFMethods#1c_Event_reweighting_using_scale
		for (int i = 0; i < selector->bJets.size(); i++){
			SFb = btagSF.at(i);
			weight0tag *= 1.0 - SFb;
			double prod = SFb;
			for (int j = 0; j < selector->bJets.size(); j++){
				if (j==i) {continue;}
				prod *= (1.-btagSF.at(j));
			}
			weight1tag += prod;
		}
		btagWeights.push_back(weight0tag);
		btagWeights.push_back(weight1tag);
		btagWeights.push_back(1.0 - weight0tag - weight1tag);
		return btagWeights;
	}
}






double makeAnalysisNtuple::WjetsBRreweight(){

	int countLeps = 0;

	//Need to try to avoid double counting of tau's (check if momPt is the same before counting, since status flag isn't there)
	double tauMomPt1 = -1.;
	double tauMomPt2 = -1.;
	
	for(int mcInd=0; mcInd<tree->nMC_; ++mcInd){
		if( (TMath::Abs(tree->mcPID->at(mcInd)) == 11 ||
			 TMath::Abs(tree->mcPID->at(mcInd)) == 13 ||
			 TMath::Abs(tree->mcPID->at(mcInd)) == 15 ) &&
			TMath::Abs(tree->mcMomPID->at(mcInd)) == 24 &&
			TMath::Abs(tree->mcGMomPID->at(mcInd)) == 6) {

			if (TMath::Abs(tree->mcPID->at(mcInd)) == 15){
				if (tauMomPt1==-1.){
					tauMomPt1 = tree->mcMomPt->at(mcInd);
					countLeps += 1;
				}
				else if (tauMomPt2==-1.){
					if (tree->mcMomPt->at(mcInd)!=tauMomPt1) {
						tauMomPt2 = tree->mcMomPt->at(mcInd);
						countLeps += 1;
					}
				}
				else{
					if (tree->mcMomPt->at(mcInd)!=tauMomPt1 && tree->mcMomPt->at(mcInd)!=tauMomPt2) {
						countLeps += 1;
					}
				}
			}
			else {
				countLeps += 1;
			}
		}
	}
	double reweight=1.;
	if (countLeps==0){reweight = .6741*.6741*9./4.;}
	else if(countLeps==1){reweight = .6741*.3259*2*9./4.;}
	else if(countLeps==2){reweight = .3259*.3259*9.;}
	else {
		std::cout << "MORE THAN TWO LEPTONS???????" << std::endl;
		std::cout << countLeps << std::endl;
	}
	
	return reweight;
	
}


vector<bool> makeAnalysisNtuple::passPhoMediumID(int phoInd){

	double pt = tree->phoEt_->at(phoInd);
    double eta = TMath::Abs(tree->phoSCEta_->at(phoInd));
    bool passMediumID = false;

	int region = 0;
	if( eta >= 1.0  ) region++;
	if( eta >= 1.479) region++;
	if( eta >= 2.0  ) region++;
	if( eta >= 2.2  ) region++;
	if( eta >= 2.3  ) region++;
	if( eta >= 2.4  ) region++;

	double rhoCorrPFChIso  = max(0.0, tree->phoPFChIso_->at(phoInd)  - photonEA[region][0] *tree->rho_);
	double rhoCorrPFNeuIso = max(0.0, tree->phoPFNeuIso_->at(phoInd) - photonEA[region][1] *tree->rho_);
	double rhoCorrPFPhoIso = max(0.0, tree->phoPFPhoIso_->at(phoInd) - photonEA[region][2] *tree->rho_);

	bool passHoverE = false;
	bool passSIEIE  = false;
	bool passChIso  = false;
	bool passNeuIso  = false;
	bool passPhoIso  = false;
	
	
    if (eta < 1.47){
		if (tree->phoHoverE_->at(phoInd) < 0.0396 )               passHoverE = true;
		if (tree->phoSigmaIEtaIEtaFull5x5_->at(phoInd) < 0.01022) passSIEIE  = true;
		if (rhoCorrPFChIso  < 0.441  )                            passChIso  = true;
		if (rhoCorrPFNeuIso < 2.725+0.0148*pt+0.000017*pt*pt)     passNeuIso = true;
		if (rhoCorrPFPhoIso < 2.571+0.0047*pt)                    passPhoIso = true;
    } else {
		if (tree->phoHoverE_->at(phoInd) < 0.0219 )                passHoverE = true;
		if (tree->phoSigmaIEtaIEtaFull5x5_->at(phoInd)  < 0.03001) passSIEIE  = true;
		if (rhoCorrPFChIso < 0.442) 							   passChIso  = true;
		if (rhoCorrPFNeuIso < 1.715+0.0163*pt+0.000014*pt*pt)	   passNeuIso = true;
		if (rhoCorrPFPhoIso < 3.863+0.0034*pt)					   passPhoIso = true;
	}

	passMediumID = passHoverE && passSIEIE && passChIso && passNeuIso && passPhoIso;

	vector<bool> cuts;
	cuts.push_back(passMediumID);
	cuts.push_back(passHoverE);
	cuts.push_back(passSIEIE);
	cuts.push_back(passChIso);
	cuts.push_back(passNeuIso);
	cuts.push_back(passPhoIso);

	return cuts;

    // if (eta < 1.47){
	// 	if ((!cutHoverE || tree->phoHoverE_->at(phoInd)                < 0.0396  ) &&
	// 		(!cutSIEIE  || tree->phoSigmaIEtaIEtaFull5x5_->at(phoInd)  < 0.01022 ) &&
	// 		(!cutIso    || (rhoCorrPFChIso                              < 0.441 &&
	// 						rhoCorrPFNeuIso                             < 2.725+0.0148*pt+0.000017*pt*pt &&
	// 						rhoCorrPFPhoIso                             < 2.571+0.0047*pt))){
	// 		passMediumID = true;
	// 	}
    // } else {
	// 	if ((!cutHoverE || tree->phoHoverE_->at(phoInd)                < 0.0219  ) &&
	// 		(!cutSIEIE  || tree->phoSigmaIEtaIEtaFull5x5_->at(phoInd)  < 0.03001 ) &&
	// 		(!cutIso    || (rhoCorrPFChIso                              < 0.442 &&
	// 						rhoCorrPFNeuIso                             < 1.715+0.0163*pt+0.000014*pt*pt &&
	// 						rhoCorrPFPhoIso                             < 3.863+0.0034*pt))){
	// 		passMediumID = true;
	// 	}
    // }
    // return passMediumID;
}


vector<bool> makeAnalysisNtuple::passPhoTightID(int phoInd){

	double pt = tree->phoEt_->at(phoInd);
    double eta = TMath::Abs(tree->phoSCEta_->at(phoInd));
    bool passTightID = false;

	int region = 0;
	if( eta >= 1.0  ) region++;
	if( eta >= 1.479) region++;
	if( eta >= 2.0  ) region++;
	if( eta >= 2.2  ) region++;
	if( eta >= 2.3  ) region++;
	if( eta >= 2.4  ) region++;

	double rhoCorrPFChIso  = max(0.0, tree->phoPFChIso_->at(phoInd)  - photonEA[region][0] *tree->rho_);
	double rhoCorrPFNeuIso = max(0.0, tree->phoPFNeuIso_->at(phoInd) - photonEA[region][1] *tree->rho_);
	double rhoCorrPFPhoIso = max(0.0, tree->phoPFPhoIso_->at(phoInd) - photonEA[region][2] *tree->rho_);

	bool passHoverE = false;
	bool passSIEIE  = false;
	bool passChIso  = false;
	bool passNeuIso  = false;
	bool passPhoIso  = false;
	
	
    if (eta < 1.47){
		if (tree->phoHoverE_->at(phoInd) < 0.0269 )               passHoverE = true;
		if (tree->phoSigmaIEtaIEtaFull5x5_->at(phoInd) < 0.00994) passSIEIE  = true;
		if (rhoCorrPFChIso  < 0.202  )                            passChIso  = true;
		if (rhoCorrPFNeuIso < 0.264+0.0148*pt+0.000017*pt*pt)     passNeuIso = true;
		if (rhoCorrPFPhoIso < 2.362+0.0047*pt)                    passPhoIso = true;
    } else {
		if (tree->phoHoverE_->at(phoInd) < 0.0213 )                passHoverE = true;
		if (tree->phoSigmaIEtaIEtaFull5x5_->at(phoInd)  < 0.03000) passSIEIE  = true;
		if (rhoCorrPFChIso < 0.034) 							   passChIso  = true;
		if (rhoCorrPFNeuIso < 0.586+0.0163*pt+0.000014*pt*pt)	   passNeuIso = true;
		if (rhoCorrPFPhoIso < 2.617+0.0034*pt)					   passPhoIso = true;
	}

	passTightID = passHoverE && passSIEIE && passChIso && passNeuIso && passPhoIso;

	vector<bool> cuts;
	cuts.push_back(passTightID);
	cuts.push_back(passHoverE);
	cuts.push_back(passSIEIE);
	cuts.push_back(passChIso);
	cuts.push_back(passNeuIso);
	cuts.push_back(passPhoIso);

	return cuts;

}


//This is defined in OverlapRemoval.cpp
double minGenDr(int myInd, const EventTree* tree);


void makeAnalysisNtuple::findPhotonCategory(int mcMatchInd, EventTree* tree, bool* genuine, bool *misIDele, bool *hadronicphoton, bool *hadronicfake){

	*genuine        = false;
	*misIDele       = false;
	*hadronicphoton = false;
	*hadronicfake   = false;

	// If no match, it's hadronic fake
	if (mcMatchInd== -1) {
		*hadronicfake = true;
		return;
	}

	//	mcMatchInd = findPhotonGenMatch(int phoInd, EventTree* tree);
	bool parentagePass = (fabs(tree->mcMomPID->at(mcMatchInd))<37 || tree->mcMomPID->at(mcMatchInd) == -999);

	if (tree->mcPID->at(mcMatchInd) == 22){
		//bool parentagePass = (fabs(tree->mcMomPID->at(mcMatchInd))<37 || tree->mcMomPID->at(mcMatchInd) == -999);
		//parentagePass = tree->mcParentage->at(mcMatchInd)==2 || tree->mcParentage->at(mcMatchInd)==10 || tree->mcParentage->at(mcMatchInd)==26;
		bool drotherPass = minGenDr(mcMatchInd, tree) > 0.2;
		if (parentagePass && drotherPass){ 
			*genuine = true;
		}
		else {
			*hadronicphoton = true;
		}
	}
	else if ( abs(tree->mcPID->at(mcMatchInd) ) == 11 && parentagePass && minGenDr(mcMatchInd, tree) > 0.2 ) {
		*misIDele = true;
	} 
	else {
		*hadronicfake = true;
	}
}
			
int makeAnalysisNtuple::findPhotonGenMatch(int phoInd, EventTree* tree){

	double minDR = 999.;
	int matchInd = -1;

	for(int mcInd=0; mcInd<tree->nMC_; ++mcInd){
		if (tree->mcStatus->at(mcInd) == 1 || tree->mcStatus->at(mcInd) == 71){ 
			double dRValue = dR(tree->mcEta->at(mcInd),tree->mcPhi->at(mcInd),tree->phoEta_->at(phoInd),tree->phoPhi_->at(phoInd));
			if (dRValue < minDR){
				if ( (fabs(tree->phoEt_->at(phoInd) - tree->mcPt->at(mcInd)) / tree->mcPt->at(mcInd)) < 0.5 ){
					minDR = dRValue;
					matchInd = mcInd;
				}
			}
		}
	}

	if (minDR > 0.1){	matchInd = -1.; }  //Only consider matches with dR < 0.1

	return matchInd;
}




int makeAnalysisNtuple::minDrIndex(double myEta, double myPhi, std::vector<int> Inds, std::vector<float> *etas, std::vector<float> *phis){
	double mindr = 999.0;
	double dr;
	int bestInd = -1;
	for( std::vector<int>::iterator it = Inds.begin(); it != Inds.end(); ++it){
		dr = dR(myEta, myPhi, etas->at(*it), phis->at(*it));
		if( mindr > dr ) {
			mindr = dr;
			bestInd = *it;
		}
	}
	return bestInd;
}

double makeAnalysisNtuple::minDr(double myEta, double myPhi, std::vector<int> Inds, std::vector<float> *etas, std::vector<float> *phis){
	int ind = minDrIndex(myEta, myPhi, Inds, etas, phis);
	if(ind>=0) return dR(myEta, myPhi, etas->at(ind), phis->at(ind));
	else return 999.0;
}

double makeAnalysisNtuple::eleEffSF(double elePt, double eleSCEta, int sysLvl)
{
    // Ele ID scale factor
    double ID = eleID_SF->GetBinContent(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    if (sysLvl == 2)
        ID += eleID_SF->GetBinError(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    else if (sysLvl == 0)
        ID -= eleID_SF->GetBinError(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));


    // Ele Reco scale factor
    double reco = eleReco_SF->GetBinContent(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    if (sysLvl == 2)
        reco += eleReco_SF->GetBinError(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    else if (sysLvl == 0)
        reco -= eleReco_SF->GetBinError(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));

    return ID * reco;
}

double makeAnalysisNtuple::eleIDEffSF(double elePt, double eleSCEta, int sysLvl)
{
    // Ele ID scale factor
    double ID = eleID_SF->GetBinContent(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    if (sysLvl == 2)
        ID += eleID_SF->GetBinError(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    else if (sysLvl == 0)
        ID -= eleID_SF->GetBinError(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));

    return ID;
}

double makeAnalysisNtuple::eleRecoEffSF(double elePt, double eleSCEta, int sysLvl)
{
    // Ele Reco scale factor
    double reco = eleReco_SF->GetBinContent(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    if (sysLvl == 2)
        reco += eleReco_SF->GetBinError(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    else if (sysLvl == 0)
        reco -= eleReco_SF->GetBinError(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));

    return reco;
}

double makeAnalysisNtuple::muEffSF(double muPt, double muEta, int sysLvl)
{
    double muAEta = abs(muEta);

    // Muon ID scale factors
    double ID_BF = muID_BF_SF->GetBinContent(muID_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        ID_BF += muID_BF_SF->GetBinError(muID_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        ID_BF -= muID_BF_SF->GetBinError(muID_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    
    double ID_GH = muID_GH_SF->GetBinContent(muID_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        ID_GH += muID_GH_SF->GetBinError(muID_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        ID_GH -= muID_GH_SF->GetBinError(muID_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));

    // Muon Isolation scale factors
    double Iso_BF = muIso_BF_SF->GetBinContent(muIso_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        Iso_BF += muIso_BF_SF->GetBinError(muIso_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        Iso_BF -= muIso_BF_SF->GetBinError(muIso_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    
    double Iso_GH = muIso_GH_SF->GetBinContent(muIso_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        Iso_GH += muIso_GH_SF->GetBinError(muIso_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        Iso_GH -= muIso_GH_SF->GetBinError(muIso_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));

    return (ID_BF * Iso_BF * lumiBF + ID_GH * Iso_GH * lumiGH) / luminosity;
}

double makeAnalysisNtuple::muIDEffSF(double muPt, double muEta, int sysLvl)
{
    double muAEta = abs(muEta);

    // Muon ID scale factors
    double ID_BF = muID_BF_SF->GetBinContent(muID_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        ID_BF += muID_BF_SF->GetBinError(muID_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        ID_BF -= muID_BF_SF->GetBinError(muID_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    
    double ID_GH = muID_GH_SF->GetBinContent(muID_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        ID_GH += muID_GH_SF->GetBinError(muID_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        ID_GH -= muID_GH_SF->GetBinError(muID_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));

    return (ID_BF * lumiBF + ID_GH * lumiGH) / luminosity; 
}

double makeAnalysisNtuple::muIsoEffSF(double muPt, double muEta, int sysLvl)
{
    double muAEta = abs(muEta);

    // Muon Isolation scale factors
    double Iso_BF = muIso_BF_SF->GetBinContent(muIso_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        Iso_BF += muIso_BF_SF->GetBinError(muIso_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        Iso_BF -= muIso_BF_SF->GetBinError(muIso_BF_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    
    double Iso_GH = muIso_GH_SF->GetBinContent(muIso_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    if (sysLvl == 2)
        Iso_GH += muIso_GH_SF->GetBinError(muIso_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));
    else if (sysLvl == 0)
        Iso_GH -= muIso_GH_SF->GetBinError(muIso_GH_SF->FindBin(muAEta, max(25.0, min(119.9, muPt))));

    return (Iso_BF * lumiBF + Iso_GH * lumiGH) / luminosity;
}

double makeAnalysisNtuple::muTrackEffSF(double muEta, int sysLvl)
{
    // Muon Tracker scale factors
    double track = muTrack_SF->Eval(muEta); 
    
    if (sysLvl != 1) 
    {
        // Find closet point
        int n = -1;
        for (int i =0; i < muTrack_SF->GetN(); i++)
        {
            if (muTrack_SF->GetX()[i] - muEta > 0)
            {
                n = i;
                break;
            }
        }

        auto xpoints = muTrack_SF->GetX();
        if (n > 0)
        {
            if (abs(xpoints[n-1] - muEta) < abs(xpoints[n] - muEta))
                n -= 1;
        }
        if (n < 14)
        {
            if (abs(xpoints[n+1] - muEta) < abs(xpoints[n] - muEta))
                n += 1;
        }
   
        double err = muTrack_SF->GetErrorY(n);

        if (sysLvl == 2)
            track += err;
        else if (sysLvl == 0)
            track -= err; 
    }

    return track;
}

double makeAnalysisNtuple::trigEffSF(double elePt, double muPt, int sysLvl)
{
    double sf = trigger_SF->GetBinContent(trigger_SF->FindBin(min(99.9, max(elePt, muPt)), min(99.9, min(elePt, muPt))));
    if (sysLvl == 2)
        sf += trigger_SF->GetBinError(trigger_SF->FindBin(min(99.9, max(elePt, muPt)), min(99.9, min(elePt, muPt))));
    else if (sysLvl == 0)
        sf -= trigger_SF->GetBinError(trigger_SF->FindBin(min(99.9, max(elePt, muPt)), min(99.9, min(elePt, muPt))));

    return sf;
}


//#endif
int main(int ac, char** av){
  if(ac != 4){
    std::cout << "usage: ./makeAnalysisNtuple sampleName outputFileDir inputFile[s]" << std::endl;
    return -1;
  }

  makeAnalysisNtuple(ac, av);


  return 0;
}
