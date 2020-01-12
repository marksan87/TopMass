.PHONY: JEC countEvents

all: JEC Selector.o EventTree.o EventPick.o makeSkim makeAnalysisNtuple 

RoccoR.o: RocMuonCorrections/RoccoR.cc
	g++ -c -I`root-config --incdir` -std=c++11 RocMuonCorrections/RoccoR.cc -o RocMuonCorrections/RoccoR.o

countEvents: EventTree.o
	g++ -I`root-config --incdir` `root-config --libs` -std=c++11 EventTree.o countEvents.cpp -o countEvents

makeCutflows: Selector.o ScaleFactors.h EventPick.o EventTree.o PUReweight.cpp BTagCalibrationStandalone.o makeCutflows.cpp OverlapRemove.cpp RocMuonCorrections/RoccoR.o
	g++ -o makeCutflows `root-config --libs` -I`root-config --incdir` -std=c++11 EventTree.o EventPick.o Selector.o RocMuonCorrections/RoccoR.o PUReweight.cpp OverlapRemove.cpp BTagCalibrationStandalone.o makeCutflows.cpp 

makeSkim: Selector.o EventPick.o EventTree.o  makeSkim.cpp OverlapRemove.cpp RocMuonCorrections/RoccoR.o
	g++ -o makeSkim `root-config --libs` -I`root-config --incdir` -std=c++11 EventTree.o EventPick.o Selector.o RocMuonCorrections/RoccoR.o  OverlapRemove.cpp makeSkim.cpp 

EventTree.o: EventTree.cpp EventTree.h
	g++ -c -I`root-config --incdir` -std=c++11 EventTree.cpp

BTagCalibrationStandalone.o: BTagCalibrationStandalone.cpp BTagCalibrationStandalone.h
	g++ -c -I`root-config --incdir` -std=c++11 BTagCalibrationStandalone.cpp

JEC: JEC/FactorizedJetCorrector.cpp JEC/JetCorrectorParameters.cpp JEC/SimpleJetCorrector.cpp JEC/JetCorrectionUncertainty.cpp JEC/SimpleJetCorrectionUncertainty.cpp
	$(MAKE) -C JEC all 

makeAnalysisNtuple: Selector.o EventPick.o EventTree.o ScaleFactors.h makeAnalysisNtuple.C makeAnalysisNtuple.h OverlapRemove.cpp JetResolutions.h PUReweight.cpp PUReweight.h BTagCalibrationStandalone.o ScaleFactors.h JEC/JECvariation.o TopEventCombinatorics.cpp RocMuonCorrections/RoccoR.o
	g++ -o makeAnalysisNtuple `root-config --libs` -I`root-config --incdir` -std=c++11 makeAnalysisNtuple.C EventTree.o EventPick.o Selector.o  OverlapRemove.cpp  PUReweight.cpp BTagCalibrationStandalone.o JEC/FactorizedJetCorrector.o JEC/JetCorrectorParameters.o JEC/SimpleJetCorrector.o JEC/JetCorrectionUncertainty.o JEC/SimpleJetCorrectionUncertainty.o JEC/JECvariation.o METzCalculator.cpp TopEventCombinatorics.cpp RocMuonCorrections/RoccoR.o

Selector.o: EventTree.o Selector.cpp Selector.h
	g++ -c -I`root-config --incdir` -std=c++11 Selector.cpp

EventPick.o: Selector.o EventPick.cpp EventPick.h
	g++ -c -I `root-config --incdir` -std=c++11 EventPick.cpp 

clean:
	rm EventTree.o Selector.o EventPick.o BTagCalibrationStandalone.o
	$(MAKE) -C JEC clean
