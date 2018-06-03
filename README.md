# Sherpa-Validation
Sherpa-Validation: madgraph gridpack vs sherpack. The packages contain all the necessary machinery to start off a validation workflow on comparing gridpack across Madgraph and Sherpa.

## Environment setup

   Clone the package into a clean directory without CMSSW environment. A standard gridpack from madgraph and sherpa was prepared in gridpacks folder. Both gridpacks were made for ZtoEE 0jets process, The following step pertains the construction of validation workflow.

   ```
   git clone https://github.com/SiewYan/Sherpa-Validation.git
   cd Sherpa-Validation
   ```
## Configures validation
   
   Configure ```submit_validation.sh``` to point to the correct path and tags, ```fragments``` folder contains madgraph and sherpa's hadronizer. Launch the validation workflow by

   ```
   source submit_validation.sh
   ```

   by default 100 LSF batch jobs will be submitted and ```samples``` folder will be created.

## DQM html

   Once all the jobs are finished, making the conparison html by

   ```
   merge_mkhtml.sh
   ```

## Processes need validation

   - [ ] Z+jets LO 3jets
   - [ ] TT+jets 2jets
   - [ ] gamma+jets

### Reference

    - [GenValidation github](https://github.com/cms-sw/genproductions/tree/master/bin/GenValidation)
