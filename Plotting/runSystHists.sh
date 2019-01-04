#!/bin/bash

eval `scramv1 runtime -sh`

declare -a signal=("TTbar" \
                   "ST_tW" \
                  )

#declare -a signal=("ST_tW" \
#                  )
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

#declare -a systematics=(
#             "EleScale" \
#             "EleSmear" \
#             "MuScale" \
#             "JEC" \
#             "JER" \
#         )
#
declare -a systematics=(
             "JER" \
         )

declare -a variations=("up" \
            "down" \
            )
#addPlots="--addPlots --plot nBJet bjetPt bjetEta bjetPhi"
addPlots=""
#test="--testone"
test=""
signalLength=${#signal[@]}
systematicsLength=${#systematics[@]}
variationsLength=${#variations[@]}
ttbarMassLength=${#ttbarMass[@]}
ttbarIsrFsrLength=${#ttbarIsrFsr[@]}
tWMassLength=${#tWMass[@]}

if [ "$1" == "sig" ] ; then
    for (( s=0; s < $signalLength; s++ )); do
        for (( sys=0; sys < $systematicsLength; sys++ )); do
            if [ "$sys" == "toppt" ] ; then
                echo "./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} ${addPlots} ${test}"
                ./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} ${addPlots} ${test}
            else
                for (( var=0; var < $variationsLength; var++ )); do 
                    echo "./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}"
                    ./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}
                done
            fi
        done
    done
elif [ "$1" == "ttmt" ] ; then
    for (( m=0; m < $ttbarMassLength; m++ )); do
        for (( sys=0; sys<systematicsLength; sys++ )); do
            if [ "$sys" == "toppt" ] ; then
                echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}"
                ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}
            else
                for (( var=0; var < $variationsLength; var++ )); do 
                    echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}"
                    ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}
                done

            fi
        done
    done
elif [ "$1" == "tWmt" ] ; then
    for (( m=0; m < $tWMassLength; m++ )); do
#    echo "./fillHistograms.py -s ${tWMass[$m]} ${addPlots} ${test}"
#    ./fillHistograms.py -s ${tWMass[$m]} ${addPlots} ${test}
        for (( sys=0; sys<systematicsLength; sys++ )); do
            if [ "$sys" == "toppt" ] ; then
                echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}"
                ./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} ${addPlots} ${test}
            else
                for (( var=0; var < $variationsLength; var++ )); do 
                    echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}"
                    ./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]} ${addPlots} ${test}
                done
            fi
        done
    done
else
    echo "Invalid option ${1}. Choose from:"
    echo "sig, ttmt, tWmt"
fi
