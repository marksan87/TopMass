isMC=999
isData=1

from ROOT import kRed,kOrange,kBlue,kBlack,kCyan,kGray,kYellow,kGreen 

samples = {"TTbar"        : [["TTbarPowheg_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           "TTbar_mt1665" : [["TTbar_mt1665_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_mt1695" : [["TTbar_mt1695_1_AnalysisNtuple.root",
                              "TTbar_mt1695_2_AnalysisNtuple.root",
                              "TTbar_mt1695_3_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_mt1715" : [["TTbar_mt1715_1_AnalysisNtuple.root",
                              "TTbar_mt1715_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_mt1735" : [["TTbar_mt1735_1_AnalysisNtuple.root",
                              "TTbar_mt1735_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_mt1755" : [["TTbar_mt1755_1_AnalysisNtuple.root",
                              "TTbar_mt1755_2_AnalysisNtuple.root",
                              "TTbar_mt1755_3_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_mt1785" : [["TTbar_mt1785_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_hdampUp" : [["TTbar_hdampUp_1_AnalysisNtuple.root",
                               "TTbar_hdampUp_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_hdampDown" : [["TTbar_hdampDown_1_AnalysisNtuple.root",
                                 "TTbar_hdampDown_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_UEUp" : [["TTbar_UEUp_1_AnalysisNtuple.root",
                            "TTbar_UEUp_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_UEDown" : [["TTbar_UEDown_1_AnalysisNtuple.root",
                              "TTbar_UEDown_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_CRerdON" : [["TTbar_CRerdON_1_AnalysisNtuple.root",
                               "TTbar_CRerdON_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_CRGluon" : [["TTbar_CRGluon_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_CRQCD" : [["TTbar_CRQCD_1_AnalysisNtuple.root",
                             "TTbar_CRQCD_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
          
           "TTbar_amcanlo" : [["TTbar_amcanlo_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
            
           "TTbar_madgraph" : [["TTbar_madgraph_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_herwigpp" : [["TTbar_herwigpp_1_AnalysisNtuple.root",
                                "TTbar_herwigpp_2_AnalysisNtuple.root",
                                "TTbar_herwigpp_3_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],

           "TTbar_fsrDown" : [["TTbar_fsrDown_1_AnalysisNtuple.root",
                               "TTbar_fsrDown_2_AnalysisNtuple.root",
                               "TTbar_fsrDown_3_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_fsrUp" : [["TTbar_fsrUp_1_AnalysisNtuple.root",
                             "TTbar_fsrUp_2_AnalysisNtuple.root",
                             "TTbar_fsrUp_3_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_isrDown" : [["TTbar_isrDown_1_AnalysisNtuple.root",
                               "TTbar_isrDown_2_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_isrUp" : [["TTbar_isrUp_1_AnalysisNtuple.root",
                             "TTbar_isrUp_2_AnalysisNtuple.root",
                             "TTbar_isrUp_3_AnalysisNtuple.root",
                             ],
                             kGray,
                             "t#bar{t}",
                             isMC
                             ],
           
           "TTbar_MuScaleUp" :  [["TTbar_muscale_up_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_MuScaleDown" : [["TTbar_muscale_down_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_EleScaleUp" :  [["TTbar_elescale_up_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_EleScaleDown" : [["TTbar_elescale_down_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_EleSmearUp" :  [["TTbar_elesmear_up_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_EleSmearDown" : [["TTbar_elesmear_down_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_JERUp" :  [["TTbar_JER_up_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_JERDown" : [["TTbar_JER_down_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_JECUp" :  [["TTbar_JECTotal_up_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "TTbar_JECDown" : [["TTbar_JECTotal_down_AnalysisNtuple.root",
                                  ],
                                  kGray,
                                  "t#bar{t}",
                                  isMC
                                  ],
           
           "ST_tW_DS" :  [["ST_tW_top_DS_AnalysisNtuple.root",
                           "ST_tW_antitop_DS_AnalysisNtuple.root",
                           ],
                           618,
                           "ST tW",
                           isMC
                           ],
           
           "ST_tW_isrUp" :  [["ST_tW_top_isrUp_AnalysisNtuple.root",
                              "ST_tW_antitop_isrUp_AnalysisNtuple.root",
                               ],
                               618,
                               "ST tW",
                               isMC
                               ],
           
           "ST_tW_isrDown" :  [["ST_tW_top_isrDown_AnalysisNtuple.root",
                                "ST_tW_antitop_isrDown_AnalysisNtuple.root",
                                ],
                                618,
                                "ST tW",
                                isMC
                                ],
           
           
           "ST_tW_fsrUp" :  [["ST_tW_top_fsrUp_AnalysisNtuple.root",
                              "ST_tW_antitop_fsrUp_AnalysisNtuple.root",
                               ],
                               618,
                               "ST tW",
                               isMC
                               ],
           
           "ST_tW_fsrDown" :  [["ST_tW_top_fsrDown_AnalysisNtuple.root",
                                "ST_tW_antitop_fsrDown_AnalysisNtuple.root",
                                ],
                                618,
                                "ST tW",
                                isMC
                                ],
           
           "ST_tW_hdampUp" :  [["ST_tW_top_hdampUp_AnalysisNtuple.root",
                                "ST_tW_antitop_hdampUp_AnalysisNtuple.root",
                               ],
                               618,
                               "ST tW",
                               isMC
                               ],
           
           "ST_tW_hdampDown" :  [["ST_tW_top_hdampDown_AnalysisNtuple.root",
                                  "ST_tW_antitop_hdampDown_AnalysisNtuple.root",
                                ],
                                618,
                                "ST tW",
                                isMC
                                ],
           
           
           "ST_tW_Q2Up" :  [["ST_tW_top_Q2Up_AnalysisNtuple.root",
                             "ST_tW_antitop_Q2Up_AnalysisNtuple.root",
                               ],
                               618,
                               "ST tW",
                               isMC
                               ],
           
           "ST_tW_Q2Down" :  [["ST_tW_top_Q2Down_AnalysisNtuple.root",
                               "ST_tW_antitop_Q2Down_AnalysisNtuple.root",
                                ],
                                618,
                                "ST tW",
                                isMC
                                ],
           
           "ST_tW_MuScaleUp" :  [["ST_tW_top_muscale_up_AnalysisNtuple.root",
                                  "ST_tW_antitop_muscale_up_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_MuScaleDown" : [["ST_tW_top_muscale_down_AnalysisNtuple.root",
                                   "ST_tW_antitop_muscale_down_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_EleScaleUp" :  [["ST_tW_top_elescale_up_AnalysisNtuple.root",
                                   "ST_tW_antitop_elescale_up_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_EleScaleDown" : [["ST_tW_top_elescale_down_AnalysisNtuple.root",
                                    "ST_tW_antitop_elescale_down_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_EleSmearUp" :  [["ST_tW_top_elesmear_up_AnalysisNtuple.root",
                                   "ST_tW_antitop_elesmear_up_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_EleSmearDown" : [["ST_tW_top_elesmear_down_AnalysisNtuple.root",
                                    "ST_tW_antitop_elesmear_down_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_JERUp" :  [["ST_tW_top_JER_up_AnalysisNtuple.root",
                              "ST_tW_antitop_JER_up_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_JERDown" : [["ST_tW_top_JER_down_AnalysisNtuple.root",
                               "ST_tW_antitop_JER_down_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_JECUp" :  [["ST_tW_top_JECTotal_up_AnalysisNtuple.root",
                              "ST_tW_antitop_JECTotal_up_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           "ST_tW_JECDown" : [["ST_tW_top_JECTotal_down_AnalysisNtuple.root",
                               "ST_tW_antitop_JECTotal_down_AnalysisNtuple.root",
                                  ],
                                  618,
                                  "ST tW",
                                  isMC
                                  ],
           
           
#           "WJets"     : [["WJetsToLNu_AnalysisNtuple.root",
           "WJets"     : [["WJetsToLNu_LO_AnalysisNtuple.root",
                           ],
                          kBlue,
                          "W+jets",
                          isMC
                          ],

           "DY"         : [["DY_M_10to50_AnalysisNtuple.root",
                            "DY_M_50_AnalysisNtuple.root", 
                           ],
                          kYellow+1,
                          "DY",
                          isMC
                          ],

           "Diboson"   : [["WWTo2L2Nu_AnalysisNtuple.root",
                           "WZTo3LNu_AnalysisNtuple.root",
                           "ZZTo2L2Nu_AnalysisNtuple.root",
                           ],
                          kCyan-7,
                          "Diboson",
                          isMC
                          ],

           "ST_tW" : [["ST_tW_top_AnalysisNtuple.root",
                       "ST_tW_antitop_AnalysisNtuple.root",
                       ],
                       618,
                       "ST tW",
                       isMC
                       ],
           
           "ST_tW_mt1695" : [["ST_tW_top_mt1695_AnalysisNtuple.root",
                              "ST_tW_antitop_mt1695_AnalysisNtuple.root",
                              ],
                              618,
                              "ST tW",
                              isMC
                              ],
           
           "ST_tW_mt1755" : [["ST_tW_top_mt1755_AnalysisNtuple.root",
                              "ST_tW_antitop_mt1755_AnalysisNtuple.root",
                              ],
                              618,
                              "ST tW",
                              isMC
                              ],
           
           "ST_bkgd" :   [["ST_s_AnalysisNtuple.root",
                           "ST_t_top_AnalysisNtuple.root",
                           "ST_t_antitop_AnalysisNtuple.root",
                           ],
                          kGreen+1,
                          "ST s+t",
                          isMC
                          ],
           
           "TTV"       : [["TTWJetsToLNu_AnalysisNtuple.root",
                           "TTZToLLNuNu_AnalysisNtuple.root",
                           ],
                          kRed-7,
                          "ttV",
                          isMC
                          ],
           
           "Data" : [["Data_MuEG2016B_AnalysisNtuple.root",
                      "Data_MuEG2016C_AnalysisNtuple.root",
                      "Data_MuEG2016D_AnalysisNtuple.root",
                      "Data_MuEG2016E_AnalysisNtuple.root",
                      "Data_MuEG2016F_1_AnalysisNtuple.root",
                      "Data_MuEG2016F_2_AnalysisNtuple.root",
                      "Data_MuEG2016G_AnalysisNtuple.root",
                      "Data_MuEG2016H_1_AnalysisNtuple.root",
                      "Data_MuEG2016H_2_AnalysisNtuple.root",
                      ],
                      kBlack,
                      "Data",
                      isData
                      ],
           
           "DataBCDEF" : [["Data_MuEG2016B_AnalysisNtuple.root",
                            "Data_MuEG2016C_AnalysisNtuple.root",
                            "Data_MuEG2016D_AnalysisNtuple.root",
                            "Data_MuEG2016E_AnalysisNtuple.root",
                            "Data_MuEG2016F_1_AnalysisNtuple.root",
                            "Data_MuEG2016F_2_AnalysisNtuple.root",
                      ],
                      kBlack,
                      "Data",
                      isData
                      ],
           
           "DataGH" : [["Data_MuEG2016G_AnalysisNtuple.root",
                        "Data_MuEG2016H_1_AnalysisNtuple.root",
                        "Data_MuEG2016H_2_AnalysisNtuple.root",
                      ],
                      kBlack,
                      "Data",
                      isData
                      ],
           }

_signals = ["TTbar", "ST_tW"]
_massFiles = {"TTbar":{1665:1, 1695:3, 1715:2, 1735:2, 1755:3, 1785:1},
             "ST_tW":{1695:1, 1755:1} }
_color = {"TTbar":(kGray), "ST_tW":618}
_title = {"TTbar":"t#bar{t}", "ST_tW":"ST_tW"}
for sig in _signals:
    for m in _massFiles[sig]:
        name = "%s_mt%d"%(sig,m)
        N = _massFiles[sig][m]
        for var in ["Up","Down"]:
            samples["%s_MuScale%s"%(name,var)] = [
                ["%s_mt%d_%smuscale_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] if sig == "TTbar" else \
                ["%s_top_mt%d_%smuscale_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] + ["%s_antitop_mt%d_%smuscale_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)],
                _color[sig],
                _title[sig],
                isMC
                ]
        
            samples["%s_EleScale%s"%(name,var)] = [
                ["%s_mt%d_%selescale_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] if sig == "TTbar" else \
                ["%s_top_mt%d_%selescale_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] + ["%s_antitop_mt%d_%selescale_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)],
                _color[sig],
                _title[sig],
                isMC
                ]
            
            samples["%s_EleSmear%s"%(name,var)] = [
                ["%s_mt%d_%selesmear_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] if sig == "TTbar" else \
                ["%s_top_mt%d_%selesmear_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] + ["%s_antitop_mt%d_%selesmear_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)],
                _color[sig],
                _title[sig],
                isMC
                ]
            
            samples["%s_JEC%s"%(name,var)] = [
                ["%s_mt%d_%sJECTotal_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] if sig == "TTbar" else \
                ["%s_top_mt%d_%sJECTotal_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] + ["%s_antitop_mt%d_%sJECTotal_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)],
                _color[sig],
                _title[sig],
                isMC
                ]
            
            samples["%s_JER%s"%(name,var)] = [
                ["%s_mt%d_%sJER_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] if sig == "TTbar" else \
                ["%s_top_mt%d_%sJER_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)] + ["%s_antitop_mt%d_%sJER_%s_AnalysisNtuple.root"%(sig,m,"" if N == 1 else "%d_" % n,var.lower()) for n in xrange(1,N+1)],
                _color[sig],
                _title[sig],
                isMC
                ]
        
#           "TTbar_MuScaleDown" : [["TTbar_muscale_down_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_EleScaleUp" :  [["TTbar_elescale_up_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_EleScaleDown" : [["TTbar_elescale_down_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_EleSmearUp" :  [["TTbar_elesmear_up_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_EleSmearDown" : [["TTbar_elesmear_down_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_JERUp" :  [["TTbar_JER_up_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_JERDown" : [["TTbar_JER_down_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_JECUp" :  [["TTbar_JECTotal_up_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           
#           "TTbar_JECDown" : [["TTbar_JECTotal_down_AnalysisNtuple.root",
#                                  ],
#                                  kGray,
#                                  "t#bar{t}",
#                                  isMC
#                                  ],
#           

# List that is the same as the keys of samples, but given in the order we want to draw
sampleList = ["TTbar",
              "ST_tW",
              "DY",
              "WJets",
              "Diboson",
              "ST_bkgd",
              "TTV",
              "Data",
              ]



