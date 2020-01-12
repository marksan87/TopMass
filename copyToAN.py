#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--inDir", default="wtau_genrec", help="plot directory to copy over")
parser.add_argument("-o", "--outDir", default="/uscms/homes/m/msaunder/private/documentation/AN-17-249/assets/genrec", help="output AN plot directory")
args = parser.parse_args()


inDir = args.inDir
if inDir[-1] == "/": inDir = inDir[:-1]
outDir = args.outDir
if outDir[-1] == "/": outDir = outDir[:-1]
os.system("mkdir -p %s" % outDir)

print "Copying plots from %s to %s..." % (inDir, outDir),
sys.stdout.flush()

plots = [\
    "diff_eleEta.pdf",
    "diff_elePhi.pdf",
    "diff_elePt.pdf",
    "diffpct_elePt.pdf",
    "diff_muEta.pdf",
    "diff_muPhi.pdf",
    "diff_muPt.pdf",
    "diffpct_muPt.pdf",
    "diff_ptll.pdf",
    "diffpct_ptll.pdf",
    "diff_Mll.pdf",
    "diffpct_Mll.pdf",
    "diff_ptpos.pdf",
    "diffpct_ptpos.pdf",
    "diff_Epos.pdf",
    "diffpct_Epos.pdf",
    "diff_ptp_ptm.pdf",
    "diffpct_ptp_ptm.pdf",
    "diff_Ep_Em.pdf",
    "diffpct_Ep_Em.pdf",
    "ptll.pdf",
    "Mll.pdf",
    "ptpos.pdf",
    "ptneg.pdf",
    "Epos.pdf",
    "Eneg.pdf",
    "ptp_ptm.pdf",
    "Ep_Em.pdf",
    "ptll_promptSF.pdf",
    "Mll_promptSF.pdf",
    "ptpos_promptSF.pdf",
    "ptneg_promptSF.pdf",
    "Epos_promptSF.pdf",
    "Eneg_promptSF.pdf",
    "ptp_ptm_promptSF.pdf",
    "Ep_Em_promptSF.pdf",
    "eleEta.pdf",
    "elePhi.pdf",
    "elePt.pdf",
    "muEta.pdf",
    "muPhi.pdf",
    "muPt.pdf",
    ]

for p in plots:
    os.system("cp %s/%s %s/" % (inDir,p,outDir))

print "done"
sys.stdout.flush()

