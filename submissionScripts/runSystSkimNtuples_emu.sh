#!/bin/bash

# TTbar and tW systematic samples

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
JEC=false
if [[ "$jobType" == "JEC"* ]] ; then
    tupleExtraName1="$jobType"
    systematic=true
    JEC=true
fi
if [ "$jobType" == "JER" ] ;    then
    tupleExtraName1="JER"
    systematic=true
fi
if [ "$jobType" == "elesmear" ] ;   then
    tupleExtraName1="elesmear"
    systematic=true
fi
if [ "$jobType" == "elescale" ] ;   then
    tupleExtraName1="elescale"
    systematic=true
fi
if [ "$jobType" == "muscale" ] ;   then
    tupleExtraName1="muscale"
    systematic=true
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

inputfiles=($LPCtop"TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/181216_231701/0000" \
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
$LPCtop"ST_tW_top_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8_TuneCUETP8M1/crab_ST_tW_top_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8_TuneCUETP8M1/181220_182521/0000" \
$LPCtop"ST_tW_antitop_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8/crab_ST_tW_antitop_5f_DS_NoFullyHadronicDecays_13TeV-powheg-pythia8_TuneCUETP8M1/181220_182551/0000" \
$LPCtop"" \
$LPCtop"" \
$LPCtop"" \
$LPCtop"" \
$LPCtop"" \
$LPCtop"" \
$LPCtop"" \
)


#name for the sample type of the file.  this is used by makeSkim as a file name and analysisNtuple to figure out which lumi scale factor to apply.
sampleType=("TTbar_hdampUp_1" \
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
"ST_tW_top_DS" \
"ST_tW_antitop_DS" \
)

#Copy skim ntuple from eos 
echo "xrdcp -f ${outputdir}skims/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root ${sampleType[job]}_skim.root"
xrdcp -f ${outputdir}skims/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root ${sampleType[job]}_skim.root 

echo $jobType
echo $JEC
if [ "$systematic" = true ] ; then
    if [ "$JEC" = false ] ; then
        # Up variation
        echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}_${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root"
        AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}_${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root

        echo "xrdcp -f ${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root"
        xrdcp -f ${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root

        # Down variation
        echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root"
        AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root

        echo "xrdcp -f ${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root"
        xrdcp -f ${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root
#        echo "xrdcp -f ${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root" 
#        xrdcp -f ${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root

    else
        if [ "$jobType" == "JEC1" ] ;   then
            jecList=("JECTotal")
        fi
        if [ "$jobType" == "JEC2" ] ;   then
            jecList=("JECAbsoluteStat" \
                "JECAbsoluteScale" \
                "JECAbsoluteMPFBias" \
                "JECFragmentation")
        fi
        if [ "$jobType" == "JEC3" ] ;   then
            jecList=("JECSinglePionECAL" \
                "JECSinglePionHCAL" \
                "JECFlavorQCD" \
                "JECTimePtEta" \
                "JECRelativeJEREC1")
        fi
        if [ "$jobType" == "JEC4" ] ;   then
            jecList=("JECRelativePtBB" \
                "JECRelativePtEC1" \
                "JECRelativeBal" \
                "JECRelativeFSR" \
                "JECRelativeStatFSR")
        fi
        if [ "$jobType" == "JEC5" ] ;   then
            jecList=("JECRelativeStatEC" \
                "JECPileUpDataMC" \
                "JECPileUpPtRef" \
                "JECPileUpPtBB" \
                "JECPileUpPtEC1")
        fi
        if [ "$jobType" == "JEC6" ] ;   then
                        jecList=("JECSubTotalPileUp" \
                                "JECSubTotalRelative" \
                                "JECSubTotalPt")
                fi
        if [ "$jobType" == "JEC7" ] ; then
                        jecList=("JECSubTotalScale" \
                                  "JECSubTotalAbsolute" \
                                  "JECSubTotalMC")
                fi

        for tupleExtraName1 in "${jecList[@]}"
        do :
            echo $jobType" "$tupleExtraName1
            # Up variation
            echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}_${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root"
            AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}_${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root

            echo "xrdcp -f ${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root"
            xrdcp -f ${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root
            rm ${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root

            # Down variation
            echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}_${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root"
            AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}_${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root

            echo "xrdcp -f ${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root"
            xrdcp -f ${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root
            rm ${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root
#            echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root"
#            AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root
#
#            echo "xrdcp -f ${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root" 
#            xrdcp -f ${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root
#            ${tupleExtraName1}_down_${sampleType[job]}_AnalysisNtuple.root

        done
    fi
fi
