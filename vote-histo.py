#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab

filename = 'vote_1000.dat'
#filename = 'population.dat'
with open(filename) as fp:
    lines = fp.readlines()
data=[]            
for line in lines:
    if not line.startswith("#"):
        data.append(line)

A =[]
B= []
C= []
        
for line in data:
    row = line.split()
    A.append(int(row[0]))
    B.append(int(row[1]))
    C.append(int(row[2]))


#rng = np.random.RandomState(10)  # deterministic random data
#a = np.hstack((rng.normal(size=1000),
#               rng.normal(loc=5, scale=2, size=1000)))

#bins = np.arange(18,86)
#print(bins)
n, bins, patches = plt.hist(C, bins='auto',density=True)  # arguments are passed to np.histogram
plt.title("Candidate C")
#Text(0.5, 1.0, "Histogram with 'auto' bins")

(mu, sigma) = norm.fit(C)
y = norm.pdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r-', linewidth=2)

print("C="+str((mu/200000)*100)+"% error="+str((sigma/200000)*100)+"%")

#plt.show()
