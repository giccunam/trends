#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

import numpy as np
import matplotlib.pyplot as plt

filename = 'vote.dat'
#filename = 'population.dat'
with open(filename) as fp:
    lines = fp.readlines()
data=[]            
for line in lines:
    if not line.startswith("#"):
        data.append(line)

#A =[]
#B= []
#C= []
#        
#for line in data:
#    row = line.split()
#    A.append(int(row[0]))
#    B.append(int(row[1]))
#    C.append(int(row[2]))


age = []

for line in data:
    age.append(int(line))

#print(age)

rng = np.random.RandomState(10)  # deterministic random data
#a = np.hstack((rng.normal(size=1000),
#               rng.normal(loc=5, scale=2, size=1000)))

bins = np.arange(18,86)
print(bins)
histo = plt.hist(age, bins=bins)  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
#Text(0.5, 1.0, "Histogram with 'auto' bins")
plt.show()
