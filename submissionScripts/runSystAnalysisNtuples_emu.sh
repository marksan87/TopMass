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
	echo "xrdcp -f root://cmseos.fnal.gov//store/user/msaunder/condorFiles/CMSSW_8_0_26_patch1.tgz ."
	xrdcp -f root://cmseos.fnal.gov//store/user/msaunder/condorFiles/CMSSW_8_0_26_patch1.tgz .

    export SCRAM_ARCH=slc6_amd64_gcc530
	source /cvmfs/cms.cern.ch/cmsset_default.sh

    echo "scramv1 project CMSSW CMSSW_8_0_26_patch1"
    scramv1 project CMSSW CMSSW_8_0_26_patch1

	echo "tar -xvf CMSSW_8_0_26_patch1.tgz"
	tar -xzf CMSSW_8_0_26_patch1.tgz

    rm CMSSW_8_0_26_patch1.tgz

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
if [ "$jobType" == "isr" ] ; then
    tupleExtraName1="isr"
    systematic=true
fi
if [ "$jobType" == "fsr" ] ; then
    tupleExtraName1="fsr"
    systematic=true
fi
if [ "$jobType" == "hdamp" ] ; then
    tupleExtraName1="hdamp"
    systematic=true
fi
if [ "$jobType" == "UE" ] ; then
    tupleExtraName1="UE"
    systematic=true
fi
if [ "$jobType" == "CRerdON" ] ; then
    tupleExtraName1="CRerdON"
    systematic=true
fi
if [ "$jobType" == "CRGluon" ] ; then
    tupleExtraName1="CRGluon"
    systematic=true
fi
if [ "$jobType" == "CRQCD" ] ; then
    tupleExtraName1="CRQCD"
    systematic=true
fi
if [ "$jobType" == "amcanlo" ] ; then
    tupleExtraName1="amcanlo"
    systematic=true
fi
if [ "$jobType" == "madgraph" ] ; then
    tupleExtraName1="madgraph"
    systematic=true
fi
if [ "$jobType" == "herwigpp" ] ; then
    tupleExtraName1="herwigpp"
    systematic=true
fi


skimdir="root://cmseos.fnal.gov//store/user/msaunder/13TeV_skims"
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
#sampleType=(
#"TTbar" \
#"TTbar_mt1665" \
#"TTbar_mt1695_1" \
#"TTbar_mt1695_2" \
#"TTbar_mt1695_3" \
#"TTbar_mt1715_1" \
#"TTbar_mt1715_2" \
#"TTbar_mt1735_1" \
#"TTbar_mt1735_2" \
#"TTbar_mt1755_1" \
#"TTbar_mt1755_2" \
#"TTbar_mt1755_3" \
#"TTbar_mt1785" \
#"ST_tW_top" \
#"ST_tW_antitop" \
#"ST_tW_top_mt1695" \
#"ST_tW_top_mt1755" \
#"ST_tW_antitop_mt1695" \
#"ST_tW_antitop_mt1755" \
#)
#sampleType=(
#    "TTbar_isrUp_1" \
#    "TTbar_isrUp_2" \
#    "TTbar_isrUp_3" \
#    "TTbar_isrDown_1" \
#    "TTbar_isrDown_2" \
#    "ST_tW_top_isrUp" \
#    "ST_tW_top_isrDown" \
#    "ST_tW_antitop_isrUp" \
#    "ST_tW_antitop_isrDown" \
#    "TTbar_fsrUp_1" \
#    "TTbar_fsrUp_2" \
#    "TTbar_fsrUp_3" \
#    "TTbar_fsrDown_1" \
#    "TTbar_fsrDown_2" \
#    "TTbar_fsrDown_3" \
#    "ST_tW_top_fsrUp" \
#    "ST_tW_top_fsrDown" \
#    "ST_tW_antitop_fsrUp" \
#    "ST_tW_antitop_fsrDown" \
#    "ST_tW_top_DS" \
#    "ST_tW_antitop_DS" \
#)
sampleType=(
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
    "TTbar" \
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
    "ST_tW_top" \
    "ST_tW_antitop" \
    "ST_tW_top_mt1695" \
    "ST_tW_top_mt1755" \
    "ST_tW_antitop_mt1695" \
    "ST_tW_antitop_mt1755" \
)

signal=""
var=""
if [ "${sampleType[job]:0:5}" == "TTbar" ] ; then
    signal="TTbar"
elif [ "${sampleType[job]:0:9}" == "ST_tW_top" ] ; then
    signal="ST_tW_top"
else
    signal="ST_tW_antitop"
fi

if [ "${sampleType[job]:${#signal}+1+${#jobType}:2}" == "Up" ] ; then
    var="up"
elif [ "${sampleType[job]:${#signal}+1+${#jobType}:4}" == "Down" ] ; then
    var="down"
fi
echo "signal: ${signal}"
echo "var: ${var}"
#Copy skim ntuple from eos

if [ "${sampleType[job]}" == "TTbar" ] ; then
    # Copy the TTbarPowheg skim file
    echo "xrdcp -f ${skimdir}/${channelDir}/V08_00_26_07/TTbarPowheg_skim.root ${sampleType[job]}_skim.root" 
    xrdcp -f ${skimdir}/${channelDir}/V08_00_26_07/TTbarPowheg_skim.root ${sampleType[job]}_skim.root 
else
    echo "xrdcp -f ${skimdir}/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root ${sampleType[job]}_skim.root"
    xrdcp -f ${skimdir}/${channelDir}/V08_00_26_07/${sampleType[job]}_skim.root ${sampleType[job]}_skim.root 
fi


echo $jobType
if [ "$systematic" = true ] ; then
    if [ "$jobType" == "DS" ] && [ "$signal" != "TTbar" ]; then
        echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]} . ${inputdir}${sampleType[job]}_skim.root"
        AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]} . ${inputdir}${sampleType[job]}_skim.root
        
        echo "xrdcp -f ${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_AnalysisNtuple.root"
        xrdcp -f ${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_AnalysisNtuple.root
    elif [ "$jobType" == "CRerdON" ] || [ "$jobType" == "CRGluon" ] || [ "$jobType" == "CRQCD" ] || [ "$jobType" == "amcanlo" ] || [ "$jobType" == "madgraph" ] || [ "$jobType" == "herwigpp" ] ; then
        echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]} . ${inputdir}${sampleType[job]}_skim.root"
        AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]} . ${inputdir}${sampleType[job]}_skim.root
        
        echo "xrdcp -f ${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_AnalysisNtuple.root"
        xrdcp -f ${sampleType[job]}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_AnalysisNtuple.root

    elif [ "$jobType" == "isr" ] || [ "$jobType" == "fsr" ] || [ "$jobType" == "hdamp" ] || [ "$jobType" == "UE" ] ; then
        echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_${var} . ${inputdir}${sampleType[job]}_skim.root"
        AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_${var} . ${inputdir}${sampleType[job]}_skim.root

        echo "xrdcp -f ${sampleType[job]}__${tupleExtraName1}_${var}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_AnalysisNtuple.root"
        xrdcp -f ${sampleType[job]}__${tupleExtraName1}_${var}_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_AnalysisNtuple.root


    elif [ "$JEC" = false ] ; then
        # Up variation
        echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root"
        AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root

        echo "xrdcp -f ${sampleType[job]}__${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root"
        xrdcp -f ${sampleType[job]}__${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root

        # Down variation
        echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root"
        AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root

        echo "xrdcp -f ${sampleType[job]}__${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root"
        xrdcp -f ${sampleType[job]}__${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root

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
            echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root"
            AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_up . ${inputdir}${sampleType[job]}_skim.root

            echo "xrdcp -f ${sampleType[job]}__${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root"
            xrdcp -f ${sampleType[job]}__${tupleExtraName1}_up_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_up_AnalysisNtuple.root
            rm ${sampleType[job]}__${tupleExtraName1}_up_AnalysisNtuple.root

            # Down variation
            echo "AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root"
            AnalysisNtuple/makeAnalysisNtuple ${sampleType[job]}__${tupleExtraName1}_down . ${inputdir}${sampleType[job]}_skim.root

            echo "xrdcp -f ${sampleType[job]}__${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root"
            xrdcp -f ${sampleType[job]}__${tupleExtraName1}_down_AnalysisNtuple.root ${outputdir}AnalysisNtuples/${channelDir}/V08_00_26_07/${sampleType[job]}_${tupleExtraName1}_down_AnalysisNtuple.root
            rm ${sampleType[job]}__${tupleExtraName1}_down_AnalysisNtuple.root
        done
    fi
fi
