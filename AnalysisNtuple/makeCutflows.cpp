#include<iostream>
#include<string>
#include"EventTree.h"
#include"Selector.h"
#include"EventPick.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>
#include<TH1F.h>
#include<TCanvas.h>
#include<TGraphAsymmErrors.h>

using std::cout;
using std::endl;
using std::string;
using std::flush;

string PUfilename = "mt_pileupNominal.root";

TString eleID_SF_path("lepSF/Ele_TightID_egammaEffi.txt_EGM2D.root");
TString eleReco_SF_path("lepSF/Ele_Reco_egammaEffi.txt_EGM2D.root");
TString muID_BF_SF_path("lepSF/Muon_TightID_EfficienciesAndSF_BCDEF.root");
TString muID_GH_SF_path("lepSF/Muon_TightID_EfficienciesAndSF_GH.root");
TString muIso_BF_SF_path("lepSF/Muon_Isolation_EfficienciesAndSF_BCDEF.root");
TString muIso_GH_SF_path("lepSF/Muon_Isolation_EfficienciesAndSF_GH.root");
TString muTrack_SF_path("lepSF/Muon_Tracking_EfficienciesAndSF_BCDEFGH.root");
TString trigger_SF_path("lepSF/triggerSFs/AN16_392_SFs.root");

double eleEffSF(double elePt, double eleSCEta, int sysLvl);
double eleIDEffSF(double elePt, double eleSCEta, int sysLvl);
double eleRecoEffSF(double elePt, double eleSCEta, int sysLvl);
double muEffSF(double muPt, double muEta, int sysLvl);
double muIDEffSF(double muPt, double muEta, int sysLvl);
double muIsoEffSF(double muPt, double muEta, int sysLvl);
double muTrackEffSF(double muEta, int sysLvl);
double trigEffSF(double elePt, double muPt, int sysLvl);

TH1F* eleID_SF;
TH1F* eleReco_SF;
TH1F* muID_BF_SF;
TH1F* muID_GH_SF;
TH1F* muIso_BF_SF;
TH1F* muIso_GH_SF;
TGraphAsymmErrors* muTrack_SF;
TH1F* trigger_SF;


#include"PUReweight.h"
#include "BTagCalibrationStandalone.h"
#include "ScaleFactors.h"

bool overlapRemovalTT(EventTree* tree);
double getBtagSF(EventTree *tree, Selector *selector,  string sysType, BTagCalibrationReader reader, int NBjet_ge);
double SFtop(double pt);
double topPtWeight(EventTree *tree);



int main(int ac, char** av){
	if(ac < 4){
		std::cout << "usage: ./makeCutflows sampleType outputFile inputFile[s]" << std::endl;
		return -1;
	}

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

	string sampleType = av[1];
	string systematicType = "";
	cout << sampleType << endl;

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
		return -1;
	}


	bool isMC = (sampleType.find("Data") == std::string::npos);
	PUReweight* PUweighter;

	if (isMC) {
		PUweighter = new PUReweight(ac-3, av+3, PUfilename);
	}

	bool doOverlapRemoval = false;
	bool doOverlapRemoval_WZ = false;	
	bool skipOverlap = false;

    bool applyTopptWeight = false;

//    if (sampleType.substr(0,5) == "TTbar")
//    {
//        cout<<"TTbar sample found. Applying top pt reweighting"<<flush<<endl;
//        applyTopptWeight = true;
//    }

//	if( sampleType == "TTbarPowheg" || sampleType == "TTbarMCatNLO") doOverlapRemoval = true;
//	if( sampleType == "W1jets" || sampleType == "W2jets" ||  sampleType == "W3jets" || sampleType == "W4jets" || sampleType=="DYjetsM10to50" || sampleType=="DYjetsM50") doOverlapRemoval_WZ = true;
//	if(doOverlapRemoval || doOverlapRemoval_WZ) std::cout << "########## Will apply overlap removal ###########" << std::endl;


	EventTree* tree = new EventTree(ac-3, av+3);
	Selector* selector = new Selector();
	double _evtWeight = getEvtWeight(sampleType);



	EventPick* evtPick = new EventPick("nominal");
	// evtPick->MET_cut = 0;

	evtPick->saveCutflows = true;

	selector->looseJetID = true; 
	selector->useDeepCSVbTag = true;
    selector->useRoccor = true;
    selector->fixedSeed = true;
    selector->isTTGamma = false;

	evtPick->Njet_ge = 2;	
	evtPick->NBjet_ge = 1;	

	//	selector->veto_jet_pho_dR = -1.;
	//	selector->veto_pho_jet_dR = -1.;

    if (selector->useRoccor) { cout<<"Applying Rochester Muon Corrections using "<<((selector->fixedSeed) ? "fixed" : "random")<<" seed"<<endl; }

    if (!selector->fixedSeed) { gRandom->SetSeed(); }

	
	BTagCalibration calib;
	if (!selector->useDeepCSVbTag){
		calib = BTagCalibration("csvv2", "CSVv2_Moriond17_B_H.csv");
	} else {
		calib = BTagCalibration("deepcsv", "DeepCSV_Moriond17_B_H.csv");
	}

	BTagCalibrationReader reader(BTagEntry::OP_MEDIUM,  // operating point
								 "central");             // central sys type

	if (isMC){
		reader.load(calib,                // calibration instance
					BTagEntry::FLAV_B,    // btag flavour
					"comb");               // measurement type
		
		reader.load(calib,                // calibration instance
					BTagEntry::FLAV_C,    // btag flavour
					"comb");               // measurement type
		
		reader.load(calib,                // calibration instance
					BTagEntry::FLAV_UDSG,    // btag flavour
					"incl");               // measurement type
	}



	selector->smearJetPt = false;

    double _muEffWeight, _muIDEffWeight, _muIsoEffWeight, _muTrackEffWeight;
    double _eleEffWeight, _eleIDEffWeight, _eleRecoEffWeight, _trigEffWeight;

    _muEffWeight = _muIDEffWeight = _muIsoEffWeight = _muTrackEffWeight = _eleEffWeight = _eleIDEffWeight = _eleRecoEffWeight = _trigEffWeight = 1.0;

	double _PUweight;
	double _muWeight = 1.0;
	double _eleWeight = 1.0;
    double _trigWeight = 1.0;
	double _btagWeight;
    double _topptWeight = 1.0;

	Long64_t nEntr = tree->GetEntries();
	//Long64_t nEntr = 1000;
	std::string outDirName(av[2]);

	if (sampleType=="Test") nEntr = 10000;

	int dumpFreq = 100;
	if (nEntr >5000)    { dumpFreq = 500; }
	if (nEntr >10000)   { dumpFreq = 1000; }
	if (nEntr >50000)   { dumpFreq = 5000; }
	if (nEntr >100000)  { dumpFreq = 10000; }
	if (nEntr >500000)  { dumpFreq = 50000; }
	if (nEntr >1000000) { dumpFreq = 100000; }
	if (nEntr >5000000) { dumpFreq = 500000; }
	if (nEntr >10000000){ dumpFreq = 1000000; }
	
	dumpFreq=10000;
	for(Long64_t entry= 0; entry < nEntr; entry++){
//        cout<<"This is entry "<<entry<<endl;
//        cout<<"--------------------------------------"<<endl;
		
        if(entry%dumpFreq == 0) {
			std::cout << "processing entry " << entry << " out of " << nEntr << std::endl;
		}
		tree->GetEntry(entry);

		if( isMC && doOverlapRemoval){
			if (overlapRemovalTT(tree)){
				//				cout << "removing event " << entry << endl;
				continue;
			}
		}

		selector->process_objects(tree);
	   
		//add in the weights
		double weight = 1.;
		if (isMC){
			weight = _evtWeight *  ((tree->genWeight_ >= 0) ? 1 : -1);
			_PUweight    = PUweighter->getWeight(tree->nPUInfo_, tree->puBX_, tree->puTrue_);
			weight *= _PUweight;

			if (selector->Muons.size()>=1) {
				int muInd_ = selector->Muons.at(0);
                _muEffWeight    = muEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),1);
                _muIDEffWeight    = muIDEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),1);
                _muIsoEffWeight    = muIsoEffSF(tree->muPt_->at(muInd_),tree->muEta_->at(muInd_),1);
                _muTrackEffWeight    = muTrackEffSF(tree->muEta_->at(muInd_),1);
				_muWeight = _muEffWeight * _muIDEffWeight * _muIsoEffWeight * _muTrackEffWeight;
				weight *= _muWeight;
			}

			if (selector->Electrons.size()>=1) {
				int eleInd_ = selector->Electrons.at(0);
                _eleEffWeight    = eleEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),1);
                _eleIDEffWeight    = eleIDEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),1);
                _eleRecoEffWeight    = eleRecoEffSF(tree->elePt_->at(eleInd_),tree->eleSCEta_->at(eleInd_),1);
				_eleWeight = _eleEffWeight * _eleIDEffWeight * _eleRecoEffWeight;
				weight *= _eleWeight;
			}

            if (selector->Muons.size() >= 1 && selector->Electrons.size() >= 1)
            {
				int eleInd_ = selector->Electrons.at(0);
				int muInd_ = selector->Muons.at(0);
                _trigEffWeight    = trigEffSF(tree->elePt_->at(eleInd_), tree->muPt_->at(muInd_),1);
                weight *= _trigEffWeight;
            }


			_btagWeight    = getBtagSF(tree, selector, "central", reader, evtPick->NBjet_ge);
            weight *= _btagWeight;

            if (applyTopptWeight)
            {
                _topptWeight = topPtWeight(tree);
                weight *= _topptWeight;
            }
		}

		evtPick->process_event(tree,selector,weight);

        if (evtPick->passPresel_emu && selector->bJets.size() > 0) 
        {
            //cout<<"Event "<<tree->event_<<"\tweight = "<<weight<<flush<<endl;
            cout<<"Event "<<tree->event_<<"\tPUweight "<<_PUweight<<"\t_btagWeight "<<_btagWeight<<flush<<endl;
            //cout<<"This is entry "<<entry<<endl;
//            cout<<"nEle =  "<<selector->Electrons.size()<<"\tnMu = "<<selector->Muons.size()<<endl;
//            cout<<"--------------------------------------"<<endl<<flush;
        }
		// if (evtPick->passPresel_mu){
		// 	cout << tree->event_ << endl;// "  " << tree->phoEt_->at(selector->PhotonsPresel.at(0)) << endl;
		// 	cout << tree->event_ << endl;// "  " << tree->phoEt_->at(selector->PhotonsPresel.at(0)) << endl;
		// }

	}

	evtPick->print_cutflow_emu(evtPick->cutFlow_emu);
    string outputDir(av[2]);
    string outputFileName = outputDir + "/" + sampleType + "_cutflow.root";
	TFile* outputFile = new TFile(outputFileName.c_str(),"RECREATE");

	outputFile->cd();
	evtPick->cutFlow_emu->Write();
	evtPick->cutFlowWeight_emu->Write();
	outputFile->Close();


	// std::map<std::string, TH1F*> histMap;
	// // copy histograms
	// for(int fileInd = 3; fileInd < ac; ++fileInd){
	// 	TFile* tempFile = TFile::Open(av[fileInd], "READ");
	// 	TIter next(((TDirectory*)tempFile->Get("ggNtuplizer"))->GetListOfKeys());
	// 	TObject* obj;
	// 	while ((obj = next())){
	// 		std::string objName(obj->GetName());
	// 		if( objName != "EventTree"){
	// 			TH1F* hist = (TH1F*)tempFile->Get(("ggNtuplizer/"+objName).c_str());
	// 			if( histMap.find(objName) != histMap.end() ){
	// 				histMap[objName]->Add(hist);
	// 			}
	// 			else {
	// 				hist->SetDirectory(0);
	// 				histMap[objName] = hist;
	// 			}
	// 		}
	// 	}
	// 	tempFile->Close();
	// }
	
	// ggDir->cd();
	// for(std::map<std::string, TH1F*>::iterator it = histMap.begin(); it!= histMap.end(); ++it){
	// 	it->second->SetDirectory(ggDir);
	// 	it->second->Write();
	// }
	// outFile->Close();
	
	return 0;
}


double getBtagSF(EventTree *tree, Selector *selector,  string sysType, BTagCalibrationReader reader, int NBjet_ge)
{
    // Saving weights w(0|n), w(1|n), w(2|n)
    vector<double> btagWeights;
    vector<double> btagSF;

    double weight0tag = 1.0;        //w(0|n)
    double weight1tag = 0.0;        //w(1|n)

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
            //          if (sysType=="central") cout << tree->event_ << " " << *bjetInd << " " << jetpt << " " << jeteta << " " << jetflavor << " " << SFb<<endl;
        }

        // if 
        // if (SFb==0 && sysType=="central"){
        //  cout << tree->event_ << " " << *bjetInd << " " << jetpt << " " << jeteta << " " << jetflavor << endl;
        // }
        btagSF.push_back(SFb);
    }

    if(selector->bJets.size() == 0) {
        btagWeights.push_back(1.0);
        btagWeights.push_back(0.0);
        btagWeights.push_back(0.0);
        
        if (NBjet_ge == 0)
        {
            return 1.0;
        }
        else if (NBjet_ge == 1)
        {
            return (1.0 - btagWeights.at(0));
        }
        else if (NBjet_ge == 2)
        {
            return btagWeights.at(2);
        }
//        return btagWeights;

    } else if (selector->bJets.size() == 1) {
        btagWeights.push_back(1-btagSF.at(0));
        btagWeights.push_back(btagSF.at(0));
        btagWeights.push_back(0.0);
        if (NBjet_ge == 0)
        {
            return 1.0;
        }
        else if (NBjet_ge == 1)
        {
            return (1.0 - btagWeights.at(0));
        }
        else if (NBjet_ge == 2)
        {
            return btagWeights.at(2);
        }

//        return btagWeights;

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
        if (NBjet_ge == 0)
        {
            return 1.0;
        }
        else if (NBjet_ge == 1)
        {
            return (1.0 - btagWeights.at(0));
        }
        else if (NBjet_ge == 2)
        {
            return btagWeights.at(2);
        }
    }
}

/*
double getBtagSF(EventTree *tree, Selector *selector,  string sysType, BTagCalibrationReader reader, int NBjet_ge){
	
	double weight0tag = 1.0; 		//w(0|n)
	double weight1tag = 0.0;		//w(1|n)

	double jetpt;
	double jeteta;
	int jetflavor;
	double SFb;
	double SFb2;

	if(selector->bJets.size() == 0) {
		return 1.0;
	}

	// We are following the method 1c from the twiki
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagSFMethods#1c_Event_reweighting_using_scale

	for(std::vector<int>::const_iterator bjetInd = selector->bJets.begin(); bjetInd != selector->bJets.end(); bjetInd++){
		jetpt = tree->jetPt_->at(*bjetInd);
		jeteta = fabs(tree->jetEta_->at(*bjetInd));
		jetflavor = abs(tree->jetPartonID_->at(*bjetInd));
		
		if (jetflavor == 5) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_B, jeteta, jetpt); 
		else if(jetflavor == 4) SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_C, jeteta, jetpt); 
		else SFb = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_UDSG, jeteta, jetpt); 

		weight0tag *= 1.0 - SFb;


		// We also have to calculate the weight for having 1 tag, given N
		double prod = 1.;
		if (NBjet_ge==2){
			for(std::vector<int>::const_iterator bjetInd2 = selector->bJets.begin(); bjetInd2 != selector->bJets.end(); bjetInd2++){
				if (*bjetInd==*bjetInd2) continue;

				jetpt = tree->jetPt_->at(*bjetInd2);
				jeteta = fabs(tree->jetEta_->at(*bjetInd2));
				jetflavor = abs(tree->jetPartonID_->at(*bjetInd2));

				if (jetflavor == 5) SFb2 = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_B, jeteta, jetpt); 
				else if(jetflavor == 4) SFb2 = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_C, jeteta, jetpt); 
				else SFb2 = reader.eval_auto_bounds(sysType, BTagEntry::FLAV_UDSG, jeteta, jetpt); 

				//product of (1-SFi), i!=j in twiki example (method 1c)
				prod *= 1.0 - SFb2;
			}

			//w(1|n) sum, SFj times product of 1-SFi
			weight1tag += prod*SFb;
		}
	}

	return 1.0 - weight0tag - weight1tag;
}
*/

double eleEffSF(double elePt, double eleSCEta, int sysLvl)
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

double eleIDEffSF(double elePt, double eleSCEta, int sysLvl)
{
    // Ele ID scale factor
    double ID = eleID_SF->GetBinContent(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    if (sysLvl == 2)
        ID += eleID_SF->GetBinError(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    else if (sysLvl == 0)
        ID -= eleID_SF->GetBinError(eleID_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));

    return ID;
}

double eleRecoEffSF(double elePt, double eleSCEta, int sysLvl)
{
    // Ele Reco scale factor
    double reco = eleReco_SF->GetBinContent(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    if (sysLvl == 2)
        reco += eleReco_SF->GetBinError(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));
    else if (sysLvl == 0)
        reco -= eleReco_SF->GetBinError(eleReco_SF->FindBin(eleSCEta, max(25.0, min(150.0, elePt))));

    return reco;
}

double muEffSF(double muPt, double muEta, int sysLvl)
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

double muIDEffSF(double muPt, double muEta, int sysLvl)
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

double muIsoEffSF(double muPt, double muEta, int sysLvl)
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

double muTrackEffSF(double muEta, int sysLvl)
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

double trigEffSF(double elePt, double muPt, int sysLvl)
{
    double sf = trigger_SF->GetBinContent(trigger_SF->FindBin(min(99.9, max(elePt, muPt)), min(99.9, min(elePt, muPt))));
    if (sysLvl == 2)
        sf += trigger_SF->GetBinError(trigger_SF->FindBin(min(99.9, max(elePt, muPt)), min(99.9, min(elePt, muPt))));
    else if (sysLvl == 0)
        sf -= trigger_SF->GetBinError(trigger_SF->FindBin(min(99.9, max(elePt, muPt)), min(99.9, min(elePt, muPt))));

    return sf;
}

double SFtop(double pt){
    return exp(0.0615 - 0.0005*pt);
}

double topPtWeight(EventTree *tree)
{
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

