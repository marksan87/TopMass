#include<iostream>
#include<string>
#include"EventTree.h"
#include<TFile.h>
#include<TTree.h>
#include<TDirectory.h>
#include<TObject.h>

using std::cout;
using std::endl;

int main(int ac, char** av){
	if(ac < 2){
		std::cout << "usage: ./countEvents inputFile[s]" << std::endl;
		return -1;
	}
	EventTree* tree = new EventTree(ac-1, av+1);
	Long64_t nEntr = tree->GetEntries();

    cout<<"Total entries: "<<nEntr<<endl<<endl;

	return 0;
}
