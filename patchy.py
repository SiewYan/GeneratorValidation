#!/bin/python                                                                                                                             

import os
from os import listdir

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_frag = dir_path+'/fragments/'
dir_genpacks = dir_path+'/GEN-packs/'
for py in listdir(dir_frag):
    with open('%s%s' %(dir_frag,py), 'r') as file1 :
        filedata = file1.read()

        #Correction
        for pair in [
            ["from SherpaGeneration.Generator.ExtendedSherpaWeights_cfi import" , "from Configuration.Generator.ExtendedSherpaWeights_cfi import"],
            ["SherpackLocation = cms.string('./')," , "SherpackLocation = cms.string('%s'),"%dir_genpacks],
            ["FetchSherpack = cms.bool(False)," , "FetchSherpack = cms.bool(True),"]
            ]:
            #print pair[0]
            #print pair[1]
            filedata = filedata.replace(pair[0], pair[1])

    with open('%s%s' %(dir_frag,py), 'w') as file2:
        file2.write(filedata)
