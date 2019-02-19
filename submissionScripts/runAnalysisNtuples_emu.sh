#!/bin/bash

job=$1
jobType=$2


#If statement to figure out if this shell script is being run in local area (interactively) or on condor. 
if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
	echo "Running Interactively" ; 
else
	echo "Running In Batch"
	(>&2 echo "Starting job on " `date`) # Date/time of start of job
	(>&2 echo "Running on: `uname -a`") # Condor job is running on this node
	(>&2 echo "System software: `cat /etc/redhat-release`") # Operating System on that node

	cd ${_CONDOR_SCRATCH_DIR}
	echo ${_CONDOR_SCRATCH_DIR}
	
	# copy tarred cmssw area over from eos (should be excluding .SCRAM area)
	echo "xrdcp root://cmseos.fnal.gov//store/user/"${USER}"/condorFiles/CMSSW_8_0_26_patch1.tgz ."
	xrdcp root://cmseos.fnal.gov//store/user/${USER}/condorFiles/CMSSW_8_0_26_patch1.tgz .

    export SCRAM_ARCH=slc6_amd64_gcc530
	source /cvmfs/cms.cern.ch/cmsset_default.sh

	eval `scramv1 project CMSSW CMSSW_8_0_26_patch1`

	echo "tar -xvf CMSSW_8_0_26_patch1.tgz"
	tar -xzf CMSSW_8_0_26_patch1.tgz
	
	cd CMSSW_8_0_26_patch1/src/
	source /cvmfs/cms.cern.ch/cmsset_default.sh
	cd TopNtuplizer/
    
	# copy tarred lep scale factors
	echo "xrdcp -f root://cmseos.fnal.gov//store/user/"${USER}"/condorFiles/lepSF.tgz ."
	xrdcp -f root://cmseos.fnal.gov//store/user/${USER}/condorFiles/lepSF.tgz .
    
    echo "tar xzvf lepSF.tgz"
	tar xzvf lepSF.tgz

	echo "xrdcp -r root://cmseos.fnal.gov//store/user/msaunder/condorFiles/Data_Pileup.tgz ."
	xrdcp -r root://cmseos.fnal.gov//store/user/msaunder/condorFiles/Data_Pileup.tgz .
	
    echo "tar xzvf Data_Pileup.tgz"
    tar xzvf Data_Pileup.tgz
	sleep 5
fi

eval `scramv1 runtime -sh`

channel="emu"
channelDir="emu"
tupleExtraName1=""
tupleExtraName2=""

if [ "$jobType" == "QCD" ] ;	then
	channel="qcdele"
	channelDir="qcdelectrons"
	tupleExtraName1="QCDcr_"
	tupleExtraName2="__QCDcr"
fi
if [ "$jobType" == "Dilep" ] ;	then
	channel="diele"
	channelDir="dielectrons"
	tupleExtraName1="Dilep_"
	tupleExtraName2="__Dilep"
fi

#outputdir="root://cmseos.fnal.gov//store/user/lpctop/TopMass/13TeV_"
outputdir="root://cmseos.fnal.gov//store/user/msaunder/13TeV_"

#variables for the directory names where the ttgamma analysis was storing ggNtuples
DannyEOS="root://cmseos.fnal.gov//store/user/dnoonan/13TeV_ggNTuples/V08_00_26_07/"
GGNtupleGroupEOSMC="root://cmseos.fnal.gov//store/user/lpcggntuples/ggNtuples/13TeV/mc/V08_00_26_07/"
TitasEOS="root://cmseos.fnal.gov//store/user/troy2012/13TeV_ggNTuples/V08_00_26_07/"
GGNtupleGroupEOSData="root://cmseos.fnal.gov//store/user/lpcggntuples/ggNtuples/13TeV/data/V08_00_26_07/"
#LPCtop="root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_ggNTuples/V08_00_26_07/"

MarkEOS="/store/user/msaunder/"
LPCtop="/store/user/lpctop/TopMass/13TeV_ggNTuples/V08_00_26_07/"

TEST="/store/user/msaunder/test/"




#name for the sample type of the file.  this is used by makeSkim as a file name and analysisNtuple to figure out which lumi scale factor to apply.
sampleType=("TTbarPowheg" \
            "TTbar_mt1665" \
            "TTbar_mt1695_1" \
            "TTbar_mt1695_2" \
            "TTbar_mt1695_3" \
            "TTbar_mt1715_1" \
            "TTbar_mt1715_2" \
            "TTbar_mt1735_1" \
            "TTbar_mt1735_2" \
            "TTbar_mt1755_1" \
            "TTbar_mt1755_2" \
            "TTbar_mt1755_3" \
            "TTbar_mt1785" \
            "WJetsToLNu" \
            "WWTo2L2Nu" \
            "WZTo3LNu" \
            "ZZTo2L2Nu" \
            "TTWJetsToLNu" \
            "TTZToLLNuNu" \
            "ST_s" \
            "ST_t_top" \
            "ST_t_antitop" \
            "ST_tW_top" \
            "ST_tW_antitop" \
            "DY_M_10to50" \
            "DY_M_50" \
            "ST_tW_top_mt1695" \
            "ST_tW_top_mt1755" \
            "ST_tW_antitop_mt1695" \
            "ST_tW_antitop_mt1755" \
            "Data_MuEG2016B" \
            "Data_MuEG2016C" \
            "Data_MuEG2016D" \
            "Data_MuEG2016E" \
            "Data_MuEG2016F_1" \
            "Data_MuEG2016F_2" \
            "Data_MuEG2016G" \
            "Data_MuEG2016H_1" \
            "Data_MuEG2016H_2" \
            "TTbar_fsrDown_1" \
            "TTbar_fsrDown_2" \
            "TTbar_fsrDown_3" \
            "TTbar_fsrUp_1" \
            "TTbar_fsrUp_2" \
            "TTbar_fsrUp_3" \
            "TTbar_isrDown_1" \
            "TTbar_isrDown_2" \
            "TTbar_isrUp_1" \
            "TTbar_isrUp_2" \
            "TTbar_isrUp_3" \
            "ST_tW_top_isrUp" \
            "ST_tW_top_isrDown" \
            "ST_tW_top_fsrUp" \
            "ST_tW_top_fsrDown" \
            "ST_tW_antitop_isrUp" \
            "ST_tW_antitop_isrDown" \
            "ST_tW_antitop_fsrUp" \
            "ST_tW_antitop_fsrDown" \
            "ST_tW_top_DS" \
            "ST_tW_antitop_DS" \
            )


#Copy skim ntuple from eos 
echo "xrdcp -f ${outputdir}skims/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root ${sampleType[job]}_skim.root"
xrdcp -f ${outputdir}skims/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root ${sampleType[job]}_skim.root 

#run makeAnalysisNtuple
echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}${tupleExtraName2} . ${sampleType[job]}_skim.root"
AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}${tupleExtraName2} . ${sampleType[job]}_skim.root

#Copy results over to eos (commented out for now)
echo "xrdcp -f ${tupleExtraName1}${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${tupleExtraName1}${sampleType[job]}_AnalysisNtuple.root"
xrdcp -f ${tupleExtraName1}${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${tupleExtraName1}${sampleType[job]}_AnalysisNtuple.root


