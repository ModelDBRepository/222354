This file was created from
inputfile_from_20150902_light1_incr20_4xgc.zip from 20150918
simple_circuit contains modifications to have stimuli as specified in
Shaina's email 20150921

The general scheme for performing the task of creating eps file traces
will be to

1) set up the model as usual with create_arrays

2) modify the model so that it just runs a few cycles with the new
stimulation timing (don't use the varying length breath and stimulus
windows - just use a fixed 400 ms time interval for both and offset
them as specified
(1.5/12)*2pi start Stim and
(7.5/12)*(2pi) start Sim
