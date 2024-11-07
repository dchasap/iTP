# iTP+xPTP
Repository for the iTP and xPTP replacement policies for TLB anc L2.   The iTP policy prioritizes instruction over data translations, while xPTP supplements iTP as a L2 cache replacement that leverages the increase in page walks due to data translations.

## Dependencies

SLURM job manager

GCC

Python >= 3.0

python packages:

	* zenodo_get
	* pandas
  	* scipy
   	* matplotlib
    	* seaborn

## Installation 

Clone this repository to deploy the artifact evaluation workflow infrastructure:
	
	clone git https://github.com/dchasap/itp_asplos25_AE.git

To prepare the simualtion environment run:

	source env.sh

The env.sh scripts can be edited to setupe a custom directory tree.

To download and deploy the necessary application traces run the following script:

	./dowload_traces.sh qualcomm_srv

Optinally to download the SPEC CPU 2006/2017 workloads run the following:

	./download_traces.sh spec

If no arguments are passed then both Qualcomm and SPEC will be downloaded.

TODO: manuall installation


## Running experiments to collect data

First prepare the simulation environment, if not done already.

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
  
  	./gen_plots.sh fig_01

If run without any arguments, all plots will be genrated.  Note however that this steps assumes the corresponding experiments have been run.


## Examining the results

The resulting figures will be placed in the figures directory, if the default directory tree has been used.  The directory figurs_PUBLISHED contains pre-generatad figures with the expected results that can be used for comparison.

