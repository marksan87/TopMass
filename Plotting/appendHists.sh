#!/bin/bash

eval `scramv1 runtime -sh`

declare -a signal=("TTbar" \
                   "ST_tW" \
                   )

#declare -a signal=("TTbar" \
#                  )
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

# One-sided systematics
declare -a onesidedSystematics=(
         "toppt" \
        )

declare -a systematics=(
             "EleIDEff"
             "EleRecoEff"
             "MuIDEff"
             "MuIsoEff"
             "MuTrackEff"
             "TrigEff"
             "BTagSF"
             "Lumi"
             "PU" \
             "Pdf" \
             "Q2" \
         )

declare -a variations=("up" \
            "down" \
            )
#addPlots="--addPlots --plot nBJet bjetPt bjetEta bjetPhi"
addPlots=""
signalLength=${#signal[@]}
backgroundLength=${#background[@]}
systematicsLength=${#systematics[@]}
onesidedSystematicsLength=${#onesidedSystematics[@]}
variationsLength=${#variations[@]}
ttbarMassLength=${#ttbarMass[@]}
ttbarIsrFsrLength=${#ttbarIsrFsr[@]}
tWMassLength=${#tWMass[@]}

if [ "$1" == "sig" ] ; then
    for (( s=0; s < $signalLength; s++ )); do
        echo ${signal[$s]} 
        echo "./fillHistograms.py -s ${signal[$s]} ${addPlots}"
        ./fillHistograms.py -s ${signal[$s]} ${addPlots}
        
        for (( sys=0; sys < $onesidedSystematicsLength; sys++ )); do
            echo "./fillHistograms.py -s ${signal[$s]} --syst ${onesidedSystematics[$sys]} ${addPlots}"
            ./fillHistograms.py -s ${signal[$s]} --syst ${onesidedSystematics[$sys]} ${addPlots}
        done
        for (( sys=0; sys < $systematicsLength; sys++ )); do
            for (( var=0; var < $variationsLength; var++ )); do 
                echo "./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots}"
                ./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots}
            done
        done
    done

elif [ "$1" == "ttmt" ] ; then
    for (( m=0; m < $ttbarMassLength; m++ )); do
        echo "./fillHistograms.py -s ${ttbarMass[$m]} ${addPlots}"
        ./fillHistograms.py -s ${ttbarMass[$m]} ${addPlots}
        
        for (( sys=0; sys < $onesidedSystematicsLength; sys++ )); do
            echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${onesidedSystematics[$sys]} ${addPlots}"
            ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${onesidedSystematics[$sys]} ${addPlots}
        done
        for (( sys=0; sys<systematicsLength; sys++ )); do
            for (( var=0; var < $variationsLength; var++ )); do 
                echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots}"
                ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots}
            done
        done
    done
elif [ "$1" == "tWmt" ] ; then
    for (( m=0; m < $tWMassLength; m++ )); do
        echo "./fillHistograms.py -s ${tWMass[$m]} ${addPlots}"
        ./fillHistograms.py -s ${tWMass[$m]} ${addPlots} 
        for (( sys=0; sys < $onesidedSystematicsLength; sys++ )); do
            echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${onesidedSystematics[$sys]} ${addPlots}"
            ./fillHistograms.py -s ${tWMass[$m]} --syst ${onesidedSystematics[$sys]} ${addPlots}
        done
        for (( sys=0; sys<systematicsLength; sys++ )); do
            for (( var=0; var < $variationsLength; var++ )); do 
                echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots}"
                ./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots}
            done
        done
    done

#for (( m=0; m < $ttbarIsrFsrLength; m++ )); do
#    echo "./fillHistograms.py -s ${ttbarIsrFsr[$m]}" ${addPlots}
#    ./fillHistograms.py -s ${ttbarIsrFsr[$m]} ${addPlots} 
#done
#
#echo "./fillHistograms.py -s Data ${addPlots}"
#./fillHistograms.py -s Data ${addPlots}
#
#
elif [ "$1" == "bkg" ] ; then
    for (( b=0; b < $backgroundLength; b++ )); do
        echo ${background[$b]}    
        echo "./fillHistograms.py -s ${background[$b]} ${addPlots}"
        ./fillHistograms.py -s ${background[$b]} ${addPlots}
    done
else
    echo "Invalid option ${1}. Choose from:"
    echo "sig, bkg, ttmt, tWmt"
fi
