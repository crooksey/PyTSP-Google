Example output for dummy data:

##############################################################################
Optimised Route
##############################################################################
Total Time 5.95 hours
Total Distance 274.23 miles
{'lat': 50.8166745, 'lng': -1.0833259, 'address': u'Portsmouth, UK'}
{'lat': 51.4544776, 'lng': -0.9781547, 'address': u'Reading, UK'}
{'lat': 50.7150463, 'lng': -1.9872525, 'address': u'Poole, UK'}
{'lat': 50.7335746, 'lng': -2.7583416, 'address': u'Bridport, Dorset DT6, UK'}
{'lat': 50.9096948, 'lng': -1.4047779, 'address': u'Southampton, UK'}
{'lat': 50.8166745, 'lng': -1.0833259, 'address': u'Portsmouth, UK'}
##############################################################################
Original Route
##############################################################################
Total Time 7.32 hours
Total Distance 334.71 miles
{'lat': 50.8166745, 'lng': -1.0833259, 'address': u'Portsmouth, UK'}
{'lat': 50.9096948, 'lng': -1.4047779, 'address': u'Southampton, UK'}
{'lat': 50.7150463, 'lng': -1.9872525, 'address': u'Poole, UK'}
{'lat': 51.4544776, 'lng': -0.9781547, 'address': u'Reading, UK'}
{'lat': 50.7335746, 'lng': -2.7583416, 'address': u'Bridport, Dorset DT6, UK'}
{'lat': 50.8166745, 'lng': -1.0833259, 'address': u'Portsmouth, UK'}
##############################################################################
Summary
##############################################################################
'''
The optimised route is 60.48 miles shorter
And also saves 1.36 hours of time
'''

###############################################################################
time python tsp.py
real	0m5.843s
user	0m0.128s
sys	0m0.040s
###############################################################################
# Taken on a virtualmachine, specs:
'''
luke@virtualbox:~/python/PyTSP-Google$ free -m
             total       used       free     shared    buffers     cached
Mem:          4872       1932       2940          0        321        672
-/+ buffers/cache:        938       3933
Swap:         4935          0       4935
luke@virtualbox:~/python/PyTSP-Google$ cat /proc/cpuinfo 
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 21
model		: 2
model name	: AMD FX(tm)-8320 Eight-Core Processor           
stepping	: 0
cpu MHz		: 3481.497
cache size	: 2048 KB
fdiv_bug	: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 5
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx fxsr_opt rdtscp extd_apicid pni monitor ssse3 cr8_legacy arat
bogomips	: 6962.99
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management:
'''