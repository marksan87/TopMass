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

declare -a systematics=("toppt" \
         )

#declare -a systematics=("toppt" \
#             "PU" \
#             "Pdf" \
#             "Q2" \
#         )

declare -a variations=("up" \
            "down" \
            )

signalLength=${#signal[@]}
backgroundLength=${#background[@]}
systematicsLength=${#systematics[@]}
variationsLength=${#variations[@]}
ttbarMassLength=${#ttbarMass[@]}
ttbarIsrFsrLength=${#ttbarIsrFsr[@]}
tWMassLength=${#tWMass[@]}

for (( m=0; m < $ttbarMassLength; m++ )); do
    for (( sys=0; sys<systematicsLength; sys++ )); do
        echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]}" 
        ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} 
    done
done

for (( m=0; m < $tWMassLength; m++ )); do
    for (( sys=0; sys<systematicsLength; sys++ )); do
        echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]}"
        ./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} 
    done
done

#for (( m=0; m < $ttbarMassLength; m++ )); do
#    echo "./fillHistograms.py -s ${ttbarMass[$m]}"
#    ./fillHistograms.py -s ${ttbarMass[$m]} 
#    for (( sys=0; sys<systematicsLength; sys++ )); do
#        for (( var=0; var < $variationsLength; var++ )); do 
#            echo "./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]}"
#            ./fillHistograms.py -s ${ttbarMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]}
#        done
#    done
#done
#
#for (( m=0; m < $tWMassLength; m++ )); do
#    echo "./fillHistograms.py -s ${tWMass[$m]}"
#    ./fillHistograms.py -s ${tWMass[$m]} 
#    for (( sys=0; sys<systematicsLength; sys++ )); do
#        for (( var=0; var < $variationsLength; var++ )); do 
#            echo "./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]}"
#            ./fillHistograms.py -s ${tWMass[$m]} --syst ${systematics[$sys]} -l ${variations[$var]}
#        done
#    done
#done
#
#for (( m=0; m < $ttbarIsrFsrLength; m++ )); do
#    echo "./fillHistograms.py -s ${ttbarIsrFsr[$m]}"
#    ./fillHistograms.py -s ${ttbarIsrFsr[$m]} 
#done

#echo "./fillHistograms.py -s Data"
#./fillHistograms.py -s Data

#for (( s=0; s < $signalLength; s++ )); do
#    echo ${signal[$s]} 
#    echo "./fillHistograms.py -s ${signal[$s]}"
#    ./fillHistograms.py -s ${signal[$s]}
#    for (( sys=0; sys < $systematicsLength; sys++ )); do
#        for (( var=0; var < $variationsLength; var++ )); do 
#            ./fillHistograms.py -s ${signal[$s]} --syst ${systematics[$sys]} -l ${variations[$var]}
#        done
#    done
#done
#
#for (( b=0; b < $backgroundLength; b++ )); do
#    echo ${background[$b]}    
#    echo "./fillHistograms.py -s ${background[$b]}"
#    ./fillHistograms.py -s ${background[$b]}
#done
