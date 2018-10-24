#!/bin/bash

folders=`( ls -d /eos/user/s/shoh/SHERPA_WtoMNu_*_CMSSW_9_4_8 | sed 's#/##')`

#9313 fail

for each in $folders
do
    echo "scp /${each}/*MASTER_cff.py ./fragments"
    echo "scp /${each}/*MASTER.tgz ./GEN-packs"

    scp /${each}/*MASTER_cff.py ./fragments
    scp /${each}/*MASTER.tgz ./GEN-packs
done
