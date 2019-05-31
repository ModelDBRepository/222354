
""" this extra function extra_gui_driver.hoc will create (write) a bunch of
build_net_Shep_NSG_gui_X.hoc's where X=0,1,2,...,num_of_jobs-1
Subsequently starting the first one with 
nrngui build_net_Shep_NSG_gui_0.hoc post_process.hoc
will run them all.

The first batch of 16 runs with onset=(1.5/12)2pi
and the second batch of 16 runs with onset=(7.5/12)2*pi
"""
import os
num_of_runs=16
# since the code has the onset set for the first case
# we only need to reference the run_num in the output
# graph file (actually this may be done with other variables)
# and reading in the hoc files in the run_X folders
for run_num in range(num_of_runs):
  print run_num
  # copy over the first section of build_net_Shep...
  os.system('echo run_num=%d > build_net_Shep_NSG_gui_%d.hoc'%(run_num,run_num))
  ## the 789 lines locates just before a parameters_dot_hoc_file assignment statement just a 
  ## a few (5) lines from the bottom of the build_net_Shep_NSG_gui.hoc file
  os.system("head -789 build_net_Shep_NSG_gui.hoc >> build_net_Shep_NSG_gui_%d.hoc"%run_num)
  f=open("build_net_Shep_NSG_gui_%d.hoc"%run_num,"a")
  filecontents="""  parameters_dot_hoc_file = "run_%d/parameters.hoc"
"""%(run_num)
  print filecontents
  print run_num
  f.write(filecontents)
  f.close()  # now append the rest of the file then add calling next
  os.system("tail -4 build_net_Shep_NSG_gui.hoc >> build_net_Shep_NSG_gui_%d.hoc"%run_num)
  f=open("build_net_Shep_NSG_gui_%d.hoc"%run_num,"a")
  # adding calling next
  if run_num<num_of_runs-1: # here last calls next group instead of run_num<num_of_runs-1:
      f.write("""
system("nrngui build_net_Shep_NSG_gui_%d.hoc post_process.hoc&")
      """%(run_num+1))
  f.close()

