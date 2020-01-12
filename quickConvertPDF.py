#!/usr/bin/env python
import os
import sys
from glob import glob
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--inDir", default="wtau_genrec")

args = parser.parse_args()

inDir = args.inDir
if inDir[-1] == "/": inDir = inDir[:-1]

files = glob("%s/*.png" % inDir)

for f in files:
    os.system("convert %s %s" % (f,f.replace(".png",".pdf")))
