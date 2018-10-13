import FWCore.ParameterSet.Config as cms
import os
from Configuration.Generator.ExtendedSherpaWeights_cfi import *

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('WtoLNu_2j_NLO_BlackHat_CKKW_13TeV'),
  SherpackLocation = cms.string('XXX/GEN-packs/'),
  SherpackChecksum = cms.string('a99fae41aa1a4701b7761e2b95e30774'),
  FetchSherpack = cms.bool(True),
  SherpaPath = cms.string('./'),
  SherpaPathPiece = cms.string('./'),
  SherpaResultDir = cms.string('Result'),
  SherpaDefaultWeight = cms.double(1.0),
  SherpaWeightsBlock = SherpaWeightsBlock,
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "MPI_Cross_Sections",
                             "Run"),
                              MPI_Cross_Sections = cms.vstring(
				" MPIs in Sherpa, Model = Amisic:",
				" semihard xsec = 2.01122e+06 mb,",
				" non-diffractive xsec = 17.0318 mb with nd factor = 0.3142."
                                                  ),
                              Run = cms.vstring(
				" (run){",
				" EVENTS 1M; ERROR 0.99;",
				" MASSIVE_PS 4 5;",
				" FSF:=1.; RSF:=1.; QSF:=1.;",
				" SCALES METS{FSF*MU_F2}{RSF*MU_R2}{QSF*MU_Q2};",
				" NJET:=2; LJET=2,3,4; QCUT:=20.;",
				" ME_SIGNAL_GENERATOR Comix Amegic LOOPGEN;",
				" OL_PREFIX=/cvmfs/cms.cern.ch/slc6_amd64_gcc700/external/openloops/2.0.b",
				" EVENT_GENERATION_MODE Weighted;",
				" LOOPGEN:=BlackHat;",
				" PDF_LIBRARY     = LHAPDFSherpa;",
				" PDF_SET          = NNPDF30_nlo_nf_5_pdfas;",
				" HEPMC_USE_NAMED_WEIGHTS=1;",
				" SCALE_VARIATIONS 0.25,0.25 0.25,1. 1.,0.25",
				" PDF_VARIATIONS NNPDF31_nnlo_hessian_pdfas[all]",
				" BEAM_1 2212; BEAM_ENERGY_1 6500.;",
				" BEAM_2 2212; BEAM_ENERGY_2 6500.;",
				"}(run)",
				" (processes){",
				" Process 93 93 -> 90 91 93{NJET};",
				" Order (*,2); CKKW sqr(QCUT/E_CMS);",
				" NLO_QCD_Mode MC@NLO {LJET};",
				" ME_Generator Amegic {LJET};",
				" RS_ME_Generator Comix {LJET};",
				" Loop_Generator LOOPGEN {LJET};",
				" Integration_Error 0.02 {4};",
				" Integration_Error 0.02 {5};",
				" Integration_Error 0.05 {6};",
				" Integration_Error 0.08 {7};",
				" Integration_Error 0.10 {8};",
				" End process;",
				"}(processes)",
				" (selector){",
				" Mass 11 -12 1. E_CMS",
				" Mass 13 -14 1. E_CMS",
				" Mass -11 12 1. E_CMS",
				" Mass -13 14 1. E_CMS",
				" Mass 15 -16 1. E_CMS",
				" Mass -15 16 1. E_CMS",
				"}(selector)"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

