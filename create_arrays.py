#import itertools
#import numpy

# below creates symmetrical arrays
add_columns=[1]

#B=range(20,780,20)# /1.0 # 0.0 20.0 ... 620.0
#(start, stop, step)
B=[200, 200, 200, 200]

#S=range(20,780,20) #/1.0 # [50 50 ... 50 50]
S=[40, 100, 160, 0]

#both=list(itertools.product(B,S))
both=zip(B,S)

# net_type=['full_net','pg_net','gc_net']

net_type=['noinhib_net','pg_net','gc_net','gc_net']
gc_strength=['4'       ,     '4',     '4',    '30']

#net_type=['full_net','gc_net','full_net','gc_net','full_net','gc_net','full_net','gc_net']
#gc_strength=['10', '10', '20','20', '30','30','40','40']

