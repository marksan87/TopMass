#!/usr/bin/env python
from ROOT import TH1F, TFile, TChain, TCanvas, gROOT, gDirectory
from HistogramListDict import GetHistogramInfo
import sys
from sampleInformation import *
import os
import sys
from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser()

parser.add_argument("-s", "--sample", dest="sample", default="", help="Specify which sample to run on" )
parser.add_argument("-l", "--level", dest="level", default="", help="Specify up/down of systematic")
parser.add_argument("--syst", "--systematic", dest="systematic", default="", help="Specify which systematic to run on")
parser.add_argument("--addPlots","--addOnly", dest="onlyAddPlots", default=False,action="store_true",
                     help="Use only if you want to add a couple of plots to the file, does not remove other plots" )
parser.add_argument("-o","--output", dest="outputFileName", default="hists",
                     help="Give the name of the root file for histograms to be saved in (default is hists.root)" )
parser.add_argument("--plot", dest="plotList",action="store", nargs='*',
                     help="Add plots" )
parser.add_argument("--multiPlots", "--multiplots", dest="multiPlotList",action="append",
                     help="Add plots" )
parser.add_argument("--testone", "--testoneplot", dest="testoneplot",action="store_true",default=False,
                     help="test one plot without replacing it in the original one" )
parser.add_argument("--allPlots","--AllPlots", dest="makeAllPlots",action="store_false",default=True,
                     help="Make full list of plots in histogramDict" )
parser.add_argument("--morePlots","--MorePlots","--makeMorePlots", dest="makeMorePlots",action="store_true",default=False,
                     help="Make larger list of plots in histogramDict (mostly object kinematics)" )
parser.add_argument("--genPlots","--genPlots", dest="makegenPlots",action="store_true",default=False,
                     help="Make only plots for 2D histograms" )
parser.add_argument("--quiet", "-q", dest="quiet",default=False,action="store_true",
                     help="Quiet outputs" )


args = parser.parse_args()

syst = args.systematic
if syst=="":
	runsystematic = False
else:
	runsystematic = True



gROOT.SetBatch(True)


sample = args.sample
level = args.level.lower()  # Make lowercase
testoneplot=args.testoneplot
onlyAddPlots = args.onlyAddPlots
outputFileName = args.outputFileName
makeAllPlots = args.makeAllPlots
makeMorePlots = args.makeMorePlots
makegenPlots=args.makegenPlots
runQuiet = args.quiet

if not runQuiet and runsystematic: print "Systematic run"


nJets = 2
nBJets = 1
if testoneplot:
	outputFileName="hist_new"

dir_=""
Lumi = 1.
Q2 = 1.
Pdf = 1.
topptWeight = 1.
Pileup ="PUweight"
#EleEff= "eleEffWeight"
#MuEff = "muEffWeight"
EleIDEff= "eleIDEffWeight"
EleRecoEff= "eleRecoEffWeight"
MuIDEff = "muIDEffWeight"
MuIsoEff = "muIsoEffWeight"
MuTrackEff = "muTrackEffWeight"
TrigEff = "trigEffWeight"
evtWeight ="evtWeight"
extraCuts = ""
btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]

# Systematics with separate analysis ntuples
separateSystSamples = ["isr", "fsr", "EleScale", "EleSmear", "MuScale", "JEC", "JER"]

#atleast 0, atleast 1, atleast 2, exactly 1, btagWeight[0] = exactly 0

sampleListName = sample


#if (sample=="TTbar" or sample=="ST_tW") and syst in separateSystSamples: 
if ("TTbar" in sample or "ST_tW" in sample) and syst in separateSystSamples: 
    if (syst=="isr" or syst=="fsr"):
        sampleListName+="_%s" % syst
#        samples={"TTbar"     : [["TTbarPowheg_AnalysisNtuple.root",
#                               #"TTbarPowheg2_AnalysisNtuple.root",
#                               #"TTbarPowheg3_AnalysisNtuple.root",
#                               #"TTbarPowheg4_AnalysisNtuple.root",
#                               ],
#                              kRed+1,
#                              "t#bar{t}",
#                              isMC
#                              ],
#                }
    elif syst=="EleScale": 
        sampleListName+="_EleScale"

    elif syst=="EleSmear": 
        sampleListName+="_EleSmear"

    elif syst=="MuScale": 
        sampleListName+="_MuScale"

    elif syst=="JEC":
        sampleListName+="_JEC"

    elif syst=="JER":
        sampleListName+="_JER"

    if level == "up":
        sampleListName+="Up"
    else:
        sampleListName+="Down"


analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/msaunder/13TeV_AnalysisNtuples/emu/V08_00_26_07/"
outputhistName = "histograms/%s"%outputFileName
if runsystematic:
    if syst=="PU":
        if level=="up":
            Pileup = "PUweight_Up"
        else:
            Pileup = "PUweight_Do"

        outputhistName = "histograms/%sPU_%s"%(outputFileName,level)

    elif syst=="Lumi":
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopSystematics#Luminosity
        # For 2016 data, 2.5% variation
        if level=="up":
            Lumi = 1.025
        else:
            Lumi = 0.975

        outputhistName = "histograms/%sLumi_%s"%(outputFileName,level)

    elif 'Q2' in syst:
        if level=="up":
            Q2="q2weight_Up"
        else:
            Q2="q2weight_Do"
        
        outputhistName = "histograms/%sQ2_%s"%(outputFileName,level)

    elif 'Pdf' in syst:
        if syst=="Pdf":
            if level=="up":
                Pdf="pdfweight_Up"
            else:
                Pdf="pdfweight_Do"
            outputhistName = "histograms/%sPdf_%s"%(outputFileName,level)

        else:
            if type(eval(syst[3:]))==type(int()):
                pdfNumber = eval(syst[3:])
                Pdf="pdfSystWeight[%i]/pdfWeight"%(pdfNumber-1)
                outputhistName = "histograms/%sPdf/Pdf%i"%(outputFileName,pdfNumber)				

    elif 'toppt' in syst:
        topptWeight = "topptWeight"
        outputhistName = "histograms/%stoppt" % outputFileName
    
    elif 'JEC' in syst:
        outputhistName = "histograms/%sJEC_%s"%(outputFileName,level)
    
    elif 'JER' in syst:
        outputhistName = "histograms/%sJER_%s"%(outputFileName,level)
    
    
#    elif 'MuEff' in syst:
#        if level=="up":
#            MuEff = "muEffWeight_Up"
#        else:
#            MuEff = "muEffWeight_Do"
#
#        outputhistName = "histograms/%sMuEff_%s"%(outputFileName,level)
#
#    elif 'EleEff' in syst:
#        if level=="up":
#            EleEff = "eleEffWeight_Up"
#        else:
#            EleEff = "eleEffWeight_Do"
#
#        outputhistName = "histograms/%sEleEff_%s"%(outputFileName,level)

#    elif 'EleScale' in syst:
#        outputhistName = "histograms/%sEleScale_%s"%(outputFileName,level)
#    
#    elif 'EleSmear' in syst:
#        outputhistName = "histograms/%sEleSmear_%s"%(outputFileName,level)
    
    elif 'EleIDEff' in syst:
        if level=="up":
            EleIDEff = "eleIDEffWeight_Up"
        else:
            EleIDEff = "eleIDEffWeight_Do"

        outputhistName = "histograms/%sEleIDEff_%s"%(outputFileName,level)
    
    elif 'EleRecoEff' in syst:
        if level=="up":
            EleRecoEff = "eleRecoEffWeight_Up"
        else:
            EleRecoEff = "eleRecoEffWeight_Do"

        outputhistName = "histograms/%sEleRecoEff_%s"%(outputFileName,level)
    
    elif 'EleScale' in syst:
        outputhistName = "histograms/%sEleScale_%s"%(outputFileName,level)
    
    elif 'EleSmear' in syst:
        outputhistName = "histograms/%sEleSmear_%s"%(outputFileName,level)
    
    elif 'MuScale' in syst:
        outputhistName = "histograms/%sMuScale_%s"%(outputFileName,level)
#    elif 'MuScale' in syst:
#        if level=="up":
#            MuScale = "muScaleWeight_Up"
#        else:
#            MuScale = "muScaleWeight_Do"
#
#        outputhistName = "histograms/%sMuScale_%s"%(outputFileName,level)

    elif 'MuIDEff' in syst:
        if level=="up":
            MuIDEff = "muIDEffWeight_Up"
        else:
            MuIDEff = "muIDEffWeight_Do"

        outputhistName = "histograms/%sMuIDEff_%s"%(outputFileName,level)

    elif 'MuIsoEff' in syst:
        if level=="up":
            MuIsoEff = "muIsoEffWeight_Up"
        else:
            MuIsoEff = "muIsoEffWeight_Do"

        outputhistName = "histograms/%sMuIsoEff_%s"%(outputFileName,level)

    elif 'MuTrackEff' in syst:
        if level=="up":
            MuTrackEff = "muTrackEffWeight_Up"
        else:
            MuTrackEff = "muTrackEffWeight_Do"

        outputhistName = "histograms/%sMuTrackEff_%s"%(outputFileName,level)

    elif 'TrigEff' in syst:
        if level=="up":
            TrigEff = "trigEffWeight_Up"
        else:
            TrigEff = "trigEffWeight_Do"

        outputhistName = "histograms/%sTrigEff_%s"%(outputFileName,level)

    elif 'BTagSF' in syst:
        if level=="up":
            btagWeightCategory = ["1","(1-btagWeight_Up[0])","(btagWeight_Up[2])","(btagWeight_Up[1])"]
        else:
            btagWeightCategory = ["1","(1-btagWeight_Do[0])","(btagWeight_Do[2])","(btagWeight_Do[1])"]

        outputhistName = "histograms/%sBTagSF_%s"%(outputFileName,level)
#elif syst=="isr" or syst=="fsr":
#	if level=="up":
#		analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples/muons/V08_00_26_07/%s_up_"%(syst)
         #               outputhistName = "histograms/mu/%s%s_up"%(outputFileName,syst)
#	if level=="down":
#		analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples/muons/V08_00_26_07/%s_down_"%(syst)
         #               outputhistName = "histograms/mu/%s%s_down"%(outputFileName,syst)

    else:
        if level=="up":
            #analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_AnalysisNtuples/systematics_muons/V08_00_26_07/%s_up_"%(syst)
            analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/msaunder/13TeV_AnalysisNtuples/emu/V08_00_26_07/%s_up_"%(syst)
            outputhistName = "histograms/%s%s_up"%(outputFileName,syst)
        if level=="down":
            analysisNtupleLocation = "root://cmseos.fnal.gov//store/user/msaunder/13TeV_AnalysisNtuples/emu/V08_00_26_07/%s_down_"%(syst)
            outputhistName = "histograms/%s%s_down"%(outputFileName,syst)


btagWeight = btagWeightCategory[nBJets]


#weights = "%s*%s*%s*%s*%s*%s*%s*%s*%s*%s"%(evtWeight,Pileup,EleEff,MuEff,TrigEff,Lumi,Q2,Pdf,btagWeight,topptWeight)
weights = "%s*%s*%s*%s*%s*%s*%s*%s*%s*%s*%s*%s*%s"%(evtWeight,Pileup,EleIDEff,EleRecoEff,MuIDEff,MuIsoEff,MuTrackEff,TrigEff,Lumi,Q2,Pdf,btagWeight,topptWeight)
print "using weights", weights
if not runQuiet: print " the output folder is:", outputhistName


histogramInfo = GetHistogramInfo(extraCuts,nBJets)


multiPlotList = args.multiPlotList

plotList = args.plotList
if plotList is None:
    if makeAllPlots:
        plotList = histogramInfo.keys()
        if not runQuiet: print "Making full list of plots"
    elif not multiPlotList is None:
        plotList = []
        for plotNameTemplate in multiPlotList:
            thisPlotList = []
            for plotName in histogramInfo.keys():
                if plotNameTemplate in plotName:
                    thisPlotList.append(plotName)
            thisPlotList.sort()
            if not runQuiet: 
                print '---'
                print '  Found the following plots matching the name key %s'%plotNameTemplate
                print '    ',thisPlotList
            plotList += thisPlotList

        #take the set to avoid duplicates (if multiple plot name templates are used, and match the same plot)
        plotList = list(set(plotList))


    else:
	    pass

plotList.sort()
if not runQuiet: print '-----'
if not runQuiet: print "Making the following plots:"
if not runQuiet: 
    for p in plotList: print "%s,"%p,
if not runQuiet: print
if not runQuiet: print '-----'

histogramsToMake = plotList

allHistsDefined = True
for hist in histogramsToMake:
    if not hist in histogramInfo:
        print "Histogram %s is not defined in HistogramListDict.py"%hist
        allHistsDefined = False
if not allHistsDefined:
    sys.exit()

transferFactor = 1.

histograms=[]
canvas = TCanvas()
#sample = sys.argv[-1]

if not sampleListName in samples.keys():
    print "Sample isn't in list:", sampleListName 
    print samples.keys()
    sys.exit()


tree = TChain("AnalysisTree")
fileList = samples[sampleListName][0]
for fileName in fileList:
    tree.Add("%s%s"%(analysisNtupleLocation,fileName))
    print "%s%s"%(analysisNtupleLocation,fileName)

print "sample =",sample

#print "Number of events:", tree.GetEntries()

for hist in histogramsToMake:
    h_Info = histogramInfo[hist]
    if not runQuiet: print "filling", h_Info[1], sample
    evtWeight = ""
#	print TH1F("%s_%s"%(h_Info[1],sample),"%s_%s"%(h_Info[1],sample),h_Info[2][0],h_Info[2][1],h_Info[2][2])
    histograms.append(TH1F("%s_%s"%(h_Info[1],sample),"%s_%s"%(h_Info[1],sample),h_Info[2][0],h_Info[2][1],h_Info[2][2]))
    if h_Info[4]=="":
        evtWeight = "%s%s"%(h_Info[3],weights)
    else:
        evtWeight = h_Info[4]

    if "Data" in sample:
        evtWeight = "%s%s"%(h_Info[3],weights)

    if evtWeight[-1]=="*":
        evtWeight= evtWeight[:-1]
    
    #print "evtWeight =", evtWeight
    tree.Draw("%s>>%s_%s"%(h_Info[0],h_Info[1],sample),evtWeight)

if not os.path.exists(outputhistName):
    os.makedirs(outputhistName)

outputFile = TFile("%s/%s.root"%(outputhistName,sample),"update")
print "%s/%s.root\n\n"%(outputhistName,sample)
for h in histograms:
    outputFile.Delete("%s;*"%h.GetName())
    if onlyAddPlots:
        gDirectory.Delete("%s;*"%(h.GetName()))
    h.Write()

outputFile.Close()

