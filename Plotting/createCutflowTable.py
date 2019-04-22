#!/usr/bin/env python
from ROOT import *
from sampleInformation import samples,sampleList
import os
import sys
from argparse import ArgumentParser
from pprint import pprint

# Mapping of cuts to bins
cutToBin = {"input":1,      # Total input events
            "trigger":2,    # Passing trigger
            "vertex":3,     # Good vertex
            "1ele1mu":4,    # At least 1 good ele and 1 good mu
            "emusigned":5,  # Top 2 pt leptons are oppositely signed emu pair
            "lepton":6,     # emu pair passing invariant mass and all other lepton cuts
            "1jet":7,       # At least 1 good jet
            "2jet":8,       # At least 2 good jets
            "1bjet":11,     # At least 1 b-tagged jet
            "2bjet":12      # At least 2 b-tagged jets
            }

cutTitle = {"input":"Pass skim",      
            "trigger":"Trigger",    
            "vertex":"$\geq 1$ Good Vertex",     
            "1ele1mu":"Good ele and mu",
            "emusigned":"Op signed emu pair",
            "lepton":"e\$mu$",
            "1jet":"$\geq 1 jet",       
            "2jet":"$\geq 2 jets",       
            "1bjet":"$\geq 1 b-tag",     
            "2bjet":"$\geq 2 b-tags"      
            }


parser = ArgumentParser()
#parser.add_argument("-i", "--inDir", default="store/user/msaunder/backup_13TeV_AnalysisNtuples/emu/V08_00_26_07/", help="input eos analysis ntuple directory") 
parser.add_argument("-i", "--inDir", default="store/user/msaunder/13TeV_cutflows/emu/V08_00_26_07/", help="input eos analysis ntuple directory") 
parser.add_argument("-c", "--cuts", nargs="+", default=["lepton", "2jet", "1bjet"], choices=cutToBin.keys(), help="which cuts to include in table")
parser.add_argument("-o", "--outF", default="cutflow.tex", help="output tex file with cutflow table")
args = parser.parse_args()

cutflowHistName = "cut_flow_weight_emu"

# Cuts sorted according to the bin number 
cuts = sorted(args.cuts, key=lambda kv: cutToBin[kv])

cutflowH = {}
totalMC = None
for sample in sampleList:
#    print "Now on", sample
    for ntupleF in samples[sample][0]:
#        print "\t", ntupleF
        f = TFile.Open("root://cmseos.fnal.gov//%s/%s" % (args.inDir, ntupleF.replace("_AnalysisNtuple.root", "_cutflow.root")) )
        if sample not in cutflowH:
            cutflowH[sample] = f.Get(cutflowHistName).Clone("_"+sample)
            cutflowH[sample].SetDirectory(0)
        else:
            cutflowH[sample].Add(f.Get(cutflowHistName))

        f.Close()

    if sample != "Data":
        if totalMC is None:
            totalMC = cutflowH[sample].Clone("totalMC")
        else:
            totalMC.Add(cutflowH[sample])

def value(sampleType, cut):    
    return cutflowH[sample].GetBinContent(cutToBin[cut])

def error(sampleType, cut):
    return cutflowH[sample].GetBinError(cutToBin[cut])
    

print "Cutflow totals"
print "-" * 90
print "\t\t",
for c in cuts:
    print c + "\t\t\t",
print ""
print "-" * 90

for sample in sampleList:
    if sample == "Data": continue
    print sample + "\t\t",
    for c in cuts:
        print "%.1f +- %.1f%s" % (cutflowH[sample].GetBinContent(cutToBin[c]), cutflowH[sample].GetBinError(cutToBin[c]), "\t\t" if (cutflowH[sample].GetBinContent(cutToBin[c]) < 10000 or cutflowH[sample].GetBinError(cutToBin[c]) < 100) else "\t"),
    print ""

print "-" * 90
print "Total MC\t",
for c in cuts:
    print "%.1f +- %.1f%s" % (totalMC.GetBinContent(cutToBin[c]), totalMC.GetBinError(cutToBin[c]), "\t\t" if totalMC.GetBinContent(cutToBin[c]) < 10000 else "\t"),
print ""
print "-" * 90
print "Data\t\t",
for c in cuts:
    print "%.0f +- %.0f%s" % (cutflowH["Data"].GetBinContent(cutToBin[c]), cutflowH["Data"].GetBinError(cutToBin[c]), "\t\t" if cutflowH["Data"].GetBinContent(cutToBin[c]) < 10000 else "\t\t"),
print ""
print "-" * 90


# Write output tex file
#with open(args.outF, "w") as f:
#    f.write( \
#"""
#\\begin{table*}[h]
#\t\\begin{center}
#\t\t\\topcaption{Event yields at various stages of the offline selection. The final selection is given in the rightmost column.}
#\t\t\\label{table:cutflow}
#\t\t\\begin{tabular}[l c c c]
#\t\t\t\\hline
#\t\t\tSample & e$\mu$ & $\\geq$ 2 jets & $\\geq$ 1 b-tag \\\\
#\t\t\t\\hline
#\t\t\t\\ttbar & %.1f & %.1f & %.1f \\\\
#\t\t\tSingle Top (\\tW channel) & %.1f & %.1f & %.1f \\\\
#\t\t\tSingle Top (t + s channel) & %.1f & %.1f & %.1f \\\\
#\t\t\tDrell-Yan & %.1f & %.1f & %.1f \\\\
#\t\t\tDiboson & %.1f & %.1f & %.1f \\\\
#\t\t\t\\WJets & %.1f & %.1f & %.1f \\\\
#\t\t\t\\TTV & %.1f & %.1f & %.1f \\\\
#\t\t\t\\hline
#\t\t\tTotal MC & %.1f & %.1f & %.1f \\\\
#\t\t\t\\hline
#\t\t\tData & %.1f & %.1f & %.1f \\\\
#\t\t\t\\hline
#\t\t\\end{tabular}
#\t\\end{center}
#\\end{table*}
#
#""" % (value("TTbar","lepton"), 
#            )

print "Output saved in %s" % args.outF
