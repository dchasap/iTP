# iTP+xPTP
Repository for the iTP and xPTP replacement policies for TLB anc L2.   The iTP policy prioritizes instruction over data translations, while xPTP supplements iTP as a L2 cache replacement that leverages the increase in page walks due to data translations.

## Dependencies

SLURM job manager

GCC >= 11.4.0 (older version will probably work, but have not been tested)

Python >= 3.0

python packages:

* zenodo_get
* argparse
* pandas
* scipy
* matplotlib
* seaborn

## Installation 

Clone this repository to deploy the artifact evaluation workflow infrastructure:
	
	clone git https://github.com/dchasap/itp_asplos25_AE.git

To prepare the simualtion environment run:

	cd itp_asplos25_AE
	source env.sh

The env.sh scripts can be edited to setup a custom directory tree.

To download and deploy the necessary application traces run the following script:

	./dowload_traces.sh qualcomm_srv

Optinally to download the SPEC CPU 2006/2017 workloads run the following:

	./download_traces.sh spec

If no arguments are passed then both Qualcomm and SPEC will be downloaded.

Alternatively, to manually deploy the traces create the corresponding directories in traces:

	mkdir -p ./traces/qualcomm_srv
 	mkdir -p ./traces/spec
Download the Qualcomm Sever and SPEC CPU 2006/2017 workloads from https://doi.org/10.5281/zenodo.10959704,  https://doi.org/10.5281/zenodo.10959704 and https://doi.org/10.5281/zenodo.10960003, and extract them in their corresponding directories.  The ./traces/qualcomm_srv and ./traces/spec directories should contain the *.champsimtrace.xz files. 

## Running experiments to collect data

First prepare the simulation environment, if not done already:

	cd itp_asplos25_AE
	source env.sh

To collect the necessary experimental data to recreate the most improtant plots, simply run the following command:
  
  	./submit_expriments.sh AE

If only a specific figure is needed, then run the scripts providing an argument with the word fig_N, where N is the two digits number of the figure as presented in the paper:
  
  	./submit_expriments.sh fig_08

To run all experiments just run ./submit_expriments.sh without any arguments.  This is not recommended as the number of jobs generated will probably exceed SLURM's queue limit.

## Parsing and plotting data

To parse and plot the raw data generated by running an experiment, run the following scripts:
  
	./gen_plots.sh AE

If a specific plot is required, then provide an argument with the word fig_N, where N is the two digit number of the figure as presented in the paper:
  
  	./gen_plots.sh fig_08

If run without any arguments, all plots will be genrated.  Note however that this steps assumes the corresponding experiments have been run.


## Examining the results

The resulting figures will be placed in the figures directory, if the default directory tree has been used.  The directory figurs_PUBLISHED contains pre-generatad figures with the expected results that can be used for comparison.

## Running custom experiments

### Adding new benchmarks:
Place your *.champsimtraces.xz in the traces directory, in their own folder (e.g. ./traces/mybenchmarks).

Create a bash script file (e.g. mybenchmarks.sh) and place it in the scripts directory. This file should define two variables, one for the directory name the traces are in and one listing all the traces names.  
Review qualcomm_srv_workloads.sh in the scripts directory to see an example.

Edit scripts/benchmarks.sh by adding at the top of the script source ./scripts/mybenchmarks.sh and a corresponding if-statement as following the example shown in the file with the Qualcomm Server workloads.  
The name you pick for the if-statement is going to be used to identify the new benchmarks in all other scripts (e.g. mybenchmarks).

### Setting and running experiments:

In the ChampSim direcotry edit the simulator configuration file champsim_fdip_baseline.json. You can edit prefetchers, replacement polcies and TLB and cache sizes.  This file is the base for all experiments.

To create you own set of experiments copy one of the bash scripts in exp_conf/fig_XX.sh.  This file is used as a configuration file by the job launching script.  Edit the variable BENCHSUITES, assigning the name of 
the benchmark suite you want to use (e.g. BENCHSUITES=mybenchmarks).  The variable CONFIGURATION_TAGS needs to also be edited. This variable should hold a list of the experiments to run.  The experiment names are 
parsed by ./scripts/gen_champsim_conf.py to modify the baseline configuration.  The naming conversion follows the scheme:

	cache_type-r.rep_pol-s.num_sets-w.num_ways}.
 
For example if you want to just enable iTP and xPTP, and change the size of the LLC, you can use:

	stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16

To launch the experiments run:

	./scripts/submit_experiment.sh ./exp_conf/myexp.sh
       
Where ./exp_conf/myexp.sh is the bash scripts you created in the previous step.  The batched version can ./scripts/submit_experiment_batch.sh can also be used in the same manner.

### Parsing experiment data:

To generate a CSV file with the experimental data generated by the previous steps, run:

	./scripts/parse_data.sh ./exp_conf/mybench.sh
	
The generated data is placed in ./stats/exp_name.csv.
