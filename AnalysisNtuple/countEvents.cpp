#include<iostream>
#include<string>
#include"EventTree.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>
#include<TH1F.h>

using std::cout;
using std::endl;

int main(int ac, char** av){
	if(ac < 2){
		std::cout << "usage: ./countEvents inputFile[s]" << std::endl;
		return -1;
	}
	EventTree* tree = new EventTree(ac-1, av+1);
	Long64_t nEntr = tree->GetEntries();

    Double_t* bins = new Double_t[3];
    bins[0] = -9999999999;
    bins[1] = 0;
    bins[2] = 9999999999;
    TH1F* h = new TH1F("h","h",2,bins);
    tree->chain->Draw("genWeight>>h");

    cout<<"Positive entries: "<<(int)h->GetBinContent(2)<<endl;
    cout<<"Negative entries: "<<(int)h->GetBinContent(1)<<endl;
    cout<<"------------------------------"<<endl;
    cout<<"Net entries: "<<(int)(h->GetBinContent(2) - h->GetBinContent(1))<<endl<<endl;
    cout<<"Total entries: "<<nEntr<<endl<<endl;
    

	return 0;
}
