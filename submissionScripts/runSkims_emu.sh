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
	echo "xrdcp root://cmseos.fnal.gov//store/user/msaunder/condorFiles/CMSSW_8_0_26_patch1.tgz CMSSW_8_0_26_patch1.tgz"
	xrdcp root://cmseos.fnal.gov//store/user/msaunder/condorFiles/CMSSW_8_0_26_patch1.tgz CMSSW_8_0_26_patch1.tgz

    export SCRAM_ARCH=slc6_amd64_gcc530
	source /cvmfs/cms.cern.ch/cmsset_default.sh

    echo "scramv1 project CMSSW CMSSW_8_0_26_patch1"
    scramv1 project CMSSW CMSSW_8_0_26_patch1

	echo "tar -xvf CMSSW_8_0_26_patch1.tgz"
	tar -xzf CMSSW_8_0_26_patch1.tgz
	
	cd CMSSW_8_0_26_patch1/src/
	source /cvmfs/cms.cern.ch/cmsset_default.sh
	cd TopNtuplizer/
    
	# copy tarred lep scale factors
	echo "xrdcp -f root://cmseos.fnal.gov//store/user/msaunder/condorFiles/lepSF.tgz lepSF.tgz"
	xrdcp -f root://cmseos.fnal.gov//store/user/msaunder/condorFiles/lepSF.tgz lepSF.tgz
    
    echo "tar xzvf lepSF.tgz"
	tar xzvf lepSF.tgz

	echo "xrdcp -f root://cmseos.fnal.gov//store/user/msaunder/condorFiles/Data_Pileup.tgz Data_Pileup.tgz"
	xrdcp -f root://cmseos.fnal.gov//store/user/msaunder/condorFiles/Data_Pileup.tgz Data_Pileup.tgz
	
    echo "tar xzvf Data_Pileup.tgz"
    tar xzvf Data_Pileup.tgz
	sleep 5
fi

eval `scramv1 runtime -sh`

channel="emu"
channelDir="emu"
tupleExtraName1=""
tupleExtraName2=""

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



#list of all of the input files, space separates to indicate new entry.  Can have multiple input files per entry
inputfiles=(
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/180423_165006/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1665_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1665_13TeV-powheg-pythia8/180425_215245/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1695_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1695_13TeV-powheg-pythia8/180425_215315/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1695_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1695_13TeV-powheg-pythia8-ext1/180425_215346/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1695_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1695_13TeV-powheg-pythia8-ext2/180425_215416/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1715_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1715_13TeV-powheg-pythia8/180425_215447/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1715_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1715_13TeV-powheg-pythia8-ext1/180425_215516/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1735_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1735_13TeV-powheg-pythia8/180425_215544/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1735_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1735_13TeV-powheg-pythia8-ext1/181207_234850/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1755_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1755_13TeV-powheg-pythia8/180425_215643/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1755_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1755_13TeV-powheg-pythia8-ext1/180425_215712/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1755_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1755_13TeV-powheg-pythia8-ext2/180425_215744/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_mtop1785_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_mtop1785_13TeV-powheg-pythia8/180425_215813/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8/180425_214506/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8-ext1/180426_143532/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8-ext2/180426_143602/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8/180425_214538/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8-ext1/180426_143635/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8-ext2/180426_143715/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8-ext1/180425_214608/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8-ext2/180426_143749/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8-ext1/180425_214641/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8-ext2/180426_143819/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8-ext2/180426_143819/0001" \
    $LPCtop"WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/180426_144604/0000" \
    $LPCtop"WWTo2L2Nu_13TeV-powheg/crab_WWTo2L2Nu_13TeV-powheg/180426_144103/0000" \
    $LPCtop"WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/crab_WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/180426_144135/0000" \
    $LPCtop"ZZTo2L2Nu_13TeV_powheg_pythia8/crab_ZZTo2L2Nu_13TeV_powheg_pythia8/180426_144208/0000" \
    $LPCtop"TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/crab_TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/180426_144725/0000" \
    $LPCtop"TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia/180426_144756/0000" \
    $LPCtop"ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/crab_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/180503_192632/0000" \
    $LPCtop"ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/crab_ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/180503_192904/0000" \
    $LPCtop"ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/crab_ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/180503_193136/0000" \
    $LPCtop"ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/crab_ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/180503_193415/0000" \
    $LPCtop"ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/crab_ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/180503_193627/0000" \
    $LPCtop"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/181209_010901/0000" \
    $LPCtop"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/181207_191716/0000" \
    $LPCtop"ST_tW_top_5f_mtop1695_NoFullyHadronicDecays_13TeV-powheg-pythia8/crab_ST_tW_top_5f_mtop1695_NoFullyHadronicDecays_13TeV-powheg-pythia8/180503_194503/0000" \
    $LPCtop"ST_tW_top_5f_mtop1755_NoFullyHadronicDecays_13TeV-powheg-pythia8/crab_ST_tW_top_5f_mtop1755_NoFullyHadronicDecays_13TeV-powheg-pythia8/180503_194650/0000" \
    $LPCtop"ST_tW_antitop_5f_mtop1695_NoFullyHadronicDecays_13TeV-powheg-pythia8/crab_ST_tW_antitop_5f_mtop1695_NoFullyHadronicDecays_13TeV-powheg-pythia8/180503_194843/0000" \
    $LPCtop"ST_tW_antitop_5f_mtop1755_NoFullyHadronicDecays_13TeV-powheg-pythia8/crab_ST_tW_antitop_5f_mtop1755_NoFullyHadronicDecays_13TeV-powheg-pythia8/180503_195031/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016B_FebReminiAOD/181206_222527/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016C_FebReminiAOD/181206_222600/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016D_FebReminiAOD/181206_222641/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016E_FebReminiAOD/181206_222712/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016F_FebReminiAOD_p1/181206_222752/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016F_FebReminiAOD_p2/181206_222823/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016G_FebReminiAOD/181206_222855/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016H_FebReminiAODv2/181206_222925/0000" \
    $LPCtop"MuonEG/crab_job_MuEG_Run2016H_FebReminiAODv3/181206_222957/0000" \
    $LPCtop"ST_tW_top_5f_isrup_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_top_5f_isrup_NoFullyHadronicDecays_13TeV-powheg/190103_200218/0000" \
    $LPCtop"ST_tW_top_isrdown_5f_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_top_isrdown_5f_NoFullyHadronicDecays_13TeV-powheg/190103_200140/0000" \
    $LPCtop"/ST_tW_top_5f_fsrup_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_top_5f_fsrup_NoFullyHadronicDecays_13TeV-powheg/190103_200102/0000" \
    $LPCtop"ST_tW_top_fsrdown_5f_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_top_fsrdown_5f_NoFullyHadronicDecays_13TeV-powheg/190103_200021/0000" \
    $LPCtop"ST_tW_antitop_5f_isrup_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_antitop_5f_isrup_NoFullyHadronicDecays_13TeV-powheg/190103_200445/0000" \
    $LPCtop"ST_tW_antitop_isrdown_5f_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_antitop_isrdown_5f_NoFullyHadronicDecays_13TeV-powheg/190103_200416/0000" \
    $LPCtop"ST_tW_antitop_5f_fsrup_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_antitop_5f_fsrup_NoFullyHadronicDecays_13TeV-powheg/190103_200328/0000" \
    $LPCtop"ST_tW_antitop_fsrdown_5f_NoFullyHadronicDecays_13TeV-powheg/crab_ST_tW_antitop_fsrdown_5f_NoFullyHadronicDecays_13TeV-powheg/190103_200255/0000" \
    $LPCtop"ST_tW_top_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_tW_top_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8_TuneCUETP8M1/181220_182521/0000" \
    $LPCtop"ST_tW_antitop_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8/crab_ST_tW_antitop_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8_TuneCUETP8M1/181220_182551/0000" \
    $LPCtop"TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/181216_231701/0000" \
    $LPCtop"TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8-ext1/181216_231731/0000" \
    $LPCtop"TT_hdampDOWN_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_TT_hdampDOWN_TuneCUETP8M2T4_13TeV-powheg-pythia8/181216_231804/0000" \
    $LPCtop"TT_hdampDOWN_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_TT_hdampDOWN_TuneCUETP8M2T4_13TeV-powheg-pythia8-ext1/190101_210317/0000" \
    $LPCtop"TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8/181217_223638/0000" \
    $LPCtop"TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8-ext1/181217_223710/0000" \
    $LPCtop"TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8/181217_223738/0000" \
    $LPCtop"TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8-ext1/181217_223806/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_erdON_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_erdON_13TeV-powheg-pythia8/181217_223849/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_erdON_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_erdON_13TeV-powheg-pythia8-ext1/181217_223920/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_GluonMoveCRTune_erdON_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_GluonMoveCRTune_erdON_13TeV-powheg-pythia8/181217_224039/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_QCDbasedCRTune_erdON_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_QCDbasedCRTune_erdON_13TeV-powheg-pythia8/181217_224106/0000" \
    $LPCtop"TT_TuneCUETP8M2T4_QCDbasedCRTune_erdON_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_QCDbasedCRTune_erdON_13TeV-powheg-pythia8-ext1/181219_145300/0000" \
    $LPCtop"TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/crab_TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/181217_225043/0000" \
    $LPCtop"TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/181217_225117/0000" \
    $LPCtop"TT_TuneEE5C_13TeV-powheg-herwigpp/crab_TT_TuneEE5C_13TeV-powheg-herwigpp/181217_225145/0000" \
    $LPCtop"TT_TuneEE5C_13TeV-powheg-herwigpp/crab_TT_TuneEE5C_13TeV-powheg-herwigpp-ext2/181217_225217/0000" \
    $LPCtop"TT_TuneEE5C_13TeV-powheg-herwigpp/crab_TT_TuneEE5C_13TeV-powheg-herwigpp-ext3/181217_225248/0000" \
)

sampleType=(
    "TTbarPowheg" \
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
    "TTbar_hdampUp_1" \
    "TTbar_hdampUp_2" \
    "TTbar_hdampDown_1" \
    "TTbar_hdampDown_2" \
    "TTbar_UEUp_1" \
    "TTbar_UEUp_2" \
    "TTbar_UEDown_1" \
    "TTbar_UEDown_2" \
    "TTbar_CRerdON_1" \
    "TTbar_CRerdON_2" \
    "TTbar_CRGluon" \
    "TTbar_CRQCD_1" \
    "TTbar_CRQCD_2" \
    "TTbar_amcanlo" \
    "TTbar_madgraph" \
    "TTbar_herwigpp_1" \
    "TTbar_herwigpp_2" \
    "TTbar_herwigpp_3" \
    )


#run the make skim
echo "AnalysisNtuple/makeSkim ${channel} ${sampleType[job]}_skim.root \`xrdfs root://cmseos.fnal.gov ls -u ${inputfiles[job]} | grep '\.root'\`"
AnalysisNtuple/makeSkim ${channel} ${sampleType[job]}_skim.root `xrdfs root://cmseos.fnal.gov ls -u ${inputfiles[job]} | grep '\.root'`


#Copy results over to eos 
echo "xrdcp -f ${sampleType[job]}_skim.root ${outputdir}skims/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root"
xrdcp -f ${sampleType[job]}_skim.root ${outputdir}skims/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root


