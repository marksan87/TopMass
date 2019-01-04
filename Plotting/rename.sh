#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
dir=/store/user/msaunder/13TeV_AnalysisNtuples/emu/V08_00_26_07/

if [ -z "$1" ] || [ -z "$2" ] ; then
    echo "Usage: ./rename.sh fileOld fileNew "
else
    eos root://cmseos.fnal.gov mv $dir$1 $dir$2
fi
