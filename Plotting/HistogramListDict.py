btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]


def GetHistogramInfo_2Dplot(extraCuts="(passPresel_Mu && nJet>=3 && nBJet>=1)*", extraPhotonCuts="(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*", nBJets=1):
    histogramInfo = {#"2D_PhotonEt" :["phoEt[0]", "mcPt", "2D_PhotonEt", [300,0,300], [300,0,300],"
#		     "phosel_2DChIsoSIEIE"         : ["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE", [500,0,0.05], [200,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                     }

    return histogramInfo

		
def GetHistogramInfo(extraCuts="", nBJets=1):
    btagCut = "((jetDeepCSVTags_b + jetDeepCSVTags_bb) > 0.6324)*"
    defaultWeight = "evtWeight * PUweight * eleEffWeight * muEffWeight * trigEffWeight * %s" % btagWeightCategory[nBJets]
    
    histogramInfo = { \
                      "presel_jet1Pt"    : ["jetPt[0]"  , "presel_jet1Pt"    ,    [1000,0,1000], extraCuts, ""],
                      "presel_jet2Pt"    : ["jetPt[1]"  , "presel_jet2Pt"    ,      [600,0,600], extraCuts, ""],
                      "presel_jet3Pt"    : ["jetPt[2]"  , "presel_jet3Pt"    ,      [600,0,600], extraCuts, ""],
                      "presel_jet4Pt"    : ["jetPt[3]"  , "presel_jet4Pt"    ,      [600,0,600], extraCuts, ""],
                      "presel_Njet"      : ["nJet"      , "presel_Njet"      ,        [15,0,15], extraCuts, ""],
                      "presel_Nbjet"     : ["nBJet"     , "presel_Nbjet"     ,        [10,0,10], extraCuts, ""],
                      "presel_muPt"      : ["muPt"      , "presel_muPt"      ,      [600,0,600], extraCuts, ""],
                      "presel_muEta"     : ["muEta"     , "presel_muEta"     ,   [100,-2.4,2.4], extraCuts, ""],
                      "presel_muPhi"     : ["muPhi"     , "presel_muPhi"     , [100,-3.15,3.15], extraCuts, ""],
                      "presel_elePt"     : ["elePt"     , "presel_elePt"     ,      [600,0,600], extraCuts, ""],
                      "presel_eleSCEta"  : ["eleSCEta"  , "presel_eleSCEta"  ,   [100,-2.4,2.4], extraCuts, ""],
                      "presel_elePhi"    : ["elePhi"    , "presel_elePhi"    , [100,-3.15,3.15], extraCuts, ""],
                      "presel_nVtx"      : ["nVtx"      , "presel_nVtx"      ,        [50,0,50], extraCuts, ""],
#                      "presel_nVtxup"   : ["nVtx"      , "presel_nVtxup"    ,        [50,0,50], extraCuts, "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*trigEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets])],
#                      "presel_nVtxdo"   : ["nVtx"      , "presel_nVtxdo"    ,        [50,0,50], extraCuts, "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*trigEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets])],
#                      "presel_nVtxNoPU" : ["nVtx"      , "presel_nVtxNoPU"  ,        [50,0,50], extraCuts, "%sevtWeight*muEffWeight*eleEffWeight*trigEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets])],
                      
                      "nVtx"             : ["nVtx"      , "nVtx"             ,   [50,-0.5,49.5], extraCuts, ""],
                      "nEle"             : ["nEle"      , "nEle"             ,     [4,-0.5,3.5], extraCuts, ""],
                      "elePt"            : ["elePt"     , "elePt"            ,     [200,20,220], extraCuts, ""],
                      "eleSCEta"         : ["eleSCEta"  , "eleSCEta"         ,    [50,-2.4,2.4], extraCuts, ""],
                      "elePhi"           : ["elePhi"    , "elePhi"           ,    [50,-3.2,3.2], extraCuts, ""],
                      "nMu"              : ["nMu"       , "nMu"              ,     [4,-0.5,3.5], extraCuts, ""],
                      "muPt"             : ["muPt"      , "muPt"             ,     [200,20,220], extraCuts, ""],
                      "muEta"            : ["muEta"     , "muEta"            ,    [50,-2.4,2.4], extraCuts, ""],
                      "muPhi"            : ["muPhi"     , "muPhi"            ,    [50,-3.2,3.2], extraCuts, ""],
                      "nJet"             : ["nJet"      , "nJet"             ,     [6, 1.5,7.5], extraCuts, ""],
                      "jetPt"            : ["jetPt"     , "jetPt"            ,     [200,20,220], extraCuts, ""],
                      "jetEta"           : ["jetEta"    , "jetEta"           ,    [50,-2.4,2.4], extraCuts, ""],
                      "jetPhi"           : ["jetPhi"    , "jetPhi"           ,    [50,-3.2,3.2], extraCuts, ""],
                      "nBJet"            : ["nBJet"     , "nBJet"             ,     [7,0.5,7.5], extraCuts, ""],
                      "bjetPt"           : ["jetPt"     , "bjetPt"           ,     [100,20,200], extraCuts+btagCut, ""],
                      "bjetEta"          : ["jetEta"    , "bjetEta"          ,    [50,-2.4,2.4], extraCuts+btagCut, ""],
                      "bjetPhi"          : ["jetPhi"    , "bjetPhi"          ,    [50,-3.2,3.2], extraCuts+btagCut, ""],
                      "rec_ptll"         : ["pt_ll"     , "rec_ptll"         ,     [220, 0,220], extraCuts, ""],
                      "rec_Mll"          : ["m_ll"      , "rec_Mll"          ,     [400,20,420], extraCuts, ""],
                      "rec_ptpos"        : ["pt_pos"    , "rec_ptpos"        ,     [200,20,220], extraCuts, ""],
                      "rec_Epos"         : ["E_pos"     , "rec_Epos"         ,     [300,20,320], extraCuts, ""],
                      "rec_ptp_ptm"      : ["ptp_ptm"   , "rec_ptp_ptm"      ,     [300,20,320], extraCuts, ""],
                      "rec_Ep_Em"        : ["Ep_Em"     , "rec_Ep_Em"        ,     [500,20,520], extraCuts, ""],
                      }
    return histogramInfo
