#include<iostream>
#include<string>
#include"EventTree.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>
#include<TH1F.h>
#include<TROOT.h>
using std::cout;
using std::endl;

int main(int ac, char** av){
	if(ac < 2){
		std::cout << "usage: ./countEvents inputFile[s]" << std::endl;
		return -1;
	}
    
    gROOT->SetBatch(true);
	EventTree* tree = new EventTree(ac-1, av+1);
	Long64_t nEntr = tree->GetEntries();

    Double_t* bins = new Double_t[3];
    TH1D* h = new TH1D("h","h",2, 0, 2);
    tree->chain->Draw("(genWeight >= 0 ? 0.5 : 1.5)>>h");

    long pos = (long)h->GetBinContent(1);
    long neg = (long)h->GetBinContent(2);
    long net = pos - neg;
    long tot = pos + neg;

    cout<<endl<<"Input tree entries: "<<nEntr<<endl<<endl;
    cout<<"Positive entries: "<<pos<<endl;
    cout<<"Negative entries: "<<neg<<endl;
    cout<<"------------------------------"<<endl;
    cout<<"Net entries: "<<net<<endl<<endl;
    cout<<"Total entries: "<<tot<<endl<<endl;
   
    if (nEntr != tot)
        cout<<"Total entries does not match input tree entries!"<<endl;

	return 0;
}
