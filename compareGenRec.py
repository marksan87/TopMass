#!/usr/bin/env python
from ROOT import *
from argparse import ArgumentParser
import os
import sys

gROOT.SetBatch(True)

obsTitle = {\
    "ptll"    : "p_{T}(ll)",
    "Mll"     : "M(ll)",
    "ptpos"   : "p_{T}(l^{+})",
    "ptneg"   : "p_{T}(l^{-})",
    "Epos"    : "E(l^{+})",
    "Eneg"    : "E(l^{-})",
    "ptp_ptm" : "p_{T}(l^{+}) + p_{T}(l^{-})",
    "Ep_Em"   : "E(l^{+}) + E(l^{-})"
}

observables = ["ptll", "ptneg", "Eneg", "ptp_ptm", "Ep_Em", "Mll", "ptpos", "Epos"]

parser = ArgumentParser()
parser.add_argument("-i", "--inF", default="root://cmseos.fnal.gov//store/user/msaunder/13TeV_AnalysisNtuples/emu/V08_00_26_07/TTbarPowheg_AnalysisNtuple.root")
parser.add_argument("-r", "--inRootF", default="", help="plot histograms from this root file instead of from AnalysisNtuples")
parser.add_argument("-o", "--outDir", default="rec_gen_comparison")
args = parser.parse_args()

outDir = args.outDir
os.system("mkdir -p %s" % outDir)
f = TFile.Open(args.inF)
t = f.Get("AnalysisTree")

inputRootF = args.inRootF


if inputRootF != "":
    # Load histograms from this root file instead of drawing
    inRootF = TFile.Open(inputRootF, "read")
    
    plots = [\
        "rec_ptp_ptm",
        "rec_ptp_ptm_full",
        "gen_ptp_ptm",
        
        "rec_Ep_Em",
        "rec_Ep_Em_full",
        "gen_Ep_Em",
        
        "rec_ptpos",
        "rec_ptpos_full",
        "gen_ptpos",

        "rec_ptneg",
        "rec_ptneg_full",
        "gen_ptneg",
        
        "rec_Epos",
        "rec_Epos_full",
        "gen_Epos",

        "rec_Eneg",
        "rec_Eneg_full",
        "gen_Eneg",

        "rec_ptll",
        "rec_ptll_full",
        "gen_ptll",

        "rec_Mll",
        "rec_Mll_full",
        "gen_Mll",

        "rec_eleEta",
        "rec_eleEta_full",
        "gen_eleEta",
        "rec_elePhi",
        "rec_elePhi_full",
        "gen_elePhi",
        "rec_elePt",
        "rec_elePt_full",
        "gen_elePt",

        "rec_muEta",
        "rec_muEta_full",
        "gen_muEta",
        "rec_muPhi",
        "rec_muPhi_full",
        "gen_muPhi",
        "rec_muPt",
        "rec_muPt_full",
        "gen_muPt",


        "diff_ptll",
        "diffpct_ptll",

        "diff_Mll",
        "diffpct_Mll",

        "diff_ptpos",
        "diffpct_ptpos",

        "diff_ptneg",
        "diffpct_ptneg",

        "diff_Epos",
        "diffpct_Epos",

        "diff_Eneg",
        "diffpct_Eneg",

        "diff_ptp_ptm",
        "diffpct_ptp_ptm",

        "diff_Ep_Em",
        "diffpct_Ep_Em",

        "diff_eleEta",
        "diff_elePhi",
        "diff_elePt",
        "diffpct_elePt",

        "diff_muEta",
        "diff_muPhi",
        "diff_muPt",
        "diffpct_muPt",
        ]
    for p in plots:
        print "now on plot:",p
        exec("%s = inRootF.Get('%s')" % (p,p))
        exec("%s.SetDirectory(0)" % p)

    inRootF.Close()

else:
    rec_ptp_ptm = TH1F("rec_ptp_ptm", "rec p_{T}(l^{+}) + p_{T}(l^{-})", 20, 45, 225)
    rec_ptp_ptm.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    rec_ptp_ptm.GetXaxis().SetTitleOffset(1.3)
    rec_ptp_ptm.GetYaxis().SetTitle("Events")
    rec_ptp_ptm.GetYaxis().SetTitleOffset(1.3)
    
    rec_ptp_ptm_full = TH1F("rec_ptp_ptm_full", "rec p_{T}(l^{+}) + p_{T}(l^{-})  no gen cuts", 20, 45, 225)
    rec_ptp_ptm_full.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    rec_ptp_ptm_full.GetXaxis().SetTitleOffset(1.3)
    rec_ptp_ptm_full.GetYaxis().SetTitle("Events")
    rec_ptp_ptm_full.GetYaxis().SetTitleOffset(1.3)

    gen_ptp_ptm = TH1F("gen_ptp_ptm", "gen p_{T}(l^{+}) + p_{T}(l^{-})", 20, 45, 225)
    gen_ptp_ptm.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    gen_ptp_ptm.GetXaxis().SetTitleOffset(1.3)
    gen_ptp_ptm.GetYaxis().SetTitle("Events")
    gen_ptp_ptm.GetYaxis().SetTitleOffset(1.3)

    gen_ptp_ptm_Wonly = TH1F("gen_ptp_ptm_Wonly", "gen p_{T}(l^{+}) + p_{T}(l^{-})  W prompt leptons", 20, 45, 225)
    gen_ptp_ptm_Wonly.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    gen_ptp_ptm_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_ptp_ptm_Wonly.GetYaxis().SetTitle("Events")
    gen_ptp_ptm_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_ptp_ptm_fromTau = TH1F("gen_ptp_ptm_fromTau", "gen p_{T}(l^{+}) + p_{T}(l^{-})  from #tau decays", 20, 45, 225)
    gen_ptp_ptm_fromTau.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    gen_ptp_ptm_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_ptp_ptm_fromTau.GetYaxis().SetTitle("Events")
    gen_ptp_ptm_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_ptp_ptm_cut = TH1F("gen_ptp_ptm_cut", "gen p_{T}(l^{+}) + p_{T}(l^{-})   |gen - rec| / rec < 0.2", 20, 45, 225)
    gen_ptp_ptm_cut.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    gen_ptp_ptm_cut.GetXaxis().SetTitleOffset(1.3)
    gen_ptp_ptm_cut.GetYaxis().SetTitle("Events")
    gen_ptp_ptm_cut.GetYaxis().SetTitleOffset(1.3)

    rec_Ep_Em = TH1F("rec_Ep_Em", "rec E(l^{+}) + E(l^{-})", 20, 50, 450)
    rec_Ep_Em.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    rec_Ep_Em.GetXaxis().SetTitleOffset(1.3)
    rec_Ep_Em.GetYaxis().SetTitle("Events")
    rec_Ep_Em.GetYaxis().SetTitleOffset(1.3)

    rec_Ep_Em_full = TH1F("rec_Ep_Em_full", "rec E(l^{+}) + E(l^{-})  no gen cuts", 20, 50, 450)
    rec_Ep_Em_full.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    rec_Ep_Em_full.GetXaxis().SetTitleOffset(1.3)
    rec_Ep_Em_full.GetYaxis().SetTitle("Events")
    rec_Ep_Em_full.GetYaxis().SetTitleOffset(1.3)

    gen_Ep_Em = TH1F("gen_Ep_Em", "gen E(l^{+}) + E(l^{-})", 20, 50, 450)
    gen_Ep_Em.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    gen_Ep_Em.GetXaxis().SetTitleOffset(1.3)
    gen_Ep_Em.GetYaxis().SetTitle("Events")
    gen_Ep_Em.GetYaxis().SetTitleOffset(1.3)

    gen_Ep_Em_Wonly = TH1F("gen_Ep_Em_Wonly", "gen E(l^{+}) + E(l^{-})  W prompt leptons", 20, 50, 450)
    gen_Ep_Em_Wonly.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    gen_Ep_Em_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_Ep_Em_Wonly.GetYaxis().SetTitle("Events")
    gen_Ep_Em_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_Ep_Em_fromTau = TH1F("gen_Ep_Em_fromTau", "gen E(l^{+}) + E(l^{-})  from #tau decays", 20, 50, 450)
    gen_Ep_Em_fromTau.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    gen_Ep_Em_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_Ep_Em_fromTau.GetYaxis().SetTitle("Events")
    gen_Ep_Em_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_Ep_Em_cut = TH1F("gen_Ep_Em_cut", "gen E(l^{+}) + E(l^{-})   |gen - rec| / rec < 0.2", 20, 50, 450)
    gen_Ep_Em_cut.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    gen_Ep_Em_cut.GetXaxis().SetTitleOffset(1.3)
    gen_Ep_Em_cut.GetYaxis().SetTitle("Events")
    gen_Ep_Em_cut.GetYaxis().SetTitleOffset(1.3)

    rec_Epos = TH1F("rec_Epos", "rec E(l^{+})", 20, 20, 220)
    rec_Epos.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    rec_Epos.GetXaxis().SetTitleOffset(1.3)
    rec_Epos.GetYaxis().SetTitle("Events")
    rec_Epos.GetYaxis().SetTitleOffset(1.3)

    rec_Epos_full = TH1F("rec_Epos_full", "rec E(l^{+})  no gen cuts", 20, 20, 220)
    rec_Epos_full.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    rec_Epos_full.GetXaxis().SetTitleOffset(1.3)
    rec_Epos_full.GetYaxis().SetTitle("Events")
    rec_Epos_full.GetYaxis().SetTitleOffset(1.3)

    gen_Epos = TH1F("gen_Epos", "gen E(l^{+})", 20, 20, 220)
    gen_Epos.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    gen_Epos.GetXaxis().SetTitleOffset(1.3)
    gen_Epos.GetYaxis().SetTitle("Events")
    gen_Epos.GetYaxis().SetTitleOffset(1.3)

    gen_Epos_Wonly = TH1F("gen_Epos_Wonly", "gen E(l^{+})  W prompt leptons", 20, 20, 220)
    gen_Epos_Wonly.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    gen_Epos_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_Epos_Wonly.GetYaxis().SetTitle("Events")
    gen_Epos_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_Epos_fromTau = TH1F("gen_Epos_fromTau", "gen E(l^{+})  from #tau decays", 20, 20, 220)
    gen_Epos_fromTau.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    gen_Epos_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_Epos_fromTau.GetYaxis().SetTitle("Events")
    gen_Epos_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_Epos_cut = TH1F("gen_Epos_cut", "gen E(l^{+})   |gen - rec| / rec < 0.2", 20, 20, 220)
    gen_Epos_cut.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    gen_Epos_cut.GetXaxis().SetTitleOffset(1.3)
    gen_Epos_cut.GetYaxis().SetTitle("Events")
    gen_Epos_cut.GetYaxis().SetTitleOffset(1.3)

    rec_Eneg = TH1F("rec_Eneg", "rec E(l^{-})", 20, 20, 220)
    rec_Eneg.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    rec_Eneg.GetXaxis().SetTitleOffset(1.3)
    rec_Eneg.GetYaxis().SetTitle("Events")
    rec_Eneg.GetYaxis().SetTitleOffset(1.3)

    rec_Eneg_full = TH1F("rec_Eneg_full", "rec E(l^{-})  no gen cuts", 20, 20, 220)
    rec_Eneg_full.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    rec_Eneg_full.GetXaxis().SetTitleOffset(1.3)
    rec_Eneg_full.GetYaxis().SetTitle("Events")
    rec_Eneg_full.GetYaxis().SetTitleOffset(1.3)

    gen_Eneg = TH1F("gen_Eneg", "gen E(l^{-})", 20, 20, 220)
    gen_Eneg.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    gen_Eneg.GetXaxis().SetTitleOffset(1.3)
    gen_Eneg.GetYaxis().SetTitle("Events")
    gen_Eneg.GetYaxis().SetTitleOffset(1.3)

    gen_Eneg_Wonly = TH1F("gen_Eneg_Wonly", "gen E(l^{-})  W prompt leptons", 20, 20, 220)
    gen_Eneg_Wonly.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    gen_Eneg_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_Eneg_Wonly.GetYaxis().SetTitle("Events")
    gen_Eneg_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_Eneg_fromTau = TH1F("gen_Eneg_fromTau", "gen E(l^{-})  from #tau decays", 20, 20, 220)
    gen_Eneg_fromTau.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    gen_Eneg_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_Eneg_fromTau.GetYaxis().SetTitle("Events")
    gen_Eneg_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_Eneg_cut = TH1F("gen_Eneg_cut", "gen E(l^{-})   |gen - rec| / rec < 0.2", 20, 20, 220)
    gen_Eneg_cut.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    gen_Eneg_cut.GetXaxis().SetTitleOffset(1.3)
    gen_Eneg_cut.GetYaxis().SetTitle("Events")
    gen_Eneg_cut.GetYaxis().SetTitleOffset(1.3)

    rec_ptpos = TH1F("rec_ptpos", "rec p_{T}(l^{+})", 20, 30, 210)
    rec_ptpos.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    rec_ptpos.GetXaxis().SetTitleOffset(1.3)
    rec_ptpos.GetYaxis().SetTitle("Events")
    rec_ptpos.GetYaxis().SetTitleOffset(1.3)

    rec_ptpos_full = TH1F("rec_ptpos_full", "rec p_{T}(l^{+})  no gen cuts", 20, 30, 210)
    rec_ptpos_full.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    rec_ptpos_full.GetXaxis().SetTitleOffset(1.3)
    rec_ptpos_full.GetYaxis().SetTitle("Events")
    rec_ptpos_full.GetYaxis().SetTitleOffset(1.3)

    gen_ptpos = TH1F("gen_ptpos", "gen p_{T}(l^{+})", 20, 30, 210)
    gen_ptpos.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    gen_ptpos.GetXaxis().SetTitleOffset(1.3)
    gen_ptpos.GetYaxis().SetTitle("Events")
    gen_ptpos.GetYaxis().SetTitleOffset(1.3)

    gen_ptpos_Wonly = TH1F("gen_ptpos_Wonly", "gen p_{T}(l^{+})  W prompt leptons", 20, 30, 210)
    gen_ptpos_Wonly.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    gen_ptpos_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_ptpos_Wonly.GetYaxis().SetTitle("Events")
    gen_ptpos_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_ptpos_fromTau = TH1F("gen_ptpos_fromTau", "gen p_{T}(l^{+})  from #tau decays", 20, 30, 210)
    gen_ptpos_fromTau.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    gen_ptpos_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_ptpos_fromTau.GetYaxis().SetTitle("Events")
    gen_ptpos_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_ptpos_cut = TH1F("gen_ptpos_cut", "gen p_{T}(l^{+})   |gen - rec| / rec < 0.2", 20, 30, 210)
    gen_ptpos_cut.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    gen_ptpos_cut.GetXaxis().SetTitleOffset(1.3)
    gen_ptpos_cut.GetYaxis().SetTitle("Events")
    gen_ptpos_cut.GetYaxis().SetTitleOffset(1.3)

    rec_ptneg = TH1F("rec_ptneg", "rec p_{T}(l^{-})", 20, 30, 210)
    rec_ptneg.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    rec_ptneg.GetXaxis().SetTitleOffset(1.3)
    rec_ptneg.GetYaxis().SetTitle("Events")
    rec_ptneg.GetYaxis().SetTitleOffset(1.3)

    rec_ptneg_full = TH1F("rec_ptneg_full", "rec p_{T}(l^{-})  no gen cuts", 20, 30, 210)
    rec_ptneg_full.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    rec_ptneg_full.GetXaxis().SetTitleOffset(1.3)
    rec_ptneg_full.GetYaxis().SetTitle("Events")
    rec_ptneg_full.GetYaxis().SetTitleOffset(1.3)

    gen_ptneg = TH1F("gen_ptneg", "gen p_{T}(l^{-})", 20, 30, 210)
    gen_ptneg.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    gen_ptneg.GetXaxis().SetTitleOffset(1.3)
    gen_ptneg.GetYaxis().SetTitle("Events")
    gen_ptneg.GetYaxis().SetTitleOffset(1.3)

    gen_ptneg_Wonly = TH1F("gen_ptneg_Wonly", "gen p_{T}(l^{-})  W prompt leptons", 20, 30, 210)
    gen_ptneg_Wonly.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    gen_ptneg_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_ptneg_Wonly.GetYaxis().SetTitle("Events")
    gen_ptneg_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_ptneg_fromTau = TH1F("gen_ptneg_fromTau", "gen p_{T}(l^{-})  from #tau decays", 20, 30, 210)
    gen_ptneg_fromTau.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    gen_ptneg_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_ptneg_fromTau.GetYaxis().SetTitle("Events")
    gen_ptneg_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_ptneg_cut = TH1F("gen_ptneg_cut", "gen p_{T}(l^{-})   |gen - rec| / rec < 0.2", 20, 30, 210)
    gen_ptneg_cut.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    gen_ptneg_cut.GetXaxis().SetTitleOffset(1.3)
    gen_ptneg_cut.GetYaxis().SetTitle("Events")
    gen_ptneg_cut.GetYaxis().SetTitleOffset(1.3)

    rec_ptll = TH1F("rec_ptll", "rec p_{T}(ll)", 20, 0, 200)
    rec_ptll.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    rec_ptll.GetXaxis().SetTitleOffset(1.3)
    rec_ptll.GetYaxis().SetTitle("Events")
    rec_ptll.GetYaxis().SetTitleOffset(1.3)

    rec_ptll_full = TH1F("rec_ptll_full", "rec p_{T}(ll)  no gen cuts", 20, 0, 200)
    rec_ptll_full.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    rec_ptll_full.GetXaxis().SetTitleOffset(1.3)
    rec_ptll_full.GetYaxis().SetTitle("Events")
    rec_ptll_full.GetYaxis().SetTitleOffset(1.3)

    gen_ptll = TH1F("gen_ptll", "gen p_{T}(ll)", 20, 0, 200)
    gen_ptll.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    gen_ptll.GetXaxis().SetTitleOffset(1.3)
    gen_ptll.GetYaxis().SetTitle("Events")
    gen_ptll.GetYaxis().SetTitleOffset(1.3)

    gen_ptll_Wonly = TH1F("gen_ptll_Wonly", "gen p_{T}(ll)  W prompt leptons", 20, 0, 200)
    gen_ptll_Wonly.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    gen_ptll_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_ptll_Wonly.GetYaxis().SetTitle("Events")
    gen_ptll_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_ptll_fromTau = TH1F("gen_ptll_fromTau", "gen p_{T}(ll)  from #tau decays", 20, 0, 200)
    gen_ptll_fromTau.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    gen_ptll_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_ptll_fromTau.GetYaxis().SetTitle("Events")
    gen_ptll_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_ptll_cut = TH1F("gen_ptll_cut", "gen p_{T}(ll)   |gen - rec| / rec < 0.2", 20, 0, 200)
    gen_ptll_cut.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    gen_ptll_cut.GetXaxis().SetTitleOffset(1.3)
    gen_ptll_cut.GetYaxis().SetTitle("Events")
    gen_ptll_cut.GetYaxis().SetTitleOffset(1.3)

    rec_Mll = TH1F("rec_Mll", "rec M(ll)", 20, 20, 260)
    rec_Mll.GetXaxis().SetTitle("M(ll) [GeV]")
    rec_Mll.GetXaxis().SetTitleOffset(1.3)
    rec_Mll.GetYaxis().SetTitle("Events")
    rec_Mll.GetYaxis().SetTitleOffset(1.3)

    rec_Mll_full = TH1F("rec_Mll_full", "rec M(ll)  no gen cuts", 20, 20, 260)
    rec_Mll_full.GetXaxis().SetTitle("M(ll) [GeV]")
    rec_Mll_full.GetXaxis().SetTitleOffset(1.3)
    rec_Mll_full.GetYaxis().SetTitle("Events")
    rec_Mll_full.GetYaxis().SetTitleOffset(1.3)

    gen_Mll = TH1F("gen_Mll", "gen M(ll)", 20, 20, 260)
    gen_Mll.GetXaxis().SetTitle("M(ll) [GeV]")
    gen_Mll.GetXaxis().SetTitleOffset(1.3)
    gen_Mll.GetYaxis().SetTitle("Events")
    gen_Mll.GetYaxis().SetTitleOffset(1.3)

    gen_Mll_Wonly = TH1F("gen_Mll_Wonly", "gen M(ll)  W prompt leptons", 20, 20, 260)
    gen_Mll_Wonly.GetXaxis().SetTitle("M(ll) [GeV]")
    gen_Mll_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_Mll_Wonly.GetYaxis().SetTitle("Events")
    gen_Mll_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_Mll_fromTau = TH1F("gen_Mll_fromTau", "gen M(ll)   from #tau decays", 20, 20, 260)
    gen_Mll_fromTau.GetXaxis().SetTitle("M(ll) [GeV]")
    gen_Mll_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_Mll_fromTau.GetYaxis().SetTitle("Events")
    gen_Mll_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_Mll_cut = TH1F("gen_Mll_cut", "gen M(ll)   |gen - rec| / rec < 0.2", 20, 20, 260)
    gen_Mll_cut.GetXaxis().SetTitle("M(ll) [GeV]")
    gen_Mll_cut.GetXaxis().SetTitleOffset(1.3)
    gen_Mll_cut.GetYaxis().SetTitle("Events")
    gen_Mll_cut.GetYaxis().SetTitleOffset(1.3)

    rec_elePt = TH1F("rec_elePt", "rec ele p_{T}", 18, 25, 205)
    rec_elePt.GetXaxis().SetTitle("p_{T} [GeV]")
    rec_elePt.GetXaxis().SetTitleOffset(1.3)
    rec_elePt.GetYaxis().SetTitle("Events")
    rec_elePt.GetYaxis().SetTitleOffset(1.3)

    rec_elePt_full = TH1F("rec_elePt_full", "rec ele p_{T}  no gen cuts", 18, 25, 205)
    rec_elePt_full.GetXaxis().SetTitle("p_{T} [GeV]")
    rec_elePt_full.GetXaxis().SetTitleOffset(1.3)
    rec_elePt_full.GetYaxis().SetTitle("Events")
    rec_elePt_full.GetYaxis().SetTitleOffset(1.3)

    gen_elePt = TH1F("gen_elePt", "gen ele p_{T}", 18, 25, 205)
    gen_elePt.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_elePt.GetXaxis().SetTitleOffset(1.3)
    gen_elePt.GetYaxis().SetTitle("Events")
    gen_elePt.GetYaxis().SetTitleOffset(1.3)

    gen_elePt_Wonly = TH1F("gen_elePt_Wonly", "gen ele p_{T}  w prompt leptons", 18, 25, 205)
    gen_elePt_Wonly.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_elePt_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_elePt_Wonly.GetYaxis().SetTitle("Events")
    gen_elePt_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_elePt_fromTau = TH1F("gen_elePt_fromTau", "gen ele p_{T}  from #tau decays", 18, 25, 205)
    gen_elePt_fromTau.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_elePt_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_elePt_fromTau.GetYaxis().SetTitle("Events")
    gen_elePt_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_cut_elePt = TH1F("gen_cut_elePt", "gen ele p_{T} cut", 18, 25, 205)
    gen_cut_elePt.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_cut_elePt.GetXaxis().SetTitleOffset(1.3)
    gen_cut_elePt.GetYaxis().SetTitle("Events")
    gen_cut_elePt.GetYaxis().SetTitleOffset(1.3)

    rec_eleEta = TH1F("rec_eleEta", "rec ele #eta", 20, -2.4, 2.4)
    rec_eleEta.GetXaxis().SetTitle("#eta")
    rec_eleEta.GetXaxis().SetTitleOffset(1.3)
    rec_eleEta.GetYaxis().SetTitle("Events")
    rec_eleEta.GetYaxis().SetTitleOffset(1.3)

    rec_eleEta_full = TH1F("rec_eleEta_full", "rec ele #eta  no gen cuts", 20, -2.4, 2.4)
    rec_eleEta_full.GetXaxis().SetTitle("#eta")
    rec_eleEta_full.GetXaxis().SetTitleOffset(1.3)
    rec_eleEta_full.GetYaxis().SetTitle("Events")
    rec_eleEta_full.GetYaxis().SetTitleOffset(1.3)

    gen_eleEta = TH1F("gen_eleEta", "gen ele #eta", 20, -2.4, 2.4)
    gen_eleEta.GetXaxis().SetTitle("#eta")
    gen_eleEta.GetXaxis().SetTitleOffset(1.3)
    gen_eleEta.GetYaxis().SetTitle("Events")
    gen_eleEta.GetYaxis().SetTitleOffset(1.3)

    gen_eleEta_Wonly = TH1F("gen_eleEta_Wonly", "gen ele #eta  W prompt leptons", 20, -2.4, 2.4)
    gen_eleEta_Wonly.GetXaxis().SetTitle("#eta")
    gen_eleEta_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_eleEta_Wonly.GetYaxis().SetTitle("Events")
    gen_eleEta_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_eleEta_fromTau = TH1F("gen_eleEta_fromTau", "gen ele #eta  from #tau decays", 20, -2.4, 2.4)
    gen_eleEta_fromTau.GetXaxis().SetTitle("#eta")
    gen_eleEta_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_eleEta_fromTau.GetYaxis().SetTitle("Events")
    gen_eleEta_fromTau.GetYaxis().SetTitleOffset(1.3)

    rec_elePhi = TH1F("rec_elePhi", "rec ele #phi", 25, -3.2, 3.2)
    rec_elePhi.GetXaxis().SetTitle("#phi")
    rec_elePhi.GetXaxis().SetTitleOffset(1.3)
    rec_elePhi.GetYaxis().SetTitle("Events")
    rec_elePhi.GetYaxis().SetTitleOffset(1.3)

    rec_elePhi_full = TH1F("rec_elePhi_full", "rec ele #phi  no gen cuts", 25, -3.2, 3.2)
    rec_elePhi_full.GetXaxis().SetTitle("#phi")
    rec_elePhi_full.GetXaxis().SetTitleOffset(1.3)
    rec_elePhi_full.GetYaxis().SetTitle("Events")
    rec_elePhi_full.GetYaxis().SetTitleOffset(1.3)

    gen_elePhi = TH1F("gen_elePhi", "gen ele #phi", 25, -3.2, 3.2)
    gen_elePhi.GetXaxis().SetTitle("#phi")
    gen_elePhi.GetXaxis().SetTitleOffset(1.3)
    gen_elePhi.GetYaxis().SetTitle("Events")
    gen_elePhi.GetYaxis().SetTitleOffset(1.3)

    gen_elePhi_Wonly = TH1F("gen_elePhi_Wonly", "gen ele #phi  W prompt leptons", 25, -3.2, 3.2)
    gen_elePhi_Wonly.GetXaxis().SetTitle("#phi")
    gen_elePhi_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_elePhi_Wonly.GetYaxis().SetTitle("Events")
    gen_elePhi_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_elePhi_fromTau = TH1F("gen_elePhi_fromTau", "gen ele #phi  from #tau decays", 25, -3.2, 3.2)
    gen_elePhi_fromTau.GetXaxis().SetTitle("#phi")
    gen_elePhi_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_elePhi_fromTau.GetYaxis().SetTitle("Events")
    gen_elePhi_fromTau.GetYaxis().SetTitleOffset(1.3)

    rec_muPt = TH1F("rec_muPt", "rec mu p_{T}", 18, 25, 205)
    rec_muPt.GetXaxis().SetTitle("p_{T} [GeV]")
    rec_muPt.GetXaxis().SetTitleOffset(1.3)
    rec_muPt.GetYaxis().SetTitle("Events")
    rec_muPt.GetYaxis().SetTitleOffset(1.3)

    rec_muPt_full = TH1F("rec_muPt_full", "rec mu p_{T}  no gen cuts", 18, 25, 205)
    rec_muPt_full.GetXaxis().SetTitle("p_{T} [GeV]")
    rec_muPt_full.GetXaxis().SetTitleOffset(1.3)
    rec_muPt_full.GetYaxis().SetTitle("Events")
    rec_muPt_full.GetYaxis().SetTitleOffset(1.3)

    gen_muPt = TH1F("gen_muPt", "gen mu p_{T}", 18, 25, 205)
    gen_muPt.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_muPt.GetXaxis().SetTitleOffset(1.3)
    gen_muPt.GetYaxis().SetTitle("Events")
    gen_muPt.GetYaxis().SetTitleOffset(1.3)

    gen_muPt_Wonly = TH1F("gen_muPt_Wonly", "gen mu p_{T}  W prompt leptons", 18, 25, 205)
    gen_muPt_Wonly.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_muPt_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_muPt_Wonly.GetYaxis().SetTitle("Events")
    gen_muPt_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_muPt_fromTau = TH1F("gen_muPt_fromTau", "gen mu p_{T}  from #tau decays", 18, 25, 205)
    gen_muPt_fromTau.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_muPt_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_muPt_fromTau.GetYaxis().SetTitle("Events")
    gen_muPt_fromTau.GetYaxis().SetTitleOffset(1.3)

    gen_cut_muPt = TH1F("gen_cut_muPt", "gen mu p_{T} cut", 18, 25, 205)
    gen_cut_muPt.GetXaxis().SetTitle("p_{T} [GeV]")
    gen_cut_muPt.GetXaxis().SetTitleOffset(1.3)
    gen_cut_muPt.GetYaxis().SetTitle("Events")
    gen_cut_muPt.GetYaxis().SetTitleOffset(1.3)

    rec_muEta = TH1F("rec_muEta", "rec mu #eta", 25, -2.4, 2.4)
    rec_muEta.GetXaxis().SetTitle("#eta")
    rec_muEta.GetXaxis().SetTitleOffset(1.3)
    rec_muEta.GetYaxis().SetTitle("Events")
    rec_muEta.GetYaxis().SetTitleOffset(1.3)

    rec_muEta_full = TH1F("rec_muEta_full", "rec mu #eta  no gen cuts", 25, -2.4, 2.4)
    rec_muEta_full.GetXaxis().SetTitle("#eta")
    rec_muEta_full.GetXaxis().SetTitleOffset(1.3)
    rec_muEta_full.GetYaxis().SetTitle("Events")
    rec_muEta_full.GetYaxis().SetTitleOffset(1.3)

    gen_muEta = TH1F("gen_muEta", "gen mu #eta", 25, -2.4, 2.4)
    gen_muEta.GetXaxis().SetTitle("#eta")
    gen_muEta.GetXaxis().SetTitleOffset(1.3)
    gen_muEta.GetYaxis().SetTitle("Events")
    gen_muEta.GetYaxis().SetTitleOffset(1.3)

    gen_muEta_Wonly = TH1F("gen_muEta_Wonly", "gen mu #eta  W prompt leptons", 25, -2.4, 2.4)
    gen_muEta_Wonly.GetXaxis().SetTitle("#eta")
    gen_muEta_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_muEta_Wonly.GetYaxis().SetTitle("Events")
    gen_muEta_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_muEta_fromTau = TH1F("gen_muEta_fromTau", "gen mu #eta  from #tau decays", 25, -2.4, 2.4)
    gen_muEta_fromTau.GetXaxis().SetTitle("#eta")
    gen_muEta_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_muEta_fromTau.GetYaxis().SetTitle("Events")
    gen_muEta_fromTau.GetYaxis().SetTitleOffset(1.3)

    rec_muPhi = TH1F("rec_muPhi", "rec mu #phi", 25, -3.2, 3.2)
    rec_muPhi.GetXaxis().SetTitle("#phi")
    rec_muPhi.GetXaxis().SetTitleOffset(1.3)
    rec_muPhi.GetYaxis().SetTitle("Events")
    rec_muPhi.GetYaxis().SetTitleOffset(1.3)

    rec_muPhi_full = TH1F("rec_muPhi_full", "rec mu #phi  no gen cuts", 25, -3.2, 3.2)
    rec_muPhi_full.GetXaxis().SetTitle("#phi")
    rec_muPhi_full.GetXaxis().SetTitleOffset(1.3)
    rec_muPhi_full.GetYaxis().SetTitle("Events")
    rec_muPhi_full.GetYaxis().SetTitleOffset(1.3)

    gen_muPhi = TH1F("gen_muPhi", "gen mu #phi", 25, -3.2, 3.2)
    gen_muPhi.GetXaxis().SetTitle("#phi")
    gen_muPhi.GetXaxis().SetTitleOffset(1.3)
    gen_muPhi.GetYaxis().SetTitle("Events")
    gen_muPhi.GetYaxis().SetTitleOffset(1.3)

    gen_muPhi_Wonly = TH1F("gen_muPhi_Wonly", "gen mu #phi  W prompt leptons", 25, -3.2, 3.2)
    gen_muPhi_Wonly.GetXaxis().SetTitle("#phi")
    gen_muPhi_Wonly.GetXaxis().SetTitleOffset(1.3)
    gen_muPhi_Wonly.GetYaxis().SetTitle("Events")
    gen_muPhi_Wonly.GetYaxis().SetTitleOffset(1.3)

    gen_muPhi_fromTau = TH1F("gen_muPhi_fromTau", "gen mu #phi  from #tau decays", 25, -3.2, 3.2)
    gen_muPhi_fromTau.GetXaxis().SetTitle("#phi")
    gen_muPhi_fromTau.GetXaxis().SetTitleOffset(1.3)
    gen_muPhi_fromTau.GetYaxis().SetTitle("Events")
    gen_muPhi_fromTau.GetYaxis().SetTitleOffset(1.3)

    
    # Diff
    diff_eleEta = TH1F("diff_eleEta", "diff ele #eta", 200, -0.02, 0.02)
    diff_eleEta.GetXaxis().SetTitle("gen - rec #eta")
    diff_eleEta.GetXaxis().SetTitleOffset(1.3)
    diff_eleEta.GetYaxis().SetTitle("Events")
    diff_eleEta.GetYaxis().SetTitleOffset(1.3)

    diff_eleEta_Wonly = TH1F("diff_eleEta_Wonly", "diff ele #eta  W prompt leptons", 200, -0.02, 0.02)
    diff_eleEta_Wonly.GetXaxis().SetTitle("gen - rec #eta")
    diff_eleEta_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_eleEta_Wonly.GetYaxis().SetTitle("Events")
    diff_eleEta_Wonly.GetYaxis().SetTitleOffset(1.3)

    diff_eleEta_fromTau = TH1F("diff_eleEta_fromTau", "diff ele #eta  from #tau decays", 200, -0.02, 0.02)
    diff_eleEta_fromTau.GetXaxis().SetTitle("gen - rec #eta")
    diff_eleEta_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_eleEta_fromTau.GetYaxis().SetTitle("Events")
    diff_eleEta_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_elePhi = TH1F("diff_elePhi", "diff ele #phi", 200, -0.02, 0.02)
    diff_elePhi.GetXaxis().SetTitle("gen - rec #phi")
    diff_elePhi.GetXaxis().SetTitleOffset(1.3)
    diff_elePhi.GetYaxis().SetTitle("Events")
    diff_elePhi.GetYaxis().SetTitleOffset(1.3)

    diff_elePhi_Wonly = TH1F("diff_elePhi_Wonly", "diff ele #phi  W prompt leptons", 200, -0.02, 0.02)
    diff_elePhi_Wonly.GetXaxis().SetTitle("gen - rec #phi")
    diff_elePhi_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_elePhi_Wonly.GetYaxis().SetTitle("Events")
    diff_elePhi_Wonly.GetYaxis().SetTitleOffset(1.3)
    
    diff_elePhi_fromTau = TH1F("diff_elePhi_fromTau", "diff ele #phi  from #tau decays", 200, -0.02, 0.02)
    diff_elePhi_fromTau.GetXaxis().SetTitle("gen - rec #phi")
    diff_elePhi_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_elePhi_fromTau.GetYaxis().SetTitle("Events")
    diff_elePhi_fromTau.GetYaxis().SetTitleOffset(1.3)
    
    diff_elePt = TH1F("diff_elePt", "diff ele p_{T}", 200, -100, 100)
    diff_elePt.GetXaxis().SetTitle("gen - rec p_{T} [GeV]")
    diff_elePt.GetXaxis().SetTitleOffset(1.3)
    diff_elePt.GetYaxis().SetTitle("Events")
    diff_elePt.GetYaxis().SetTitleOffset(1.3)

    diff_elePt_Wonly = TH1F("diff_elePt_Wonly", "diff ele p_{T}  W prompt leptons", 200, -100, 100)
    diff_elePt_Wonly.GetXaxis().SetTitle("gen - rec p_{T} [GeV]")
    diff_elePt_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_elePt_Wonly.GetYaxis().SetTitle("Events")
    diff_elePt_Wonly.GetYaxis().SetTitleOffset(1.3)

    diff_elePt_fromTau = TH1F("diff_elePt_fromTau", "diff ele p_{T}  from #tau decays", 200, -100, 100)
    diff_elePt_fromTau.GetXaxis().SetTitle("gen - rec p_{T} [GeV]")
    diff_elePt_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_elePt_fromTau.GetYaxis().SetTitle("Events")
    diff_elePt_fromTau.GetYaxis().SetTitleOffset(1.3)
    
    diffpct_elePt = TH1F("diffpct_elePt", "diffpct ele p_{T}", 200, -1.0, 1.0)
    diffpct_elePt.GetXaxis().SetTitle("(gen - rec)/rec p_{T} [GeV]")
    diffpct_elePt.GetXaxis().SetTitleOffset(1.3)
    diffpct_elePt.GetYaxis().SetTitle("Events")
    diffpct_elePt.GetYaxis().SetTitleOffset(1.3)

    diffpct_elePt_Wonly = TH1F("diffpct_elePt_Wonly", "diffpct ele p_{T}  W prompt leptons", 200, -1.0, 1.0)
    diffpct_elePt_Wonly.GetXaxis().SetTitle("(gen - rec)/rec p_{T} [GeV]")
    diffpct_elePt_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_elePt_Wonly.GetYaxis().SetTitle("Events")
    diffpct_elePt_Wonly.GetYaxis().SetTitleOffset(1.3)

    diffpct_elePt_fromTau = TH1F("diffpct_elePt_fromTau", "diffpct ele p_{T}  from #tau decays", 200, -1.0, 1.0)
    diffpct_elePt_fromTau.GetXaxis().SetTitle("(gen - rec)/rec p_{T} [GeV]")
    diffpct_elePt_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_elePt_fromTau.GetYaxis().SetTitle("Events")
    diffpct_elePt_fromTau.GetYaxis().SetTitleOffset(1.3)
    
    
    diff_muEta = TH1F("diff_muEta", "diff mu #eta", 200, -0.02, 0.02)
    diff_muEta.GetXaxis().SetTitle("gen - rec #eta")
    diff_muEta.GetXaxis().SetTitleOffset(1.3)
    diff_muEta.GetYaxis().SetTitle("Events")
    diff_muEta.GetYaxis().SetTitleOffset(1.3)

    diff_muEta_Wonly = TH1F("diff_muEta_Wonly", "diff mu #eta  W prompt leptons", 200, -0.02, 0.02)
    diff_muEta_Wonly.GetXaxis().SetTitle("gen - rec #eta")
    diff_muEta_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_muEta_Wonly.GetYaxis().SetTitle("Events")
    diff_muEta_Wonly.GetYaxis().SetTitleOffset(1.3)

    diff_muEta_fromTau = TH1F("diff_muEta_fromTau", "diff mu #eta  from #tau decays", 200, -0.02, 0.02)
    diff_muEta_fromTau.GetXaxis().SetTitle("gen - rec #eta")
    diff_muEta_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_muEta_fromTau.GetYaxis().SetTitle("Events")
    diff_muEta_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_muPhi = TH1F("diff_muPhi", "diff mu #phi", 200, -0.02, 0.02)
    diff_muPhi.GetXaxis().SetTitle("gen - rec #phi")
    diff_muPhi.GetXaxis().SetTitleOffset(1.3)
    diff_muPhi.GetYaxis().SetTitle("Events")
    diff_muPhi.GetYaxis().SetTitleOffset(1.3)

    diff_muPhi_Wonly = TH1F("diff_muPhi_Wonly", "diff mu #phi  W prompt leptons", 200, -0.02, 0.02)
    diff_muPhi_Wonly.GetXaxis().SetTitle("gen - rec #phi")
    diff_muPhi_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_muPhi_Wonly.GetYaxis().SetTitle("Events")
    diff_muPhi_Wonly.GetYaxis().SetTitleOffset(1.3)
    
    diff_muPhi_fromTau = TH1F("diff_muPhi_fromTau", "diff mu #phi  from #tau decays", 200, -0.02, 0.02)
    diff_muPhi_fromTau.GetXaxis().SetTitle("gen - rec #phi")
    diff_muPhi_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_muPhi_fromTau.GetYaxis().SetTitle("Events")
    diff_muPhi_fromTau.GetYaxis().SetTitleOffset(1.3)
    
    diff_muPt = TH1F("diff_muPt", "diff mu p_{T}", 200, -100, 100)
    diff_muPt.GetXaxis().SetTitle("gen - rec p_{T} [GeV]")
    diff_muPt.GetXaxis().SetTitleOffset(1.3)
    diff_muPt.GetYaxis().SetTitle("Events")
    diff_muPt.GetYaxis().SetTitleOffset(1.3)

    diff_muPt_Wonly = TH1F("diff_muPt_Wonly", "diff mu p_{T}  W prompt leptons", 200, -100, 100)
    diff_muPt_Wonly.GetXaxis().SetTitle("gen - rec p_{T} [GeV]")
    diff_muPt_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_muPt_Wonly.GetYaxis().SetTitle("Events")
    diff_muPt_Wonly.GetYaxis().SetTitleOffset(1.3)

    diff_muPt_fromTau = TH1F("diff_muPt_fromTau", "diff mu p_{T}  from #tau decays", 200, -100, 100)
    diff_muPt_fromTau.GetXaxis().SetTitle("gen - rec p_{T} [GeV]")
    diff_muPt_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_muPt_fromTau.GetYaxis().SetTitle("Events")
    diff_muPt_fromTau.GetYaxis().SetTitleOffset(1.3)
    
    diffpct_muPt = TH1F("diffpct_muPt", "diffpct mu p_{T}", 200, -1.0, 1.0)
    diffpct_muPt.GetXaxis().SetTitle("(gen - rec)/rec p_{T} [GeV]")
    diffpct_muPt.GetXaxis().SetTitleOffset(1.3)
    diffpct_muPt.GetYaxis().SetTitle("Events")
    diffpct_muPt.GetYaxis().SetTitleOffset(1.3)

    diffpct_muPt_Wonly = TH1F("diffpct_muPt_Wonly", "diffpct mu p_{T}  W prompt leptons", 200, -1.0, 1.0)
    diffpct_muPt_Wonly.GetXaxis().SetTitle("(gen - rec)/rec p_{T} [GeV]")
    diffpct_muPt_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_muPt_Wonly.GetYaxis().SetTitle("Events")
    diffpct_muPt_Wonly.GetYaxis().SetTitleOffset(1.3)

    diffpct_muPt_fromTau = TH1F("diffpct_muPt_fromTau", "diffpct mu p_{T}  from #tau decays", 200, -1.0, 1.0)
    diffpct_muPt_fromTau.GetXaxis().SetTitle("(gen - rec)/rec p_{T} [GeV]")
    diffpct_muPt_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_muPt_fromTau.GetYaxis().SetTitle("Events")
    diffpct_muPt_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_eleEta.SetTitle("Electron  gen #eta - rec #eta")
    diff_eleEta_Wonly.SetTitle("Electron  gen #eta - rec #eta  W prompt leptons")
    diff_eleEta_fromTau.SetTitle("Electron  gen #eta - rec #eta  from #tau decays")

    diff_elePhi.SetTitle("Electron  gen #phi - rec #phi")
    diff_elePhi_Wonly.SetTitle("Electron  gen #phi - rec #phi  W prompt leptons")
    diff_elePhi_fromTau.SetTitle("Electron  gen #phi - rec #phi  from #tau decays")
    
    diff_elePt.SetTitle("Electron  gen p_{T} - rec p_{T}")
    diff_elePt_Wonly.SetTitle("Electron  gen p_{T} - rec p_{T}  W prompt leptons")
    diff_elePt_fromTau.SetTitle("Electron  gen p_{T} - rec p_{T}  from #tau decays")
    diffpct_elePt.SetTitle("Electron  (gen p_{T} - rec p_{T}) / rec p_{T}")
    diffpct_elePt_Wonly.SetTitle("Electron  (gen p_{T} - rec p_{T}) / rec p_{T}  W prompt leptons")
    diffpct_elePt_fromTau.SetTitle("Electron  (gen p_{T} - rec p_{T}) / rec p_{T}  from #tau decays")

    diff_muEta.SetTitle("Muon  gen #eta - rec #eta")
    diff_muEta_Wonly.SetTitle("Muon  gen #eta - rec #eta  W prompt leptons")
    diff_muEta_fromTau.SetTitle("Muon  gen #eta - rec #eta  from #tau decays")

    diff_muPhi.SetTitle("Muon  gen #phi - rec #phi")
    diff_muPhi_Wonly.SetTitle("Muon  gen #phi - rec #phi  W prompt leptons")
    diff_muPhi_fromTau.SetTitle("Muon  gen #phi - rec #phi  from #tau decays")

    diff_muPt.SetTitle("Muon  gen p_{T} - rec p_{T}")
    diff_muPt_Wonly.SetTitle("Muon  gen p_{T} - rec p_{T}  W prompt leptons")
    diff_muPt_fromTau.SetTitle("Muon  gen p_{T} - rec p_{T}  from #tau decays")
    diffpct_muPt.SetTitle("Muon  (gen p_{T} - rec p_{T}) / rec p_{T}")
    diffpct_muPt_Wonly.SetTitle("Muon  (gen p_{T} - rec p_{T}) / rec p_{T}  W prompt leptons")
    diffpct_muPt_fromTau.SetTitle("Muon  (gen p_{T} - rec p_{T}) / rec p_{T}  from #tau decays")

    weight = "PUweight * (1. - btagWeight[0]) * eleIDEffWeight * eleRecoEffWeight * muIDEffWeight * muIsoEffWeight * muTrackEffWeight * trigEffWeight * evtWeight"
    Wonly = " * (gen_eleMatched * (abs(gen_eleMomPID) == 24) && (gen_muMatched * (abs(gen_muMomPID) == 24)))"
    fromTau = " * (gen_eleMatched * (abs(gen_eleMomPID) == 15) || (gen_muMatched * (abs(gen_muMomPID) == 15)))"

    gen_eleMatched = "gen_eleMatched * (gen_eleParentage == 10)"
    gen_muMatched = "gen_muMatched * (gen_muParentage == 10)"
    #genMatched = "gen_eleMatched * (gen_eleParentage == 10) * gen_muMatched * (gen_muParentage == 10) * "
    genMatched = "gen_eleMatched * (gen_eleParentage == 10) * gen_muMatched * (gen_muParentage == 10) * ( ((gen_eleEta - eleEta[0])**2 + (gen_elePhi - elePhi[0])**2)**0.5 < 0.2 ) * ( ((gen_muEta - muEta[0])**2 + (gen_muPhi - muPhi[0])**2)**0.5 < 0.2 ) * "

    eleWonly = " * (gen_eleMatched * (abs(gen_eleMomPID) == 24))"
    muWonly = " * (gen_muMatched * (abs(gen_muMomPID) == 24))"
    elefromTau = " * (gen_eleMatched * (abs(gen_eleMomPID) == 15))"
    mufromTau = " * (gen_muMatched * (abs(gen_muMomPID) == 15))"

    print "Now drawing histograms"
#gROOT.SetBatch(True)
    t.Draw("eleEta[0]>>rec_eleEta_full", weight, "goff") 
    t.Draw("eleEta[0]>>rec_eleEta", genMatched + weight, "goff") 
    t.Draw("gen_eleEta>>gen_eleEta", genMatched + weight, "goff") 
    t.Draw("gen_eleEta>>gen_eleEta_Wonly", genMatched + weight + eleWonly, "goff") 
    t.Draw("gen_eleEta>>gen_eleEta_fromTau", genMatched + weight + elefromTau, "goff") 
    t.Draw("(gen_eleEta - eleEta[0])>>diff_eleEta", genMatched + weight, "goff")
    t.Draw("(gen_eleEta - eleEta[0])>>diff_eleEta_Wonly", genMatched + weight + eleWonly, "goff")
    t.Draw("(gen_eleEta - eleEta[0])>>diff_eleEta_fromTau", genMatched + weight + elefromTau, "goff")

    t.Draw("elePt[0]>>rec_elePt_full", weight, "goff") 
    t.Draw("elePt[0]>>rec_elePt", genMatched + weight, "goff") 
    t.Draw("gen_elePt>>gen_elePt", genMatched + weight, "goff")
    t.Draw("gen_elePt>>gen_elePt_Wonly", genMatched + weight + eleWonly, "goff") 
    t.Draw("gen_elePt>>gen_elePt_fromTau", genMatched + weight + elefromTau, "goff") 
    t.Draw("gen_elePt>>gen_cut_elePt", "gen_eleMatched * (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) * " + weight, "goff")
    t.Draw("(gen_elePt - elePt[0])>>diff_elePt", genMatched + weight, "goff") 
    t.Draw("(gen_elePt - elePt[0])>>diff_elePt_Wonly", genMatched + weight + eleWonly, "goff") 
    t.Draw("(gen_elePt - elePt[0])>>diff_elePt_fromTau", genMatched + weight + elefromTau, "goff") 
    t.Draw("(gen_elePt - elePt[0])/elePt[0]>>diffpct_elePt", genMatched + weight, "goff") 
    t.Draw("(gen_elePt - elePt[0])/elePt[0]>>diffpct_elePt_Wonly", genMatched + weight + eleWonly, "goff") 
    t.Draw("(gen_elePt - elePt[0])/elePt[0]>>diffpct_elePt_fromTau", genMatched + weight + elefromTau, "goff") 

    t.Draw("elePhi[0]>>rec_elePhi_full", weight, "goff") 
    t.Draw("elePhi[0]>>rec_elePhi", genMatched + weight, "goff") 
    t.Draw("gen_elePhi>>gen_elePhi", genMatched + weight, "goff")
    t.Draw("gen_elePhi>>gen_elePhi_Wonly", genMatched + weight + eleWonly, "goff") 
    t.Draw("gen_elePhi>>gen_elePhi_fromTau", genMatched + weight + elefromTau, "goff") 
    t.Draw("(gen_elePhi - elePhi[0])>>diff_elePhi", genMatched + weight, "goff") 
    t.Draw("(gen_elePhi - elePhi[0])>>diff_elePhi_Wonly", genMatched + weight + eleWonly, "goff") 
    t.Draw("(gen_elePhi - elePhi[0])>>diff_elePhi_fromTau", genMatched + weight + elefromTau, "goff") 

    t.Draw("muPt[0]>>rec_muPt_full", weight, "goff") 
    t.Draw("muPt[0]>>rec_muPt", genMatched + weight, "goff") 
    t.Draw("gen_muPt>>gen_muPt", genMatched + weight, "goff") 
    t.Draw("gen_muPt>>gen_muPt_Wonly", genMatched + weight + muWonly, "goff") 
    t.Draw("gen_muPt>>gen_muPt_fromTau", genMatched + weight + mufromTau, "goff") 
    t.Draw("gen_muPt>>gen_cut_muPt", "gen_muMatched * (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) * " + weight, "goff")
    t.Draw("(gen_muPt - muPt[0])>>diff_muPt", genMatched + weight, "goff") 
    t.Draw("(gen_muPt - muPt[0])>>diff_muPt_Wonly", genMatched + weight + muWonly, "goff") 
    t.Draw("(gen_muPt - muPt[0])>>diff_muPt_fromTau", genMatched + weight + mufromTau, "goff") 
    t.Draw("(gen_muPt - muPt[0])/muPt[0]>>diffpct_muPt", genMatched + weight, "goff") 
    t.Draw("(gen_muPt - muPt[0])/muPt[0]>>diffpct_muPt_Wonly", genMatched + weight + muWonly, "goff") 
    t.Draw("(gen_muPt - muPt[0])/muPt[0]>>diffpct_muPt_fromTau", genMatched + weight + mufromTau, "goff") 

    t.Draw("muEta[0]>>rec_muEta_full", weight, "goff") 
    t.Draw("muEta[0]>>rec_muEta", genMatched + weight, "goff") 
    t.Draw("gen_muEta>>gen_muEta", genMatched + weight, "goff") 
    t.Draw("gen_muEta>>gen_muEta_Wonly", genMatched + weight + muWonly, "goff") 
    t.Draw("gen_muEta>>gen_muEta_fromTau", genMatched + weight + mufromTau, "goff") 
    t.Draw("(gen_muEta - muEta[0])>>diff_muEta", genMatched + weight, "goff") 
    t.Draw("(gen_muEta - muEta[0])>>diff_muEta_Wonly", genMatched + weight + muWonly, "goff") 
    t.Draw("(gen_muEta - muEta[0])>>diff_muEta_fromTau", genMatched + weight + mufromTau, "goff") 

    t.Draw("muPhi[0]>>rec_muPhi_full", weight, "goff") 
    t.Draw("muPhi[0]>>rec_muPhi", genMatched + weight, "goff") 
    t.Draw("gen_muPhi>>gen_muPhi", genMatched + weight, "goff") 
    t.Draw("gen_muPhi>>gen_muPhi_Wonly", genMatched + weight + muWonly, "goff") 
    t.Draw("gen_muPhi>>gen_muPhi_fromTau", genMatched + weight + mufromTau, "goff") 
    t.Draw("(gen_muPhi - muPhi[0])>>diff_muPhi", genMatched + weight, "goff") 
    t.Draw("(gen_muPhi - muPhi[0])>>diff_muPhi_Wonly", genMatched + weight + muWonly, "goff") 
    t.Draw("(gen_muPhi - muPhi[0])>>diff_muPhi_fromTau", genMatched + weight + mufromTau, "goff") 

    t.Draw("pt_ll>>rec_ptll_full", weight, "goff")
    t.Draw("pt_ll>>rec_ptll", genMatched + weight, "goff")
    t.Draw("gen_pt_ll>>gen_ptll", genMatched + weight, "goff")
    t.Draw("gen_pt_ll>>gen_ptll_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_pt_ll>>gen_ptll_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_pt_ll>>gen_ptll_cut", genMatched + " ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_pt_ll - pt_ll)>>diff_ptll", genMatched + weight, "goff")
    t.Draw("(gen_pt_ll - pt_ll)>>diff_ptll_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_pt_ll - pt_ll)>>diff_ptll_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_pt_ll - pt_ll)/pt_ll>>diffpct_ptll", genMatched + weight, "goff")
    t.Draw("(gen_pt_ll - pt_ll)/pt_ll>>diffpct_ptll_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_pt_ll - pt_ll)/pt_ll>>diffpct_ptll_fromTau", genMatched + weight + fromTau, "goff")

    t.Draw("m_ll>>rec_Mll_full", weight, "goff")
    t.Draw("m_ll>>rec_Mll", genMatched + weight, "goff")
    t.Draw("gen_m_ll>>gen_Mll", genMatched + weight, "goff")
    t.Draw("gen_m_ll>>gen_Mll_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_m_ll>>gen_Mll_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_m_ll>>gen_Mll_cut", genMatched + " ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_m_ll - m_ll)>>diff_Mll", genMatched + weight, "goff")
    t.Draw("(gen_m_ll - m_ll)>>diff_Mll_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_m_ll - m_ll)>>diff_Mll_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_m_ll - m_ll)/m_ll>>diffpct_Mll", genMatched + weight, "goff")
    t.Draw("(gen_m_ll - m_ll)/m_ll>>diffpct_Mll_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_m_ll - m_ll)/m_ll>>diffpct_Mll_fromTau", genMatched + weight + fromTau, "goff")

    t.Draw("pt_pos>>rec_ptpos_full", weight, "goff")
    t.Draw("pt_pos>>rec_ptpos", genMatched + weight, "goff")
    t.Draw("gen_pt_pos>>gen_ptpos", genMatched + weight, "goff")
    t.Draw("gen_pt_pos>>gen_ptpos_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_pt_pos>>gen_ptpos_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_pt_pos>>gen_ptpos_cut", genMatched + " ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_pt_pos - pt_pos)>>diff_ptpos", genMatched + weight, "goff")
    t.Draw("(gen_pt_pos - pt_pos)>>diff_ptpos_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_pt_pos - pt_pos)>>diff_ptpos_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_pt_pos - pt_pos)/pt_pos>>diffpct_ptpos", genMatched + weight, "goff")
    t.Draw("(gen_pt_pos - pt_pos)/pt_pos>>diffpct_ptpos_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_pt_pos - pt_pos)/pt_pos>>diffpct_ptpos_fromTau", genMatched + weight + fromTau, "goff")

    t.Draw("pt_neg>>rec_ptneg_full", weight, "goff")
    t.Draw("pt_neg>>rec_ptneg", genMatched + weight, "goff")
    t.Draw("gen_pt_neg>>gen_ptneg", genMatched + weight, "goff")
    t.Draw("gen_pt_neg>>gen_ptneg_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_pt_neg>>gen_ptneg_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_pt_neg>>gen_ptneg_cut", genMatched + " ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_pt_neg - pt_neg)>>diff_ptneg", genMatched + weight, "goff")
    t.Draw("(gen_pt_neg - pt_neg)>>diff_ptneg_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_pt_neg - pt_neg)>>diff_ptneg_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_pt_neg - pt_neg)/pt_neg>>diffpct_ptneg", genMatched + weight, "goff")
    t.Draw("(gen_pt_neg - pt_neg)/pt_neg>>diffpct_ptneg_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_pt_neg - pt_neg)/pt_neg>>diffpct_ptneg_fromTau", genMatched + weight + fromTau, "goff")

    t.Draw("E_pos>>rec_Epos_full", weight, "goff")
    t.Draw("E_pos>>rec_Epos", genMatched + weight, "goff")
    t.Draw("gen_E_pos>>gen_Epos", genMatched + weight, "goff")
    t.Draw("gen_E_pos>>gen_Epos_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_E_pos>>gen_Epos_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_E_pos>>gen_Epos_cut", genMatched + " * ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_E_pos - E_pos)>>diff_Epos", genMatched + weight, "goff")
    t.Draw("(gen_E_pos - E_pos)>>diff_Epos_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_E_pos - E_pos)>>diff_Epos_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_E_pos - E_pos)/E_pos>>diffpct_Epos", genMatched + weight, "goff")
    t.Draw("(gen_E_pos - E_pos)/E_pos>>diffpct_Epos_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_E_pos - E_pos)/E_pos>>diffpct_Epos_fromTau", genMatched + weight + fromTau, "goff")

    t.Draw("E_neg>>rec_Eneg_full", weight, "goff")
    t.Draw("E_neg>>rec_Eneg", genMatched + weight, "goff")
    t.Draw("gen_E_neg>>gen_Eneg", genMatched + weight, "goff")
    t.Draw("gen_E_neg>>gen_Eneg_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_E_neg>>gen_Eneg_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_E_neg>>gen_Eneg_cut", genMatched + " * ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_E_neg - E_neg)>>diff_Eneg", genMatched + weight, "goff")
    t.Draw("(gen_E_neg - E_neg)>>diff_Eneg_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_E_neg - E_neg)>>diff_Eneg_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_E_neg - E_neg)/E_neg>>diffpct_Eneg", genMatched + weight, "goff")
    t.Draw("(gen_E_neg - E_neg)/E_neg>>diffpct_Eneg_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_E_neg - E_neg)/E_neg>>diffpct_Eneg_fromTau", genMatched + weight + fromTau, "goff")

    t.Draw("ptp_ptm>>rec_ptp_ptm_full", weight, "goff")
    t.Draw("ptp_ptm>>rec_ptp_ptm", genMatched + weight, "goff")
    t.Draw("gen_ptp_ptm>>gen_ptp_ptm", genMatched + weight, "goff")
    t.Draw("gen_ptp_ptm>>gen_ptp_ptm_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_ptp_ptm>>gen_ptp_ptm_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_ptp_ptm>>gen_ptp_ptm_cut", genMatched + " * ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_ptp_ptm - ptp_ptm)>>diff_ptp_ptm", genMatched + weight, "goff")
    t.Draw("(gen_ptp_ptm - ptp_ptm)>>diff_ptp_ptm_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_ptp_ptm - ptp_ptm)>>diff_ptp_ptm_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_ptp_ptm - ptp_ptm)/ptp_ptm>>diffpct_ptp_ptm", genMatched + weight, "goff")
    t.Draw("(gen_ptp_ptm - ptp_ptm)/ptp_ptm>>diffpct_ptp_ptm_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_ptp_ptm - ptp_ptm)/ptp_ptm>>diffpct_ptp_ptm_fromTau", genMatched + weight + fromTau, "goff")

    t.Draw("Ep_Em>>rec_Ep_Em_full", weight, "goff")
    t.Draw("Ep_Em>>rec_Ep_Em", genMatched + weight, "goff")
    t.Draw("gen_Ep_Em>>gen_Ep_Em", genMatched + weight, "goff")
    t.Draw("gen_Ep_Em>>gen_Ep_Em_Wonly", genMatched + weight + Wonly, "goff") 
    t.Draw("gen_Ep_Em>>gen_Ep_Em_fromTau", genMatched + weight + fromTau, "goff") 
    t.Draw("gen_Ep_Em>>gen_Ep_Em_cut", genMatched + " * ( (abs(gen_elePt - elePt[0])/elePt[0] < 0.2) && (abs(gen_muPt - muPt[0])/muPt[0] < 0.2) ) * " + weight, "goff")
    t.Draw("(gen_Ep_Em - Ep_Em)>>diff_Ep_Em", genMatched + weight, "goff")
    t.Draw("(gen_Ep_Em - Ep_Em)>>diff_Ep_Em_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_Ep_Em - Ep_Em)>>diff_Ep_Em_fromTau", genMatched + weight + fromTau, "goff")
    t.Draw("(gen_Ep_Em - Ep_Em)/Ep_Em>>diffpct_Ep_Em", genMatched + weight, "goff")
    t.Draw("(gen_Ep_Em - Ep_Em)/Ep_Em>>diffpct_Ep_Em_Wonly", genMatched + weight + Wonly, "goff")
    t.Draw("(gen_Ep_Em - Ep_Em)/Ep_Em>>diffpct_Ep_Em_fromTau", genMatched + weight + fromTau, "goff")


    print "Done drawing histograms"
# Get histograms
#    diff_eleEta = gDirectory.Get("diff_eleEta")
#    diff_eleEta_Wonly = gDirectory.Get("diff_eleEta_Wonly")
#    diff_eleEta_fromTau = gDirectory.Get("diff_eleEta_fromTau")
#    diff_elePhi = gDirectory.Get("diff_elePhi")
#    diff_elePhi_Wonly = gDirectory.Get("diff_elePhi_Wonly")
#    diff_elePhi_fromTau = gDirectory.Get("diff_elePhi_fromTau")
#    diff_elePt = gDirectory.Get("diff_elePt")
#    diff_elePt_Wonly = gDirectory.Get("diff_elePt_Wonly")
#    diff_elePt_fromTau = gDirectory.Get("diff_elePt_fromTau")
#    diffpct_elePt = gDirectory.Get("diffpct_elePt")
#    diffpct_elePt_Wonly = gDirectory.Get("diffpct_elePt_Wonly")
#    diffpct_elePt_fromTau = gDirectory.Get("diffpct_elePt_fromTau")
#
#    diff_muEta = gDirectory.Get("diff_muEta")
#    diff_muEta_Wonly = gDirectory.Get("diff_muEta_Wonly")
#    diff_muEta_fromTau = gDirectory.Get("diff_muEta_fromTau")
#    diff_muPhi = gDirectory.Get("diff_muPhi")
#    diff_muPhi_Wonly = gDirectory.Get("diff_muPhi_Wonly")
#    diff_muPhi_fromTau = gDirectory.Get("diff_muPhi_fromTau")
#    diff_muPt = gDirectory.Get("diff_muPt")
#    diff_muPt_Wonly = gDirectory.Get("diff_muPt_Wonly")
#    diff_muPt_fromTau = gDirectory.Get("diff_muPt_fromTau")
#    diffpct_muPt = gDirectory.Get("diffpct_muPt")
#    diffpct_muPt_Wonly = gDirectory.Get("diffpct_muPt_Wonly")
#    diffpct_muPt_fromTau = gDirectory.Get("diffpct_muPt_fromTau")

    diff_ptll = gDirectory.Get("diff_ptll")
    diff_ptll_Wonly = gDirectory.Get("diff_ptll_Wonly")
    diff_ptll_fromTau = gDirectory.Get("diff_ptll_fromTau")
    diffpct_ptll = gDirectory.Get("diffpct_ptll")
    diffpct_ptll_Wonly = gDirectory.Get("diffpct_ptll_Wonly")
    diffpct_ptll_fromTau = gDirectory.Get("diffpct_ptll_fromTau")

    diff_Mll = gDirectory.Get("diff_Mll")
    diff_Mll_Wonly = gDirectory.Get("diff_Mll_Wonly")
    diff_Mll_fromTau = gDirectory.Get("diff_Mll_fromTau")
    diffpct_Mll = gDirectory.Get("diffpct_Mll")
    diffpct_Mll_Wonly = gDirectory.Get("diffpct_Mll_Wonly")
    diffpct_Mll_fromTau = gDirectory.Get("diffpct_Mll_fromTau")

    diff_ptpos = gDirectory.Get("diff_ptpos")
    diff_ptpos_Wonly = gDirectory.Get("diff_ptpos_Wonly")
    diff_ptpos_fromTau = gDirectory.Get("diff_ptpos_fromTau")
    diffpct_ptpos = gDirectory.Get("diffpct_ptpos")
    diffpct_ptpos_Wonly = gDirectory.Get("diffpct_ptpos_Wonly")
    diffpct_ptpos_fromTau = gDirectory.Get("diffpct_ptpos_fromTau")

    diff_ptneg = gDirectory.Get("diff_ptneg")
    diff_ptneg_Wonly = gDirectory.Get("diff_ptneg_Wonly")
    diff_ptneg_fromTau = gDirectory.Get("diff_ptneg_fromTau")
    diffpct_ptneg = gDirectory.Get("diffpct_ptneg")
    diffpct_ptneg_Wonly = gDirectory.Get("diffpct_ptneg_Wonly")
    diffpct_ptneg_fromTau = gDirectory.Get("diffpct_ptneg_fromTau")

    diff_Epos = gDirectory.Get("diff_Epos")
    diff_Epos_Wonly = gDirectory.Get("diff_Epos_Wonly")
    diff_Epos_fromTau = gDirectory.Get("diff_Epos_fromTau")
    diffpct_Epos = gDirectory.Get("diffpct_Epos")
    diffpct_Epos_Wonly = gDirectory.Get("diffpct_Epos_Wonly")
    diffpct_Epos_fromTau = gDirectory.Get("diffpct_Epos_fromTau")

    diff_Eneg = gDirectory.Get("diff_Eneg")
    diff_Eneg_Wonly = gDirectory.Get("diff_Eneg_Wonly")
    diff_Eneg_fromTau = gDirectory.Get("diff_Eneg_fromTau")
    diffpct_Eneg = gDirectory.Get("diffpct_Eneg")
    diffpct_Eneg_Wonly = gDirectory.Get("diffpct_Eneg_Wonly")
    diffpct_Eneg_fromTau = gDirectory.Get("diffpct_Eneg_fromTau")

    diff_ptp_ptm = gDirectory.Get("diff_ptp_ptm")
    diff_ptp_ptm_Wonly = gDirectory.Get("diff_ptp_ptm_Wonly")
    diff_ptp_ptm_fromTau = gDirectory.Get("diff_ptp_ptm_fromTau")
    diffpct_ptp_ptm = gDirectory.Get("diffpct_ptp_ptm")
    diffpct_ptp_ptm_Wonly = gDirectory.Get("diffpct_ptp_ptm_Wonly")
    diffpct_ptp_ptm_fromTau = gDirectory.Get("diffpct_ptp_ptm_fromTau")

    diff_Ep_Em = gDirectory.Get("diff_Ep_Em")
    diff_Ep_Em_Wonly = gDirectory.Get("diff_Ep_Em_Wonly")
    diff_Ep_Em_fromTau = gDirectory.Get("diff_Ep_Em_fromTau")
    diffpct_Ep_Em = gDirectory.Get("diffpct_Ep_Em")
    diffpct_Ep_Em_Wonly = gDirectory.Get("diffpct_Ep_Em_Wonly")
    diffpct_Ep_Em_fromTau = gDirectory.Get("diffpct_Ep_Em_fromTau")

#f.Close()


    diff_ptll.SetTitle("p_{T}(ll)  gen - rec")
    diff_ptll.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    diff_ptll.GetXaxis().SetTitleOffset(1.3)
    diff_ptll.GetYaxis().SetTitle("Events")
    diff_ptll.GetYaxis().SetTitleOffset(1.3)
    diff_ptll_Wonly.SetTitle("p_{T}(ll)  gen - rec  W prompt leptons")
    diff_ptll_Wonly.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    diff_ptll_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_ptll_Wonly.GetYaxis().SetTitle("Events")
    diff_ptll_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_ptll_fromTau.SetTitle("p_{T}(ll)  gen - rec  from #tau decays")
    diff_ptll_fromTau.GetXaxis().SetTitle("p_{T}(ll) [GeV]")
    diff_ptll_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_ptll_fromTau.GetYaxis().SetTitle("Events")
    diff_ptll_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptll.SetTitle("p_{T}(ll)  (gen - rec) / rec")
    diffpct_ptll.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptll.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptll.GetYaxis().SetTitle("Events")
    diffpct_ptll.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptll_Wonly.SetTitle("p_{T}(ll)  (gen - rec) / rec  W prompt leptons")
    diffpct_ptll_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptll_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptll_Wonly.GetYaxis().SetTitle("Events")
    diffpct_ptll_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptll_fromTau.SetTitle("p_{T}(ll)  (gen - rec) / rec  from #tau decays")
    diffpct_ptll_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptll_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptll_fromTau.GetYaxis().SetTitle("Events")
    diffpct_ptll_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_ptpos.SetTitle("p_{T}(l^{+})  gen - rec")
    diff_ptpos.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    diff_ptpos.GetXaxis().SetTitleOffset(1.3)
    diff_ptpos.GetYaxis().SetTitle("Events")
    diff_ptpos.GetYaxis().SetTitleOffset(1.3)
    diff_ptpos_Wonly.SetTitle("p_{T}(l^{+})  gen - rec  W prompt leptons")
    diff_ptpos_Wonly.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    diff_ptpos_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_ptpos_Wonly.GetYaxis().SetTitle("Events")
    diff_ptpos_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_ptpos_fromTau.SetTitle("p_{T}(l^{+})  gen - rec  from #tau decays")
    diff_ptpos_fromTau.GetXaxis().SetTitle("p_{T}(l^{+}) [GeV]")
    diff_ptpos_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_ptpos_fromTau.GetYaxis().SetTitle("Events")
    diff_ptpos_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptpos.SetTitle("p_{T}(l^{+})  (gen - rec) / rec")
    diffpct_ptpos.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptpos.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptpos.GetYaxis().SetTitle("Events")
    diffpct_ptpos.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptpos_Wonly.SetTitle("p_{T}(l^{+})  (gen - rec) / rec  W prompt leptons")
    diffpct_ptpos_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptpos_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptpos_Wonly.GetYaxis().SetTitle("Events")
    diffpct_ptpos_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptpos_fromTau.SetTitle("p_{T}(l^{+})  (gen - rec) / rec  from #tau decays")
    diffpct_ptpos_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptpos_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptpos_fromTau.GetYaxis().SetTitle("Events")
    diffpct_ptpos_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_ptneg.SetTitle("p_{T}(l^{-})  gen - rec")
    diff_ptneg.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    diff_ptneg.GetXaxis().SetTitleOffset(1.3)
    diff_ptneg.GetYaxis().SetTitle("Events")
    diff_ptneg.GetYaxis().SetTitleOffset(1.3)
    diff_ptneg_Wonly.SetTitle("p_{T}(l^{-})  gen - rec  W prompt leptons")
    diff_ptneg_Wonly.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    diff_ptneg_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_ptneg_Wonly.GetYaxis().SetTitle("Events")
    diff_ptneg_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_ptneg_fromTau.SetTitle("p_{T}(l^{-})  gen - rec  from #tau decays")
    diff_ptneg_fromTau.GetXaxis().SetTitle("p_{T}(l^{-}) [GeV]")
    diff_ptneg_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_ptneg_fromTau.GetYaxis().SetTitle("Events")
    diff_ptneg_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptneg.SetTitle("p_{T}(l^{-})  (gen - rec) / rec")
    diffpct_ptneg.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptneg.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptneg.GetYaxis().SetTitle("Events")
    diffpct_ptneg.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptneg_Wonly.SetTitle("p_{T}(l^{-})  (gen - rec) / rec  W prompt leptons")
    diffpct_ptneg_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptneg_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptneg_Wonly.GetYaxis().SetTitle("Events")
    diffpct_ptneg_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptneg_fromTau.SetTitle("p_{T}(l^{-})  (gen - rec) / rec  from #tau decays")
    diffpct_ptneg_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptneg_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptneg_fromTau.GetYaxis().SetTitle("Events")
    diffpct_ptneg_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_Mll.SetTitle("M(ll)  gen - rec")
    diff_Mll.GetXaxis().SetTitle("M(ll) [GeV]")
    diff_Mll.GetXaxis().SetTitleOffset(1.3)
    diff_Mll.GetYaxis().SetTitle("Events")
    diff_Mll.GetYaxis().SetTitleOffset(1.3)
    diff_Mll_Wonly.SetTitle("M(ll)  gen - rec  W prompt leptons")
    diff_Mll_Wonly.GetXaxis().SetTitle("M(ll) [GeV]")
    diff_Mll_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_Mll_Wonly.GetYaxis().SetTitle("Events")
    diff_Mll_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_Mll_fromTau.SetTitle("M(ll)  gen - rec  from #tau decays")
    diff_Mll_fromTau.GetXaxis().SetTitle("M(ll) [GeV]")
    diff_Mll_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_Mll_fromTau.GetYaxis().SetTitle("Events")
    diff_Mll_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_Mll.SetTitle("M(ll)  (gen - rec) / rec")
    diffpct_Mll.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Mll.GetXaxis().SetTitleOffset(1.3)
    diffpct_Mll.GetYaxis().SetTitle("Events")
    diffpct_Mll.GetYaxis().SetTitleOffset(1.3)
    diffpct_Mll_Wonly.SetTitle("M(ll)  (gen - rec) / rec  W prompt leptons")
    diffpct_Mll_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Mll_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_Mll_Wonly.GetYaxis().SetTitle("Events")
    diffpct_Mll_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_Mll_fromTau.SetTitle("M(ll)  (gen - rec) / rec  from #tau decays")
    diffpct_Mll_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Mll_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_Mll_fromTau.GetYaxis().SetTitle("Events")
    diffpct_Mll_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_Epos.SetTitle("E(l^{+})  gen - rec")
    diff_Epos.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    diff_Epos.GetXaxis().SetTitleOffset(1.3)
    diff_Epos.GetYaxis().SetTitle("Events")
    diff_Epos.GetYaxis().SetTitleOffset(1.3)
    diff_Epos_Wonly.SetTitle("E(l^{+})  gen - rec  W prompt leptons")
    diff_Epos_Wonly.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    diff_Epos_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_Epos_Wonly.GetYaxis().SetTitle("Events")
    diff_Epos_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_Epos_fromTau.SetTitle("E(l^{+})  gen - rec  from #tau decays")
    diff_Epos_fromTau.GetXaxis().SetTitle("E(l^{+}) [GeV]")
    diff_Epos_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_Epos_fromTau.GetYaxis().SetTitle("Events")
    diff_Epos_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_Epos.SetTitle("E(l^{+})  (gen - rec) / rec")
    diffpct_Epos.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Epos.GetXaxis().SetTitleOffset(1.3)
    diffpct_Epos.GetYaxis().SetTitle("Events")
    diffpct_Epos.GetYaxis().SetTitleOffset(1.3)
    diffpct_Epos_Wonly.SetTitle("E(l^{+})  (gen - rec) / rec  W prompt leptons")
    diffpct_Epos_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Epos_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_Epos_Wonly.GetYaxis().SetTitle("Events")
    diffpct_Epos_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_Epos_fromTau.SetTitle("E(l^{+})  (gen - rec) / rec  from #tau decays")
    diffpct_Epos_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Epos_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_Epos_fromTau.GetYaxis().SetTitle("Events")
    diffpct_Epos_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_Eneg.SetTitle("E(l^{-})  gen - rec")
    diff_Eneg.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    diff_Eneg.GetXaxis().SetTitleOffset(1.3)
    diff_Eneg.GetYaxis().SetTitle("Events")
    diff_Eneg.GetYaxis().SetTitleOffset(1.3)
    diff_Eneg_Wonly.SetTitle("E(l^{-})  gen - rec  W prompt leptons")
    diff_Eneg_Wonly.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    diff_Eneg_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_Eneg_Wonly.GetYaxis().SetTitle("Events")
    diff_Eneg_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_Eneg_fromTau.SetTitle("E(l^{-})  gen - rec  from #tau decays")
    diff_Eneg_fromTau.GetXaxis().SetTitle("E(l^{-}) [GeV]")
    diff_Eneg_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_Eneg_fromTau.GetYaxis().SetTitle("Events")
    diff_Eneg_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_Eneg.SetTitle("E(l^{-})  (gen - rec) / rec")
    diffpct_Eneg.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Eneg.GetXaxis().SetTitleOffset(1.3)
    diffpct_Eneg.GetYaxis().SetTitle("Events")
    diffpct_Eneg.GetYaxis().SetTitleOffset(1.3)
    diffpct_Eneg_Wonly.SetTitle("E(l^{-})  (gen - rec) / rec  W prompt leptons")
    diffpct_Eneg_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Eneg_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_Eneg_Wonly.GetYaxis().SetTitle("Events")
    diffpct_Eneg_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_Eneg_fromTau.SetTitle("E(l^{-})  (gen - rec) / rec  from #tau decays")
    diffpct_Eneg_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Eneg_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_Eneg_fromTau.GetYaxis().SetTitle("Events")
    diffpct_Eneg_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_ptp_ptm.SetTitle("p_{T}(l^{+}) + p_{T}(l^{-})  gen - rec")
    diff_ptp_ptm.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    diff_ptp_ptm.GetXaxis().SetTitleOffset(1.3)
    diff_ptp_ptm.GetYaxis().SetTitle("Events")
    diff_ptp_ptm.GetYaxis().SetTitleOffset(1.3)
    diff_ptp_ptm_Wonly.SetTitle("p_{T}(l^{+}) + p_{T}(l^{-})  gen - rec  W prompt leptons")
    diff_ptp_ptm_Wonly.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    diff_ptp_ptm_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_ptp_ptm_Wonly.GetYaxis().SetTitle("Events")
    diff_ptp_ptm_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_ptp_ptm_fromTau.SetTitle("p_{T}(l^{+}) + p_{T}(l^{-})  gen - rec  from #tau leptons")
    diff_ptp_ptm_fromTau.GetXaxis().SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) [GeV]")
    diff_ptp_ptm_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_ptp_ptm_fromTau.GetYaxis().SetTitle("Events")
    diff_ptp_ptm_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptp_ptm.SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) (gen - rec) / rec")
    diffpct_ptp_ptm.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptp_ptm.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptp_ptm.GetYaxis().SetTitle("Events")
    diffpct_ptp_ptm.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptp_ptm_Wonly.SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) (gen - rec) / rec  W prompt leptons")
    diffpct_ptp_ptm_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptp_ptm_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptp_ptm_Wonly.GetYaxis().SetTitle("Events")
    diffpct_ptp_ptm_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_ptp_ptm_fromTau.SetTitle("p_{T}(l^{+}) + p_{T}(l^{-}) (gen - rec) / rec  from #tau decays")
    diffpct_ptp_ptm_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_ptp_ptm_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_ptp_ptm_fromTau.GetYaxis().SetTitle("Events")
    diffpct_ptp_ptm_fromTau.GetYaxis().SetTitleOffset(1.3)

    diff_Ep_Em.SetTitle("E(l^{+}) + E(l^{-})  gen - rec")
    diff_Ep_Em.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    diff_Ep_Em.GetXaxis().SetTitleOffset(1.3)
    diff_Ep_Em.GetYaxis().SetTitle("Events")
    diff_Ep_Em.GetYaxis().SetTitleOffset(1.3)
    diff_Ep_Em_Wonly.SetTitle("E(l^{+}) + E(l^{-})  gen - rec  W prompt leptons")
    diff_Ep_Em_Wonly.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    diff_Ep_Em_Wonly.GetXaxis().SetTitleOffset(1.3)
    diff_Ep_Em_Wonly.GetYaxis().SetTitle("Events")
    diff_Ep_Em_Wonly.GetYaxis().SetTitleOffset(1.3)
    diff_Ep_Em_fromTau.SetTitle("E(l^{+}) + E(l^{-})  gen - rec  from #tau decays")
    diff_Ep_Em_fromTau.GetXaxis().SetTitle("E(l^{+}) + E(l^{-}) [GeV]")
    diff_Ep_Em_fromTau.GetXaxis().SetTitleOffset(1.3)
    diff_Ep_Em_fromTau.GetYaxis().SetTitle("Events")
    diff_Ep_Em_fromTau.GetYaxis().SetTitleOffset(1.3)
    diffpct_Ep_Em.SetTitle("E(l^{+}) + E(l^{-}) (gen - rec) / rec")
    diffpct_Ep_Em.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Ep_Em.GetXaxis().SetTitleOffset(1.3)
    diffpct_Ep_Em.GetYaxis().SetTitle("Events")
    diffpct_Ep_Em.GetYaxis().SetTitleOffset(1.3)
    diffpct_Ep_Em_Wonly.SetTitle("E(l^{+}) + E(l^{-}) (gen - rec) / rec  W prompt leptons")
    diffpct_Ep_Em_Wonly.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Ep_Em_Wonly.GetXaxis().SetTitleOffset(1.3)
    diffpct_Ep_Em_Wonly.GetYaxis().SetTitle("Events")
    diffpct_Ep_Em_Wonly.GetYaxis().SetTitleOffset(1.3)
    diffpct_Ep_Em_fromTau.SetTitle("E(l^{+}) + E(l^{-}) (gen - rec) / rec  from #tau decays")
    diffpct_Ep_Em_fromTau.GetXaxis().SetTitle("(gen - rec) / rec")
    diffpct_Ep_Em_fromTau.GetXaxis().SetTitleOffset(1.3)
    diffpct_Ep_Em_fromTau.GetYaxis().SetTitle("Events")
    diffpct_Ep_Em_fromTau.GetYaxis().SetTitleOffset(1.3)


outF = TFile.Open("%s/%s.root" % (outDir, outDir), "recreate")

rec_ptll.Write()
rec_ptll_full.Write()
gen_ptll.Write()

rec_Mll.Write()
rec_Mll_full.Write()
gen_Mll.Write()

rec_ptpos.Write()
rec_ptpos_full.Write()
gen_ptpos.Write()

rec_ptneg.Write()
rec_ptneg_full.Write()
gen_ptneg.Write()

rec_Epos.Write()
rec_Epos_full.Write()
gen_Epos.Write()

rec_Eneg.Write()
rec_Eneg_full.Write()
gen_Eneg.Write()

rec_ptp_ptm.Write()
rec_ptp_ptm_full.Write()
gen_ptp_ptm.Write()

rec_Ep_Em.Write()
rec_Ep_Em_full.Write()
gen_Ep_Em.Write()

rec_eleEta.Write()
rec_eleEta_full.Write()
gen_eleEta.Write()
rec_elePhi.Write()
rec_elePhi_full.Write()
gen_elePhi.Write()
rec_elePt.Write()
rec_elePt_full.Write()
gen_elePt.Write()

rec_muEta.Write()
rec_muEta_full.Write()
gen_muEta.Write()
rec_muPhi.Write()
rec_muPhi_full.Write()
gen_muPhi.Write()
rec_muPt.Write()
rec_muPt_full.Write()
gen_muPt.Write()


diff_ptll.Write()
diffpct_ptll.Write()

diff_Mll.Write()
diffpct_Mll.Write()

diff_ptpos.Write()
diffpct_ptpos.Write()

diff_ptneg.Write()
diffpct_ptneg.Write()

diff_Epos.Write()
diffpct_Epos.Write()

diff_Eneg.Write()
diffpct_Eneg.Write()

diff_ptp_ptm.Write()
diffpct_ptp_ptm.Write()

diff_Ep_Em.Write()
diffpct_Ep_Em.Write()

diff_eleEta.Write()
diff_elePhi.Write()
diff_elePt.Write()
diffpct_elePt.Write()

diff_muEta.Write()
diff_muPhi.Write()
diff_muPt.Write()
diffpct_muPt.Write()

outF.Close()


c = TCanvas("c","c",1200,800)

cRatio = TCanvas("c2", "c2", 1200,1200)
pad1 = TPad("pad1", "pad1", 0., 0.25, 1., 1.)
pad2 = TPad("pad2", "pad2", 0., 0., 1., 0.25)

#rec_ptll.Draw("hist")
#gen_ptll_cut.SetLineColor(kRed)
#gen_ptll_cut.Draw("hist same")

gen_ptll_diffpct = (gen_ptll.Integral() - rec_ptll.Integral()) / rec_ptll.Integral()
#gen_ptll_cut_diffpct = (gen_ptll_cut.Integral() - rec_ptll.Integral()) / rec_ptll.Integral()
print "ptll"
print "Gen: %.2f%%" % (gen_ptll_diffpct * 100)
#print "Gen with pt cut: %.2f%%\n" % (gen_ptll_cut_diffpct * 100)

gen_Mll_diffpct = (gen_Mll.Integral() - rec_Mll.Integral()) / rec_Mll.Integral()
#gen_Mll_cut_diffpct = (gen_Mll_cut.Integral() - rec_Mll.Integral()) / rec_Mll.Integral()
print "Mll"
print "Gen: %.2f%%" % (gen_Mll_diffpct * 100)
#print "Gen with pt cut: %.2f%%\n" % (gen_Mll_cut_diffpct * 100)

gen_ptpos_diffpct = (gen_ptpos.Integral() - rec_ptpos.Integral()) / rec_ptpos.Integral()
#gen_ptpos_cut_diffpct = (gen_ptpos_cut.Integral() - rec_ptpos.Integral()) / rec_ptpos.Integral()
print "ptpos"
print "Gen: %.2f%%" % (gen_ptpos_diffpct * 100)
#print "Gen with pt cut: %.2f%%\n" % (gen_ptpos_cut_diffpct * 100)

gen_Epos_diffpct = (gen_Epos.Integral() - rec_Epos.Integral()) / rec_Epos.Integral()
#gen_Epos_cut_diffpct = (gen_Epos_cut.Integral() - rec_Epos.Integral()) / rec_Epos.Integral()
print "Epos"
print "Gen: %.2f%%" % (gen_Epos_diffpct * 100)
#print "Gen with pt cut: %.2f%%\n" % (gen_Epos_cut_diffpct * 100)

gen_ptp_ptm_diffpct = (gen_ptp_ptm.Integral() - rec_ptp_ptm.Integral()) / rec_ptp_ptm.Integral()
#gen_ptp_ptm_cut_diffpct = (gen_ptp_ptm_cut.Integral() - rec_ptp_ptm.Integral()) / rec_ptp_ptm.Integral()
print "ptp_ptm"
print "Gen: %.2f%%" % (gen_ptp_ptm_diffpct * 100)
#print "Gen with pt cut: %.2f%%\n" % (gen_ptp_ptm_cut_diffpct * 100)

gen_Ep_Em_diffpct = (gen_Ep_Em.Integral() - rec_Ep_Em.Integral()) / rec_Ep_Em.Integral()
#gen_Ep_Em_cut_diffpct = (gen_Ep_Em_cut.Integral() - rec_Ep_Em.Integral()) / rec_Ep_Em.Integral()
print "Ep_Em"
print "Gen: %.2f%%" % (gen_Ep_Em_diffpct * 100)
#print "Gen with pt cut: %.2f%%\n" % (gen_Ep_Em_cut_diffpct * 100)



def drawHist(h, outfile, includeLogY = True, format=['.png','.pdf']):
    h.Draw("hist")
    for f in format:
        c.SaveAs(outfile+f)

    if includeLogY:
        c.SetLogy(True)
        for f in format:
            c.SaveAs(outfile+"_logY"+f)

        c.SetLogy(False)


c.cd()

plots = [\
    "diff_eleEta",
    "diff_elePhi",
    "diff_elePt", 
    "diffpct_elePt", 
    "diff_muEta",
    "diff_muPhi",
    "diff_muPt", 
    "diffpct_muPt", 
    "diff_ptll",
    "diff_Mll",
    "diff_ptpos",
    "diff_ptneg",
    "diff_Epos",
    "diff_Eneg",
    "diff_ptp_ptm",
    "diff_Ep_Em",
    "diffpct_ptll",
    "diffpct_Mll",
    "diffpct_ptpos",
    "diffpct_ptneg",
    "diffpct_Epos",
    "diffpct_Eneg",
    "diffpct_ptp_ptm",
    "diffpct_Ep_Em",
    ]

for p in plots:
    exec("drawHist(%s,'%s/%s')" % (p,outDir,p))

#diff_eleEta.Draw("hist")
#c.SaveAs("%s/diff_eleEta.png" % outDir)
#c.SaveAs("%s/diff_eleEta.pdf" % outDir)
#c.SetLogy(True)
#c.SaveAs("%s/diff_eleEta_logY.png" % outDir)
#c.SaveAs("%s/diff_eleEta_logY.pdf" % outDir)
#c.SetLogy(False)
#diff_elePhi.Draw("hist")
#c.SaveAs("%s/diff_elePhi.png" % outDir)
#c.SaveAs("%s/diff_elePhi.pdf" % outDir)
#c.SetLogy(True)
#c.SaveAs("%s/diff_elePhi_logY.png" % outDir)
#c.SaveAs("%s/diff_elePhi_logY.pdf" % outDir)
#c.SetLogy(False)
#diff_elePt.Draw("hist")
#c.SaveAs("%s/diff_elePt.png" % outDir)
#c.SaveAs("%s/diff_elePt.pdf" % outDir)
#c.SetLogy(True)
#c.SaveAs("%s/diff_elePt_logY.png" % outDir)
#c.SaveAs("%s/diff_elePt_logY.pdf" % outDir)
#c.SetLogy(False)
#diffpct_elePt.Draw("hist")
#c.SaveAs("%s/diffpct_elePt.png" % outDir)
#c.SaveAs("%s/diffpct_elePt.pdf" % outDir)
#c.SetLogy(True)
#
#diff_muEta.Draw("hist")
#c.SaveAs("%s/diff_muEta.png" % outDir)
#c.SaveAs("%s/diff_muEta.pdf" % outDir)
#diff_muPhi.Draw("hist")
#c.SaveAs("%s/diff_muPhi.png" % outDir)
#c.SaveAs("%s/diff_muPhi.pdf" % outDir)
#diff_muPt.Draw("hist")
#c.SaveAs("%s/diff_muPt.png" % outDir)
#c.SaveAs("%s/diff_muPt.pdf" % outDir)
#diffpct_muPt.Draw("hist")
#c.SaveAs("%s/diffpct_muPt.png" % outDir)
#c.SaveAs("%s/diffpct_muPt.pdf" % outDir)
#
#
#diff_ptll.Draw("hist")
#c.SaveAs("%s/diff_ptll.png" % outDir)
#c.SaveAs("%s/diff_ptll.pdf" % outDir)
#diffpct_ptll.Draw("hist")
#c.SaveAs("%s/diffpct_ptll.png" % outDir)
#c.SaveAs("%s/diffpct_ptll.pdf" % outDir)
#
#diff_Mll.Draw("hist")
#c.SaveAs("%s/diff_Mll.png" % outDir)
#c.SaveAs("%s/diff_Mll.pdf" % outDir)
#diffpct_Mll.Draw("hist")
#c.SaveAs("%s/diffpct_Mll.png" % outDir)
#c.SaveAs("%s/diffpct_Mll.pdf" % outDir)
#
#diff_ptpos.Draw("hist")
#c.SaveAs("%s/diff_ptpos.png" % outDir)
#c.SaveAs("%s/diff_ptpos.pdf" % outDir)
#diffpct_ptpos.Draw("hist")
#c.SaveAs("%s/diffpct_ptpos.png" % outDir)
#c.SaveAs("%s/diffpct_ptpos.pdf" % outDir)
#
#diff_Epos.Draw("hist")
#c.SaveAs("%s/diff_Epos.png" % outDir)
#c.SaveAs("%s/diff_Epos.pdf" % outDir)
#diffpct_Epos.Draw("hist")
#c.SaveAs("%s/diffpct_Epos.png" % outDir)
#c.SaveAs("%s/diffpct_Epos.pdf" % outDir)
#
#diff_ptp_ptm.Draw("hist")
#c.SaveAs("%s/diff_ptp_ptm.png" % outDir)
#c.SaveAs("%s/diff_ptp_ptm.pdf" % outDir)
#diffpct_ptp_ptm.Draw("hist")
#c.SaveAs("%s/diffpct_ptp_ptm.png" % outDir)
#c.SaveAs("%s/diffpct_ptp_ptm.pdf" % outDir)
#
#diff_Ep_Em.Draw("hist")
#c.SaveAs("%s/diff_Ep_Em.png" % outDir)
#c.SaveAs("%s/diff_Ep_Em.pdf" % outDir)
#diffpct_Ep_Em.Draw("hist")
#c.SaveAs("%s/diffpct_Ep_Em.png" % outDir)
#c.SaveAs("%s/diffpct_Ep_Em.pdf" % outDir)
#
#
#
#
c.SetLogy(False)
gStyle.SetOptStat(0)

def drawRecGen(rec, gen, title, outF, lX = 0.7, lY = 0.7):
    c.cd()
    c.ResetDrawn()

    l = TLegend(lX, lY, lX+0.18, lY+0.18)
    l.SetBorderSize(0)
    l.AddEntry(rec, "rec")
    l.AddEntry(gen, "gen")

    rec.SetLineWidth(2)
    rec.SetLineColor(kBlack)
    gen.SetLineWidth(2)
    gen.SetLineColor(kRed)

    oldTitle = rec.GetTitle()
    rec.SetTitle(title)

    rec.Draw("hist")
    gen.Draw("hist same")
    l.Draw("same")
    c.SaveAs(outF)

    rec.SetTitle(oldTitle)

def drawRecGenRatioOnly(rec, gen, title, outF, formats = [".png",".pdf"], color=kRed, lX = 0.7, lY = 0.7):
    c.cd()
    c.ResetDrawn()
    c.Draw()
#    pad1.Draw()
#    pad2.Draw()
    
#    l = TLegend(lX, lY, lX+0.18, lY+0.18)
#    l.SetBorderSize(0)
#    l.AddEntry(rec, "rec")
#    l.AddEntry(gen, "gen")

    rec.SetLineWidth(2)
    rec.SetLineColor(kBlack)
    gen.SetLineWidth(2)
    gen.SetLineColor(color)

    recNoErr = rec.Clone("rec_noerr")
    for b in xrange(1,recNoErr.GetNbinsX()+1):
        recNoErr.SetBinError(b, 0.)
    ratio = gen.Clone("ratio")
    #ratio.Divide(recNoErr)
    ratio.Divide(rec)
    ratio.SetTitle(title)
    ratio.GetYaxis().SetTitle("prompt lep / all lep")
    #ratio.GetYaxis().SetTitleSize(ratio.GetYaxis().GetTitleSize()*2)
    #ratio.GetYaxis().SetTitleOffset(ratio.GetYaxis().GetTitleOffset()/2)
    
    line = TLine(rec.GetXaxis().GetBinLowEdge(1), 1., rec.GetXaxis().GetBinUpEdge(rec.GetNbinsX()), 1.)
    line.SetLineWidth(2)
#
#    pad1.cd()
#    rec.Draw("hist")
#    gen.Draw("hist same")
#    
#    pad2.cd()
    #ratio.Draw("hist e1")
    ratio.Draw("hist")
 #   l.Draw("same")
#    line.Draw("same")
    for f in formats:
        c.SaveAs(outF+f)



def drawRecGenRatio(rec, gen, title, outF, formats = [".png",".pdf"], lX = 0.7, lY = 0.7):
    cRatio.cd()
    cRatio.ResetDrawn()
    cRatio.Draw()
    pad1.Draw()
    pad2.Draw()
    
    l = TLegend(lX, lY, lX+0.18, lY+0.18)
    l.SetBorderSize(0)
    l.AddEntry(rec, "rec")
    l.AddEntry(gen, "gen")
#    l.AddEntry(gen_cut, "gen p_{T} cut")

    rec.SetLineWidth(2)
    rec.SetLineColor(kBlack)
    gen.SetLineWidth(2)
    gen.SetLineColor(kRed)
#    gen_cut.SetLineWidth(2)
#    gen_cut.SetLineColor(kBlue)

    recNoErr = rec.Clone("rec_noerr")
    for b in xrange(1,recNoErr.GetNbinsX()+1):
        recNoErr.SetBinError(b, 0.)
    ratio = gen.Clone("ratio")
    #ratio.Divide(recNoErr)
    ratio.Divide(rec)
    ratio.SetTitle("")
    ratio.GetXaxis().SetTitle("")
    ratio.GetYaxis().SetTitle("gen / rec")
    ratio.GetYaxis().SetTitleSize(ratio.GetYaxis().GetTitleSize()*2)
    ratio.GetYaxis().SetTitleOffset(ratio.GetYaxis().GetTitleOffset()/2)
    
    #ratio_cut = gen_cut.Clone("ratio_cut")
    #ratio_cut.Divide(recNoErr)
   # ratio_cut.Divide(rec)
   
    oldTitle = rec.GetTitle()
    rec.SetTitle(title)
    
    line = TLine(rec.GetXaxis().GetBinLowEdge(1), 1., rec.GetXaxis().GetBinUpEdge(rec.GetNbinsX()), 1.)
    line.SetLineWidth(2)

    pad1.cd()
    rec.Draw("hist")
    gen.Draw("hist same")
#    gen_cut.Draw("hist same")
    l.Draw("same")
    
    pad2.cd()
    ratio.Draw("hist e1")
#    ratio_cut.Draw("hist e1 same")
    line.Draw("same")
    for f in formats:
        cRatio.SaveAs(outF+f)

    rec.SetTitle(oldTitle)

def drawDiffRecGen_Wtau(total, gen_Wonly, gen_fromTau, title, outF, lX = 0.7, lY = 0.7, scalingY = 1, logX = False, logY = True, genColor=kRed, genWColor=kGray, genTauColor=kBlue, genOtherColor=kGreen):
    c.cd()
    c.ResetDrawn()
    c.Draw()
    c.SetLogx(logX)
    c.SetLogy(logY)

    gen_other = total.Clone(total.GetName() + "_other")
    gen_other.Add(gen_Wonly, -1)
    gen_other.Add(gen_fromTau, -1)
    gen_other.SetFillColor(genOtherColor)
    gen_other.SetLineColor(genOtherColor)
    gen_other.SetMarkerStyle(22)
    gen_other.SetMarkerSize(0)

    #rec.SetLineWidth(0)
#    total.SetLineColor(recColor)
#    total.SetMarkerStyle(20)
#    total.SetMarkerSize(1)
    gen_Wonly.SetLineWidth(2)
    gen_Wonly.SetLineColor(genWColor)
    gen_Wonly.SetFillColor(genWColor)
    gen_Wonly.SetMarkerStyle(22)
    gen_Wonly.SetMarkerSize(0)
    gen_fromTau.SetLineWidth(2)
    gen_fromTau.SetLineColor(genTauColor)
    gen_fromTau.SetFillColor(genTauColor)
    gen_fromTau.SetMarkerStyle(22)
    gen_fromTau.SetMarkerSize(0)
    
   
    l = TLegend(lX, lY, lX+0.15, lY+0.15)
    l.SetBorderSize(0)
#    l.AddEntry(rec, "rec")
    #l.AddEntry(gen, "gen total")
    l.AddEntry(gen_Wonly, "gen W prompt")
    l.AddEntry(gen_fromTau, "gen #tau decay")
    l.AddEntry(gen_other, "gen other")

    stack = THStack("%s_stack" % total.GetName(), title)
    stack.Add(gen_other)
    stack.Add(gen_fromTau)
    stack.Add(gen_Wonly)
    
   
#    if title == "Electron #phi":
#        global r 
#        r = rec.Clone()
#        global rRatio
#        rRatio = recRatio.Clone()
#
#        global g
#        g = gen.Clone()
#        global gRatio
#        gRatio = ratio.Clone()
#        sys.exit()
    #line = TLine(rec.GetXaxis().GetBinLowEdge(1), 1., rec.GetXaxis().GetBinUpEdge(rec.GetNbinsX()), 1.)
    #line.SetLineWidth(2)

  #  pad1.cd()
    #rec.Draw("hist")
    #gen.Draw("hist same")
    #gen_cut.Draw("hist same")
    stack.SetMinimum(10)
    stack.SetMaximum(scalingY * total.GetMaximum())
    stack.Draw("hist")
    print "Now on %s" % title
    print "X axis title:", gen_Wonly.GetXaxis().GetTitle()
    stack.GetXaxis().SetTitle(total.GetXaxis().GetTitle())
    stack.GetXaxis().SetTitleOffset(total.GetXaxis().GetTitleOffset())
    stack.GetYaxis().SetTitle(total.GetYaxis().GetTitle())
    stack.GetYaxis().SetTitleOffset(total.GetYaxis().GetTitleOffset())
#    gen.Draw("hist same")
#    rec.Draw("hist e1 same")
    l.Draw("same")
    
    c.SaveAs(outF)
    c.SaveAs(outF.replace(".png",".pdf"))

def drawRecGenRatio_Wtau(rec, gen, gen_Wonly, gen_fromTau, title, outF, lX = 0.75, lY = 0.75, scalingY = 1.2, ratioYmin = 0.9, ratioYmax = 1.1, logY = True, recColor=kBlack, genColor=kRed, genWColor=kGray, genTauColor=kBlue, genOtherColor=kGreen):
    cRatio.cd()
    cRatio.ResetDrawn()
    cRatio.Draw()
    pad1.Draw()
    pad2.Draw()
  
    pad1.SetLogy(logY)
    gen_other = gen.Clone(gen.GetName() + "_other")
    gen_other.Add(gen_Wonly, -1)
    gen_other.Add(gen_fromTau, -1)
    gen_other.SetFillColor(genOtherColor)
    gen_other.SetLineColor(genOtherColor)
    gen_other.SetMarkerStyle(22)
    gen_other.SetMarkerSize(0)

    rec.SetLineWidth(0)
    rec.SetLineColor(recColor)
    rec.SetMarkerStyle(20)
    rec.SetMarkerSize(1)
    gen.SetLineWidth(2)
    gen.SetLineColor(genColor)
    gen_Wonly.SetLineWidth(2)
    gen_Wonly.SetLineColor(genWColor)
    gen_Wonly.SetFillColor(genWColor)
    gen_Wonly.SetMarkerStyle(22)
    gen_Wonly.SetMarkerSize(0)
    gen_fromTau.SetLineWidth(2)
    gen_fromTau.SetLineColor(genTauColor)
    gen_fromTau.SetFillColor(genTauColor)
    gen_fromTau.SetMarkerStyle(22)
    gen_fromTau.SetMarkerSize(0)
    
   
    l = TLegend(lX, lY, lX+0.14, lY+0.14)
    l.SetBorderSize(0)
    l.AddEntry(rec, "rec")
    l.AddEntry(gen, "gen total")
    l.AddEntry(gen_Wonly, "gen W prompt")
    l.AddEntry(gen_fromTau, "gen #tau decay")
    l.AddEntry(gen_other, "gen other")

    recNoErr = rec.Clone("rec_noerr")
    for b in xrange(1,recNoErr.GetNbinsX()+1):
        recNoErr.SetBinError(b, 0.)
    ratio = gen.Clone("ratio")
    ratio.Divide(recNoErr)
    ratio.SetTitle("")
    ratio.GetXaxis().SetTitle("")
    ratio.GetXaxis().SetLabelSize(ratio.GetYaxis().GetLabelSize()*2)
    ratio.GetYaxis().SetTitle("gen / rec")
    ratio.GetYaxis().SetTitleSize(ratio.GetYaxis().GetTitleSize()*3)
    ratio.GetYaxis().SetTitleOffset(ratio.GetYaxis().GetTitleOffset()/3)
    ratio.GetYaxis().SetLabelSize(ratio.GetYaxis().GetLabelSize()*2)
   

    ratio_Wonly = gen_Wonly.Clone("ratio_Wonly")
    ratio_Wonly.Divide(recNoErr)
    #ratio_Wonly.Divide(rec)
   
    ratio_fromTau = gen_fromTau.Clone("ratio_fromTau")
    ratio_fromTau.Divide(recNoErr)
    #ratio_fromTau.Divide(rec)
    

    stack = THStack("%s_stack" % rec.GetName(), title)
    stack.Add(gen_other)
    stack.Add(gen_fromTau)
    stack.Add(gen_Wonly)
    #oldTitle = rec.GetTitle()
    #rec.SetTitle(title)
    
    recRatio = rec.Clone(rec.GetName()+"_ratio")
    recRatio.Divide(recNoErr)
    recRatio.SetLineWidth(2) 
#    if title == "Electron #phi":
#        global r 
#        r = rec.Clone()
#        global rRatio
#        rRatio = recRatio.Clone()
#
#        global g
#        g = gen.Clone()
#        global gRatio
#        gRatio = ratio.Clone()
#        sys.exit()
    line = TLine(rec.GetXaxis().GetBinLowEdge(1), 1., rec.GetXaxis().GetBinUpEdge(rec.GetNbinsX()), 1.)
    line.SetLineWidth(2)

    pad1.cd()
    #rec.Draw("hist")
    #gen.Draw("hist same")
    #gen_cut.Draw("hist same")
    stack.SetMinimum(10)
    stack.SetMaximum(scalingY * rec.GetMaximum())
    stack.Draw("hist")
    stack.GetXaxis().SetTitle(rec.GetXaxis().GetTitle())
    stack.GetXaxis().SetTitleOffset(rec.GetXaxis().GetTitleOffset())
    stack.GetYaxis().SetTitle(rec.GetYaxis().GetTitle())
    stack.GetYaxis().SetTitleOffset(rec.GetYaxis().GetTitleOffset()+0.2)
    gen.Draw("hist same")
    rec.Draw("hist e1 same")
    l.Draw("same")
    
    pad2.cd()
    ratio.GetYaxis().SetRangeUser(ratioYmin,ratioYmax)
    ratio.Draw("hist e1")
    recRatio.Draw("hist e1 same")
    #line.Draw("same")
    cRatio.SaveAs(outF)
    cRatio.SaveAs(outF.replace(".png",".pdf"))



#drawRecGenCutRatio(rec_eleEta, gen_eleEta, "Electron #eta", "%s/eleEta.png" % outDir)
#drawRecGenCutRatio(rec_elePhi, gen_elePhi, "Electron #phi", "%s/elePhi.png" % outDir, lX=0.41, lY=0.2)
#drawRecGenCutRatio(rec_elePt, gen_elePt, "Electron p_{T}", "%s/elePt.png" % outDir)
#
#drawRecGenCutRatio(rec_muEta, gen_muEta, "Muon #eta", "%s/muEta.png" % outDir)
#drawRecGenCutRatio(rec_muPhi, gen_muPhi, "Muon #phi", "%s/muPhi.png" % outDir, lX=0.41, lY=0.2)
#drawRecGenCutRatio(rec_muPt, gen_muPt, "Muon p_{T}", "%s/muPt.png" % outDir)



# pT cut plots
cutPlotDir = "%s/cutplots" % outDir
os.system("mkdir -p %s" % cutPlotDir)

for obs in observables:
    exec("drawRecGenRatioOnly(rec_%s_full, gen_%s, '%s  prompt lepton SF', '%s')" % (obs,obs,obsTitle[obs], "%s/%s_promptSF" % (outDir,obs)))
    exec("drawRecGenRatio(rec_%s, gen_%s, '%s', '%s')" % (obs,obs,obsTitle[obs], "%s/%s" % (outDir,obs)))



#drawRecGenRatio(rec_ptll, gen_ptll, "p_{T}(ll)", "%s/ptll.png" % cutPlotDir)
#drawRecGenRatio(rec_ptll, gen_ptll_cut, "p_{T}(ll)   gen lepton p_{T} cut", "%s/ptll_cut.png" % cutPlotDir, color=kBlue)
#drawRecGenCutRatio(rec_ptll, gen_ptll, gen_ptll_cut, "p_{T}(ll)   gen lepton p_{T} cut", "%s/ptll_gen_cut.png" % cutPlotDir)
#
#drawRecGenRatio(rec_Mll, gen_Mll, "M(ll)", "%s/Mll.png" % cutPlotDir)
#drawRecGenRatio(rec_Mll, gen_Mll_cut, "M(ll)   gen lepton p_{T} cut", "%s/Mll_cut.png" % cutPlotDir, color=kBlue)
#drawRecGenCutRatio(rec_Mll, gen_Mll, gen_Mll_cut, "M(ll)   gen lepton p_{T} cut", "%s/Mll_gen_cut.png" % cutPlotDir)
#
#drawRecGenRatio(rec_ptpos, gen_ptpos, "p_{T}(l^{+})", "%s/ptpos.png" % cutPlotDir)
#drawRecGenRatio(rec_ptpos, gen_ptpos_cut, "p_{T}(l^{+})   gen lepton p_{T} cut", "%s/ptpos_cut.png" % cutPlotDir, color=kBlue)
#drawRecGenCutRatio(rec_ptpos, gen_ptpos, gen_ptpos_cut, "p_{T}(l^{+})   gen lepton p_{T} cut", "%s/ptpos_gen_cut.png" % cutPlotDir)
#
#drawRecGenRatio(rec_Epos, gen_Epos, "E(l^{+})", "%s/Epos.png" % cutPlotDir)
#drawRecGenRatio(rec_Epos, gen_Epos_cut, "E(l^{+})   gen lepton p_{T} cut", "%s/Epos_cut.png" % cutPlotDir, color=kBlue)
#drawRecGenCutRatio(rec_Epos, gen_Epos, gen_Epos_cut, "E(l^{+})   gen lepton p_{T} cut", "%s/Epos_gen_cut.png" % cutPlotDir)
#
#drawRecGenRatio(rec_ptp_ptm, gen_ptp_ptm, "p_{T}(l^{+}) + p_{T}(l^{-}", "%s/ptp_ptm.png" % cutPlotDir)
#drawRecGenRatio(rec_ptp_ptm, gen_ptp_ptm_cut, "p_{T}(l^{+}) + p_{T}(l^{-})   gen lepton p_{T} cut", "%s/ptp_ptm_cut.png" % cutPlotDir, color=kBlue)
#drawRecGenCutRatio(rec_ptp_ptm, gen_ptp_ptm, gen_ptp_ptm_cut, "p_{T}(l^{+}) + p_{T}(l^{-})   gen lepton p_{T} cut", "%s/ptp_ptm_gen_cut.png" % cutPlotDir)
#
#drawRecGenRatio(rec_Ep_Em, gen_Ep_Em, "E(l^{+}) + E(l^{-})", "%s/Ep_Em.png" % cutPlotDir)
#drawRecGenRatio(rec_Ep_Em, gen_Ep_Em_cut, "E(l^{+}) + E(l^{-})   gen lepton p_{T} cut", "%s/Ep_Em_cut.png" % cutPlotDir, color=kBlue)
#drawRecGenCutRatio(rec_Ep_Em, gen_Ep_Em, gen_Ep_Em_cut, "E(l^{+}) + E(l^{-})   gen lepton p_{T} cut", "%s/Ep_Em_gen_cut.png" % cutPlotDir)
#
drawRecGenRatio(rec_eleEta, gen_eleEta, "Electron #eta", "%s/eleEta" % outDir, lX=0.41, lY=0.2)
drawRecGenRatio(rec_elePhi, gen_elePhi, "Electron #phi", "%s/elePhi" % outDir, lX=0.41, lY=0.2)
drawRecGenRatio(rec_elePt, gen_elePt, "Electron p_{T}", "%s/elePt" % outDir)

drawRecGenRatio(rec_muEta, gen_muEta, "Muon #eta", "%s/muEta" % outDir, lX=0.41, lY=0.2)
drawRecGenRatio(rec_muPhi, gen_muPhi, "Muon #phi", "%s/muPhi" % outDir, lX=0.41, lY=0.2)
drawRecGenRatio(rec_muPt, gen_muPt, "Muon p_{T}", "%s/muPt" % outDir)


# Diff plots
#drawDiffRecGen_Wtau(diff_eleEta, diff_eleEta_Wonly, diff_eleEta_fromTau, diff_eleEta.GetTitle(), "%s/diffWtau_eleEta.png" % outDir, scalingY=1.3)
#drawDiffRecGen_Wtau(diff_elePhi, diff_elePhi_Wonly, diff_elePhi_fromTau, diff_elePhi.GetTitle(), "%s/diffWtau_elePhi.png" % outDir, scalingY=1.3)
#drawDiffRecGen_Wtau(diff_elePt,diff_elePt_Wonly, diff_elePt_fromTau, diff_elePt.GetTitle(), "%s/diffWtau_elePt.png" % outDir)
#drawDiffRecGen_Wtau(diffpct_elePt, diffpct_elePt_Wonly, diffpct_elePt_fromTau, diffpct_elePt.GetTitle(), "%s/diffpctWtau_elePt.png" % outDir)
#
#drawDiffRecGen_Wtau(diff_muEta, diff_muEta_Wonly, diff_muEta_fromTau, diff_muEta.GetTitle(), "%s/diffWtau_muEta.png" % outDir, scalingY=1.3)
#drawDiffRecGen_Wtau(diff_muPhi, diff_muPhi_Wonly, diff_muPhi_fromTau, diff_muPhi.GetTitle(), "%s/diffWtau_muPhi.png" % outDir, scalingY=1.3)
#drawDiffRecGen_Wtau(diff_muPt, diff_muPt_Wonly, diff_muPt_fromTau, diff_muPt.GetTitle(), "%s/diffWtau_muPt.png" % outDir)
#drawDiffRecGen_Wtau(diffpct_muPt, diffpct_muPt_Wonly, diffpct_muPt_fromTau, diffpct_muPt.GetTitle(), "%s/diffpctWtau_muPt.png" % outDir)
#

# W/tau plots
#drawRecGenRatio_Wtau(rec_ptll, gen_ptll, gen_ptll_Wonly, gen_ptll_fromTau, "p_{T}(ll)", "%s/ptll.png" % outDir)
#drawRecGenRatio_Wtau(rec_Mll, gen_Mll, gen_Mll_Wonly, gen_Mll_fromTau, "M(ll)", "%s/Mll.png" % outDir)
#drawRecGenRatio_Wtau(rec_ptpos, gen_ptpos, gen_ptpos_Wonly, gen_ptpos_fromTau, "p_{T}(l^{+})", "%s/ptpos.png" % outDir)
#drawRecGenRatio_Wtau(rec_ptneg, gen_ptneg, gen_ptneg_Wonly, gen_ptneg_fromTau, "p_{T}(l^{-})", "%s/ptneg.png" % outDir)
#drawRecGenRatio_Wtau(rec_Epos, gen_Epos, gen_Epos_Wonly, gen_Epos_fromTau, "E(l^{+})", "%s/Epos.png" % outDir)
#drawRecGenRatio_Wtau(rec_Eneg, gen_Eneg, gen_Eneg_Wonly, gen_Eneg_fromTau, "E(l^{-})", "%s/Eneg.png" % outDir)
#drawRecGenRatio_Wtau(rec_ptp_ptm, gen_ptp_ptm, gen_ptp_ptm_Wonly, gen_ptp_ptm_fromTau, "p_{T}(l^{+}) + p_{T}(l^{-})", "%s/ptp_ptm.png" % outDir)
#drawRecGenRatio_Wtau(rec_Ep_Em, gen_Ep_Em, gen_Ep_Em_Wonly, gen_Ep_Em_fromTau, "E(l^{+}) + E(l^{-})", "%s/Ep_Em.png" % outDir)

#drawRecGenRatio(rec_eleEta, gen_eleEta, "Electron #eta", "%s/eleEta" % outDir, scalingY=5, ratioYmin=0.98, ratioYmax=1.02)
#drawRecGenRatio(rec_elePhi, gen_elePhi, "Electron #phi", "%s/elePhi" % outDir, scalingY=8, ratioYmin=0.98, ratioYmax=1.02)
#drawRecGenRatio( rec_elePt,  gen_elePt, "Electron p_{T}", "%s/elePt" % outDir)
#
#drawRecGenRatio(rec_muEta, gen_muEta,  "Muon #eta", "%s/muEta" % outDir, scalingY=5, ratioYmin=0.98, ratioYmax=1.02)
#drawRecGenRatio(rec_muPhi, gen_muPhi,  "Muon #phi", "%s/muPhi" % outDir, scalingY=8, ratioYmin=0.98, ratioYmax=1.02)
#drawRecGenRatio(rec_muPt, gen_muPt, "Muon p_{T}", "%s/muPt" % outDir)


