#!/usr/bin/python
"""init_dev.py
develop with this to run simulation individually
1) make a place to set the the stimulus and breath phases
2) create the stimulus and breath events from that
3) create the special graphs
4) run the simulation
5) save the graphs

When this works individually can consider to run the whole thing on NSG
"""
"""init.py 
Relies on pre_init.py having been run and then the archive compressed
(zip'ed) and uploaded to the NSG.  This file will start a parallel
context, forms three relevant file/folder variables (the relative
paths to and then loads) the num_of_columns.hoc and parameters.hoc,
and the path to tdt2mat_data). Then the build_net_Shep_NSG.hoc which runs
the simulations.  Subsequently the tanks are written in the
appropriate location.

"""

#from mpi4py import MPI
from neuron import h, gui
#pc = h.ParallelContext()
#id = int(pc.id())
#nhost = int(pc.nhost())
#print "I am", id, "of", nhost
id = 0 # try the no inhib net first alhough this shouldn't matter
# form the three relevant files/folders based on id
#if id<12:
import os
for id in range(12):
  run_folder = "run_%d"%(id) # helper folder name variable
  parameters_dot_hoc_file = run_folder+"/parameters.hoc"
  num_of_columns_dot_hoc_file = run_folder+"/num_of_columns.hoc"
  tank_folder = "tdt2mat_data/"
  #tank_folder = run_folder+"_tdt2mat_data_"
  
  # make these variables exist in NEURON so the approp. files and can be loaded/saved
  # The first two are used in buil_net_Shep_NSG.hoc and the tank_folder is used
  # in this NSG version of tdt2mat_data.hoc
  
  h("strdef parameters_dot_hoc_file")
  h("strdef num_of_columns_dot_hoc_file")
  h("strdef tank_folder")
  
  h('parameters_dot_hoc_file="%s"'%(parameters_dot_hoc_file))
  h('num_of_columns_dot_hoc_file="%s"'%(num_of_columns_dot_hoc_file))
  h('tank_folder="%s"'%(tank_folder))
  
  # create the simulation model structure, run and store
  h.xopen("build_net_Shep_NSG_gui.hoc")
  # the _gui version of build_net_Shep_NSG.hoc will do the 5 steps listed
  # at the top of this file
  os.getcwd()
  h.xopen("post_process.hoc")
  
