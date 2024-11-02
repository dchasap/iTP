import plots
from recall_dist_input_files import get_recall_dist_files
from benchmark_names import get_benchmark_names
import pandas as pd

FIGURES_DIR = "/mnt/c/Users/bscuser/BSC/figures"

xlabels = { 
			'qualcomm_srv_ap': "Qualcomm Server Workloads"
			'selected_qualcomm_srv_ap': "Qualcomm Server Workloads",
			'smt_qualcomm_srv_ap': "SMT Qualcomm Server Workloads",
			'spec': "SPEC CPU 2006/2017",
			}



plot_fig_01 = False
plot_fig_02 = False
plot_fig_03 = False
plot_fig_04 = False
plot_fig_08 = False
plot_fig_09 = False
plot_fig_10 = False
plot_fig_11 = False
plot_fig_12 = False


if (plot_fig_01):
	
	benchsuite = "selected_qualcomm_srv_ap"	
	input_qualcomm_baseline_files =	[ "./stats/" + benchsuite + "_fdip_itlb-s.128-w.8_llc-s.1537-w.16.csv" ]

	input_qualcomm_data_files = [ 
												"./stats/" + benchsuite  + "_fdip_itlb-s.256-w.4_llc-s.1537-w.16.csv",
												"./stats/" + benchsuite  + "_fdip_itlb-s.128-w.4_llc-s.1537-w.16.csv",
												"./stats/" + benchsuite  + "_fdip_itlb-s.32-w.4_llc-s.1537-w.16.csv",
												"./stats/" + benchsuite  + "_fdip_itlb-s.16-w.4_llc-s.1537-w.16.csv",
												"./stats/" + benchsuite  + "_fdip_itlb-s.2-w.4_llc-s.1537-w.16.csv"
											]


	benchsuite = "spec"	
	input_spec_baseline_files =	[ "./stats/" + benchsuite + "_fdip_itlb-s.128-w.8_llc-s.1537-w.16.csv" ]

	input_spec_data_files = [ 
														"./stats/" + benchsuite  + "_fdip_itlb-s.256-w.4_llc-s.1537-w.16.csv",
														"./stats/" + benchsuite  + "_fdip_itlb-s.128-w.4_llc-s.1537-w.16.csv",
														"./stats/" + benchsuite  + "_fdip_itlb-s.32-w.4_llc-s.1537-w.16.csv",
														"./stats/" + benchsuite  + "_fdip_itlb-s.16-w.4_llc-s.1537-w.16.csv",
														"./stats/" + benchsuite  + "_fdip_itlb-s.2-w.4_llc-s.1537-w.16.csv"
													]



	plot_conf = { 'xlabel':  xlabels[benchsuite], 'plot_type': 'violin'}
	plot_conf['plot_width'] = 7
	plot_conf['plot_height'] = 1.8

	input_tags = [
									"1024 entries", 
									"512 entries", 
									"128 entries",
									"64 entries",
									"8 entries"
								]

	op_type = "TOTAL"
	cache_type = "cpu0_ITLB"
	plot_conf['ylabel'] = 'Cycles Spent on\nInstruction Address\nTranslation (%)'
	plot_conf['ylim1'] = 20
	plot_conf['ylim2'] = 15
	plot_conf['legend_cols'] = 3
	stat_name = "MISS_CYCLES"
	output_file = FIGURES_DIR + "/fig_itlb_sensitivity.pdf"
	print(FIGURES_DIR + "/fig_itlb_sensitivity.pdf")
	plots.plot_itlb_sensitivity(	input_qualcomm_baseline_files, input_qualcomm_data_files, 
																input_spec_baseline_files, input_spec_data_files,
																input_tags, cache_type, op_type, stat_name, plot_conf, output_file)


if (plot_fig_02):

	input_data_files =	[ 	
												"./stats/spec_fdip_llc-s.15370-w.16.csv",
												"./stats/selected_qualcomm_srv_ap_fdip_llc-s.1537-w.16.csv"
											]

	input_tags = ["SPEC CPU 2006/17", "Qualcomm Server"]


	plot_conf = { 'xlabel':  'Workloads', 'plot_type': 'point'}
	plot_conf['plot_width'] = 6
	plot_conf['plot_height'] = 1.2	
	plot_conf['ylim1'] = 1
	plot_conf['ylim2'] = 0.8

	cache_type = "cpu0_STLB"
	op_type = "TOTAL"
	plot_conf['ylabel'] = 'Instruction MPKI\nin the STLB\n'
	stat_name = "dMPKI"
	output_file = FIGURES_DIR + "/fig_stlb_mpki_comparison.pdf"
	print(FIGURES_DIR + "/fig_stlb_mpki_comparison.pdf")
	plots.plot_qualcom_vs_spec(	input_data_files, input_tags, 
															cache_type, op_type, stat_name, plot_conf, output_file)

	cache_type = "cpu0_ITLB"
	plot_conf['ylabel'] = 'Cycles Spent on\nInstruction Address\nTranslation (%)'
	plot_conf['ylim1'] = None
	plot_conf['ylim2'] = None
	stat_name = "MISS_CYCLES"
	output_file = "./figures/fig_instruction_latency.pdf"
	plots.plot_qualcom_vs_spec(	input_data_files, input_tags, 
															cache_type, op_type, stat_name, plot_conf, output_file)


if (plot_fig_03):

	benchsuite = "selected_qualcomm_srv_ap"
	input_baseline_files =	[ "./stats/" + benchsuite  + "_fdip_baseline_llc-s.1537-w.16.csv"]

	input_data_files =	[ 	
							"./stats/" + benchsuite + "_fdip_probi.20_stlb-r.probi_llc-s.1537-w.16.csv",
							"./stats/" + benchsuite + "_fdip_probi.40_stlb-r.probi_llc-s.1537-w.16.csv",
							"./stats/" + benchsuite + "_fdip_probi.60_stlb-r.probi_llc-s.1537-w.16.csv",
							"./stats/" + benchsuite + "_fdip_probi.80_stlb-r.probi_llc-s.1537-w.16.csv"
						]

	input_tags = [ "P=0.2", "P=0.4", "P=0.6", "P=0.8" ]

	plot_conf = { 'xlabel':  xlabels[benchsuite], 'plot_type': 'points'}
	plot_conf['plot_width'] = 6
	plot_conf['plot_height'] = 1.4
	plot_conf['xlabel'] = xlabels[benchsuite]


	cache_type = "cpu0_STLB"
	op_type = "TOTAL"
	output_file = FIGURES_DIR + "/figures/fig_itp_vs_dtp_" + benchsuite + ".pdf"
	print(FIGURES_DIR + "/figures/fig_itp_vs_dtp_" + benchsuite + ".pdf"_
	plots.plot_ipc_improvement_w_means(	input_baseline_files, input_data_files, input_tags, 
																			cache_type, op_type, plot_conf, output_file)
			
	# TODO: remove
	input_data_files =	[ 	"./stats/" + benchsuite + "_fdip_probi.10_stlb-r.probi_llc-s.1537-w.16.csv" ]

	input_tags = [	"LRU" ]

	plot_conf = { 'xlabel':  xlabels[benchsuite], 'plot_type': 'points'}
	plot_conf['plot_width'] = 6
	plot_conf['plot_height'] = 2	

	output_file = "./figures/fig_itp_vs_dtp_latency_" + benchsuite + ".pdf"

	cache_type = "cpu0_STLB"
	op_type = "TOTAL"
	plots.plot_latency_w_means(	input_data_files, input_tags, 
															cache_type, op_type, plot_conf, output_file)


if (plot_fig_04):
	
	input_data_files =	[	
							"./stats/" + "selected_qualcomm_srv_ap" + "_fdip_baseline_llc-s.1537-w.16.csv",
							"./stats/" + "selected_qualcomm_srv_ap" + "_fdip_probi.80_stlb-r.probi_llc-s.1537-w.16.csv"
						]

	plot_conf = { 'xlabel':  'smth', 'plot_type': 'barplot'}
	plot_conf['plot_width'] = 6.2
	plot_conf['plot_height'] = 2
	#cache_types = [ 'cpu0_L1D', 'cpu0_L2C', 'LLC' ]
	cache_types = [ 'cpu0_L2C', 'LLC' ]
	input_tags = [ 'LRU', 'KiT' ]
	op_type = "TOTAL"
	output_file = FIGURES_DIR + "/figures/fig_kit_mpki_breakdown_all_log.pdf"
	print(FIGURES_DIR + "/figures/fig_kit_mpki_breakdown_all_log.pdf")
	plots.plot_kit_mpki_breakdown(input_data_files, input_tags, 
									cache_types, op_type, plot_conf, output_file)



if (plot_fig_08):
	benchsuites = [ "selected_qualcomm_src_ap", "smt_qualcomm_srv_ap" ]
	for benchsuite in benchsuites:

		input_baseline_files =	[ "./stats/" + benchsuite  + "_fdip_baseline_llc-s.1537-w.16.csv" ]
								#"./stats/" + benchsuite + "_dev_stlb-itp:0:2:12.csv",

		input_data_files = [	"./stats/" + benchsuite + "_fdip_l2c-r.tdrrip_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_l2c-r.ptp_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_l2c-r.tdrrip_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_l2c-r.ptp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.tdrrip_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.ptp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
							]

		plot_conf = { 'xlabel':  xlabels[benchsuite], 'plot_type': 'violin'}
		plot_conf['plot_width'] = 9
		plot_conf['plot_height'] = 3
		plot_conf['rotation'] = 20
		plot_conf['fontsize'] = 16
		plot_conf['add_seperator'] = True

		input_tags = [ 	"TDRRIP",
						"PTP",
						"CHiRP",
						"ChiRP+TDRRIP",
						"ChiRP+PTP",
						"iTP",
						"iTP+TDRRIP",
						"iTP+PTP",
						"iTP+xPTP",
					]

		cache_type = "cpu0_STLB"
		op_type = "TOTAL"
		output_file = "./figures/fig_soa_ipc_" + benchsuite + ".pdf"
		print(FIGURES_DIR + "/figures/fig_soa_ipc_" + benchsuite + ".pdf")
		plots.plot_ipc_improvement_single(	input_baseline_files, input_data_files, input_tags, 
																cache_type, op_type, plot_conf, output_file)
		

if (plot_fig_09):

	benchsuite = 'selected_qualcomm_srv_ap'
	input_st_data_files =	[ 	
								"./stats/" + benchsuite + "_fdip_baseline_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_l2c-r.tdrrip_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_l2c-r.ptp_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_l2c-r.tdrrip_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_l2c-r.ptp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.tdrrip_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.ptp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
							]

	benchsuite = 'smt_qualcomm_srv_ap'
	input_smt_data_files =	[ 	
								"./stats/" + benchsuite + "_fdip_baseline_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_l2c-r.tdrrip_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_l2c-r.ptp_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_l2c-r.tdrrip_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.chirp_l2c-r.ptp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.tdrrip_llc-s.1537-w.16.csv",	
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.ptp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv"
							]



	plot_conf = { 'xlabel':  xlabels[benchsuite], 'plot_type': 'violin'}
	input_tags = [ 	"LRU",
									"TDRRIP",
									"PTP",
									"CHiRP",
									"ChiRP+TDRRIP",
									"ChiRP+PTP",
									"iTP",
									"iTP+TDRRIP",
									"iTP+PTP",
									"iTP+xPTP"]

	plot_conf['plot_type'] = 'barplot'
	plot_conf['plot_width'] = 16
	plot_conf['plot_height'] = 1.8
	plot_conf['fontsize'] = 14
	plot_conf['ylabel'] = "MPKI"
	plot_conf['show_legend'] = True
	plot_conf['extra_xlabels'] = False
	cache_types=["cpu0_STLB", "cpu0_L2C", "LLC"]
	op_type = "TOTAL"
	output_file = FIGURES_DIR + "/figures/fig_soa_mpki_comparison.pdf"
	print(FIGURES_DIR + "/figures/fig_soa_mpki_comparison.pdf")
	plots.plot_average_multiple_caches_single_fig(	input_st_data_files, input_smt_data_files, 
																									input_tags, cache_types, op_type, "MPKI", 
																									plot_conf, output_file)

	plot_conf['show_legend'] = False
	plot_conf['extra_xlabels'] = True
	plot_conf['ylabel'] = "Avg Miss Latency"
	output_file = FIGURES_DIR + "/figures/fig_soa_avg_miss_lat_comparison.pdf"
	print(FIGURES_DIR + "/figures/fig_soa_avg_miss_lat_comparison.pdf")
	plots.plot_average_multiple_caches_single_fig(	input_st_data_files, input_smt_data_files, 
																									input_tags, cache_types, op_type, 
																									"AVERAGE_MISS_LATENCY", plot_conf, output_file)

if (plot_fig_11):
	benchsuites = [ "selected_qualcomm_server_ap", "smt_qualcomm_server_ap" ]

		input_baseline_files =	[	
									"./stats/" + benchsuite + "_fdip_baseline_llc-s.1537-w.16.csv",
									"./stats/" + benchsuite + "_fdip_baseline_llc-s.1537-w.16.csv",
									"./stats/" + benchsuite + "_fdip_llc-r.ship-s.1537-w.16.csv",
									"./stats/" + benchsuite + "_fdip_llc-r.ship-s.1537-w.16.csv",
									"./stats/" + benchsuite + "_fdip_llc-r.mockingjay-s.1537-w.16.csv",
									"./stats/" + benchsuite + "_fdip_llc-r.mockingjay-s.1537-w.16.csv"
								]

		input_data_files = [
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_llc-r.ship-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.xptp_llc-r.ship-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_stlb-r.itp_llc-r.mockingjay-s.1537-w.16.csv",
								"./stats/" + benchsuite + "_fdip_dyn-1-2.5_stlb-r.itp_l2c-r.xptp_llc-r.mockingjay-s.1537-w.16.csv"
							]


		l2c_tags = [ "iTP", "iTP+xPTP", "iTP", "iTP+xPTP", "iTP", "iTP+xPTP" ]
		llc_tags = [ "LRU", "LRU", "SHiP", "SHiP", "Mockingjay", "Mockingjay", ]

		plot_conf = { 'xlabel':  'dummy', 'plot_type': 'violin'}
		plot_conf['plot_width'] = 4
		plot_conf['plot_height'] = 1	

		cache_type = "cpu0_STLB"
		op_type = "TOTAL"

		output_file = FIGURES_DIR + "/figures/fig_soa_llc_comparison_ipc_" + benchsuite + "_over_lru.pdf"
		print(FIGURES_DIR + "/figures/fig_soa_llc_comparison_ipc_" + benchsuite + "_over_lru.pdf")
		plots.plot_llc_pol_comparison(	input_baseline_files, input_data_files, 
										l2c_tags, llc_tags, cache_type, op_type, plot_conf, 
										output_file)


if (plot_fig_12):
	

	input_smt1_baseline_files =	["./stats/selected_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv"]


	input_smt1_data_files = [
		"./stats/selected_qualcomm_srv_ap_fdip_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
		"./stats/selected_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv"]

	input_smt2_baseline_files =	["./stats/smt_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_baseline_llc-s.1537-w.16.csv",
								 "./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_baseline_llc-s.1537-w.16.csv"]


	input_smt2_data_files = [
		"./stats/smt_qualcomm_srv_ap_fdip_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_l2c-r.tdrrip_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_l2c-r.ptp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_stlb-r.chirp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.10-d.10_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.50-d.50_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv",
		"./stats/smt_qualcomm_srv_ap_fdip_mlpg-i.100-d.100_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv"]




	input_tags1 = [ "0%", "10%", "50%", "100%" ]
	input_tags2 = [ "TDRRIP", "PTP", "CHiRP", "iTP+xPTP" ]

	plot_conf = { 'xlabel':  'dummy', 'plot_type': 'violin'}
	plot_conf['plot_width'] = 4
	plot_conf['plot_height'] = 1	

	cache_type = "cpu0_STLB"
	op_type = "TOTAL"

	output_file = FIGURES_DIR + "/figures/fig_2mbi_comparison_ipc.pdf"
	print(FIGURES_DIR + "/figures/fig_2mbi_comparison_ipc.pdf")
	plots.plot_mlt_instr_pages(	input_smt1_baseline_files, 
								input_smt2_baseline_files, 
								input_smt1_data_files, input_smt2_data_files, 
								input_tags1, input_tags2, cache_type, op_type, 
								plot_conf, output_file)




if (plot_mpki_breakdown):

	input_baseline_files =	[ 	"./stats/" + benchsuite + "_fdip_baseline_llc-s.1537-w.16.csv"]

	input_data_files =	[	
							"./stats/" + benchsuite + "_fdip_baseline_llc-s.1537-w.16.csv",
							"./stats/" + benchsuite + "_fdip_stlb-r.itp_llc-s.1537-w.16.csv",
							"./stats/" + benchsuite + "_fdip_stlb-r.itp_l2c-r.xptp_llc-s.1537-w.16.csv" 
						]

	plot_conf = { 'xlabel':  'xlabel', 'plot_type': 'barplot'}
	plot_conf['plot_width'] = 6.2
	plot_conf['plot_height'] = 1.5
	plot_conf['rotation'] = 15
	input_tags = [ "LRU", "iTP", "iTP+xPTP" ]
	cache_types = [ "cpu0_STLB", "cpu0_L2C", "LLC" ]
	op_type = "TOTAL"
	output_file = "./figures/fig_itp_mpki_breakdown_" + benchsuite + "_rebuttal.pdf"
	plots.plot_mpki_breakdown(	input_data_files, input_tags, cache_types, op_type, 
															plot_conf, output_file)



if (plot_page_access_characterization):

	benchsuite = "selected_qualcomm_srv_ap"	
	input_data_file = "./stats/" + benchsuite  + "_fdip_baseline_l1d-p.berti_llc-s.1537-w.16_page_access_stats.csv"

	plot_conf = { 'xlabel':  xlabels[benchsuite], 'plot_type': 'barplot'}
	plot_conf['plot_width'] = 6
	plot_conf['plot_height'] = 1.4
	plot_conf['ylabel'] = 'total accesses'


	cache_type = "cpu0_STLB"
	op_type = "TOTAL"
	for page_type in ['instr', 'data']:
		stat_name = "total_unique_pages"
		output_file = "./figures/fig_" + stat_name + "_" + benchsuite + ".pdf"
		plots.plot_stat_w_mean(	input_data_file, stat_name, page_type, cache_type, op_type, plot_conf, output_file)
		stat_name = "total_accesses"
		plots.plot_stat_w_mean(	input_data_file, stat_name, page_type, cache_type, op_type, plot_conf, output_file)
		stat_name = "accesses_90"
		plots.plot_stat_w_mean(	input_data_file, stat_name, page_type, cache_type, op_type, plot_conf, output_file)
		stat_name = "accesses_80"
		plots.plot_stat_w_mean(	input_data_file, stat_name, page_type, cache_type, op_type, plot_conf, output_file)


if (plot_cross_page_misses):
		
	benchsuite = "selected_qualcomm_srv_ap"	
	input_data_file = "./stats/" + benchsuite  + "_fdip_baseline2_l1d-p.berti_llc-s.1537-w.16.csv"
	#input_data_file = "./stats/" + "test"  + "_fdip_test_l1d-p.berti_llc-s.1537-w.16.csv"
	
	df = pd.read_csv(input_data_file, sep=',', index_col='benchmarks')
	l1d_df = df.loc[(df['CACHE'] == "cpu0_L1D") & (df['OP'] == 'TOTAL')]
	print(l1d_df)
	print(l1d_df['PAGE_CROSS_MISSES'].mean())	
	
	mean_sum = 0
	for cache in ["cpu0_ITLB", "cpu0_DTLB", "cpu0_STLB"]:
		stlb_df = df.loc[(df['CACHE'] == cache) & (df['OP'] == 'TOTAL')]
		print(stlb_df['MISS'].mean())	
		mean_sum += stlb_df['MISS'].mean()
			
	print((l1d_df['PAGE_CROSS_MISSES'].mean() * 100) / mean_sum)

