#!/usr/bin/env python
from ROOT import gROOT,TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, kRed,kAzure,kBlack,kRed,kOrange,kBlue,kViolet,kGreen,kPink
from sampleInformation import *
import os
import sys
from optparse import OptionParser
from argparse import ArgumentParser
from numpy import log10
from array import array
from Style import *
import CMS_lumi
from pprint import pprint
import pdb

obsTitle = {"ptll":"p_{T}(ll)", "ptpos":"p_{T}(l^{+})", "Epos":"E(l^{+})", "ptp_ptm":"p_{T}(l^{+}) + p_{T}(l^{-})", "Ep_Em":"E(l^{+}) + E(l^{-})", "Mll":"M(ll)"}

# Available systematics
tWSystematics = ["PU", "Lumi", "EleIDEff", "EleRecoEff","EleScale","EleSmear","MuIDEff","MuIsoEff","MuTrackEff","MuScale","TrigEff","JEC","JER","Q2","Pdf","isr","fsr", "DS"] 
ttSystematics = ["PU", "Lumi", "isr", "fsr", "EleIDEff", "EleRecoEff", "EleScale", "EleSmear", "MuIDEff", "MuIsoEff", "MuTrackEff", "MuScale", "TrigEff", "JEC", "JER", "Q2", "Pdf", "toppt", "hdamp", "UE", "CRerdON", "CRGluon", "CRQCD", "amcanlo", "madgraph", "herwigpp" ]
backgroundSystematics = ["PU"]  # Systematics to load for background processes
experimentalSysts = ["PU", "Lumi", "EleIDEff", "EleRecoEff", "EleScale", "EleSmear", "MuIDEff", "MuIsoEff", "MuTrackEff", "MuScale", "TrigEff", "JEC", "JER" ]
theorySysts = ["toppt", "Q2", "isr", "fsr", "Pdf", "hdamp", "UE", "CRerdON", "CRGluon", "CRQCD", "amcanlo", "madgraph", "herwigpp", "DS" ]
oneSidedSysts = ["toppt", "CRerdON", "CRGluon", "CRQCD", "DS", "amcanlo", "madgraph", "herwigpp" ]
systematics = experimentalSysts + theorySysts
systColors = { 
    "toppt":kRed,
    "LumiUp":kRed-1,
    "LumiDown":kRed-2,
    "PUUp":kBlue, 
    "PUDown":kAzure, 
    "isrUp":kAzure-1,
    "isrDown":kAzure-2,
    "fsrup":kAzure-3,
    "fsrdown":kAzure-4,
    "EleIDEffUp":kGreen,
    "EleIDEffDown":kGreen-1,
    "EleRecoEffUp":kGreen-2,
    "EleRecoEffDown":kGreen-3,
    "EleScaleUp":kGreen-4,
    "EleScaleDown":kGreen-5,
    "EleSmearUp":kGreen-6,
    "EleSmearDown":kGreen-7,
    "MuIDEffUp":kOrange,
    "MuIDEffDown":kOrange-1,
    "MuIsoEffUp":kOrange-2,
    "MuIsoEffDown":kOrange-3,
    "MuTrackEffUp":kOrange-4,
    "MuTrackEffDown":kOrange-5,
    "MuScaleUp":kOrange-6,
    "MuScaleDown":kOrange-7,
    "TrigEffUp":kOrange-8,
    "TrigEffDown":kOrange-9,
    "JECUp":kViolet,
    "JECDown":kViolet-1,
    "JERUp":kViolet-2,
    "JERDown":kViolet-3,
    "Q2Up":kPink,
    "Q2Down":kPink-1,
    "PdfUp":kPink-2,
    "PdfDown":kPink-3,
    "hdampUp":kPink-4,
    "hdampDown":kPink-5,
    "UEUp":kPink-6,
    "UEDown":kPink-7,
    "CR_erdON":kBlue+1,
    "CRGluon":kBlue+2,
    "CRQCD":kBlue+3,
    "amcanlo":kBlue+4,
    "madgraph":kBlue+5,
    "herwigpp":kBlue+6,
    "DS":kBlue+7,
    }
#systematics = ["PU", "Q2", "Pdf", "isr", "fsr", "toppt", "EleIDEff", "EleRecoEff", "EleScale", "EleSmear", "MuIDEff", "MuIsoEff", "MuTrackEff", "MuScale", "JEC", "JER"]
signal = ["TTbar", "ST_tW", "TTbar_amcanlo"]

observables = obsTitle.keys()


padRatio = 0.25
padOverlap = 0.15

#padGap = 0.01
padGap = 0.08

parser = ArgumentParser()
parser.add_argument("--overflow", dest="useOverflow",default=False,action="store_true",
		  help="Add oveflow bin to the plots" )
parser.add_argument("--plot", dest="plotList",action="append",
		  help="Add plots" )
parser.add_argument("--morePlots","--MorePlots",dest="makeMorePlots",action="store_true",default=False,
                     help="Make larger list of kinematic distributions" )
parser.add_argument("--allPlots","--allPlots",dest="makeAllPlots",action="store_false",default=True,
                     help="Make plots of all distributions" )
parser.add_argument("--file",dest="inputFile",default=None,
		  help="Specify specific input file")
parser.add_argument("--reverse", action="store_true", default=False, help="reverse stack ordering")
parser.add_argument("--reorderTop", dest="newStackListTop",action="append",
		  help="New order for stack list (which plots will be put on top of the stack)" )
parser.add_argument("--reorderBot", dest="newStackListBot",action="append",
		  help="New order for stack list (which plots will be put on top of the stack)" )
parser.add_argument("--theoryTTxs", action="store_true", default=False, help="Use theory xs of 831.76 pb instead of 803")
parser.add_argument("--norm", action="store_true", default=False, help="normalize plots")

args = parser.parse_args()

plotList = args.plotList

newStackListTop = args.newStackListTop
newStackListBot = args.newStackListBot

useOverflow = args.useOverflow

inputFile = args.inputFile
makeMorePlots = args.makeMorePlots
makeAllPlots = args.makeAllPlots

scaleTTbarXS = not args.theoryTTxs     # Scale to 803 pb, value from TOP-17-001

showUnc = False    # If true, include data/mc uncertainty in plot


_fileDir = "histograms/hists"
plotDirectory = "plots"
regionText = ""
channel = 'emu'

CMS_lumi.writeExtraText = True
CMS_lumi.extraText = "Work in Progress"

#print channel
if not inputFile is None:
	_fileDir = "histograms/%s"%inputFile
	if not _file.IsOpen():
		print "Unable to open file"
		sys.exit()



if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)


gROOT.SetBatch(True)

YesLog = True
NoLog=False

# Histogram Information:
# [X-axis title, 
#  Y-axis title,
#  Rebinning factor,
#  [x-min,x-max], -1 means keep as is
#  Extra text about region
#  log plot]

histograms_dilep = {"presel_DilepMass"   : ["m_(lepton,lepton) (GeV)", "<Events/GeV>", [20., 30., 40., 50., 60., 70., 80., 85., 95., 100., 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270.], [-1,-1], regionText, NoLog, " "],
		}




histograms = {  \
          "nVtx"            : ["Vertex multiplicity", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "nEle"            : ["Ele multiplicity", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "elePt"           : ["Ele p_{T} [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "eleSCEta"        : ["Ele SC #eta", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "elePhi"          : ["Ele #phi", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "nMu"             : ["Muon multiplicity", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "muPt"            : ["Muon p_{T} [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "muEta"           : ["Muon #eta", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "muPhi"           : ["Muon #phi", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "nJet"            : ["Jet multiplicity", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "jetPt"           : ["Jet p_{T} [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "jetEta"          : ["Jet #eta", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "jetPhi"          : ["Jet #phi", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "nBJet"           : ["BJet multiplicity", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "bjetPt"          : ["BJet p_{T} [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "bjetEta"         : ["BJet #eta", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "bjetPhi"         : ["BJet #phi", "Events", 1, [-1,-1], regionText, NoLog, " "],
          "rec_ptll"        : ["Reco p_{T}(ll) [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "rec_Mll"         : ["Reco M(ll) [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "rec_ptpos"       : ["Reco p_{T}(l^{+}) [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "rec_Epos"        : ["Reco E(l^{+}) [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "rec_ptp_ptm"     : ["Reco p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
          "rec_Ep_Em"       : ["Reco E(l^{+}) + E(l^{-}) [GeV]", "Events", 5, [-1,-1], regionText, NoLog, " "],
	      }


if not plotList is None:
	allHistsDefined = True
	for hist in plotList:
		if not hist in histograms:
			print "Histogram %s plotting information not defined" % hist
			allHistsDefined = False
	if not allHistsDefined:
		sys.exit()

if plotList is None:
    if makeAllPlots:
        plotList = histograms.keys()
        plotList.sort()


thestyle = Style()

HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
    ROOT.gROOT.ProcessLine('.L tdrstyle.C')
    ROOT.setTDRStyle()
    print "Found tdrstyle.C file, using this style."
    HasCMSStyle = True
    if os.path.isfile('CMSTopStyle.cc'):
        gROOT.ProcessLine('.L CMSTopStyle.cc+')
        style = CMSTopStyle()
        style.setupICHEPv1()
        print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
    print "Using default style defined in cuy package."
    thestyle.SetStyle()

ROOT.gROOT.ForceStyle()

stackList = sampleList[:-1]
stackList.reverse()

if args.reverse:
    stackList.reverse()

#pprint(stackList)
print "Using samples:", stackList

print "Experimental syst:", experimentalSysts
print "      Theory syst:", theorySysts 

if not newStackListTop is None:
	newStackListTop.reverse()
	for sample in newStackListTop:
		if not sample in stackList:
			print "Unknown sample name %s"%sample
			continue
		stackList.remove(sample)
		stackList.append(sample)

if not newStackListBot is None:
	newStackListBot.reverse()
	for sample in newStackListBot:
		if not sample in stackList:
			print "Unknown sample name %s"%sample
			continue
		stackList.remove(sample)
		stackList.insert(0,sample)

_channelText = ""
#_channelText = "emu"
#CMS_lumi.channelText = _channelText
#CMS_lumi.writeChannelText = True 
#CMS_lumi.writeChannelText = True 



H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W


# SetOwnership(canvas, False)
# SetOwnership(canvasRatio, False)
# SetOwnership(pad1, False)
# SetOwnership(pad2, False)



legendHeightPer = 0.04
legList = stackList[:]
legList.reverse()

#legendStart = 0.69
legendStart = 0.73
legendEnd = 0.97-(R/W)

#legend = TLegend(2*legendStart - legendEnd, 1-T/H-0.01 - legendHeightPer*(len(legList)+1), legendEnd, 0.99-(T/H)-0.01)
legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)

#legendR = TLegend(0.71, 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*(len(legList)+1), 0.99-(R/W), 0.99-(T/H)/(1.-padRatio+padOverlap))


legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))

legendR.SetNColumns(2)

legendR.SetBorderSize(0)
legendR.SetFillColor(0)



legend.SetBorderSize(0)
legend.SetFillColor(0)

_file = {}
#	if finalState=="mu":
#		stackList.remove("QCDMu")
#	else:
#		stackList.remove("QCDEle")




#systematics = ["JER","JECTotal","BTagSF","Q2","Pdf","PU","MuEff","TrigEff","isr","fsr"]
#systematics = ["BTagSF","Q2","Pdf","PU","MuEff","TrigEff"] #,"isr","fsr"]
#systematics = ["PU", "Q2", "Pdf", "toppt"]
#systematics = ["PU", "Q2", "Pdf", "isr", "fsr", "toppt", "EleIDEff", "EleRecoEff", "EleScale", "EleSmear", "MuIDEff", "MuIsoEff", "MuTrackEff", "MuScale", "JEC", "JER"]
#signal = ["TTbar", "ST_tW"]


_filesys_up={}
_filesys_down={}
for sample in (stackList+["TTbar_amcanlo"]):
    _filesys_up[sample]={}
    _filesys_down[sample]={}
    if sample == "TTbar_amcanlo":
        print "Loading TTbar_amcanlo and Q2 variations"
        _file[sample] = TFile.Open("%samcanlo/TTbar.root" % _fileDir)
        _filesys_up[sample]["Q2"] = TFile.Open("histograms/histsQ2_up/%s.root" % (sample))
        _filesys_down[sample]["Q2"] = TFile.Open("histograms/histsQ2_down/%s.root" % (sample))
    else:
        _file[sample] = TFile.Open("%s/%s.root"%(_fileDir,sample),"read")
        #if sample not in signal: continue
        
        for syst in systematics:
#        if syst=="isr" or syst=="fsr":
#            if sample not in ["TTGamma" ,"TTbar"]:continue
            if syst != "PU" and sample not in signal: continue
            print "Loading sample %s  syst %s" % (sample,syst)
            if sample == "TTbar" and syst == "DS": continue
            if sample == "ST_tW" and syst not in tWSystematics: continue
            
            if syst not in oneSidedSysts:
                _filesys_up[sample][syst]=TFile.Open("histograms/hists%s_up/%s.root"%(syst,sample),"read")
                _filesys_down[sample][syst]=TFile.Open("histograms/hists%s_down/%s.root"%(syst,sample),"read")
            else:
                _filesys_up[sample][syst]=TFile.Open("histograms/hists%s/%s.root"%(syst,sample),"read")
            


sample = "Data"
_file[sample] = TFile.Open("%s/%s.root"%(_fileDir,sample),"read")

histName = plotList[0]

#print "\n\n_filesys_up"
#pprint(_filesys_up)
#print "\n\n_filesys_down"
#pprint(_filesys_down)
print "\n"

dataHist = _file["Data"].Get("%s_Data" % histName)

legend.AddEntry(dataHist, "Data", 'pe')
legendR.AddEntry(dataHist, "Data", 'pe')
#legList.remove("QCD_DD")


for sample in legList:
    hist = _file[sample].Get("%s_%s"%(histName,sample))
    hist.SetFillColor(samples[sample][1])
    hist.SetLineColor(samples[sample][1])
    legend.AddEntry(hist,samples[sample][2],'f')

    #legendR.AddEntry(hist,samples[sample][2],'f')

### Splitting the legend into two columns (with order going top to bottom in first column, then top to bottom in second column)
X = int(len(legList)/2)
sample = legList[X]
#print histName, _file[sample], "%s_%s"%(histName,sample)
hist = _file[sample].Get("%s_%s"%(histName,sample))
hist.SetFillColor(samples[sample][1])
hist.SetLineColor(samples[sample][1])
legendR.AddEntry(hist,samples[sample][2],'f')

for i in range(X):
	sample = legList[i]
	hist = _file[sample].Get("%s_%s"%(histName,sample))
	hist.SetFillColor(samples[sample][1])
	hist.SetLineColor(samples[sample][1])
	legendR.AddEntry(hist,samples[sample][2],'f')

	if X+i+1 < len(legList):
		sample = legList[i+X+1]
		hist = _file[sample].Get("%s_%s"%(histName,sample))
		hist.SetFillColor(samples[sample][1])
		hist.SetLineColor(samples[sample][1])
		legendR.AddEntry(hist,samples[sample][2],'f')




errorband=TH1F("error","error",20,0,20)
errorband.SetLineColor(0)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)
if showUnc: legendR.AddEntry(errorband,"Uncertainty","f")

TGaxis.SetMaxDigits(3)




def drawHist(histName,plotInfo, plotDirectory, _file):
    #print "start drawing"


    canvas = TCanvas('c1','c1',W,H)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetLeftMargin( L/W )
    canvas.SetRightMargin( R/W )
    canvas.SetTopMargin( T/H )
    canvas.SetBottomMargin( B/H )
    canvas.SetTickx(0)


    canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
    canvasRatio.SetFillColor(0)
    canvasRatio.SetBorderMode(0)
    canvasRatio.SetFrameFillStyle(0)
    canvasRatio.SetFrameBorderMode(0)
    canvasRatio.SetLeftMargin( L/W )
    canvasRatio.SetRightMargin( R/W )
    canvasRatio.SetTopMargin( T/H )
    canvasRatio.SetBottomMargin( B/H )
    canvasRatio.SetTickx(0)
    canvasRatio.SetTicky(0)
    canvasRatio.Draw()
    canvasRatio.cd()

    pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
    pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
    pad1.SetLeftMargin( L/W )
    pad1.SetRightMargin( R/W )
    pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
    pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
    pad2.SetLeftMargin( L/W )
    pad2.SetRightMargin( R/W )
    pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
    pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )

    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameBorderMode(0)
    pad1.SetTickx(0)
    pad1.SetTicky(0)

    pad2.SetFillColor(0)
    pad2.SetFillStyle(4000)
    pad2.SetBorderMode(0)
    pad2.SetFrameFillStyle(0)
    pad2.SetFrameBorderMode(0)
    pad2.SetTickx(0)
    pad2.SetTicky(0)


    canvasRatio.cd()
    pad1.Draw()
    pad2.Draw()


    canvas.cd()

    canvas.ResetDrawn()
    stack = THStack(histName,histName)
    SetOwnership(stack,True)
    for sample in stackList:
        #print sample, histName, _file[sample], "%s_%s"%(histName,sample)
        hist = _file[sample].Get("%s_%s"%(histName,sample))
        if type(hist)==type(TObject()):continue
        hist = hist.Clone(sample)	
        hist.SetFillColor(samples[sample][1])
        hist.SetLineColor(samples[sample][1])
        if scaleTTbarXS and sample == "TTbar":
            # Scale to xsec measured in TOP-17-001
            hist.Scale(803./831)

        if type(plotInfo[2]) is type(list()):
            hist = hist.Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
            if "MassEGamma" not in histName:
                hist.Scale(1.,"width")
        else:
            hist.Rebin(plotInfo[2])
#print "number of bins:  ",plotInfo[2], hist.GetNbinsX(), sample

        if useOverflow:
            lastBin = hist.GetNbinsX()
            lastBinContent = hist.GetBinContent(lastBin)
            lastBinError   = hist.GetBinError(lastBin)
            overFlowContent = hist.GetBinContent(lastBin+1)
            overFlowError   = hist.GetBinError(lastBin+1)
            hist.SetBinContent(lastBin,lastBinContent + overFlowContent)
            hist.SetBinError(lastBin, (lastBinError**2 + overFlowError**2)**0.5 )

	
	#print sample, histName, hist.Integral(-1,-1)
	#if type(plotInfo[2]) is type(list()):
	#	hist.Scale(1.,"width")
        stack.Add(hist)


    dataHist = _file["Data"].Get("%s_Data" % histName)

    noData = False
    #print dataHist
    if type(dataHist)==type(TObject()): noData = True
    print histName	
    
    if not noData:
	    dataHist.Sumw2()
	    if type(plotInfo[2]) is type(list()):	
		    dataHist = dataHist.Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
		    if "MassEGamma" not in histName:
		    	dataHist.Scale(1.,"width")
	    else:
		    dataHist.Rebin(plotInfo[2])
            #        print "number of bins in data:  ",plotInfo[2], hist.GetNbinsX()
#	    dataHist.Rebin(plotInfo[2])
	    #print dataHist.GetMarkerStyle()
	    #dataHist.Sumw2()
	    print "Total data events:", dataHist.Integral()
	    #exit()
	    if useOverflow:
		    lastBin = dataHist.GetNbinsX()
		    lastBinContent = dataHist.GetBinContent(lastBin)
		    lastBinError   = dataHist.GetBinError(lastBin)
		    overFlowContent = dataHist.GetBinContent(lastBin+1)
		    overFlowError   = dataHist.GetBinError(lastBin+1)
		    dataHist.SetBinContent(lastBin,lastBinContent + overFlowContent)
		    dataHist.SetBinError(lastBin, (lastBinError**2 + overFlowError**2)**0.5 )



    oneLine = TF1("oneline","1",-9e9,9e9)
    oneLine.SetLineColor(kBlack)
    oneLine.SetLineWidth(1)
    oneLine.SetLineStyle(2)
	
    _text = TPaveText(0.35,.75,0.45,0.85,"NDC")
    _text.SetTextColor(kBlack)
    _text.SetFillColor(0)
    _text.SetTextSize(0.04)
    _text.SetTextFont(42)
    _text.AddText(plotInfo[6])

    #histograms list has flag whether it's log or not
    canvas.SetLogy(plotInfo[5])
    #canvas.SetLogy()
    maxVal = stack.GetMaximum()
    if not noData: 
	    maxVal = max(dataHist.GetMaximum(),maxVal)
    
    minVal = 1
    if plotInfo[5]:
	    #print histName, plotInfo[5], stack.GetStack()[1].GetMinimum()
	    minVal = max(stack.GetStack()[0].GetMinimum(),1)
	    stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
#	    stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(stack.GetMinimum())))
#	    print minVal
	    stack.SetMinimum(minVal)
	    # print stack.GetStack()[0]
	    # print stack.GetStack()[0].GetName()
	    # print stack.GetStack()[0].GetMinimum()
    else:
	    stack.SetMaximum(1.5*maxVal)
	    stack.SetMinimum(minVal)

    # if not noData:
    #     stack.SetMaximum(1.35*max(dataHist.GetMaximum(),stack.GetMaximum()))
    # else:
    # 	stack.SetMaximum(1.35*stack.GetMaximum())
    #print histName
    errorband=stack.GetStack().Last().Clone("error")
    errorband.Sumw2()
    errorband.SetLineColor(kBlack)
    errorband.SetFillColor(kBlack)
    errorband.SetFillStyle(3245)
    errorband.SetMarkerSize(0)
    h1_up={}
    h1_do={}
    
    
    for sample in (stackList+["TTbar_amcanlo"]):
#        if sample not in signal: continue
        
        h1_up[sample]={}
        h1_do[sample]={}
        for syst in systematics:
            if sample not in signal and syst not in backgroundSystematics:
                continue
            print "Now on sample %s syst %s" % (sample,syst)
            if sample == "TTbar" and syst == "DS": continue
            elif sample == "ST_tW" and syst not in tWSystematics: continue
            elif sample == "TTbar_amcanlo" and syst != "Q2": continue
#            if syst=="Q2" or syst=="Pdf" or syst=="isr" or syst=="fsr":
#                if sample not in ["TTbar","ST_tW"]:continue
            #if sys=="toppt":
            if syst in oneSidedSysts:
                h1_up[sample][syst]=_filesys_up[sample][syst].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(syst,sample))
            else:
                h1_up[sample][syst]=_filesys_up[sample][syst].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(syst,sample))
                h1_do[sample][syst]=_filesys_down[sample][syst].Get("%s_%s"%(histName,sample)).Clone("%s_%s_do"%(syst,sample))

            if type(plotInfo[2]) is type(list()):
                h1_up[sample][syst] = h1_up[sample][syst].Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
                h1_do[sample][syst] = h1_do[sample][syst].Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
                h1_do[sample][syst].Scale(1,"width")
                h1_up[sample][syst].Scale(1,"width")

            else:
                h1_up[sample][syst].Rebin(plotInfo[2])
                #if sys!="toppt":
                if syst not in oneSidedSysts:
                    h1_do[sample][syst].Rebin(plotInfo[2])
    error=0.
    diff={}		
    sum_={}
    for i_bin in range(1,errorband.GetNbinsX()+1):
        sum_[i_bin]=0.	
        diff[i_bin]=[]
        for syst in systematics:
            for sample in stackList:
                if sample not in signal: continue
                if sample == "TTbar" and syst == "DS": continue
                if sample == "ST_tW" and syst not in tWSystematics: continue
#                if sys=="Q2" or sys=="Pdf" or sys=="isr" or sys=="fsr":
#                    if sample not in ["TTbar"]:continue
#			print "adding sys",sample,sys, ((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2
                #if sys != "toppt":
                if syst not in oneSidedSysts: 
                    sum_[i_bin]+=((h1_up[sample][syst].GetBinContent(i_bin)-h1_do[sample][syst].GetBinContent(i_bin))/2.)**2
#diff[i_bin].append(((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2.)


#print (sum_[i_bin])**0.5		
        errorband.SetBinError(i_bin,(sum_[i_bin])**0.5)
    
    stack.Draw('hist')
    _text.Draw("same")

    #histograms list has x-axis title
    stack.GetXaxis().SetTitle(plotInfo[0])
    stack.GetXaxis().SetTitleOffset(1.1)

    #stack.GetHistogram().GetYaxis().SetTitle(plotInfo[1])
    stack.GetYaxis().SetTitle("%sEntries / %.1f GeV" % ("Normalized " if args.norm else "", plotInfo[2]) )
    stack.GetYaxis().SetTitleOffset(1.1)
    
    #histograms list has x-axis title
#    stack.GetHistogram().GetXaxis().SetTitle(plotInfo[0])
#    stack.GetHistogram().GetXaxis().SetTitleOffset(1.1)
#
#    #stack.GetHistogram().GetYaxis().SetTitle(plotInfo[1])
#    stack.GetHistogram().GetYaxis().SetTitle("%sEntries / %.1f GeV" % ("Normalized " if args.norm else "", plotInfo[2]) )
#    stack.GetHistogram().GetYaxis().SetTitleOffset(1.1)
    
    
    if not -1 in plotInfo[3]:
        stack.GetHistogram().GetXaxis().SetRangeUser(plotInfo[3][0],plotInfo[3][1])
	if not noData:
            dataHist.GetXaxis().SetRangeUser(plotInfo[3][0],plotInfo[3][1])

    if not noData:
	dataHist.SetLineColor(kBlack)
	dataHist.Draw("e,X0,same")
     
    #residue=dataHist.Clone()
    #temp=stack.GetStack().Last().Clone("temp")
    #residue.Add(temp,-1)
    #residue.Draw("hist")
    #canvas.Print("%s/%s_residue.pdf"%(plotDirectory,histName))
    #canvas.Clear()

    legend.Draw("same")


    #_text.Draw()
    CMS_lumi.channelText = _channelText+plotInfo[4]
    CMS_lumi.CMS_lumi(canvas, 4, 11)

    canvas.Print("%s/%s.pdf"%(plotDirectory,histName))
    canvas.Print("%s/%s.png"%(plotDirectory,histName))

    if not noData:
        ratio = dataHist.Clone("temp")
        temp = stack.GetStack().Last().Clone("temp")

        for i_bin in range(1,temp.GetNbinsX()+1):
            temp.SetBinError(i_bin,0.)
        ratio.Divide(temp)
#errorband.Divide(temp)


# pad1.Clear()
# pad2.Clear()

        canvasRatio.cd()
        canvasRatio.ResetDrawn()
        canvasRatio.Draw()
        canvasRatio.cd()

        pad1.Draw()
        pad2.Draw()

        pad1.cd()
        pad1.SetLogy(plotInfo[5])

        stack.Draw('HIST')
        y2 = pad1.GetY2()

        #print "stack.GetXaxis().GetTitle() =", stack.GetXaxis().GetTitle() 

#	stack.SetMinimum(1)
#    pad1.Update()
#        stack.GetXaxis().SetTitle('')
        #stack.GetXaxis().SetTitle(dataHist.GetXaxis().GetTitle())
        #stack.GetYaxis().SetTitle(dataHist.GetYaxis().GetTitle())

        stack.SetTitle(histName)    # Set ratio plot title here
        
        # No x axis title on upper pad of stack plot
        stack.GetXaxis().SetTitle("")

        stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
        stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
        #stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
        
        #stack.GetYaxis().SetTitle(plotInfo[1])
        dataHist.Draw('E,X0,SAME')
        #print "dataHist.GetXaxis().GetTitle() =", dataHist.GetXaxis().GetTitle() 
#       legendR.AddEntry(errorband,"Uncertainty","f")
        legendR.Draw()

        _text = TPaveText(0.42,.75,0.5,0.85,"NDC")
        _text.AddText(plotInfo[6])
        _text.SetTextColor(kBlack)
        _text.SetFillColor(0)
        _text.SetTextSize(0.05)
        _text.SetTextFont(42)
        _text.Draw("same")
        
        ratio.SetTitle('')

        ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
        ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
        ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
#	ratio.GetYaxis().SetRangeUser(0.5,1.5)

        maxRatio = ratio.GetMaximum()
        minRatio = ratio.GetMinimum()


        maxRatio = 1.5
        minRatio = 0.5
        for i_bin in range(1,ratio.GetNbinsX()):
            if ratio.GetBinError(i_bin)<1:
                if ratio.GetBinContent(i_bin)>maxRatio:
                    maxRatio = ratio.GetBinContent(i_bin)
                if ratio.GetBinContent(i_bin)<minRatio:
                    minRatio = ratio.GetBinContent(i_bin)

        if maxRatio > 1.8:
            ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
        elif maxRatio < 1:
            ratio.GetYaxis().SetRangeUser(0,1.2)
        elif maxRatio-1 < 1-minRatio:
            ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)		
        else:
            ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)
        

        #maxRatio = 1.5
            #minRatio = 0.5	
        ratio.GetYaxis().SetRangeUser(0.7,1.3)
        ratio.GetYaxis().SetNdivisions(504)
        ratio.GetXaxis().SetTitle(plotInfo[0])
        ratio.GetYaxis().SetTitle("Data/MC")
        CMS_lumi.CMS_lumi(pad1, 4, 11)

        pad2.cd()
        #for i_bin in range(1,errorband.GetNbinsX()):
        #	errorband.SetBinContent(i_bin,1.)
        maxRatio = 1.5
        minRatio = 0.5
        ratio.SetMarkerStyle(dataHist.GetMarkerStyle())
        ratio.SetMarkerSize(dataHist.GetMarkerSize())
        ratio.SetLineColor(dataHist.GetLineColor())
        ratio.SetLineWidth(dataHist.GetLineWidth())
        ratio.Draw('e,x0')
        errorband.Divide(temp)
        if showUnc: errorband.Draw('e2,same')
        oneLine.Draw("same")
        
        #    pad2.Update()
        canvasRatio.Update()
        canvasRatio.RedrawAxis()
        canvasRatio.SaveAs("%s/%s_ratio.pdf"%(plotDirectory,histName))
        canvasRatio.SaveAs("%s/%s_ratio.png"%(plotDirectory,histName))
            #canvasRatio.Clear()
        canvasRatio.SetLogy(0)


    if histName.find("nVtx") >= 0:
        print "Making pileup comparison plots"
        # Pileup comparison plots
        for var in ["Up","Down"]:
#            canvasRatio.cd()
#            canvasRatio.ResetDrawn()
#            canvasRatio.Draw()
#            canvasRatio.cd()
#
#            pad1.Draw()
#            pad2.Draw()
#
#            pad1.cd()
#            pad1.SetLogy(plotInfo[5])


            stack = THStack(histName+"_PU"+var,histName+"_PU"+var)
            SetOwnership(stack,True)
            for sample in stackList:
                #print sample, histName, _file[sample], "%s_%s"%(histName,sample)
                #hist = _file[sample].Get("%s_%s"%(histName,sample))
                #breakpoint()
                if var == "Up":
                    hist = h1_up[sample]["PU"].Clone()
                else:
                    hist = h1_do[sample]["PU"].Clone()

                if type(hist)==type(TObject()):continue
                hist = hist.Clone(sample)
                hist.SetFillColor(samples[sample][1])
                hist.SetLineColor(samples[sample][1])
                if scaleTTbarXS and sample == "TTbar":
                    # Scale to xsec measured in TOP-17-001
                    hist.Scale(803./831)

                if type(plotInfo[2]) is type(list()):
                    hist = hist.Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
                    if "MassEGamma" not in histName:
                        hist.Scale(1.,"width")
                else:
                    hist.Rebin(plotInfo[2])
#print "number of bins:  ",plotInfo[2], hist.GetNbinsX(), sample

                if useOverflow:
                    lastBin = hist.GetNbinsX()
                    lastBinContent = hist.GetBinContent(lastBin)
                    lastBinError   = hist.GetBinError(lastBin)
                    overFlowContent = hist.GetBinContent(lastBin+1)
                    overFlowError   = hist.GetBinError(lastBin+1)
                    hist.SetBinContent(lastBin,lastBinContent + overFlowContent)
                    hist.SetBinError(lastBin, (lastBinError**2 + overFlowError**2)**0.5 )


            #print sample, histName, hist.Integral(-1,-1)
            #if type(plotInfo[2]) is type(list()):
            #   hist.Scale(1.,"width")
                stack.Add(hist)
            if not noData:
                ratio = dataHist.Clone("temp")
                temp = stack.GetStack().Last().Clone("temp")

                for i_bin in range(1,temp.GetNbinsX()+1):
                    temp.SetBinError(i_bin,0.)
                ratio.Divide(temp)
#errorband.Divide(temp)


# pad1.Clear()
# pad2.Clear()

                canvasRatio.cd()
                canvasRatio.ResetDrawn()
                canvasRatio.Draw()
                canvasRatio.cd()

                pad1.Draw()
                pad2.Draw()

                pad1.cd()
                pad1.SetLogy(plotInfo[5])

                stack.Draw('HIST')
                y2 = pad1.GetY2()


                stack.SetTitle(histName + "  Pileup %s" % var)    # Set ratio plot title here

                # No x axis title on upper pad of stack plot
                stack.GetXaxis().SetTitle("")

                stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
                stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
                #stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))

                #stack.GetYaxis().SetTitle(plotInfo[1])
                dataHist.Draw('E,X0,SAME')
                #print "dataHist.GetXaxis().GetTitle() =", dataHist.GetXaxis().GetTitle() 
#       legendR.AddEntry(errorband,"Uncertainty","f")
                legendR.Draw("same")

                _text = TPaveText(0.42,.75,0.5,0.85,"NDC")
                _text.AddText(plotInfo[6])
                _text.SetTextColor(kBlack)
                _text.SetFillColor(0)
                _text.SetTextSize(0.05)
                _text.SetTextFont(42)
               # _text.Draw("same")

                ratio.SetTitle('')

                ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
                ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
                ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
                ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
                ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
#   ratio.GetYaxis().SetRangeUser(0.5,1.5)

                maxRatio = ratio.GetMaximum()
                minRatio = ratio.GetMinimum()


                maxRatio = 1.5
                minRatio = 0.5
                for i_bin in range(1,ratio.GetNbinsX()):
                    if ratio.GetBinError(i_bin)<1:
                        if ratio.GetBinContent(i_bin)>maxRatio:
                            maxRatio = ratio.GetBinContent(i_bin)
                        if ratio.GetBinContent(i_bin)<minRatio:
                            minRatio = ratio.GetBinContent(i_bin)

                if maxRatio > 1.8:
                    ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
                elif maxRatio < 1:
                    ratio.GetYaxis().SetRangeUser(0,1.2)
                elif maxRatio-1 < 1-minRatio:
                    ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)
                else:
                    ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)


                #maxRatio = 1.5
                    #minRatio = 0.5 
                ratio.GetYaxis().SetRangeUser(0.7,1.3)
                ratio.GetYaxis().SetNdivisions(504)
                ratio.GetXaxis().SetTitle(plotInfo[0])
                ratio.GetYaxis().SetTitle("Data/MC")
                CMS_lumi.CMS_lumi(pad1, 4, 12)

                pad2.cd()
                #for i_bin in range(1,errorband.GetNbinsX()):
                #   errorband.SetBinContent(i_bin,1.)
                maxRatio = 1.5
                minRatio = 0.5
                ratio.SetMarkerStyle(dataHist.GetMarkerStyle())
                ratio.SetMarkerSize(dataHist.GetMarkerSize())
                ratio.SetLineColor(dataHist.GetLineColor())
                ratio.SetLineWidth(dataHist.GetLineWidth())
                ratio.Draw('e,x0')
                errorband.Divide(temp)
                if showUnc: errorband.Draw('e2,same')
                oneLine.Draw("same")

                #    pad2.Update()
                canvasRatio.Update()
                canvasRatio.RedrawAxis()
                canvasRatio.SaveAs("%s/%s_PU_%s_ratio.pdf"%(plotDirectory,histName,var))
                canvasRatio.SaveAs("%s/%s_PU_%s_ratio.png"%(plotDirectory,histName,var))
                    #canvasRatio.Clear()
                canvasRatio.SetLogy(0)
    

    
    #if histName.find("rec_") >= 0 or histName.find("gen_") >=0 or histName.find("nVtx") >= 0:
    if histName.find("rec_") >= 0 or histName.find("gen_") >=0:
        # Systematic variation plots
        print "\n","="*50
        print "Now making systematics plots for %s" % histName
        print "="*50,"\n"
        for sample in signal: 
            print "Now on:", sample
            if sample == "TTbar_amcanlo":
                nominal = _file[sample].Get("%s_TTbar" % (histName))
            else:
                nominal = _file[sample].Get("%s_%s"%(histName,sample))
            
            # Set X,Y axis labels
            #nominal.GetXaxis().SetTitle(obsTitle[histName[4:]] + " [GeV]")
            nominal.GetYaxis().SetTitle("%sEntries / %.1f GeV" % ("Normalized " if args.norm else "", plotInfo[2]) )
            nominal.GetYaxis().SetTitleOffset(1.1)
            nominal.SetLineColor(kBlack)
            nominal.SetMarkerSize(0)
            if args.norm: nominal.Scale(1./nominal.Integral())
            one = nominal.Clone()
            one.Divide(nominal)

            if type(plotInfo[2]) is type(list()):
                nominal = hist.Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
                if "MassEGamma" not in histName:
                    nominal.Scale(1.,"width")
            else:
                nominal.Rebin(plotInfo[2])

            nominalTitle = nominal.GetTitle()
            #################################################################    
            for sysType,systsToPlot in [("Experimental",experimentalSysts), ("Theory",theorySysts)]:
                if sample == "TTbar_amcanlo": break

                print "Now on %s plot" % sysType
                l = TLegend(0.73,0.7,0.9,0.9)
                l.SetNColumns(2)
                l.SetBorderSize(0)
                 
                canvasRatio.cd()
                canvasRatio.ResetDrawn()
                canvasRatio.Draw()
                canvasRatio.cd()

                pad1.Draw()
                pad2.Draw()

                pad1.cd()
                pad1.SetLogy(plotInfo[5])

                #y2 = pad1.GetY2()

                nominal.Draw("hist")
                nominal.SetTitle(nominalTitle + " %s Systematics"%sysType)
            
                pad2.cd()
                one.Draw("hist")
                one.SetTitle("")
                one.GetXaxis().SetTitleSize(0.1)
                #one.GetXaxis().SetTitle(obsTitle[histName[4:]] + " [GeV]")
                one.GetXaxis().SetTitle((obsTitle[histName[4:]] if (histName[4:].find("rec_") >=0 or histName[4:].find("gen_") >=0) else histName) + " [GeV]")
                one.GetXaxis().SetTitleOffset(1.1)
                one.GetYaxis().SetRangeUser(0.8,1.2)
                one.GetYaxis().SetTitle("ratio wrt nominal")
                one.GetYaxis().SetTitleOffset(1.2)

                for i,syst in enumerate(systsToPlot): 
                    if sample == "TTbar" and syst == "DS": continue
                    if sample == "ST_tW" and syst not in tWSystematics: continue
                    #print "Now in %s %s %s syst plots" % (sample,sysType,syst)    
                    pad1.cd()
                    try:
                        up = h1_up[sample][syst]
                        #up.SetLineColor(kRed)
                        up.SetLineColor(systColors[syst] if syst in oneSidedSysts else systColors["%s%s" % (syst,"Up")])
                        up.SetMarkerSize(0)
                        up.SetLineWidth(3)
                        if args.norm: up.Scale(1./up.Integral())
                        
                        l.AddEntry(up, "%s" % (syst if syst in oneSidedSysts else syst + " Up"))
                    except:
                        up = None
                    try:
                        down = h1_do[sample][syst]
                        #down.SetLineColor(kAzure)
                        down.SetLineColor(systColors["%s%s" % (syst,"Down")])
                        down.SetMarkerSize(0)
                        down.SetLineWidth(3)
                        if args.norm: down.Scale(1./down.Integral())
                        l.AddEntry(down, "%s Down" % syst)
                    except:
                        down = None
                   
                    if up is not None:
                        up.Draw("hist same")
                    if down is not None:
                        down.Draw("hist same")
                        #l.Draw("same")

                    pad2.cd()
#                    if i == 0:
#                        one.Draw("hist")

                    if up is not None:
                        ratioUp = up.Clone()
                        ratioUp.Divide(nominal)
                       
                        # Ratio plot lables
                        ratioUp.SetTitle("")
#                        ratioUp.SetLineColor(systColors[syst] if syst in oneSidedSysts else systColors["%s%s" % (syst,"Up")])
                        ratioUp.GetXaxis().SetTitleSize(0.1)
                        #print "ratioUp.GetXaxis().GetTitleSize() = %.2f" % ratioUp.GetXaxis().GetTitleSize()
                        #ratioUp.GetXaxis().SetTitle(obsTitle[histName[4:]] + " [GeV]")
                        ratioUp.GetXaxis().SetTitle((obsTitle[histName[4:]] if (histName[4:].find("rec_") >=0 or histName[4:].find("gen_") >=0) else histName) + " [GeV]")
                        ratioUp.GetXaxis().SetTitleOffset(1.1)
                        

                        ratioUp.GetYaxis().SetRangeUser(0.8,1.2)
                        ratioUp.GetYaxis().SetTitle("ratio wrt nominal")
                        ratioUp.GetYaxis().SetTitleOffset(1.2)
                        ratioUp.Draw("hist same")
#                        if not ratioDrawn:
#                            ratioUp.Draw("hist")
#                            ratioDrawn = True
#                        else:
#                            ratioUp.Draw("hist same")
#                        if i == 0: 
#                            ratioUp.Draw("hist")
#                        else:
#                            ratioUp.Draw("hist same")
                    if down is not None:
                        ratioDown = down.Clone()
#                        ratioDown.SetLineColor(systColors["%s%s" % (syst,"Down")])
                        ratioDown.Divide(nominal)
                        ratioDown.GetYaxis().SetRangeUser(0.8,1.2)
                        ratioDown.Draw("hist same")
#                        if i == 0 and up is None:
#                            ratioDown.Draw("hist")
#                        else:
#                            ratioDown.Draw("hist same")
                    #l.Draw("same")
#                pad1.Draw()
#                pad2.Draw()
                    #one.Draw("hist same")
                    CMS_lumi.CMS_lumi(canvasRatio, 4, 12)
                
                pad1.cd()                
                l.AddEntry(nominal, "nominal")
                l.Draw("same")
                canvasRatio.SaveAs("%s/%s_%s_%sSysts.pdf" %(plotDirectory,sample,histName,sysType))
                canvasRatio.SaveAs("%s/%s_%s_%sSysts.png" %(plotDirectory,sample,histName,sysType))

            canvasRatio.cd()
            canvasRatio.ResetDrawn()
            canvasRatio.Draw()
            canvasRatio.cd()

            pad1.Draw()
            pad2.Draw()

            pad1.cd()
            pad1.SetLogy(plotInfo[5])

            #################################################################    
            nominal.SetTitle(nominalTitle)
            # Individual systematic plots
            for syst in systematics:
                if sample == "TTbar" and syst == "DS": continue
                elif sample == "ST_tW" and syst not in tWSystematics: continue
                elif sample == "TTbar_amcanlo" and syst != "Q2": continue
                
                print "\n","***  Now on %s individual %s plot  ***\n" % (sample,syst)

                
#                print "Now in indiv syst plot: %s  %s" % (sample,syst)    
                l = TLegend(0.75,0.75,0.9,0.9)
                l.SetBorderSize(0)
                l.AddEntry(nominal, "nominal")
                try:
                    up = h1_up[sample][syst]
                    up.SetLineColor(kRed)
                    up.SetMarkerSize(0)
                    if args.norm: up.Scale(1./up.Integral())
                    l.AddEntry(up, "%s" % (syst if syst in oneSidedSysts else syst + " Up"))
                except:
                    up = None
                try:
                    down = h1_do[sample][syst]
                    down.SetLineColor(kAzure)
                    down.SetMarkerSize(0)
                    if args.norm: down.Scale(1./down.Integral())
                    l.AddEntry(down, "%s Down" % syst)
                except:
                    down = None
                
                canvasRatio.cd()
                canvasRatio.ResetDrawn()
                canvasRatio.Draw()
                canvasRatio.cd()

                pad1.Draw()
                pad2.Draw()

                pad1.cd()
                pad1.SetLogy(plotInfo[5])

                #y2 = pad1.GetY2()
                maxH = {up:(0 if up == None else up.GetMaximum()), down:(0 if down == None else down.GetMaximum()), nominal:nominal.GetMaximum()}
                maxHsorted = sorted(maxH.items(), key=lambda kv: kv[1])
                maxHsorted.reverse()
              
                

                histsSorted = [h[0] for h in maxHsorted if h[0] is not None]
                for i,h in enumerate(histsSorted):
                    if i == 0:
                        h.Draw("hist")
                        h.GetYaxis().SetTitle("%sEntries / %.1f GeV" % ("Normalized " if args.norm else "", plotInfo[2]) )
                        h.GetYaxis().SetTitleOffset(1.1)
                    else:
                        h.Draw("hist same")
                
                
#                if up is not None:
#                    up.Draw("hist same")
#                if down is not None:
#                    down.Draw("hist same")

                l.Draw("same")

                pad2.cd()

                if up is not None:
                    ratioUp = up.Clone()
                    ratioUp.Divide(nominal)
                    
                    # Ratio plot lables
                    ratioUp.SetTitle("")
                    ratioUp.GetXaxis().SetTitleSize(0.1)
                    #print "ratioUp.GetXaxis().GetTitleSize() = %.2f" % ratioUp.GetXaxis().GetTitleSize()
                    #ratioUp.GetXaxis().SetTitle(obsTitle[histName[4:]] + " [GeV]")
                    ratioUp.GetXaxis().SetTitle((obsTitle[histName[4:]] if (histName[4:].find("rec_") >=0 or histName[4:].find("gen_") >=0) else histName) + " [GeV]")
                    ratioUp.GetXaxis().SetTitleOffset(1.1)
                    if syst == "Q2":
                        ratioUp.GetYaxis().SetRangeUser(0.5,1.5)
                    elif syst in ["EleIDEff", "EleRecoEff", "PU", "MuIDEff", "MuIsoEff", "MuTrackEff"]:
                        ratioUp.GetYaxis().SetRangeUser(0.95,1.05)
                    else:
                        ratioUp.GetYaxis().SetRangeUser(0.8,1.2)
                    
                    ratioUp.GetYaxis().SetTitle("ratio wrt nominal")
                    ratioUp.GetYaxis().SetTitleOffset(1.2)
                    ratioUp.Draw("hist")
                if down is not None:
                    ratioDown = down.Clone()
                    ratioDown.Divide(nominal)
                    ratioDown.GetYaxis().SetRangeUser(0.8,1.2)
                    ratioDown.Draw("hist same")
                #l.Draw("same")
#                pad1.Draw()
#                pad2.Draw()
                one.Draw("hist same")
                CMS_lumi.CMS_lumi(canvasRatio, 4, 12)
                canvasRatio.SaveAs("%s/%s_%s_%s.pdf" %(plotDirectory,sample,histName,syst))
                canvasRatio.SaveAs("%s/%s_%s_%s.png" %(plotDirectory,sample,histName,syst))

    canvas.Close()
    canvasRatio.Close()


for histName in plotList:
    drawHist(histName,histograms[histName],plotDirectory,_file)

# for histName in phoselhistograms:
#         drawHist("phosel_%s"%histName,phoselhistograms[histName],plotDirectory,_file)

