from typing import List

names_list: List[str] = ["AccountType,"
"UN_AddressFormat,"
"AddressFormat,"
"AddressType,"
"Allowance,"
"IdentificationCode,"
"CountrySubentityCode,"
"CurrencyCode,"
"LifeCycle,"
"LineStatus,"
"LossRisk,"
"PaymentChannel,"
"PriceType,"
"Response,"
"TaxExemption,"
"TaxType,"
"TaxType2,"
"PaymentID,"
"ProfileID,"
]
codelist_list: List[List[str]]= [["1,""2,""3,"],
["1,""2,""3,""4,""5,""6,""7,""8,""9,"],
["StructuredDK,""StructuredID,""StructuredLax,""StructuredRegion,""Unstructured,"],
["Home,""Business,"],
["1,""2,""3,""4,""5,""6,""7,""8,""9,""10,""11,""12,""13,""14,""15,""16,""17,""18,""19,""20,""21,""22,""23,""24,""25,""26,""27,""28,""29,""30,""31,""32,""33,""34,""35,""36,""37,""38,""39,""40,""41,""42,""43,""44,""45,""46,""47,""48,""49,""50,""51,""52,""53,""54,""55,""56,""57,""58,""59,""60,""61,""62,""63,""64,""65,""66,""67,""68,""69,""70,""71,""72,""73,""ZZZ,"],
["AD,""AE,""AF,""AG,""AI,""AL,""AM,""AO,""AQ,""AR,""AS,""AT,""AU,""AW,""AX,""AZ,""BA,""BB,""BD,""BE,""BF,""BG,""BH,""BI,""BJ,""BM,""BN,""BO,""BQ,""BR,""BS,""BT,""BV,""BW,""BY,""BZ,""CA,""CC,""CD,""CF,""CG,""CH,""CI,""CK,""CL,""CM,""CN,""CO,""CR,""CU,""CV,""CW,""CX,""CY,""CZ,""DE,""DJ,""DK,""DM,""DO,""DZ,""EC,""EE,""EG,""EH,""ER,""ES,""ET,""FI,""FJ,""FK,""FM,""FO,""FR,""GA,""GB,""GD,""GE,""GF,""GG,""GH,""GI,""GL,""GM,""GN,""GP,""GQ,""GR,""GS,""GT,""GU,""GW,""GY,""HK,""HM,""HN,""HR,""HT,""HU,""ID,""IE,""IL,""IM,""IN,""IO,""IQ,""IR,""IS,""IT,""JE,""JM,""JO,""JP,""KE,""KG,""KH,""KI,""KM,""KN,""KP,""KR,""KW,""KY,""KZ,""LA,""LB,""LC,""LI,""LK,""LR,""LS,""LT,""LU,""LV,""LY,""MA,""MC,""MD,""ME,""MG,""MH,""MK,""ML,""MM,""MN,""MO,""MP,""MQ,""MR,""MS,""MT,""MU,""MV,""MW,""MX,""MY,""MZ,""NA,""NC,""NE,""NF,""NG,""NI,""NL,""NO,""NP,""NR,""NU,""NZ,""OM,""PA,""PE,""PF,""PG,""PH,""PK,""PL,""PM,""PN,""PR,""PS,""PT,""PW,""PY,""QA,""RE,""RO,""RS,""RU,""RW,""SA,""SB,""SC,""SD,""SE,""SG,""SH,""SI,""SJ,""SK,""SL,""SM,""SN,""SO,""SR,""SS,""ST,""SV,""SX,""SY,""SZ,""TC,""TD,""TF,""TG,""TH,""TJ,""TK,""TL,""TM,""TN,""TO,""TR,""TT,""TV,""TW,""TZ,""UA,""UG,""UM,""US,""UY,""UZ,""VA,""VC,""VE,""VG,""VI,""VN,""VU,""WF,""WS,""YE,""YT,""ZA,""ZM,""ZW,"],
["DK-81,"],
["EUR,""AFA,""DZD,""ADP,""ARS,""AMD,""AWG,""AUD,""AZM,""BSD,""BHD,""THB,""PAB,""BBD,""BYB,""BYR,""BEF,""BZD,""BMD,""VEB,""BOB,""BRL,""BND,""BGN,""BIF,""CAD,""CVE,""KYD,""GHC,""XOF,""XAF,""XPF,""CLP,""COP,""KMF,""BAM,""NIO,""CRC,""HRK,""CUP,""CYP,""CZK,""GMD,""DKK,""MKD,""DEM,""DJF,""STD,""DOP,""VND,""GRD,""XCD,""EGP,""SVC,""ETB,""FKP,""FJD,""HUF,""CDF,""FRF,""GIP,""HTG,""PYG,""GNF,""GWP,""GYD,""HKD,""UAH,""ISK,""INR,""IRR,""IQD,""IEP,""ITL,""JMD,""JOD,""KES,""PGK,""LAK,""EEK,""KWD,""MWK,""ZMK,""AOA,""MMK,""GEL,""LVL,""LBP,""ALL,""HNL,""SLL,""ROL,""BGL,""LRD,""LYD,""SZL,""LTL,""LSL,""LUF,""MGF,""MYR,""MTL,""TMM,""FIM,""MUR,""MZM,""MXN,""MXV,""MDL,""MAD,""BOV,""NGN,""ERN,""NAD,""NPR,""ANG,""NLG,""ILS,""TWD,""NZD,""BTN,""KPW,""NOK,""PEN,""MRO,""TOP,""PKR,""MOP,""UYU,""PHP,""PTE,""GBP,""BWP,""QAR,""GTQ,""ZAR,""OMR,""KHR,""MVR,""IDR,""RUB,""RUR,""RWF,""SHP,""SAR,""ATS,""XDR,""SCR,""SGD,""SKK,""SBD,""KGS,""SOS,""ESP,""LKR,""SDD,""SRG,""SEK,""CHF,""SYP,""TJR,""BDT,""WST,""TZS,""KZT,""TPE,""SIT,""TTD,""MNT,""TND,""TRL,""AED,""UGX,""CLF,""USD,""UZS,""VUV,""KRW,""YER,""JPY,""CNY,""YUM,""ZWD,""PLN,""AFA,""DZD,""ADP,""ARS,""AMD,""AWG,""AUD,""AZM,""BSD,""BHD,""THB,""PAB,""BBD,""BYB,""BYR,""BEF,""BZD,""BMD,""VEB,""BOB,""BRL,""BND,""BGN,"],
["Available,""DeletedAnnouncement,""ItemDeleted,""NewAnnouncement,""NewAvailable,""ItemTemporarilyUnavailable,"],
["Added,""Cancelled,""Disputed,""NoStatus,""Revised,"],
["FOB,"],
["BBAN,""DK:BANK,""DK:FIK,""DK:GIRO,""DK:NEMKONTO,""FI:BANK,""FI:GIRO,""GB:BACS,""GB:BANK,""GB:GIRO,""IBAN,""IS:BANK,""IS:GIRO,""IS:IK66,""IS:RB,""NO:BANK,""SE:BANKGIRO,""SE:PLUSGIRO,""SWIFTUS,""ZZZ,"],
["AAA,""AAB,""AAC,""AAD,""AAE,""AAF,""AAG,""AAH,""AAI,""AAJ,""AAK,""AAL,""AAM,""AAN,""AAO,""AAP,""AAQ,""AAR,""AAS,""AAT,""AAU,""AAV,""AAW,""AAX,""AAY,""AAZ,""ABA,""ABB,""ABC,""ABD,""ABE,""ABF,""ABG,""ABH,""ABI,""ABJ,""ABK,""ABL,""ABM,""ABN,""ABO,""ABP,""ABQ,""ABR,""ABS,""ABT,""ABU,""ABV,""AI,""ALT,""AP,""BR,""CAT,""CDV,""CON,""CP,""CU,""CUP,""CUS,""DAP,""DIS,""DPR,""DR,""DSC,""EC,""ES,""EUP,""FCR,""GRP,""INV,""LBL,""MAX,""MIN,""MNR,""MSR,""MXR,""NE,""NQT,""NTP,""NW,""OCR,""OFR,""PAQ,""PBQ,""PPD,""PPR,""PRO,""PRP,""PW,""QTE,""RES,""RTP,""SHD,""SRP,""SW,""TB,""TRF,""TU,""TW,""WH,"],
["BusinessAccept,""BusinessReject,""ProfileAccept,""ProfileReject,""TechnicalAccept,""TechnicalReject,"],
["AAA,""AAB,""AAC,""AAE,""AAF,""AAG,""AAH,""AAI,""AAJ,""AAK,""AAL,""AAM,""AAN,""AAO,"],
["StandardRated,""ZeroRated,"],
["StandardRated,""ZeroRated,""ReverseCharge,"],
["01,""04,""15,""71,""73,""75,"],
["NONE,""Procurement-BilSim-1.0,""Procurement-BilSimR-1.0,""Procurement-PayBas-1.0,""Procurement-PayBasR-1.0,""Procurement-OrdSim-BilSim-1.0,""Procurement-OrdSimR-BilSim-1.0,""Procurement-OrdSim-BilSimR-1.0,""Procurement-OrdSimR-BilSimR-1.0,""Procurement-OrdAdv-BilSim-1.0,""Procurement-OrdAdv-BilSimR-1.0,""Procurement-OrdAdvR-BilSim-1.0,""Procurement-OrdAdvR-BilSimR-1.0,""Procurement-OrdSel-BilSim-1.0,""Procurement-OrdSel-BilSimR-1.0,""Catalogue-CatBas-1.0,""Catalogue-CatBasR-1.0,""Catalogue-CatSim-1.0,""Catalogue-CatSimR-1.0,""Catalogue-CatExt-1.0,""Catalogue-CatExtR-1.0,""Catalogue-CatAdv-1.0,""Catalogue-CatAdvR-1.0,""urn:www.nesubl.eu:profiles:profile1:ver1.0,""urn:www.nesubl.eu:profiles:profile2:ver1.0,""urn:www.nesubl.eu:profiles:profile5:ver1.0,""urn:www.nesubl.eu:profiles:profile7:ver1.0,""urn:www.nesubl.eu:profiles:profile8:ver1.0,""urn:www.nesubl.eu:profiles:profile1:ver2.0,""urn:www.nesubl.eu:profiles:profile2:ver2.0,""urn:www.nesubl.eu:profiles:profile5:ver2.0,""urn:www.nesubl.eu:profiles:profile7:ver2.0,""urn:www.nesubl.eu:profiles:profile8:ver2.0,"]
]