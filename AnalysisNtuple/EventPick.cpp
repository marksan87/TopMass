#include"EventPick.h"
#include <iostream> 
#include <iomanip>
#include <cmath>


EventPick::EventPick(std::string titleIn){
	title = titleIn;
	saveCutflows = false;

	cutFlow_ele = new TH1D("cut_flow_ele","cut flow e+jets",15,-0.5,14.5);
	cutFlow_ele->SetDirectory(0);
	set_cutflow_labels_ele(cutFlow_ele); 

	cutFlow_mu = new TH1D("cut_flow_mu","cut flow mu+jets",15,-0.5,14.5);
	cutFlow_mu->SetDirectory(0);
	set_cutflow_labels_mu(cutFlow_mu); 

	cutFlow_emu = new TH1D("cut_flow_emu","cut flow dilep e+mu",15,-0.5,14.5);
	cutFlow_emu->SetDirectory(0);
	set_cutflow_labels_emu(cutFlow_emu); 
	
	cutFlowWeight_ele = new TH1D("cut_flow_weight_ele","cut flow with PU weight e+jets",15,-0.5,14.5);
	cutFlowWeight_ele->SetDirectory(0);
	set_cutflow_labels_ele(cutFlowWeight_ele);

	cutFlowWeight_mu = new TH1D("cut_flow_weight_mu","cut flow with PU weight mu+jets",15,-0.5,14.5);
	cutFlowWeight_mu->SetDirectory(0);
	set_cutflow_labels_mu(cutFlowWeight_mu);

	cutFlowWeight_emu = new TH1D("cut_flow_weight_emu","cut flow with PU weight dilep e+mu",15,-0.5,14.5);
	cutFlowWeight_emu->SetDirectory(0);
	set_cutflow_labels_emu(cutFlowWeight_emu);




	// Cut levels
	Nmu_eq = 1;
	Nele_eq = 1;
	NlooseMuVeto_le = 0;
	NlooseEleVeto_le = 0;

	LeadingLepPt = 25.;
	invMassCut = 20.;

	// These dR cuts are all done at selection level now
	// assign cut values
	//	veto_jet_dR = 0.1;
	// veto_lep_jet_dR = 0.4;
	// veto_pho_jet_dR = 0.7;
	// veto_pho_lep_dR = 0.7;

	MET_cut = 0.0;
	no_trigger = false;
	
	skimEMu = false;
	skimEE = false;
	skimMuMu = false;

	Njet_ge = 2;
	SkimNjet_ge = 2;

	NBjet_ge = 1;
	SkimNBjet_ge = 0;

	ZeroBExclusive = false;

	NlooseMuVeto_le = 0;
	NlooseEleVeto_le = 0;

}

EventPick::~EventPick(){
}

void EventPick::process_event(EventTree* tree, Selector* selector, double weight){

	//	clear_vectors();
	passSkim = false;
	passPresel_emu = false;

	passPresel_ele = false;
	passPresel_mu = false;
	passAll_ele = false;
	passAll_mu = false;

	ULong64_t HLT = tree->HLTEleMuX;

	bool Pass_trigger_emu = ( HLT >> 23 & 1 || //HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v
							  HLT >> 24 & 1 || //HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v
							  HLT >> 45 & 1 || //HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v
							  HLT >> 46 & 1 || //HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v
							  HLT >> 51 & 1 || //HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v
							  HLT >> 52 & 1); //HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v


	bool Pass_trigger_mu  = ( HLT >> 19 & 1 || HLT >> 20 & 1) || no_trigger;
	bool Pass_trigger_ele = ( HLT >> 3 & 1) || no_trigger;

	if (saveCutflows) {
		cutFlow_emu->Fill(0.0); // Input events
		cutFlow_ele->Fill(0.0); // Input events
		cutFlow_mu->Fill(0.0); // Input events
		cutFlowWeight_emu->Fill(0.0,weight);
		cutFlowWeight_ele->Fill(0.0,weight);
		cutFlowWeight_mu->Fill(0.0,weight);
	}

	passPresel_emu  = true;


	//	cout << "-------" << endl;
	// Cut events that fail ele trigger
	if( passPresel_emu &&  Pass_trigger_emu) { if (saveCutflows) {cutFlow_emu->Fill(1); cutFlowWeight_emu->Fill(1,weight); } }
	else { passPresel_emu = false;}
	if( passPresel_emu && tree->isPVGood_) { if (saveCutflows) {cutFlow_emu->Fill(2); cutFlowWeight_emu->Fill(2,weight); } }
	else { passPresel_emu = false;}



	if ( passPresel_emu || passPresel_ele || passPresel_mu ) {
        selector->process_objects(tree);
	}
	else {
		return;
	}

	double mu0pt = 0, mu1pt = 0, ele0pt = 0, ele1pt = 0;
	double mu0Q = 0, mu1Q = 0, ele0Q = 0, ele1Q = 0;

	// Cut on events with at least 1 mu and 1 ele 
	if( passPresel_emu && selector->Muons.size() >= 1 && selector->Electrons.size() >= 1){
		mu0pt = tree->muPt_->at(selector->Muons.at(0));
		mu0Q = tree->muCharge_->at(selector->Muons.at(0));
		ele0pt = tree->elePt_->at(selector->Electrons.at(0));
		ele0Q = tree->eleCharge_->at(selector->Electrons.at(0));
		int muInd = selector->Muons.at(0);
		int eleInd = selector->Electrons.at(0);
		lepton1.SetPtEtaPhiE(tree->muPt_->at(muInd),tree->muEta_->at(muInd),tree->muPhi_->at(muInd),tree->muEn_->at(muInd));
		lepton2.SetPtEtaPhiE(tree->elePt_->at(eleInd),tree->eleEta_->at(eleInd),tree->elePhi_->at(eleInd),tree->eleEn_->at(eleInd));

		if (selector->Muons.size()>1){
			mu1pt = tree->muPt_->at(selector->Muons.at(1));
			mu1Q = tree->muCharge_->at(selector->Muons.at(1));
		}
		if (selector->Electrons.size()>1){
			ele1pt = tree->elePt_->at(selector->Electrons.at(1));
			ele1Q = tree->eleCharge_->at(selector->Electrons.at(1));
		}

		if (saveCutflows){cutFlow_emu->Fill(3); cutFlowWeight_emu->Fill(3,weight);}
	}
	else { passPresel_emu = false;}


	//skim just requires 2 of the top 3 leptons to be oppositely charge emu pair
	if (skimEMu){
		if (passPresel_emu){
			//3 possible combinations allowed, mu0/e0, mu0/e1, mu1/e0
			if ( mu0Q*ele0Q < -0.5 || mu0Q*ele1Q < -0.5 || mu1Q*ele0Q < -0.5 ){	 //cut at < -0.5 to avoid potential weird rounding/precision errors (should be -1)
				if ( selector->Jets.size() >= SkimNjet_ge && selector->bJets.size() >= SkimNBjet_ge ){ passSkim = true;}
			}
		}
		return; //if running on the skim, there is no reason to run the rest of the selection requirements
	}

	// Charges of leading muon and electron are opposite
	// Muon and electron are two leading leptons
	// Leading muon is higher than second electron
	// Leading electron is higher than second muon 
	// Leading lepton is pt of at least LeadingLepPt
	if (passPresel_emu && mu0Q*ele0Q < -0.5 && mu0pt >= ele1pt && ele0pt >= mu1pt && (mu0pt>LeadingLepPt || ele0pt > LeadingLepPt) ){   
		if (saveCutflows){cutFlow_emu->Fill(4); cutFlowWeight_emu->Fill(4,weight);}
	}
	else { passPresel_emu = false;}


	//InvariantMass cut

	//cout << (lepton1+lepton2).M() << endl;
	if (passPresel_emu && (lepton1+lepton2).M() > invMassCut){
		if (saveCutflows){cutFlow_emu->Fill(5); cutFlowWeight_emu->Fill(4,weight);}
	}
	else { passPresel_emu = false;}
		
	
	
	// NJet cuts 
	// Implemented in this way (with a loop) to check for numbers failing each level of cut < Njet cut, and filling cutflow histo
	// cutflow histo will not be filled for bins where the cut is > Njet_ge (ex, if cut is at 3, Njets>=4 bin is left empty)
	for (int ijetCut = 1; ijetCut <= Njet_ge; ijetCut++){
		if(passPresel_emu && selector->Jets.size() >= ijetCut ) { if (saveCutflows) {cutFlow_emu->Fill(5+ijetCut); cutFlowWeight_emu->Fill(5+ijetCut,weight);}}
		else passPresel_emu = false;
	}

	// Nbtag cuts 
	if (!ZeroBExclusive){
		for (int ibjetCut = 1; ibjetCut <= NBjet_ge; ibjetCut++){
			if(passPresel_emu && selector->bJets.size() >= ibjetCut ) { if (saveCutflows) {cutFlow_emu->Fill(9+ibjetCut); cutFlowWeight_emu->Fill(9+ibjetCut,weight);}}
			else passPresel_emu = false;
		}
	} else {
		if(passPresel_emu && selector->bJets.size() !=0) passPresel_emu = false;
	}

	// MET cut 
	if(passPresel_emu && tree->pfMET_ >= MET_cut) { if (saveCutflows) {cutFlow_emu->Fill(12); cutFlowWeight_emu->Fill(12,weight);}}
	else passPresel_emu = false;

	
}

void EventPick::print_cutflow_mu(TH1D* _cutflow){
	std::cout << "Cut-Flow for the event selector: " << title << std::endl;
	std::cout << "Input Events :                " << _cutflow->GetBinContent(1) << std::endl;
	std::cout << "Passing Trigger               " << _cutflow->GetBinContent(2) << std::endl;
	std::cout << "Has Good Vtx               " << _cutflow->GetBinContent(3) << std::endl;
	std::cout << "Events with 1 muon     " << _cutflow->GetBinContent(4) << std::endl;
	std::cout << "Events with no loose muons " << _cutflow->GetBinContent(5) << std::endl;
	std::cout << "Events with no electrons " << _cutflow->GetBinContent(6) << std::endl;
	std::cout << "Events with >= " << 1 << " jets        " << _cutflow->GetBinContent(7) << std::endl;
	std::cout << "Events with >= " << 2 << " jets        " << _cutflow->GetBinContent(8) << std::endl;
 	std::cout << "Events with >= " << 3 << " jets     " << _cutflow->GetBinContent(9) << std::endl;
	std::cout << "Events with >= " << 4 << " jets "<< _cutflow->GetBinContent(10) << std::endl;
	std::cout << "Events with >= " << 1 <<     " bjets "<< _cutflow->GetBinContent(11) << std::endl;
	std::cout << "Events with >= " << 2 << " bjets       " << _cutflow->GetBinContent(12) << std::endl;
	std::cout << "Events passing MET cut       " << _cutflow->GetBinContent(14) << std::endl;
	std::cout << "Events with >= 1 photon      " << _cutflow->GetBinContent(15) << std::endl;
	std::cout << std::endl;
}

void EventPick::print_cutflow_ele(TH1D* _cutflow){
	std::cout << "Cut-Flow for the event selector: " << title << std::endl;
	std::cout << "Input Events :                " << _cutflow->GetBinContent(1) << std::endl;
	std::cout << "Passing Trigger               " << _cutflow->GetBinContent(2) << std::endl;
	std::cout << "Has Good Vtx               " << _cutflow->GetBinContent(3) << std::endl;
	std::cout << "Events with 1 electron     " << _cutflow->GetBinContent(4) << std::endl;
	std::cout << "Events with no loose electrons " << _cutflow->GetBinContent(5) << std::endl;
	std::cout << "Events with no muons " << _cutflow->GetBinContent(6) << std::endl;
	std::cout << "Events with >= " << 1 << " jets        " << _cutflow->GetBinContent(7) << std::endl;
	std::cout << "Events with >= " << 2 << " jets        " << _cutflow->GetBinContent(8) << std::endl;
 	std::cout << "Events with >= " << 3 << " jets     " << _cutflow->GetBinContent(9) << std::endl;
	std::cout << "Events with >= " << 4 << " jets "<< _cutflow->GetBinContent(10) << std::endl;
	std::cout << "Events with >= " << 1 <<     " bjets "<< _cutflow->GetBinContent(11) << std::endl;
	std::cout << "Events with >= " << 2 << " bjets       " << _cutflow->GetBinContent(12) << std::endl;
	std::cout << "Events passing MET cut       " << _cutflow->GetBinContent(14) << std::endl;
	std::cout << "Events with >= 1 photon      " << _cutflow->GetBinContent(15) << std::endl;
	std::cout << std::endl;
}

void EventPick::set_cutflow_labels_mu(TH1D* hist){
	hist->GetXaxis()->SetBinLabel(1,"Input");
	hist->GetXaxis()->SetBinLabel(2,"Trigger");
	hist->GetXaxis()->SetBinLabel(3,"Good Vtx");
	hist->GetXaxis()->SetBinLabel(4,"1 Muons");
	hist->GetXaxis()->SetBinLabel(5,"No Loose Muons");
 	hist->GetXaxis()->SetBinLabel(6,"Veto Electrons");
	hist->GetXaxis()->SetBinLabel(7,">=1 jet");
	hist->GetXaxis()->SetBinLabel(8,">=2 jets");
	hist->GetXaxis()->SetBinLabel(9,">=3 jets");
	hist->GetXaxis()->SetBinLabel(10,">=4 jets");
	hist->GetXaxis()->SetBinLabel(11,">=1 b-tags");
	hist->GetXaxis()->SetBinLabel(12,">=2 b-tags");
	hist->GetXaxis()->SetBinLabel(13,"MET Cut");
	hist->GetXaxis()->SetBinLabel(14,"Photon");
}

void EventPick::set_cutflow_labels_ele(TH1D* hist){
	hist->GetXaxis()->SetBinLabel(1,"Input");
	hist->GetXaxis()->SetBinLabel(2,"Trigger");
	hist->GetXaxis()->SetBinLabel(3,"Good Vtx");
	hist->GetXaxis()->SetBinLabel(4,"1 Electrons");
	hist->GetXaxis()->SetBinLabel(5,"No Loose Electrons");
 	hist->GetXaxis()->SetBinLabel(6,"Veto Muons");
	hist->GetXaxis()->SetBinLabel(7,">=1 jet");
	hist->GetXaxis()->SetBinLabel(8,">=2 jets");
	hist->GetXaxis()->SetBinLabel(9,">=3 jets");
	hist->GetXaxis()->SetBinLabel(10,">=4 jets");
	hist->GetXaxis()->SetBinLabel(11,">=1 b-tags");
	hist->GetXaxis()->SetBinLabel(12,">=2 b-tags");
	hist->GetXaxis()->SetBinLabel(13,"MET Cut");
	hist->GetXaxis()->SetBinLabel(14,"Photon");
}

void EventPick::set_cutflow_labels_emu(TH1D* hist){
	hist->GetXaxis()->SetBinLabel(1,"Input");
	hist->GetXaxis()->SetBinLabel(2,"Trigger");
	hist->GetXaxis()->SetBinLabel(3,"Good Vtx");
	hist->GetXaxis()->SetBinLabel(4,"At least 1 e 1 mu");
	hist->GetXaxis()->SetBinLabel(5,"Top 2 pt / Opp Ch");
 	hist->GetXaxis()->SetBinLabel(6,"");
	hist->GetXaxis()->SetBinLabel(7,">=1 jet");
	hist->GetXaxis()->SetBinLabel(8,">=2 jets");
	hist->GetXaxis()->SetBinLabel(9,">=3 jets");
	hist->GetXaxis()->SetBinLabel(10,">=4 jets");
	hist->GetXaxis()->SetBinLabel(11,">=1 b-tags");
	hist->GetXaxis()->SetBinLabel(12,">=2 b-tags");
	hist->GetXaxis()->SetBinLabel(13,"MET Cut");

}

// void EventPick::clear_vectors(){
// 	Electrons.clear();
// 	ElectronsLoose.clear();
// 	ElectronsMedium.clear();
// 	Muons.clear();
// 	MuonsLoose.clear();
// 	Jets.clear();
// 	bJets.clear();
// 	Photons.clear();
// 	LoosePhotons.clear();
// 	PhotonsPresel.clear();
// 	PhoPassChHadIso.clear();
// 	PhoPassPhoIso.clear();
// 	PhoPassSih.clear();
// }

// double EventPick::dR_jet_ele(int jetInd, int eleInd){
// 	return dR(tree->jetEta_->at(jetInd), tree->jetPhi_->at(jetInd), tree->eleSCEta_->at(eleInd), tree->elePhi_->at(eleInd));
// }
// double EventPick::dR_jet_mu(int jetInd, int muInd){
// 	return dR(tree->jetEta_->at(jetInd), tree->jetPhi_->at(jetInd), tree->muEta_->at(muInd), tree->muPhi_->at(muInd));
// }
// double EventPick::dR_jet_pho(int jetInd, int phoInd){
// 	return dR(tree->jetEta_->at(jetInd), tree->jetPhi_->at(jetInd), tree->phoSCEta_->at(phoInd), tree->phoPhi_->at(phoInd));
// }
// double EventPick::dR_ele_pho(int eleInd, int phoInd){
// 	return dR(tree->eleSCEta_->at(eleInd), tree->elePhi_->at(eleInd), tree->phoSCEta_->at(phoInd), tree->phoPhi_->at(phoInd));
// }
// double EventPick::dR_mu_pho(int muInd, int phoInd){
// 	return dR(tree->muEta_->at(muInd), tree->muPhi_->at(muInd), tree->phoSCEta_->at(phoInd), tree->phoPhi_->at(phoInd));
// }

