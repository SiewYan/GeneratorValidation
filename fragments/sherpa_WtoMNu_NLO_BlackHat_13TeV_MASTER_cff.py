import FWCore.ParameterSet.Config as cms
import os

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('WtoMNu_NLO_BlackHat_13TeV'),
  SherpackLocation = cms.string('/afs/cern.ch/work/s/shoh/analysis/SherpaStudies/Sherpa-Generation/CMSSW_9_4_8/src/GeneratorValidation/GEN-packs/'),
  SherpackChecksum = cms.string('f781dc34050e5937b3677bfb0da4f93e'),
  FetchSherpack = cms.bool(True),
  SherpaPath = cms.string('./'),
  SherpaPathPiece = cms.string('./'),
  SherpaResultDir = cms.string('Result'),
  SherpaDefaultWeight = cms.double(1.0),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "MPI_Cross_Sections",
                             "Run"),
                              MPI_Cross_Sections = cms.vstring(
				" MPIs in Sherpa, Model = Amisic:",
				" semihard xsec = 1.92371e+06 mb,",
				" non-diffractive xsec = 17.0318 mb with nd factor = 0.3142."
                                                  ),
                              Run = cms.vstring(
				" (run){",
				" EVENTS 1M; ERROR 0.99;",
				" FSF:=1.; RSF:=1.; QSF:=1.;",
				" ##",
				" ## SHERPA_LDADD MyJetCriterion;",
				" ## JET_CRITERION FASTJET[A:antikt,R:0.4,y:5];",
				" NJET:=0; LJET:=2; QCUT:=0;",
				" ME_SIGNAL_GENERATOR Comix Amegic LOOPGEN;",
				" EVENT_GENERATION_MODE Unweighted;",
				" LOOPGEN:=BlackHat;",
				" MASSIVE[15] 1;",
				" PDF_LIBRARY     = LHAPDFSherpa;",
				" PDF_SET         = NNPDF31_nnlo_hessian_pdfas;",
				" HEPMC_USE_NAMED_WEIGHTS=1;",
				" BEAM_1 2212; BEAM_ENERGY_1 = 6500.;",
				" BEAM_2 2212; BEAM_ENERGY_2 = 6500.;",
				"}(run)",
				" (processes){",
				" Process 93 93 -> 13 -14;",
				" Order (*,2);",
				" NLO_QCD_Mode MC@NLO {LJET};",
				" ME_Generator Amegic {LJET};",
				" RS_ME_Generator Comix {LJET};",
				" Loop_Generator LOOPGEN {LJET};",
				" End process;",
				" Process 93 93 -> -13 14;",
				" Order (*,2);",
				" NLO_QCD_Mode MC@NLO {LJET};",
				" ME_Generator Amegic {LJET};",
				" RS_ME_Generator Comix {LJET};",
				" Loop_Generator LOOPGEN {LJET};",
				" End process;",
				"}(processes)",
				" (selector){",
				" Mass 13 -14 1. E_CMS",
				" Mass -13 14 1. E_CMS",
				"}(selector)"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

