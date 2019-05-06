#ifndef SCALEFACTORS_H
#define SCALEFACTORS_H

/////////////////////////////////
// Total integrated luminosity //
/////////////////////////////////


double luminosity = 35862.4;
double lumiBF = 19716.2;
double lumiGH = 16146.2;

/////////////////////////////////////////////////
// Total number of events in the MC simulation //
/////////////////////////////////////////////////

double totalTTGamma_hadronic      = 4966371.;
double totalTTGamma_semilept_Tbar = 4836134.;
double totalTTGamma_semilept_T    = 4791766.;
double totalTTGamma_dilept        = 4907307.;

double totalTTGJets               = 3199101.; //9884993 Total before weights (6542047 +weights, 3342946 -weights)

double totalTGJets                = 310437.; //1556973 before negative weights

double totalTTbarMCatNLO          = 77227178.;

double totalTTbarMadgraph_SingleLeptFromT     = 11956689.;
double totalTTbarMadgraph_SingleLeptFromTbar  = 11943716.;
double totalTTbarMadgraph_Dilepton            = 6094300.;

double totalTTbarMadgraph         = 10139697.;

double totalWjetsInclusive   = 161142175.; // 235572523 Total before weights (198357349 +weights, 37215174 -weights)

double totalW1jets           = 45366416.;
double totalW2jets           = 30318880.;
double totalW3jets           = 39268750.;
double totalW4jets           = 18751100.;

double totalDYjetsM50       = 122053259.;
double totalDYjetsM10to50   = 71301217.;

double totalTTWtoQQ         = 833257.;
double totalTTWtoLNu        = 2160030.;
double totalTTZtoLL         = 5933898.;

double totalZGamma           = 11411341.; //Total 16679515 before negative weights 
double totalWGamma           = 17589398.; //Total 27426836 before negative weights

double totalWW               = 6987017.;
double totalWZ               = 2995783.;
double totalZZ               = 998018.;

double totalST_tchannel      = 67225849.;
double totalST_tbarchannel   = 38810350;
double totalST_schannel      = 2989123.;
double totalST_tW            = 6932903.;
double totalST_tbarW         = 6932903.;

double totalQCD_Pt20to30_Mu    = 31474692.;
double totalQCD_Pt30to50_Mu    = 29954322.;
double totalQCD_Pt50to80_Mu    = 19806515.;
double totalQCD_Pt80to120_Mu   = 13786651.;
double totalQCD_Pt120to170_Mu  =  8042452.;
double totalQCD_Pt170to300_Mu  =  7946703.;
double totalQCD_Pt300to470_Mu  =  7936465.;
double totalQCD_Pt470to600_Mu  =  3850452.;
double totalQCD_Pt600to800_Mu  =  4008200.;
double totalQCD_Pt800to1000_Mu =  3959757.;
double totalQCD_Pt1000toInf_Mu =  3985729.;
double totalQCD_Pt20to30_Ele   =  9218839.;
double totalQCD_Pt30to50_Ele   =  4730140.;
double totalQCD_Pt50to80_Ele   = 22336804.;
double totalQCD_Pt80to120_Ele  = 35841321.;
double totalQCD_Pt120to170_Ele = 35816734.;
double totalQCD_Pt170to300_Ele = 11539879.;
double totalQCD_Pt300toInf_Ele =  7373130.;

double totalGJets_HT40to100  = 4467939.;
double totalGJets_HT100to200 = 5131808.;
double totalGJets_HT200to400 = 9930766.;
double totalGJets_HT400to600 = 2529663.;
double totalGJets_HT600toInf = 2463751.;


// Top mass analysis
double totalTTbarPowheg   = 77078997.;   // Updated for mt analysis
double totalTTWJetsToLNu  = 1112646.;  // Positive: 1636338   Negative:  523692  Total:  2160030
double totalTTZToLLNuNu   = 927930.;   // Positive: 1460132   Negative:  532202  Total:  1992334
double totalWJetsToLNu    = 16496760.; // Positive: 20308358  Negative: 3811598  Total: 24119956 
double totalWJetsToLNu_LO = 29705372.;
double totalWWTo2L2Nu     = 1998956.; 
double totalWZTo3LNu      = 1993154.;
double totalZZTo2L2Nu     = 8842251.;
double totalST_s          = 622974.;  // Positive: 811475  Negative: 188501  Total: 999976
double totalST_t_top      = 67130469.;
double totalST_t_antitop  = 38736451.;
double totalST_tW_top     = 3256548.; 
double totalST_tW_antitop = 3256309.; 
double totalDY_M_10to50   = 35291236.; 
double totalDY_M_50       = 49143455.;

double totalTTGamma_dilept_fsrDown      = 3983729.;
double totalTTGamma_dilept_fsrUp        = 3926890.;
double totalTTGamma_dilept_isrDown      = 3886639.;
double totalTTGamma_dilept_isrUp        = 3940857.;

double totalTTGamma_semilept_T_fsrDown  = 4813819.;
double totalTTGamma_semilept_T_fsrUp    = 4985392.;
double totalTTGamma_semilept_T_isrDown  = 4966800.;
double totalTTGamma_semilept_T_isrUp    = 4922478.;

double totalTTGamma_semilept_Tbar_fsrDown = 4770115.;
double totalTTGamma_semilept_Tbar_fsrUp   = 4802977.;
double totalTTGamma_semilept_Tbar_isrDown = 4952386.;
double totalTTGamma_semilept_Tbar_isrUp   = 4838684.;




//// Top Mass systematics samples
double totalTTbar_mt1665 = 19379727.;
double totalTTbar_mt1695 = 58540996.;
double totalTTbar_mt1715 = 79484355.;
double totalTTbar_mt1735 = 79276800.; 
double totalTTbar_mt1755 = 59382995.;
double totalTTbar_mt1785 = 16376678.;

// alphaS
double totalTTbar_fsrDown = 155987323.;
double totalTTbar_fsrUp   = 152613640.;
double totalTTbar_isrDown = 120675570.;
double totalTTbar_isrUp   = 156465594.;

// ME-PS matching  hdamp
double totalTTbar_hdampUp   = 58856922.; 
double totalTTbar_hdampDown = 58162350.; 

// Underlying event
double totalTTbar_UEUp   = 58952087.; 
double totalTTbar_UEDown = 58336680.; 

// Color reconnection
double totalTTbar_CRerdON = 59880545.;
double totalTTbar_CRGluon = 56167431.;
double totalTTbar_CRQCD   = 59618551.; 

// Alternate generators      

double totalTTbar_amcanlo  = 15065312.;  // Positive: 29312822  Negative: 14247510  Total: 43560332
double totalTTbar_madgraph = 10139697.;
double totalTTbar_herwigpp = 59172906.;

// tt/tW interference DS
double totalST_tW_top_DS     = 3192538.;
double totalST_tW_antitop_DS = 3257226.; 


double totalST_tW_top_mt1695     = 3198907.;
double totalST_tW_top_mt1755     = 2958469.;
double totalST_tW_antitop_mt1695 = 3028484.;
double totalST_tW_antitop_mt1755 = 3253383.;

double totalST_tW_top_fsrUp       = 3212324.; 
double totalST_tW_top_fsrDown     = 2975323.; 
double totalST_tW_antitop_fsrUp   = 3001527.; 
double totalST_tW_antitop_fsrDown = 3234964.;

double totalST_tW_top_isrUp       = 3129727.; 
double totalST_tW_top_isrDown     = 3201563.; 
double totalST_tW_antitop_isrUp   = 3076275.; 
double totalST_tW_antitop_isrDown = 3101321.; 

double totalST_tW_top_Q2Up       = 3188665.; 
double totalST_tW_top_Q2Down     = 3051991.; 
double totalST_tW_antitop_Q2Up   = 1606961.; 
double totalST_tW_antitop_Q2Down = 1575142.; 

double totalST_tW_top_hdampUp       = 3124846.; 
double totalST_tW_top_hdampDown     = 3181559.; 
double totalST_tW_antitop_hdampUp   = 1628470.; 
double totalST_tW_antitop_hdampDown = 1628292.; 

//////////////////////////
// Cross Sections Used  //
//////////////////////////

// Theory TT xsec
//double TTbar_xs             =  831.76;  //ttbar NNLO (http://inspirehep.net/search?p=find+eprint+1112.5675)
//
//// TOP 17-007  AN-16-327
//double TTbar_mt1665_xs  = 982.; 
//double TTbar_mt1695_xs  = 903.; 
//double TTbar_mt1715_xs  = 855.;
//double TTbar_mt1735_xs  = 809.;
//double TTbar_mt1755_xs  = 767.;
//double TTbar_mt1785_xs  = 708.;

double TTbar_xs             =  803.; // TOP-17-001: Dilepton channel TT xsec measurement 

// Calculated from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO#Parametrisations 
// using NNPDF2.3 NNLO 5f central with sigma_ref = 803, a1 = -0.745047, a2 = 0.127417
double TTbar_mt1665_xs  = 949.; 
double TTbar_mt1695_xs  = 872.; 
double TTbar_mt1715_xs  = 825.;
double TTbar_mt1735_xs  = 781.;
double TTbar_mt1755_xs  = 740.;
double TTbar_mt1785_xs  = 682.;

double WJetsToLNu_xs = 61526.7;
double WWTo2L2Nu_xs = 12.178;
double WZTo3LNu_xs = 2.165;
double ZZTo2L2Nu_xs = 0.414;
double TTWJetsToLNu_xs = 0.2043;
double TTZToLLNuNu_xs = 0.253;
double ST_s_xs = 3.4;
double ST_t_top_xs = 136.02;
double ST_t_antitop_xs = 80.95;
double ST_tW_top_xs = 19.467;
double ST_tW_antitop_xs = 19.467;


double ST_tW_top_mt1695_xs = 20.4;
double ST_tW_antitop_mt1695_xs = 20.4;
double ST_tW_top_mt1755_xs = 18.6;
double ST_tW_antitop_mt1755_xs = 18.6;

double TTbar_dilepton_xs             =  87.315;
double TTbar_semilept_xs             =  182.175;
double TTbar_hadronic_xs             =  831.76-TTbar_dilepton_xs-2*TTbar_semilept_xs;

double TTGJets_xs               =  3.697; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#TT_X

double TGJets_xs                =  2.967;

double TTGamma_hadronic_xs  =  3.482;   //4.599;
double TTGamma_semilept_xs  =  5.017/2.;//4.499/2.;
double TTGamma_dilept_xs    =  1.679;   //0.899;

double WjetsInclusive_xs    = 61526.7; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#W_jets

double W1jets_xs            =  9493.0;
double W2jets_xs            =  3120.0;
double W3jets_xs            =  942.3;
double W4jets_xs            =  524.2;

double DYjetsM50_xs         =  5765.4; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
double DYjetsM10to50_xs     =  18610.; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns

double TTWtoQQ_xs               =  0.40620; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
double TTWtoLNu_xs              =  0.2043; //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
double TTZtoLL_xs               =  0.2728;  //????? https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns lists it as 0.2529

double ZGamma_xs            = 131.3; // ?????? https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns lists it as 117.864
double WGamma_xs            = 585.8; // ?????? https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns lists it as 489

double WW_xs                = 118.7;
double WZ_xs                = 47.13;
double ZZ_xs                = 16.523;  //https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns

double ST_tW_xs             =  35.85 ;
double ST_tbarW_xs          =  35.85 ;
double ST_tchannel_xs       =  136.02 ;
double ST_tbarchannel_xs    =  80.95 ;
double ST_schannel_xs       =  10.32;


//Product fo XS and filter eff from table at:
//https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
double QCD_Pt20to30_Mu_xs    = 2960198.4;
double QCD_Pt30to50_Mu_xs    = 1652471.46;
double QCD_Pt50to80_Mu_xs    =  437504.1;
double QCD_Pt80to120_Mu_xs   =  106033.6648;
double QCD_Pt120to170_Mu_xs  =   25190.5151;
double QCD_Pt170to300_Mu_xs  =    8654.4932;
double QCD_Pt300to470_Mu_xs  =     797.3527;
double QCD_Pt470to600_Mu_xs  =      79.0255;
double QCD_Pt600to800_Mu_xs  =      25.0951;
double QCD_Pt800to1000_Mu_xs =       4.7074;
double QCD_Pt1000toInf_Mu_xs =       1.6213;
double QCD_Pt20to30_Ele_xs   = 5352960.;
double QCD_Pt30to50_Ele_xs   = 9928000.;
double QCD_Pt50to80_Ele_xs   = 2890800.;
double QCD_Pt80to120_Ele_xs  =  350000.;
double QCD_Pt120to170_Ele_xs =   62964.;
double QCD_Pt170to300_Ele_xs =   18810.;
double QCD_Pt300toInf_Ele_xs =    1350.;

// GJets cross sections taken from AN2016_471_v6 (SUSY photon + MET analysis)
double GJets_HT40to100_xs  = 20790.;
double GJets_HT100to200_xs = 9238.;
double GJets_HT200to400_xs = 2305.;
double GJets_HT400to600_xs = 274.4;
double GJets_HT600toInf_xs = 93.46;

double TTGJets_SF               = TTGJets_xs * luminosity / totalTTGJets;

double TGJets_SF               = TGJets_xs * luminosity / totalTGJets;
double TTGamma_hadronic_SF = TTGamma_hadronic_xs * luminosity / totalTTGamma_hadronic;
double TTGamma_semilept_T_SF = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_T;
double TTGamma_semilept_Tbar_SF = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_Tbar;
double TTGamma_dilept_SF   = TTGamma_dilept_xs * luminosity / totalTTGamma_dilept;

double TTbarMCatNLO_SF = TTbar_xs * luminosity / totalTTbarMCatNLO;
double TTbarMadgraph_SF = TTbar_xs * luminosity / totalTTbarMadgraph;

double TTbarMadgraph_SingleLeptFromT_SF = TTbar_semilept_xs * luminosity / totalTTbarMadgraph_SingleLeptFromT;
double TTbarMadgraph_SingleLeptFromTbar_SF = TTbar_semilept_xs * luminosity / totalTTbarMadgraph_SingleLeptFromTbar;
double TTbarMadgraph_Dilepton_SF = TTbar_dilepton_xs * luminosity / totalTTbarMadgraph_Dilepton;

double WjetsInclusive_SF = WjetsInclusive_xs * luminosity / totalWjetsInclusive;

double W1jets_SF = W1jets_xs * luminosity / totalW1jets;
double W2jets_SF = W2jets_xs * luminosity / totalW2jets;
double W3jets_SF = W3jets_xs * luminosity / totalW3jets;
double W4jets_SF = W4jets_xs * luminosity / totalW4jets;

double DYjetsM10to50_SF = DYjetsM10to50_xs * luminosity / totalDYjetsM10to50;
double DYjetsM50_SF = DYjetsM50_xs * luminosity / totalDYjetsM50;

double TTWtoQQ_SF = TTWtoQQ_xs * luminosity / totalTTWtoQQ;
double TTWtoLNu_SF = TTWtoLNu_xs * luminosity / totalTTWtoLNu;
double TTZtoLL_SF = TTZtoLL_xs * luminosity / totalTTZtoLL;

double ZGamma_SF = ZGamma_xs * luminosity / totalZGamma;
double WGamma_SF = WGamma_xs * luminosity / totalWGamma;

double WW_SF = WW_xs * luminosity / totalWW;
double WZ_SF = WZ_xs * luminosity / totalWZ;
double ZZ_SF = ZZ_xs * luminosity / totalZZ;

double ST_tW_SF       = ST_tW_xs * luminosity / totalST_tW;
double ST_tbarW_SF    = ST_tbarW_xs * luminosity / totalST_tbarW;
double ST_tchannel_SF = ST_tchannel_xs * luminosity / totalST_tchannel;
double ST_tbarchannel_SF = ST_tbarchannel_xs * luminosity / totalST_tbarchannel;
double ST_schannel_SF = ST_schannel_xs * luminosity / totalST_schannel;

double QCD_Pt20to30_Mu_SF    = QCD_Pt20to30_Mu_xs    * luminosity / totalQCD_Pt20to30_Mu    ;
double QCD_Pt30to50_Mu_SF    = QCD_Pt30to50_Mu_xs    * luminosity / totalQCD_Pt30to50_Mu    ;
double QCD_Pt50to80_Mu_SF    = QCD_Pt50to80_Mu_xs    * luminosity / totalQCD_Pt50to80_Mu    ;
double QCD_Pt80to120_Mu_SF   = QCD_Pt80to120_Mu_xs   * luminosity / totalQCD_Pt80to120_Mu   ;
double QCD_Pt120to170_Mu_SF  = QCD_Pt120to170_Mu_xs  * luminosity / totalQCD_Pt120to170_Mu  ;
double QCD_Pt170to300_Mu_SF  = QCD_Pt170to300_Mu_xs  * luminosity / totalQCD_Pt170to300_Mu  ;
double QCD_Pt300to470_Mu_SF  = QCD_Pt300to470_Mu_xs  * luminosity / totalQCD_Pt300to470_Mu  ;
double QCD_Pt470to600_Mu_SF  = QCD_Pt470to600_Mu_xs  * luminosity / totalQCD_Pt470to600_Mu  ;
double QCD_Pt600to800_Mu_SF  = QCD_Pt600to800_Mu_xs  * luminosity / totalQCD_Pt600to800_Mu  ;
double QCD_Pt800to1000_Mu_SF = QCD_Pt800to1000_Mu_xs * luminosity / totalQCD_Pt800to1000_Mu ;
double QCD_Pt1000toInf_Mu_SF = QCD_Pt1000toInf_Mu_xs * luminosity / totalQCD_Pt1000toInf_Mu ;
double QCD_Pt20to30_Ele_SF   = QCD_Pt20to30_Ele_xs   * luminosity / totalQCD_Pt20to30_Ele   ;
double QCD_Pt30to50_Ele_SF   = QCD_Pt30to50_Ele_xs   * luminosity / totalQCD_Pt30to50_Ele   ;
double QCD_Pt50to80_Ele_SF   = QCD_Pt50to80_Ele_xs   * luminosity / totalQCD_Pt50to80_Ele   ;
double QCD_Pt80to120_Ele_SF  = QCD_Pt80to120_Ele_xs  * luminosity / totalQCD_Pt80to120_Ele  ;
double QCD_Pt120to170_Ele_SF = QCD_Pt120to170_Ele_xs * luminosity / totalQCD_Pt120to170_Ele ;
double QCD_Pt170to300_Ele_SF = QCD_Pt170to300_Ele_xs * luminosity / totalQCD_Pt170to300_Ele ;
double QCD_Pt300toInf_Ele_SF = QCD_Pt300toInf_Ele_xs * luminosity / totalQCD_Pt300toInf_Ele ;

double GJets_HT40to100_SF  = GJets_HT40to100_xs  * luminosity / totalGJets_HT40to100  ;
double GJets_HT100to200_SF = GJets_HT100to200_xs * luminosity / totalGJets_HT100to200 ;
double GJets_HT200to400_SF = GJets_HT200to400_xs * luminosity / totalGJets_HT200to400 ;
double GJets_HT400to600_SF = GJets_HT400to600_xs * luminosity / totalGJets_HT400to600 ;
double GJets_HT600toInf_SF = GJets_HT600toInf_xs * luminosity / totalGJets_HT600toInf ;

double TTGamma_dilept_fsrDown_SF   = TTGamma_dilept_xs * luminosity / totalTTGamma_dilept_fsrDown;
double TTGamma_dilept_fsrUp_SF     = TTGamma_dilept_xs * luminosity / totalTTGamma_dilept_fsrUp;
double TTGamma_dilept_isrDown_SF   = TTGamma_dilept_xs * luminosity / totalTTGamma_dilept_isrDown;
double TTGamma_dilept_isrUp_SF     = TTGamma_dilept_xs * luminosity / totalTTGamma_dilept_isrUp;

double TTGamma_semilept_T_fsrDown_SF = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_T_fsrDown;
double TTGamma_semilept_T_fsrUp_SF   = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_T_fsrUp;
double TTGamma_semilept_T_isrDown_SF = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_T_isrDown;
double TTGamma_semilept_T_isrUp_SF   = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_T_isrUp;

double TTGamma_semilept_Tbar_fsrDown_SF = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_Tbar_fsrDown;
double TTGamma_semilept_Tbar_fsrUp_SF   = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_Tbar_fsrUp;
double TTGamma_semilept_Tbar_isrDown_SF = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_Tbar_isrDown;
double TTGamma_semilept_Tbar_isrUp_SF   = TTGamma_semilept_xs * luminosity / totalTTGamma_semilept_Tbar_isrUp;

// Top mass analysis
double TTbarPowheg_SF = TTbar_xs * luminosity / totalTTbarPowheg;
double TTbar_mt1665_SF = TTbar_mt1665_xs * luminosity / totalTTbar_mt1665;
double TTbar_mt1695_SF = TTbar_mt1695_xs * luminosity / totalTTbar_mt1695;
double TTbar_mt1715_SF = TTbar_mt1715_xs * luminosity / totalTTbar_mt1715;
double TTbar_mt1735_SF = TTbar_mt1735_xs * luminosity / totalTTbar_mt1735;
double TTbar_mt1755_SF = TTbar_mt1755_xs * luminosity / totalTTbar_mt1755;
double TTbar_mt1785_SF = TTbar_mt1785_xs * luminosity / totalTTbar_mt1785;

double TTbar_fsrDown_SF = TTbar_xs  * luminosity / totalTTbar_fsrDown;
double TTbar_fsrUp_SF = TTbar_xs  * luminosity / totalTTbar_fsrUp;
double TTbar_isrDown_SF = TTbar_xs  * luminosity / totalTTbar_isrDown;
double TTbar_isrUp_SF = TTbar_xs  * luminosity / totalTTbar_isrUp;

double TTbar_UEUp_SF = TTbar_xs  * luminosity / totalTTbar_UEUp;
double TTbar_UEDown_SF = TTbar_xs  * luminosity / totalTTbar_UEDown;

double TTbar_hdampUp_SF = TTbar_xs  * luminosity / totalTTbar_hdampUp;
double TTbar_hdampDown_SF = TTbar_xs  * luminosity / totalTTbar_hdampDown;

double TTbar_CRerdON_SF = TTbar_xs  * luminosity / totalTTbar_CRerdON;
double TTbar_CRGluon_SF = TTbar_xs  * luminosity / totalTTbar_CRGluon;
double TTbar_CRQCD_SF = TTbar_xs  * luminosity / totalTTbar_CRQCD;

double TTbar_amcanlo_SF = TTbar_xs  * luminosity / totalTTbar_amcanlo;
double TTbar_madgraph_SF = TTbar_xs  * luminosity / totalTTbar_madgraph;
double TTbar_herwigpp_SF = TTbar_xs  * luminosity / totalTTbar_herwigpp;


double WJetsToLNu_SF = WJetsToLNu_xs * luminosity / totalWJetsToLNu;
double WJetsToLNu_LO_SF = WJetsToLNu_xs * luminosity / totalWJetsToLNu_LO;
double WWTo2L2Nu_SF = WWTo2L2Nu_xs * luminosity / totalWWTo2L2Nu;
double WZTo3LNu_SF = WZTo3LNu_xs * luminosity / totalWZTo3LNu;
double ZZTo2L2Nu_SF = ZZTo2L2Nu_xs * luminosity / totalZZTo2L2Nu;
double TTWJetsToLNu_SF = TTWJetsToLNu_xs * luminosity / totalTTWJetsToLNu;
double TTZToLLNuNu_SF = TTZToLLNuNu_xs * luminosity / totalTTZToLLNuNu;
double ST_s_SF = ST_s_xs * luminosity / totalST_s;
double ST_t_top_SF = ST_t_top_xs * luminosity / totalST_t_top;
double ST_t_antitop_SF = ST_t_antitop_xs * luminosity / totalST_t_antitop;
double DY_M_10to50_SF = DYjetsM10to50_xs * luminosity / totalDY_M_10to50;
double DY_M_50_SF = DYjetsM50_xs * luminosity / totalDY_M_50;

double ST_tW_top_SF = ST_tW_top_xs * luminosity / totalST_tW_top;
double ST_tW_antitop_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop;

double ST_tW_top_DS_SF = ST_tW_top_xs * luminosity / totalST_tW_top_DS;
double ST_tW_antitop_DS_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_DS;

double ST_tW_top_mt1695_SF = ST_tW_top_mt1695_xs * luminosity / totalST_tW_top_mt1695;
double ST_tW_top_mt1755_SF = ST_tW_top_mt1755_xs * luminosity / totalST_tW_top_mt1755;
double ST_tW_antitop_mt1695_SF = ST_tW_antitop_mt1695_xs * luminosity / totalST_tW_antitop_mt1695;
double ST_tW_antitop_mt1755_SF = ST_tW_antitop_mt1755_xs * luminosity / totalST_tW_antitop_mt1755;

double ST_tW_top_fsrUp_SF = ST_tW_top_xs * luminosity / totalST_tW_top_fsrUp;
double ST_tW_top_fsrDown_SF = ST_tW_top_xs * luminosity / totalST_tW_top_fsrDown;
double ST_tW_antitop_fsrUp_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_fsrUp;
double ST_tW_antitop_fsrDown_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_fsrDown;
double ST_tW_top_isrUp_SF = ST_tW_top_xs * luminosity / totalST_tW_top_isrUp;
double ST_tW_top_isrDown_SF = ST_tW_top_xs * luminosity / totalST_tW_top_isrDown;
double ST_tW_antitop_isrUp_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_isrUp;
double ST_tW_antitop_isrDown_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_isrDown;

double ST_tW_top_Q2Up_SF = ST_tW_top_xs * luminosity / totalST_tW_top_Q2Up;
double ST_tW_top_Q2Down_SF = ST_tW_top_xs * luminosity / totalST_tW_top_Q2Down;
double ST_tW_antitop_Q2Up_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_Q2Up;
double ST_tW_antitop_Q2Down_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_Q2Down;
double ST_tW_top_hdampUp_SF = ST_tW_top_xs * luminosity / totalST_tW_top_hdampUp;
double ST_tW_top_hdampDown_SF = ST_tW_top_xs * luminosity / totalST_tW_top_hdampDown;
double ST_tW_antitop_hdampUp_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_hdampUp;
double ST_tW_antitop_hdampDown_SF = ST_tW_antitop_xs * luminosity / totalST_tW_antitop_hdampDown;


double getEvtWeight(string sampleType){
	double evtWeight = -1.;
	if( sampleType.substr(0,4)=="Data") {evtWeight = 1.;}
	else if( sampleType=="Test") {evtWeight = 1.;}
	else if( sampleType=="TestAll") {evtWeight = 1.;}
    else if( sampleType=="TTbar_mt1665") {evtWeight = TTbar_mt1665_SF;}
    else if( sampleType=="TTbar_mt1695_1") {evtWeight = TTbar_mt1695_SF;}
    else if( sampleType=="TTbar_mt1695_2") {evtWeight = TTbar_mt1695_SF;}
    else if( sampleType=="TTbar_mt1695_3") {evtWeight = TTbar_mt1695_SF;}
    else if( sampleType=="TTbar_mt1715_1") {evtWeight = TTbar_mt1715_SF;}
    else if( sampleType=="TTbar_mt1715_2") {evtWeight = TTbar_mt1715_SF;}
    else if( sampleType=="TTbar_mt1735_1") {evtWeight = TTbar_mt1735_SF;}
    else if( sampleType=="TTbar_mt1735_2") {evtWeight = TTbar_mt1735_SF;}
    else if( sampleType=="TTbar_mt1755_1") {evtWeight = TTbar_mt1755_SF;}
    else if( sampleType=="TTbar_mt1755_2") {evtWeight = TTbar_mt1755_SF;}
    else if( sampleType=="TTbar_mt1755_3") {evtWeight = TTbar_mt1755_SF;}
    else if( sampleType=="TTbar_mt1785") {evtWeight = TTbar_mt1785_SF;}
	else if( sampleType=="TTbar_fsrDown_1") {evtWeight = TTbar_fsrDown_SF;}
	else if( sampleType=="TTbar_fsrDown_2") {evtWeight = TTbar_fsrDown_SF;}
	else if( sampleType=="TTbar_fsrDown_3") {evtWeight = TTbar_fsrDown_SF;}
	else if( sampleType=="TTbar_fsrUp_1") {evtWeight = TTbar_fsrUp_SF;}
	else if( sampleType=="TTbar_fsrUp_2") {evtWeight = TTbar_fsrUp_SF;}
	else if( sampleType=="TTbar_fsrUp_3") {evtWeight = TTbar_fsrUp_SF;}
	else if( sampleType=="TTbar_isrDown_1") {evtWeight = TTbar_isrDown_SF;}
	else if( sampleType=="TTbar_isrDown_2") {evtWeight = TTbar_isrDown_SF;}
	else if( sampleType=="TTbar_isrUp_1") {evtWeight = TTbar_isrUp_SF;}
	else if( sampleType=="TTbar_isrUp_2") {evtWeight = TTbar_isrUp_SF;}
	else if( sampleType=="TTbar_isrUp_3") {evtWeight = TTbar_isrUp_SF;}
	else if( sampleType=="TTbar_hdampUp_1") {evtWeight = TTbar_hdampUp_SF;}
	else if( sampleType=="TTbar_hdampUp_2") {evtWeight = TTbar_hdampUp_SF;}
	else if( sampleType=="TTbar_hdampDown_1") {evtWeight = TTbar_hdampDown_SF;}
	else if( sampleType=="TTbar_hdampDown_2") {evtWeight = TTbar_hdampDown_SF;}
	else if( sampleType=="TTbar_UEUp_1") {evtWeight = TTbar_UEUp_SF;}
	else if( sampleType=="TTbar_UEUp_2") {evtWeight = TTbar_UEUp_SF;}
	else if( sampleType=="TTbar_UEDown_1") {evtWeight = TTbar_UEDown_SF;}
	else if( sampleType=="TTbar_UEDown_2") {evtWeight = TTbar_UEDown_SF;}
	else if( sampleType=="TTbar_CRerdON_1") {evtWeight = TTbar_CRerdON_SF;}
	else if( sampleType=="TTbar_CRerdON_2") {evtWeight = TTbar_CRerdON_SF;}
	else if( sampleType=="TTbar_CRGluon") {evtWeight = TTbar_CRGluon_SF;}
	else if( sampleType=="TTbar_CRQCD_1") {evtWeight = TTbar_CRQCD_SF;}
	else if( sampleType=="TTbar_CRQCD_2") {evtWeight = TTbar_CRQCD_SF;}
	else if( sampleType=="TTbar_amcanlo") {evtWeight = TTbar_amcanlo_SF;}
	else if( sampleType=="TTbar_madgraph") {evtWeight = TTbar_madgraph_SF;}
	else if( sampleType=="TTbar_herwigpp_1") {evtWeight = TTbar_herwigpp_SF;}
	else if( sampleType=="TTbar_herwigpp_2") {evtWeight = TTbar_herwigpp_SF;}
	else if( sampleType=="TTbar_herwigpp_3") {evtWeight = TTbar_herwigpp_SF;}
    else if( sampleType=="WJetsToLNu"){evtWeight = WJetsToLNu_SF;} 
    else if( sampleType=="WJetsToLNu_LO"){evtWeight = WJetsToLNu_LO_SF;} 
    else if( sampleType=="WWTo2L2Nu"){evtWeight = WWTo2L2Nu_SF;} 
    else if( sampleType=="WZTo3LNu"){evtWeight = WZTo3LNu_SF;} 
    else if( sampleType=="ZZTo2L2Nu"){evtWeight = ZZTo2L2Nu_SF;} 
    else if( sampleType=="TTWJetsToLNu"){evtWeight = TTWJetsToLNu_SF;} 
    else if( sampleType=="TTZToLLNuNu"){evtWeight = TTZToLLNuNu_SF;}
    else if( sampleType=="ST_s"){evtWeight = ST_s_SF;} 
    else if( sampleType=="ST_t_top"){evtWeight = ST_t_top_SF;} 
    else if( sampleType=="ST_t_antitop"){evtWeight = ST_t_antitop_SF;} 
    else if( sampleType=="DY_M_10to50"){evtWeight = DY_M_10to50_SF;} 
    else if( sampleType=="DY_M_50"){evtWeight = DY_M_50_SF;} 
    else if( sampleType=="ST_tW_top"){evtWeight = ST_tW_top_SF;} 
    else if( sampleType=="ST_tW_antitop"){evtWeight = ST_tW_antitop_SF;} 
    else if( sampleType=="ST_tW_top_mt1695"){evtWeight = ST_tW_top_mt1695_SF;} 
    else if( sampleType=="ST_tW_top_mt1755"){evtWeight = ST_tW_top_mt1755_SF;} 
    else if( sampleType=="ST_tW_antitop_mt1695"){evtWeight = ST_tW_antitop_mt1695_SF;} 
    else if( sampleType=="ST_tW_antitop_mt1755"){evtWeight = ST_tW_antitop_mt1755_SF;} 
    else if( sampleType=="ST_tW_top_fsrUp"){evtWeight = ST_tW_top_fsrUp_SF;} 
    else if( sampleType=="ST_tW_top_fsrDown"){evtWeight = ST_tW_top_fsrDown_SF;} 
    else if( sampleType=="ST_tW_antitop_fsrUp"){evtWeight = ST_tW_antitop_fsrUp_SF;} 
    else if( sampleType=="ST_tW_antitop_fsrDown"){evtWeight = ST_tW_antitop_fsrDown_SF;} 
    else if( sampleType=="ST_tW_top_isrUp"){evtWeight = ST_tW_top_isrUp_SF;} 
    else if( sampleType=="ST_tW_top_isrDown"){evtWeight = ST_tW_top_isrDown_SF;} 
    else if( sampleType=="ST_tW_antitop_isrUp"){evtWeight = ST_tW_antitop_isrUp_SF;} 
    else if( sampleType=="ST_tW_antitop_isrDown"){evtWeight = ST_tW_antitop_isrDown_SF;} 
    else if( sampleType=="ST_tW_top_DS"){evtWeight = ST_tW_top_DS_SF;} 
    else if( sampleType=="ST_tW_antitop_DS"){evtWeight = ST_tW_antitop_DS_SF;} 
    else if( sampleType=="ST_tW_top_Q2Up"){evtWeight = ST_tW_top_Q2Up_SF;} 
    else if( sampleType=="ST_tW_top_Q2Down"){evtWeight = ST_tW_top_Q2Down_SF;} 
    else if( sampleType=="ST_tW_antitop_Q2Up"){evtWeight = ST_tW_antitop_Q2Up_SF;} 
    else if( sampleType=="ST_tW_antitop_Q2Down"){evtWeight = ST_tW_antitop_Q2Down_SF;} 
    else if( sampleType=="ST_tW_top_hdampUp"){evtWeight = ST_tW_top_hdampUp_SF;} 
    else if( sampleType=="ST_tW_top_hdampDown"){evtWeight = ST_tW_top_hdampDown_SF;} 
    else if( sampleType=="ST_tW_antitop_hdampUp"){evtWeight = ST_tW_antitop_hdampUp_SF;} 
    else if( sampleType=="ST_tW_antitop_hdampDown"){evtWeight = ST_tW_antitop_hdampDown_SF;} 
    else if( sampleType=="TGJets"){evtWeight = TGJets_SF;} 
	else if( sampleType=="TTGJets"){evtWeight = TTGJets_SF;} 
	else if( sampleType=="TTGamma_Hadronic") {evtWeight = TTGamma_hadronic_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromTbar") {evtWeight = TTGamma_semilept_Tbar_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromT") {evtWeight = TTGamma_semilept_T_SF;}
	else if( sampleType=="TTGamma_Dilepton") {evtWeight = TTGamma_dilept_SF;}
	else if( sampleType=="TTbar") {evtWeight = TTbarPowheg_SF;}
	else if( sampleType=="TTbarPowheg") {evtWeight = TTbarPowheg_SF;}
	else if( sampleType=="TTbarPowheg1") {evtWeight = TTbarPowheg_SF;}
	else if( sampleType=="TTbarPowheg2") {evtWeight = TTbarPowheg_SF;}
	else if( sampleType=="TTbarPowheg3") {evtWeight = TTbarPowheg_SF;}
	else if( sampleType=="TTbarPowheg4") {evtWeight = TTbarPowheg_SF;}
	else if( sampleType=="TTbarMCatNLO") {evtWeight = TTbarMCatNLO_SF;}
	else if( sampleType=="TTbarMadgraph") {evtWeight = TTbarMadgraph_SF;}
	else if( sampleType=="TTbarMadgraph_Dilepton") {evtWeight = TTbarMadgraph_Dilepton_SF;}
	else if( sampleType=="TTbarMadgraph_SingleLeptFromT") {evtWeight = TTbarMadgraph_SingleLeptFromT_SF;}
	else if( sampleType=="TTbarMadgraph_SingleLeptFromTbar") {evtWeight = TTbarMadgraph_SingleLeptFromTbar_SF;}
	else if( sampleType=="WjetsInclusive") {evtWeight = WjetsInclusive_SF;}
	else if( sampleType=="WjetsInclusive1") {evtWeight = WjetsInclusive_SF;}
	else if( sampleType=="WjetsInclusive2") {evtWeight = WjetsInclusive_SF;}
	else if( sampleType=="WjetsInclusive3") {evtWeight = WjetsInclusive_SF;}
	else if( sampleType=="WjetsInclusive4") {evtWeight = WjetsInclusive_SF;}
	else if( sampleType=="WjetsInclusive5") {evtWeight = WjetsInclusive_SF;}
	else if( sampleType=="WjetsInclusive6") {evtWeight = WjetsInclusive_SF;}
	else if( sampleType=="W1jets") {evtWeight = W1jets_SF;}
	else if( sampleType=="W2jets") {evtWeight = W2jets_SF;}
	else if( sampleType=="W3jets") {evtWeight = W3jets_SF;}
	else if( sampleType=="W4jets") {evtWeight = W4jets_SF;}
	else if( sampleType=="DYjetsM10to50") {evtWeight = DYjetsM10to50_SF;}
	else if( sampleType=="DYjetsM50") {evtWeight = DYjetsM50_SF;}
	else if( sampleType=="TTWtoQQ") {evtWeight = TTWtoLNu_SF;}
	else if( sampleType=="TTWtoLNu") {evtWeight = TTWtoLNu_SF;}
	else if( sampleType=="TTZtoLL") {evtWeight = TTZtoLL_SF;}
	else if( sampleType=="ZGamma") {evtWeight = ZGamma_SF;}
	else if( sampleType=="WGamma") {evtWeight = WGamma_SF;}
	else if( sampleType=="WW") {evtWeight = WW_SF;}
	else if( sampleType=="WZ") {evtWeight = WZ_SF;}
	else if( sampleType=="ZZ") {evtWeight = ZZ_SF;}
	else if( sampleType=="ST_tW-channel") {evtWeight = ST_tW_SF;}
	else if( sampleType=="ST_tbarW-channel") {evtWeight = ST_tbarW_SF;}
	else if( sampleType=="ST_t-channel") {evtWeight = ST_tchannel_SF;}
	else if( sampleType=="ST_tbar-channel") {evtWeight = ST_tbarchannel_SF;}
	else if( sampleType=="ST_s-channel") {evtWeight = ST_schannel_SF;}
	else if( sampleType=="QCD_Pt20to30_Mu") {evtWeight = QCD_Pt20to30_Mu_SF;}
	else if( sampleType=="QCD_Pt30to50_Mu") {evtWeight = QCD_Pt30to50_Mu_SF;}
	else if( sampleType=="QCD_Pt50to80_Mu") {evtWeight = QCD_Pt50to80_Mu_SF;}
	else if( sampleType=="QCD_Pt80to120_Mu") {evtWeight = QCD_Pt80to120_Mu_SF;}
	else if( sampleType=="QCD_Pt120to170_Mu") {evtWeight = QCD_Pt120to170_Mu_SF;}
	else if( sampleType=="QCD_Pt170to300_Mu") {evtWeight = QCD_Pt170to300_Mu_SF;}
	else if( sampleType=="QCD_Pt300to470_Mu") {evtWeight = QCD_Pt300to470_Mu_SF;}
	else if( sampleType=="QCD_Pt470to600_Mu") {evtWeight = QCD_Pt470to600_Mu_SF;}
	else if( sampleType=="QCD_Pt600to800_Mu") {evtWeight = QCD_Pt600to800_Mu_SF;}
	else if( sampleType=="QCD_Pt800to1000_Mu") {evtWeight = QCD_Pt800to1000_Mu_SF;}
	else if( sampleType=="QCD_Pt1000toInf_Mu") {evtWeight = QCD_Pt1000toInf_Mu_SF;}
	else if( sampleType=="QCD_Pt20to30_Ele") {evtWeight = QCD_Pt20to30_Ele_SF;}
	else if( sampleType=="QCD_Pt30to50_Ele") {evtWeight = QCD_Pt30to50_Ele_SF;}
	else if( sampleType=="QCD_Pt50to80_Ele") {evtWeight = QCD_Pt50to80_Ele_SF;}
	else if( sampleType=="QCD_Pt80to120_Ele") {evtWeight = QCD_Pt80to120_Ele_SF;}
	else if( sampleType=="QCD_Pt120to170_Ele") {evtWeight = QCD_Pt120to170_Ele_SF;}
	else if( sampleType=="QCD_Pt170to300_Ele") {evtWeight = QCD_Pt170to300_Ele_SF;}
	else if( sampleType=="QCD_Pt300toInf_Ele") {evtWeight = QCD_Pt300toInf_Ele_SF;}
	else if( sampleType=="GJets_HT-40To100")  {evtWeight = GJets_HT40to100_SF;}
	else if( sampleType=="GJets_HT-100To200") {evtWeight = GJets_HT100to200_SF;}
	else if( sampleType=="GJets_HT-200To400") {evtWeight = GJets_HT200to400_SF;}
	else if( sampleType=="GJets_HT-400To600") {evtWeight = GJets_HT400to600_SF;}
	else if( sampleType=="GJets_HT-600ToInf") {evtWeight = GJets_HT600toInf_SF;}

	else if( sampleType=="TTGamma_Dilepton_fsrDown") {evtWeight = TTGamma_dilept_fsrDown_SF;}
	else if( sampleType=="TTGamma_Dilepton_fsrUp")   {evtWeight = TTGamma_dilept_fsrUp_SF;}
	else if( sampleType=="TTGamma_Dilepton_isrDown") {evtWeight = TTGamma_dilept_isrDown_SF;}
	else if( sampleType=="TTGamma_Dilepton_isrUp")   {evtWeight = TTGamma_dilept_isrUp_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromT_fsrDown") {evtWeight = TTGamma_semilept_T_fsrDown_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromT_fsrUp")   {evtWeight = TTGamma_semilept_T_fsrUp_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromT_isrDown") {evtWeight = TTGamma_semilept_T_isrDown_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromT_isrUp")   {evtWeight = TTGamma_semilept_T_isrUp_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromTbar_fsrDown") {evtWeight = TTGamma_semilept_Tbar_fsrDown_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromTbar_fsrUp")   {evtWeight = TTGamma_semilept_Tbar_fsrUp_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromTbar_isrDown") {evtWeight = TTGamma_semilept_Tbar_isrDown_SF;}
	else if( sampleType=="TTGamma_SingleLeptFromTbar_isrUp")   {evtWeight = TTGamma_semilept_Tbar_isrUp_SF;}
	else {
		cout << "-------------------------------------------------" << endl;
		cout << "-------------------------------------------------" << endl;
		cout << "-- Unable to find event weight for this sample --" << endl;
		cout << "-- Sample will be saved with a weight of -1    --" << endl;
		cout << "-------------------------------------------------" << endl;
		cout << "-------------------------------------------------" << endl;
	}

	cout << "Using event weight " << evtWeight << endl;

	return evtWeight;
}











const std::string allowedSampleTypes[199] = {"Data",
											"Data_MuEG2016B",
                                            "Data_MuEG2016C",
                                            "Data_MuEG2016D",
                                            "Data_MuEG2016E",
                                            "Data_MuEG2016F_1",
                                            "Data_MuEG2016F_2",
                                            "Data_MuEG2016G",
                                            "Data_MuEG2016H_1",
                                            "Data_MuEG2016H_2",
                                            "TTbar_mt1665",
                                            "TTbar_mt1695_1",
                                            "TTbar_mt1695_2",
                                            "TTbar_mt1695_3",
                                            "TTbar_mt1715_1",
                                            "TTbar_mt1715_2",
                                            "TTbar_mt1735_1",
                                            "TTbar_mt1735_2",
                                            "TTbar_mt1755_1",
                                            "TTbar_mt1755_2",
                                            "TTbar_mt1755_3",
                                            "TTbar_mt1785",
                                            "TTbar_fsrDown_1",
                                            "TTbar_fsrDown_2",
                                            "TTbar_fsrDown_3",
                                            "TTbar_fsrUp_1",
                                            "TTbar_fsrUp_2",
                                            "TTbar_fsrUp_3",
                                            "TTbar_isrDown_1",
                                            "TTbar_isrDown_2",
                                            "TTbar_isrUp_1",
                                            "TTbar_isrUp_2",
                                            "TTbar_isrUp_3",
                                            "TTbar_hdampUp_1",
                                            "TTbar_hdampUp_2",
                                            "TTbar_hdampDown_1",
                                            "TTbar_hdampDown_2",
                                            "TTbar_UEUp_1",
                                            "TTbar_UEUp_2",
                                            "TTbar_UEDown_1",
                                            "TTbar_UEDown_2",
                                            "TTbar_CRerdON_1",
                                            "TTbar_CRerdON_2",
                                            "TTbar_CRGluon",
                                            "TTbar_CRQCD_1",
                                            "TTbar_CRQCD_2",
                                            "TTbar_amcanlo",
                                            "TTbar_madgraph",
                                            "TTbar_herwigpp_1",
                                            "TTbar_herwigpp_2",
                                            "TTbar_herwigpp_3",
                                            "WJetsToLNu",
                                            "WJetsToLNu_LO",
                                            "WWTo2L2Nu",
                                            "WZTo3LNu",
                                            "ZZTo2L2Nu",
                                            "TTWJetsToLNu",
                                            "TTZToLLNuNu",
                                            "ST_s",
                                            "ST_t_top",
                                            "ST_t_antitop",
                                            "DY_M_10to50",
                                            "DY_M_50",
                                            "ST_tW_top",
                                            "ST_tW_antitop",
                                            "ST_tW_top_DS",
                                            "ST_tW_antitop_DS",
                                            "ST_tW_top_mt1695",
                                            "ST_tW_top_mt1755",
                                            "ST_tW_antitop_mt1695",
                                            "ST_tW_antitop_mt1755",
                                            "ST_tW_top_fsrUp",
                                            "ST_tW_top_fsrDown",
                                            "ST_tW_top_isrUp",
                                            "ST_tW_top_isrDown",
                                            "ST_tW_antitop_fsrUp",
                                            "ST_tW_antitop_fsrDown",
                                            "ST_tW_antitop_isrUp",
                                            "ST_tW_antitop_isrDown",
                                            "ST_tW_top_Q2Up",
                                            "ST_tW_top_Q2Down",
                                            "ST_tW_top_hdampUp",
                                            "ST_tW_top_hdampDown",
                                            "ST_tW_antitop_Q2Up",
                                            "ST_tW_antitop_Q2Down",
                                            "ST_tW_antitop_hdampUp",
                                            "ST_tW_antitop_hdampDown",
                                            "Data_SingleMu_b",
											"Data_SingleMu_c",
											"Data_SingleMu_d",
											"Data_SingleMu_e",
											"Data_SingleMu_f",
											"Data_SingleMu_g",
											"Data_SingleMu_h",
											"Data_SingleEle_b",
											"Data_SingleEle_c",
											"Data_SingleEle_d",
											"Data_SingleEle_e",
											"Data_SingleEle_f",
											"Data_SingleEle_g",
											"Data_SingleEle_h",
											"TTGamma_Hadronic",
											"TTGamma_SingleLeptFromTbar",
											"TTGamma_SingleLeptFromT",
											"TTGamma_Dilepton",
											"TTbar",
											"TTbarPowheg",
											"TTbarPowheg1",
											"TTbarPowheg2",
											"TTbarPowheg3",
											"TTbarPowheg4",
											"TTbarMCatNLO",
											"TTbarMadgraph",
											"TTbarMadgraph_SingleLeptFromTbar",
											"TTbarMadgraph_SingleLeptFromT",
											"TTbarMadgraph_Dilepton",
											"WjetsInclusive",
											"WjetsInclusive1",
											"WjetsInclusive2",
											"WjetsInclusive3",
											"WjetsInclusive4",
											"WjetsInclusive5",
											"WjetsInclusive6",
											"W1jets",
											"W2jets",
											"W3jets",
											"W4jets",
											"DYjetsM10to50",
											"DYjetsM50",
											"TTWtoQQ",
											"TTWtoLNu",
											"TTZtoLL",
											"ZGamma",
											"WGamma",
											"WW",
											"WZ",
											"ZZ",
											"ST_tW-channel",
											"ST_tbarW-channel",
											"ST_t-channel",
											"ST_tbar-channel",
											"ST_s-channel",
											"QCD_Pt20to30_Mu",
											"QCD_Pt30to50_Mu",
											"QCD_Pt50to80_Mu",
											"QCD_Pt80to120_Mu",
											"QCD_Pt120to170_Mu",
											"QCD_Pt170to300_Mu",
											"QCD_Pt300to470_Mu",
											"QCD_Pt470to600_Mu",
											"QCD_Pt600to800_Mu",
											"QCD_Pt800to1000_Mu",
											"QCD_Pt1000toInf_Mu",
											"QCD_Pt20to30_Ele",
											"QCD_Pt30to50_Ele",
											"QCD_Pt50to80_Ele",
											"QCD_Pt80to120_Ele",
											"QCD_Pt120to170_Ele",
											"QCD_Pt170to300_Ele",
											"QCD_Pt300toInf_Ele",
											"GJets_HT-40To100",
											"GJets_HT-100To200",
											"GJets_HT-200To400",
											"GJets_HT-400To600",
											"GJets_HT-600ToInf",
											"TGJets",
											"TTGJets",
											"TTGamma_SingleLeptFromTbar_isrUp",
											"TTGamma_SingleLeptFromT_isrUp",
											"TTGamma_Dilepton_isrUp",
											"TTGamma_SingleLeptFromTbar_isrDown",
											"TTGamma_SingleLeptFromT_isrDown",
											"TTGamma_Dilepton_isrDown",
											"TTGamma_SingleLeptFromTbar_fsrUp",
											"TTGamma_SingleLeptFromT_fsrUp",
											"TTGamma_Dilepton_fsrUp",
											"TTGamma_SingleLeptFromTbar_fsrDown",
											"TTGamma_SingleLeptFromT_fsrDown",
											"TTGamma_Dilepton_fsrDown",
											"TestAll",
											"Test",
                                                                                        };

#endif
