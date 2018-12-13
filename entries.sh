#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh

AnalysisNtuple/countEvents `xrdfs root://cmseos.fnal.gov ls -u /$1 | grep '\.root'`
