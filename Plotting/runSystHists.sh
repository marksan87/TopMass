#!/bin/bash

eval `scramv1 runtime -sh`

declare -a signal=("TTbar" \
                   "ST_tW" \
                  )


declare -a background=("ST_bkgd" \
                       "DY" \
                       "TTV" \
                       "WJets" \
                       "Diboson" \
                      )


declare -a ttbarMass=("TTbar_mt1665" \
                      "TTbar_mt1695" \
                      "TTbar_mt1715" \
                      "TTbar_mt1735" \
                      "TTbar_mt1755" \
                      "TTbar_mt1785" \
                     )

declare -a ttbarIsrFsr=("TTbar_fsrDown" \
                        "TTbar_fsrUp" \
                        "TTbar_isrDown" \
                        "TTbar_isrUp" \
                       )

declare -a tWMass=("ST_tW_mt1695" \
                   "ST_tW_mt1755" \
                  )

declare -a systematics=(
             "EleScale" \
             "EleSmear" \
             "MuScale" \
             "JEC" \
             "JER" \
             "isr" \
             "fsr" \
             "hdamp" \
             "UE" \
             "EleIDEff" \
             "EleRecoEff" \
             "MuIDEff" \
             "MuIsoEff" \
             "MuTrackEff" \
             "TrigEff" \
             "BTagSF" \
             "Lumi" \
             "PU" \
             "Pdf" \
             "Q2" \
             "CRerdON" \
             "CRGluon" \
             "CRQCD" \
             "amcanlo" \
             "herwigpp" \
             "madgraph" \
             "DS" \
             "toppt" \
             )

#declare -a systematics=(
#             "MEscale1" \
#             "MEscale2" \
#             "MEscale3" \
#             "MEscale4" \
#             "MEscale5" \
#             "MEscale6" \
#             )

declare -a oneSidedSysts=(
        "CRerdON" \
        "CRGluon" \
        "CRQCD" \
        "amcanlo" \
        "madgraph" \
        "herwigpp" \
        "DS" \
        "MEscale1" \
        "MEscale2" \
        "MEscale3" \
        "MEscale4" \
        "MEscale5" \
        "MEscale6" \
        )
declare -a backgroundSystematics=( 
        "PU" \
        )


# Systematics only available at nominal mass point 
declare -a separateSampleSysts=(
        "DS" \
        "isr" \
        "fsr" \
        "hdamp" \
        "UE" \
        "CRerdON" \
        "CRGluon" \
        "CRQCD" \
        "amcanlo" \
        "herwigpp" \
        "madgraph"
        )

declare -a ttOnlySysts=(
        "toppt" \
        "UE" \
        "Pdf" \
        "CRerdON" \ 
        "CRGluon" \
        "CRQCD" \
        "amcanlo" \
        "madgraph" \
        "herwigpp" \
        "MEscale1" \
        "MEscale2" \
        "MEscale3" \
        "MEscale4" \
        "MEscale5" \
        "MEscale6" \
        )


declare -a tWOnlySysts=(
        "DS" \
        )

declare -a variations=("up" \
            "down" \
)

#addPlots="--addPlots --analysisNtupleDir 13TeV_AnalysisNtuples_BCDEF --outDir histograms_BCDEF"
#addPlots="--addPlots --analysisNtupleDir 13TeV_AnalysisNtuples_GH --outDir histograms_GH"
##addPlots="--addPlots --plot rec_ptll rec_Mll rec_ptpos rec_Epos rec_ptp_ptm rec_Ep_Em"
#addPlots="--addPlots --plot rec_ptll_M0_E0 rec_ptll_M0_E1 rec_ptll_M0_E2 rec_ptll_M1_E0 rec_ptll_M1_E1 rec_ptll_M1_E2 rec_ptll_M2_E0 rec_ptll_M2_E1 rec_ptll_M2_E2 --varBins '[0,50,70,100,300]'"
#addPlots="--addPlots --plot rec_leadJetPt rec_leadLepPt rec_Mll --analysisNtupleDir 1jet_13TeV_AnalysisNtuples --outDir 1jet_histograms"
#addPlots="--addPlots --plot nBJet bjetPt bjetEta bjetPhi"
#addPlots="--addPlots --plot rec_ptll --outDir secondtry_histograms"
#addPlots="--addPlots --plot rec_ptll elePt muPt jetPt --outDir histograms"
#addPlots="--addPlots --analysisNtupleDir fixed_13TeV_AnalysisNtuples --plot rec_ptll elePt muPt jetPt --outDir histograms"
#addPlots="--addPlots --plot rec_ptll --binning 300 20 320 --outDir histograms_cut320"
#addPlots="--addPlots --plot rec_ptll --binning 20 0 200 --outDir histograms_bin10"
#addPlots='--addPlots --plot rec_ptll --varBins "range(0,210,10) + [220]" --outDir histograms_varbin_220'
#addPlots="--addPlots --plot rec_ptneg gen_ptneg rec_Eneg gen_Eneg --outDir histograms"

addPlots="--outDir histograms"
#test="--testone"
test=""
signalLength=${#signal[@]}
backgroundLength=${#background[@]}
backgroundSystematicsLength=${#backgroundSystematics[@]}
systematicsLength=${#systematics[@]}
variationsLength=${#variations[@]}
ttbarMassLength=${#ttbarMass[@]}
ttbarIsrFsrLength=${#ttbarIsrFsr[@]}
tWMassLength=${#tWMass[@]}

option=$1



if [ "$option" == "nosyst" ] ; then
    for (( s=0; s < $signalLength; s++ )); do
        echo ${signal[$s]} 
        echo "./fillHistograms.py -s ${signal[$s]} ${addPlots}"
        eval ./fillHistograms.py -s ${signal[$s]} ${addPlots}
    done

    for (( m=0; m < $ttbarMassLength; m++ )); do
        echo "./fillHistograms.py -s ${ttbarMass[$m]} ${addPlots}"
        eval ./fillHistograms.py -s ${ttbarMass[$m]} ${addPlots}
    done

    for (( m=0; m < $tWMassLength; m++ )); do
        echo "./fillHistograms.py -s ${tWMass[$m]} ${addPlots}"
        eval ./fillHistograms.py -s ${tWMass[$m]} ${addPlots}
    done

elif [ "$option" == "sig" ] ; then
    for (( s=0; s < $signalLength; s++ )); do
        for (( sys=0; sys < $systematicsLength; sys++ )); do
            if [ "${signal[$s]}" == "TTbar" ] && [[ "${tWOnlySysts[@]}" =~ "${systematics[$sys]}" ]] ; then 
                continue
            elif [ "${signal[$s]}" == "ST_tW" ] && [[ "${ttOnlySysts[@]}" =~ "${systematics[$sys]}" ]] ; then
                continue
            fi
            echo "Now on signal ${signal[$s]}  syst ${systematics[$sys]}"
            
#            if [ "${signal[$s]}" == "ST_tW" ] && [[ ! "${tWOnlySysts[@]}" =~ "${systematics[$sys]}" ]] ; then
#            _sig="${signal[$s]}"
#            echo "Signal = $_sig"
#            #if [ "S{signal[$s]}" == "ST_tW" ] ; then
#            if [ "$_sig" == "ST_tW" ] ; then
#                echo "On ST_tW systematic ${systematics[$sys]}"
#                _syst="${systematics[$sys]}"
#                #if [[ ! "${tWOnlySysts[@]}" =~ "${systematics[$sys]}" ]] ; then
#                if [[ ! "${tWOnlySysts[@]}" =~ "$_syst" ]] ; then
                    # If tW, skip systematics which are not available
#                    echo "Skipping systematic ${systematics[sys]} for tW"
#                    continue
##                fi
            if [[ "${oneSidedSysts[@]}" =~  "${systematics[$sys]}" ]] ; then
                # One sided systs
                echo "${systematics[sys]} is a one-sided systematic"
                echo "./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} ${addPlots} ${test}"
                eval ./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} ${addPlots} ${test}
            else
                # Up/Down variations
                echo "${systematics[sys]} has up/down variations"
                for (( var=0; var < $variationsLength; var++ )); do 
                    echo "./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}"
                    eval ./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}
                done
            fi
        done
    done
elif [ "$option" == "ttmt" ] || [ "$option" == "ttmt_1" ] || [ "$option" == "ttmt_2" ] ; then
    if [ "$option" == "ttmt_1" ] ; then 
        declare -a ttbarMass=(
                      "TTbar_mt1665" \
                      "TTbar_mt1695" \
                      "TTbar_mt1715" \
                     )
    elif [ "$option" == "ttmt_2" ] ; then
        declare -a ttbarMass=(
                      "TTbar_mt1735" \
                      "TTbar_mt1755" \
                      "TTbar_mt1785" \
                     )
        
    fi
    ttbarMassLength=${#ttbarMass[@]}
    for (( m=0; m < $ttbarMassLength; m++ )); do
        for (( sys=0; sys<systematicsLength; sys++ )); do
            if [[ "${tWOnlySysts[@]}" =~ "${systematics[$sys]}" ]] ; then
                continue
            fi
            
            if [[ "${separateSampleSysts[@]}" =~  "${systematics[$sys]}" ]] ; then
                # Separate sample syst not available at alternate mass points
                continue
            elif [[ "${oneSidedSysts[@]}" =~  "${systematics[$sys]}" ]] ; then
                # One sided systs
                echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}"
                eval ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}
            else
                # Up/Down variations
                for (( var=0; var < $variationsLength; var++ )); do 
                    echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}"
                    eval ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}
                done

            fi
        done
    done
elif [ "$option" == "tWmt" ] ; then
    for (( m=0; m < $tWMassLength; m++ )); do
#        echo "./fillHistograms.py -s ${tWMass[$m]} ${addPlots} ${test}"
#        ./fillHistograms.py -s ${tWMass[$m]} ${addPlots} ${test}
        for (( sys=0; sys<systematicsLength; sys++ )); do
            if [[ "${ttOnlySysts[@]}" =~ "${systematics[$sys]}" ]] ; then
                continue
            fi
            
            if [[ "${separateSampleSysts[@]}" =~  "${systematics[$sys]}" ]] || [[ "Q2" =~ "${systematics[$sys]}" ]] ; then
                # Separate sample syst not available at alternate mass points
                continue
            elif [[ "${oneSidedSysts[@]}" =~  "${systematics[$sys]}" ]] ; then
                # One sided systs
                echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}"
                eval ./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}
            else
                # Up/Down variations
                for (( var=0; var < $variationsLength; var++ )); do 
                    echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}"
                    eval ./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}
                done
            fi
        done
    done
elif [ "$option" == "bkg" ] ; then
   echo "backgroundSystematicsLength = $backgroundSystematicsLength"
   
   for (( b=0; b < $backgroundLength; b++ )); do
        echo ${background[$b]}    
        echo "./fillHistograms.py -s ${background[$b]} ${addPlots}"
        eval ./fillHistograms.py -s ${background[$b]} ${addPlots}
        for (( sys=0; sys < $backgroundSystematicsLength; sys++ )); do
            for (( var=0; var < $variationsLength; var++ )); do
                echo "./fillHistograms.py -s ${background[$b]} --syst ${backgroundSystematics[$sys]} -l ${variations[$var]} ${addPlots}"
                eval ./fillHistograms.py -s ${background[$b]} --syst ${backgroundSystematics[$sys]} -l ${variations[$var]} ${addPlots}
            done
        done
    done 

elif [ "${option,,}" == "data" ] ; then
    echo "./fillHistograms.py -s Data ${addPlots}"
    eval ./fillHistograms.py -s Data ${addPlots}
elif [ "${option,,}" == "databcdef" ] ; then
    echo "./fillHistograms.py -s DataBCDEF ${addPlots}"
    eval ./fillHistograms.py -s DataBCDEF ${addPlots}
elif [ "${option,,}" == "datagh" ] ; then
    echo "./fillHistograms.py -s DataGH ${addPlots}"
    eval ./fillHistograms.py -s DataGH ${addPlots}

else
    echo "Invalid option ${1}. Choose from:"
    echo "sig, nosyst, ttmt, ttmt_1, ttmt_2, tWmt, bkg, data, databcdef, datagh"
fi
