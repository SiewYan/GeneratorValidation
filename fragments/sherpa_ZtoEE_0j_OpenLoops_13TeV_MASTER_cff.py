import FWCore.ParameterSet.Config as cms
import os
from Configuration.Generator.ExtendedSherpaWeights_cfi import *

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('ZtoEE_0j_OpenLoops_13TeV'),
  SherpackLocation = cms.string('XXX/GEN-packs/'),
  SherpackChecksum = cms.string('72063dda9a58948e1b666e20a37ce35e'),
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
				" semihard xsec = 2.00392e+06 mb,",
				" non-diffractive xsec = 17.0318 mb with nd factor = 0.3142."
                                                  ),
                              Run = cms.vstring(
				" (run){",
				" EVENTS 5000; ERROR 0.99;",
				" MASSIVE_PS 4 5;",
				" FSF:=1.; RSF:=1.; QSF:=1.;",
				" NJET:=0; LJET:=0; QCUT:=0.;",
				" ME_SIGNAL_GENERATOR Comix Amegic LOOPGEN;",
				" OL_PREFIX=/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/openloops/1.3.1-mlhled2",
				" EVENT_GENERATION_MODE Unweighted;",
				" LOOPGEN:=OpenLoops;",
				" BEAM_1 2212; BEAM_ENERGY_1 = 6500.;",
				" BEAM_2 2212; BEAM_ENERGY_2 = 6500.;",
				" PDF_LIBRARY     = LHAPDFSherpa;",
				" PDF_SET         = NNPDF30_nlo_nf_4_pdfas;",
				" HEPMC_USE_NAMED_WEIGHTS=1;",
				" SCALE_VARIATIONS 0.25,0.25 0.25,1. 1.,0.25 1.,4. 4.,1. 4.,4.;",
				" PDF_VARIATIONS NNPDF30_nlo_nf_4_pdfas[all];",
				"}(run)",
				" (processes){",
				" Process 93 93 -> 11 -11 93{NJET};",
				" Order (*,2);",
				" NLO_QCD_Mode MC@NLO {LJET};",
				" ME_Generator Amegic {LJET};",
				" RS_ME_Generator Comix {LJET};",
				" Loop_Generator LOOPGEN {LJET};",
				" End process;",
				"}(processes)",
				" (mi){",
				" MI_HANDLER = Amisic  # None or Amisic",
				"}(mi)"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

