#!/usr/bin/env python
from ROOT import *

samples = ["TTbar", "ST_tW", "DY", "Diboson", "TTV", "Data"]

mc = {"nom":None, "up":None, "down":None}
data = dataBF = dataGH = None 

mc_BF = {"nom":None, "up":None, "down":None}
mc_GH = {"nom":None, "up":None, "down":None}


for s in samples:
    # Nominal
    f = TFile.Open("histograms/hists/%s.root" % s)
    if s == "Data":
        data = f.Get("nVtx_Data")
        data.SetDirectory(0)
    elif mc["nom"] is None:
        mc["nom"] = f.Get("nVtx_%s" % s)
        mc["nom"].SetDirectory(0)
    else:
        mc["nom"].Add(f.Get("nVtx_%s" % s))
    f.Close()

    f = TFile.Open("histograms_BCDEF/hists/%s.root" % s)
    if s == "Data":
        data_BF = f.Get("nVtx_Data")
        data_BF.SetDirectory(0)
    elif mc_BF["nom"] is None:
        mc_BF["nom"] = f.Get("nVtx_%s" % s)
        mc_BF["nom"].SetDirectory(0)
    else:
        mc_BF["nom"].Add(f.Get("nVtx_%s" % s))
    f.Close()
    
    f = TFile.Open("histograms_GH/hists/%s.root" % s)
    if s == "Data":
        data_GH = f.Get("nVtx_Data")
        data_GH.SetDirectory(0)
    elif mc_GH["nom"] is None:
        mc_GH["nom"] = f.Get("nVtx_%s" % s)
        mc_GH["nom"].SetDirectory(0)
    else:
        mc_GH["nom"].Add(f.Get("nVtx_%s" % s))
    f.Close()

    for var in ["up","down"]: 
        if s == "Data":
            continue
        f = TFile.Open("histograms/histsPU_%s/%s.root" % (var,s))
        if mc[var] is None:
            mc[var] = f.Get("nVtx_%s" % s)
            mc[var].SetDirectory(0)
        else:
            mc[var].Add(f.Get("nVtx_%s" % s))
        f.Close()

        f = TFile.Open("histograms_BCDEF/histsPU_%s/%s.root" % (var,s))
        if s == "Data":
            continue
        elif mc_BF[var] is None:
            mc_BF[var] = f.Get("nVtx_%s" % s)
            mc_BF[var].SetDirectory(0)
        else:
            mc_BF[var].Add(f.Get("nVtx_%s" % s))
        f.Close()
        
        f = TFile.Open("histograms_GH/histsPU_%s/%s.root" % (var,s))
        if s == "Data":
            continue
        elif mc_GH[var] is None:
            mc_GH[var] = f.Get("nVtx_%s" % s)
            mc_GH[var].SetDirectory(0)
        else:
            mc_GH[var].Add(f.Get("nVtx_%s" % s))
        f.Close()
   
gStyle.SetOptStat(0)
c = TCanvas("c","c",1200,800)

maxY_BF = -100
maxY_BF = max(maxY_BF, mc_BF["nom"].GetMaximum())
maxY_BF = max(maxY_BF, mc_BF["up"].GetMaximum())
maxY_BF = max(maxY_BF, mc_BF["down"].GetMaximum())
maxY_BF = max(maxY_BF, data_BF.GetMaximum())

mc_BF["nom"].SetTitle("nVtx eras BCDEF")
mc_BF["nom"].GetXaxis().SetTitle("nVtx")
mc_BF["nom"].GetXaxis().SetTitleOffset(1.1)
mc_BF["nom"].GetYaxis().SetTitle("Entries")
mc_BF["nom"].GetYaxis().SetTitleOffset(1.2)
mc_BF["nom"].GetYaxis().SetRangeUser(0, maxY_BF*1.05)
mc_BF["nom"].SetLineColor(kGreen+3)
mc_BF["nom"].Draw("hist")
mc_BF["up"].SetMarkerStyle(22)
mc_BF["up"].SetMarkerSize(1)
mc_BF["up"].SetMarkerColor(kRed)
mc_BF["up"].SetLineColor(kRed)

mc_BF["down"].SetMarkerStyle(23)
mc_BF["down"].SetMarkerSize(1)
mc_BF["down"].SetMarkerColor(kBlue)
mc_BF["down"].SetLineColor(kBlue)

mc_BF["up"].Draw("hist PL same")
mc_BF["down"].Draw("hist PL same")

data_BF.SetMarkerStyle(20)
data_BF.SetMarkerSize(1)
data_BF.Draw("e,X0,same")

l = TLegend(0.7, 0.7, 0.88, 0.88)
l.SetBorderSize(0)
l.AddEntry(mc_BF["up"], "pileup up")
l.AddEntry(mc_BF["nom"], "nominal MC")
l.AddEntry(mc_BF["down"], "pileup down")
l.AddEntry(data_BF, "Data")
l.Draw("same")

c.SaveAs("eraBF_nVtx.png")

maxY_GH = -100
maxY_GH = max(maxY_GH, mc_GH["nom"].GetMaximum())
maxY_GH = max(maxY_GH, mc_GH["up"].GetMaximum())
maxY_GH = max(maxY_GH, mc_GH["down"].GetMaximum())
maxY_GH = max(maxY_GH, data_GH.GetMaximum())

mc_GH["nom"].SetTitle("nVtx eras GH")
mc_GH["nom"].GetXaxis().SetTitle("nVtx")
mc_GH["nom"].GetXaxis().SetTitleOffset(1.1)
mc_GH["nom"].GetYaxis().SetTitle("Entries")
mc_GH["nom"].GetYaxis().SetTitleOffset(1.2)
mc_GH["nom"].GetYaxis().SetRangeUser(0, maxY_GH*1.05)
mc_GH["nom"].SetLineColor(kGreen+3)
mc_GH["nom"].Draw("hist")
mc_GH["up"].SetMarkerStyle(22)
mc_GH["up"].SetMarkerSize(1)
mc_GH["up"].SetMarkerColor(kRed)
mc_GH["up"].SetLineColor(kRed)

mc_GH["down"].SetMarkerStyle(23)
mc_GH["down"].SetMarkerSize(1)
mc_GH["down"].SetMarkerColor(kBlue)
mc_GH["down"].SetLineColor(kBlue)

mc_GH["up"].Draw("hist PL same")
mc_GH["down"].Draw("hist PL same")

data_GH.SetMarkerStyle(20)
data_GH.SetMarkerSize(1)
data_GH.Draw("e,X0,same")

l = TLegend(0.7, 0.7, 0.88, 0.88)
l.SetBorderSize(0)
l.AddEntry(mc_GH["up"], "pileup up")
l.AddEntry(mc_GH["nom"], "nominal MC")
l.AddEntry(mc_GH["down"], "pileup down")
l.AddEntry(data_GH, "Data")
l.Draw("same")

c.SaveAs("eraGH_nVtx.png")




