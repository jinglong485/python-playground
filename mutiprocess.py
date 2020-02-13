import random
import threading
import time
import multiprocessing

import psutil
pt = psutil.Process()
all_cpus = list(range(psutil.cpu_count()))
pt.cpu_affinity(all_cpus)
pt.cpu_affinity()

def getPi(num=10000):
    k = 0
    r = 1.0
    for _ in range(num):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < r:
            k=k+1
    pi = 4* float(k)/float(num)
    print('PI is: {}'.format(pi))
    
MC_loop = 100000
core_num = 100#multiprocessing.cpu_count()

time_start_mp = time.time()
for _ in range(core_num):
    p = multiprocessing.Process(target = getPi(MC_loop))
    p.start()
    #p.join()
time_end_mp = time.time()
print('The total time is:{}'.format(time_end_mp-time_start_mp))

time_start_mt = time.time()
for _ in range(core_num):
    t = threading.Thread(target = getPi(MC_loop))
    t.start()
    #t.join()
time_end_mt = time.time()
print('The total time is:{}'.format(time_end_mt-time_start_mt))
