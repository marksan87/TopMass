#!/usr/bin/env python
from ROOT import *
import os
import sys
from array import array
from pprint import pprint
from argparse import ArgumentParser

gStyle.SetOptStat(0)
oneSidedSysts = ["toppt", "CRerdON", "CRGluon", "CRQCD", "DS", "amcanlo", "madgraph", "herwigpp" ]

parser = ArgumentParser()
parser.add_argument("--old", default="histograms", help="old template directory")
parser.add_argument("--new", default="secondtry_histograms", help="new template directory")
parser.add_argument("-p", "--plot", default="elePt", help="plot to consider")
parser.add_argument("-s", "--syst", default="EleScale", help="systematic to plot")
parser.add_argument("--noerrors", action="store_true", default=False, help="don't plot errors")
parser.add_argument("-o", "--outDir", default="compOldNewHists", help="output directory")

rebin = 10

args = parser.parse_args()
if args.outDir[-1] == "/": args.outDir = args.outDir[:-1]
os.system("mkdir -p %s" % args.outDir)

recoObs = "rec_ptll"
signal = "TTbar"
gROOT.SetBatch(True)
masses = [1665, 1695, 1715, 1725, 1735, 1755, 1785]

c = TCanvas("c", "c", 800, 1200)
pad1 = TPad("pad1", "pad1", 0., 0.5, 1., 1.)
pad2 = TPad("pad2", "pad2", 0., 0.25, 1., 0.5)
pad3 = TPad("pad3", "pad3", 0., 0., 1., 0.25)

canvasCompare = TCanvas("c2", "c2", 800,1200)
compPad1 = TPad("compPad1", "compPad1", 0., 0.5, 1., 1.)
compPad2 = TPad("compPad2", "compPad2", 0., 0., 1., 0.5)



for m in masses:
    print "Now on mass %d" % m

    signalMass = signal + ("" if m == 1725 else "_mt%d" % m)
    old_nomF = TFile.Open("%s/hists/%s.root" % (args.old, signalMass), "read")
    new_nomF = TFile.Open("%s/hists/%s.root" % (args.new, signalMass), "read")
    oldNom = old_nomF.Get("%s_%s" % (args.plot, signalMass)).Clone()
    oldNom.SetDirectory(0)
    oldNom.SetLineWidth(2)
    
    newNom = new_nomF.Get("%s_%s" % (args.plot, signalMass)).Clone()
    newNom.SetDirectory(0)
    newNom.SetLineWidth(2)

    old_nomF.Close()
    new_nomF.Close()

    oldNom.Rebin(rebin)
    newNom.Rebin(rebin)



    for _bin in xrange(1,oldNom.GetNbinsX()+1):
        oldNom.SetBinError(_bin, 0.)
        newNom.SetBinError(_bin, 0.)


    # Old histograms
    old_SystUpF = TFile.Open("%s/hists%s%s/%s.root" % (args.old, args.syst, "" if args.syst in oneSidedSysts else "_up", signalMass), 'read')
    
    oldUp = old_SystUpF.Get("%s_%s" % (args.plot, signalMass)).Clone()
    oldUp.SetDirectory(0)
    oldUp.SetLineColor(kRed)
    oldUp.SetFillColor(kWhite)
    oldUp.SetLineWidth(2)
    oldUp.Rebin(rebin)

    old_SystUpF.Close()

    resOldUp = oldUp.Clone()
    resOldUp.SetDirectory(0)
    resOldUp.Add(oldNom, -1)
    ratioOldUp = oldUp.Clone()
    ratioOldUp.SetDirectory(0)
    ratioOldUp.Divide(oldNom)


    if args.syst not in oneSidedSysts:
        old_SystDnF = TFile.Open("%s/hists%s_down/%s.root" % (args.old, args.syst, signalMass), 'read')
        oldDn = old_SystDnF.Get("%s_%s" % (args.plot, signalMass)).Clone()
        oldDn.SetDirectory(0)
        oldDn.SetLineColor(kBlue)
        oldDn.SetFillColor(kWhite)
        oldDn.SetLineWidth(2)
        oldDn.Rebin(rebin)
        old_SystDnF.Close()
        
        resOldDn = oldDn.Clone()
        resOldDn.SetDirectory(0)
        resOldDn.Add(oldNom, -1)
        ratioOldDn = oldDn.Clone()
        ratioOldDn.SetDirectory(0)
        ratioOldDn.Divide(oldNom)

    
    maxOldRes = -100
    maxOldRatio = -100
    minOldRes = 100
    minOldRatio = 100

    if args.syst not in oneSidedSysts:
        maxOldRes = max(maxOldRes, max(resOldUp.GetMaximum(), resOldDn.GetMaximum()))
        minOldRes = min(minOldRes, min(resOldUp.GetMinimum(), resOldDn.GetMinimum()))
        maxOldRatio = max(maxOldRatio, max(ratioOldUp.GetMaximum(), ratioOldDn.GetMaximum()))
        minOldRatio = min(minOldRatio, min(ratioOldUp.GetMinimum(), ratioOldDn.GetMinimum()))
    
    else:
        maxOldRes = max(maxOldRes, resOldUp.GetMaximum())
        minOldRes = min(minOldRes, resOldUp.GetMinimum())
        maxOldRatio = max(maxOldRatio, ratioOldUp.GetMaximum())
        minOldRatio = min(minOldRatio, ratioOldUp.GetMinimum())


    paddingOldRes = 0.05 * abs(maxOldRes - minOldRes)
    paddingOldRatio = 0.05 * abs(maxOldRatio - minOldRatio)

    # New histograms
    new_SystUpF = TFile.Open("%s/hists%s%s/%s.root" % (args.new, args.syst, "" if args.syst in oneSidedSysts else "_up", signalMass), 'read')
    newUp = new_SystUpF.Get("%s_%s" % (args.plot, signalMass)).Clone()
    newUp.SetDirectory(0)
    newUp.SetLineColor(kRed)
    newUp.SetFillColor(kWhite)
    newUp.SetLineWidth(2)
    newUp.Rebin(rebin)
    new_SystUpF.Close()

    resNewUp = newUp.Clone()
    resNewUp.SetDirectory(0)
    resNewUp.Add(newNom, -1)
    ratioNewUp = newUp.Clone()
    ratioNewUp.SetDirectory(0)
    ratioNewUp.Divide(newNom)
    
    
    if args.syst not in oneSidedSysts:
        new_SystDnF = TFile.Open("%s/hists%s_down/%s.root" % (args.new, args.syst, signalMass), 'read')
        newDn = new_SystDnF.Get("%s_%s" % (args.plot, signalMass)).Clone()
        newDn.SetDirectory(0)
        newDn.SetLineColor(kBlue)
        newDn.SetFillColor(kWhite)
        newDn.SetLineWidth(2)
        newDn.Rebin(rebin)
        new_SystDnF.Close()

        resNewDn = newDn.Clone()
        resNewDn.SetDirectory(0)
        resNewDn.Add(newNom, -1)
        ratioNewDn = newDn.Clone()
        ratioNewDn.SetDirectory(0)
        ratioNewDn.Divide(newNom)

    resLine = TLine(newNom.GetXaxis().GetBinLowEdge(1), 0., newNom.GetXaxis().GetBinUpEdge(newNom.GetNbinsX()), 0.)
    ratioLine = TLine(newNom.GetXaxis().GetBinLowEdge(1), 1., newNom.GetXaxis().GetBinUpEdge(newNom.GetNbinsX()), 1.)

    resLine.SetLineWidth(2)
    ratioLine.SetLineWidth(2)

    maxNewRes = -100
    maxNewRatio = -100
    minNewRes = 100
    minNewRatio = 100

    if args.syst not in oneSidedSysts:
        maxNewRes = max(maxNewRes, max(resNewUp.GetMaximum(), resNewDn.GetMaximum()))
        minNewRes = min(minNewRes, min(resNewUp.GetMinimum(), resNewDn.GetMinimum()))
        maxNewRatio = max(maxNewRatio, max(ratioNewUp.GetMaximum(), ratioNewDn.GetMaximum()))
        minNewRatio = min(minNewRatio, min(ratioNewUp.GetMinimum(), ratioNewDn.GetMinimum()))
    else:
        maxNewRes = max(maxNewRes, resNewUp.GetMaximum())
        minNewRes = min(minNewRes, resNewUp.GetMinimum())
        maxNewRatio = max(maxNewRatio, ratioNewUp.GetMaximum())
        minNewRatio = min(minNewRatio, ratioNewUp.GetMinimum())

    paddingNewRes = 0.05 * abs(maxNewRes - minNewRes)
    paddingNewRatio = 0.05 * abs(maxNewRatio - minNewRatio)



    if args.syst not in oneSidedSysts:
        maxOld = max(oldUp.GetMaximum(), max(oldNom.GetMaximum(), oldDn.GetMaximum()))
        maxNew = max(newUp.GetMaximum(), max(newNom.GetMaximum(), newDn.GetMaximum()))
    else:
        maxOld = max(oldUp.GetMaximum(), oldNom.GetMaximum())
        maxNew = max(newUp.GetMaximum(), newNom.GetMaximum())

    l = TLegend(0.7, 0.7, 0.88, 0.88)
    l.SetBorderSize(0)
    l.AddEntry(oldUp, "%s Up" % args.syst)
    l.AddEntry(oldNom, "nominal")
    l.AddEntry(oldDn, "%s Dn" % args.syst)

    c.cd()
    c.Draw()
    pad1.Draw()
    pad2.Draw()
    pad3.Draw()


    ### Old syst ###
    pad1.cd()
    oldUp.SetTitle("Old %s %s  m_{t} = %.1f GeV" % (args.plot, args.syst, m/10.))
    oldUp.GetYaxis().SetRangeUser(0, 1.05*maxOld) 
    oldUp.Draw("hist")
    oldNom.Draw("hist same")
    oldDn.Draw("hist same")
    l.Draw("same")

    pad2.cd()
    resOldUp.GetYaxis().SetRangeUser(minOldRes - paddingOldRes, maxOldRes + paddingOldRes)
    resOldUp.SetTitle("Residual")
    resOldUp.Draw("hist%s" % ("" if args.noerrors else " e1"))
    resOldDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    resLine.Draw("same")

    pad3.cd()
    ratioOldUp.GetYaxis().SetRangeUser(minOldRatio - paddingOldRatio, maxOldRatio + paddingOldRatio)
    ratioOldUp.SetTitle("Ratio")
    ratioOldUp.Draw("hist%s" % ("" if args.noerrors else " e1"))
    ratioOldDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    ratioLine.Draw("same")

    c.SaveAs("%s/old%s_mt%d.png" % (args.outDir, args.syst, m))

    c.cd()
    c.ResetDrawn()
    c.Draw()
    pad1.Draw()
    pad2.Draw()
    pad3.Draw()


    ### New syst ###
    pad1.cd()
    newUp.SetTitle("New %s %s  m_{t} = %.1f GeV" % (args.plot, args.syst, m/10.))
    newUp.GetYaxis().SetRangeUser(0, 1.05*maxNew)
    newUp.Draw("hist")
    newNom.Draw("hist same")
    newDn.Draw("hist same")
    l.Draw("same")

    pad2.cd()
    resNewUp.GetYaxis().SetRangeUser(minNewRes - paddingNewRes, maxNewRes + paddingNewRes)
    resNewUp.SetTitle("Residual")
    resNewUp.Draw("hist%s" % ("" if args.noerrors else " e1"))
    resNewDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    resLine.Draw("same")

    pad3.cd()
    ratioNewUp.GetYaxis().SetRangeUser(minNewRatio - paddingNewRatio, maxNewRatio + paddingNewRatio)
    ratioNewUp.SetTitle("Ratio")
    ratioNewUp.Draw("hist%s" % ("" if args.noerrors else " e1"))
    ratioNewDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    ratioLine.Draw("same")

    c.SaveAs("%s/new%s_mt%d.png" % (args.outDir, args.syst, m))

    c.cd()
    c.ResetDrawn()
    c.Draw()
    pad1.Draw()
    pad2.Draw()
    pad3.Draw()


    ### Comparison ###
    pad1.cd()

    newUp.SetLineColor(kOrange)
    newDn.SetLineColor(kCyan)

    resNewUp.SetLineColor(kOrange)
    ratioNewUp.SetLineColor(kOrange)
    resNewDn.SetLineColor(kCyan)
    ratioNewDn.SetLineColor(kCyan)


    oldNom.SetLineStyle(7)
    l = TLegend(0.7, 0.6, 0.88, 0.88)
    l.SetBorderSize(0)
    l.AddEntry(oldUp, "Old %s Up" % args.syst)
    l.AddEntry(newUp, "New %s Up" % args.syst) 
    l.AddEntry(oldNom, "Old nominal")
    l.AddEntry(newNom, "New nominal")
    l.AddEntry(oldDn, "Old %s Dn" % args.syst)
    l.AddEntry(newDn, "New %s Dn" % args.syst)

    oldUp.SetTitle("Old and New %s %s  m_{t} = %.1f GeV" % (args.plot, args.syst, m/10.))
    oldUp.Draw("hist")
    newUp.Draw("hist same")
    oldNom.Draw("hist same")
    newNom.Draw("hist same")
    oldDn.Draw("hist same")
    newDn.Draw("hist same")
    l.Draw("same")

    pad2.cd()
    resOldUp.GetYaxis().SetRangeUser(min(minOldRes, minNewRes) - max(paddingOldRes, paddingNewRes), max(maxOldRes, maxNewRes) + max(paddingOldRes, paddingNewRes))
    resOldUp.Draw("hist%s" % ("" if args.noerrors else " e1"))
    resNewUp.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    resOldDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    resNewDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    resLine.Draw("same")

    pad3.cd()
    ratioOldUp.GetYaxis().SetRangeUser(min(minOldRatio, minNewRatio) - max(paddingOldRatio, paddingNewRatio), max(maxOldRatio, maxNewRatio) + max(paddingOldRatio, paddingNewRatio))
    ratioOldUp.Draw("hist%s" % ("" if args.noerrors else " e1"))
    ratioNewUp.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    ratioOldDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    ratioNewDn.Draw("hist%s same" % ("" if args.noerrors else " e1"))
    ratioLine.Draw("same")

    c.SaveAs("%s/comparison_old_new_%s_mt%d.png" % (args.outDir, args.syst, m))


    canvasCompare.cd()
    canvasCompare.ResetDrawn()
    canvasCompare.Draw()
    compPad1.Draw()
    compPad2.Draw()

    compPad1.cd()
    ratioNewOldUp = newUp.Clone("ratioNewOldUp")
    ratioNewOldUp.SetDirectory(0)
    ratioNewOldUp.Divide(oldUp)
    ratioNewOldUp.GetYaxis().SetRangeUser(ratioNewOldUp.GetBinContent(ratioNewOldUp.GetMinimumBin())*0.95, ratioNewOldUp.GetBinContent(ratioNewOldUp.GetMaximumBin())*1.05)
    ratioNewOldUp.SetTitle("New / Old %s %s Up  m_{t} = %.1f GeV" % (args.plot, args.syst, m/10.))
    ratioNewOldUp.SetLineColor(kRed)

    ratioNewOldDn = newDn.Clone("ratioNewOldDn")
    ratioNewOldDn.SetDirectory(0)
    ratioNewOldDn.Divide(oldDn)
    ratioNewOldDn.SetTitle("New / Old %s %s Down  m_{t} = %.1f GeV" % (args.plot, args.syst, m/10.))
    ratioNewOldDn.SetLineColor(kBlue)

    compPad1.cd()
    ratioNewOldUp.Draw("hist%s" % ("" if args.noerrors else " e1"))
    ratioLine.Draw("same")

    compPad2.cd()
    ratioNewOldDn.Draw("hist%s" % ("" if args.noerrors else " e1"))
    ratioLine.Draw("same")
    canvasCompare.SaveAs("%s/ratio_new_old_%s_mt%d.png" % (args.outDir, args.syst, m))

    
