#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

from people import People
import random
import numpy as np

class Population:

    population = []
    stat_population = {}

    def __init__(self, population):
        self.population = population
        
    def __init__(self, filename, npeople):
        total_population = 0
        probability_age = {}
        p = []
        with open(filename) as fp:
            lines = fp.readlines()
        data=[]            
        for line in lines:
            if not line.startswith("#"):
                data.append(line)
        for line in data:
            row = line.split()
            self.stat_population[int(row[0])] = float(row[2])
            if int(row[0]) >= 18:
                total_population = total_population + float(row[2])
        #for i in range(86):
        for i in range(86):            
            if i >= 18:
                #probability_age[j] = self.stat_population[j] / total_population             
                p.append(self.stat_population[i] / total_population)
        #print(probability_age)

        n = 85-18
        random.seed()
        choice = np.random.choice(68, npeople, p=p)
        for j in range(npeople):
            self.population.append(People(choice[j]+18,'none'))

        
#        for j in range(npeople): 
#            age = 0
#            while age < 18:
#                a = b = 0.0
#                x = random.random()
#                for i in range(85):
#                    a = b
#                    b = b + float(probability_age[i+1])
#                    #print(a,b)
#                    if ((a <= x) and (x < b)):
#                        age = i
#                        break
#            self.population.append(People(age,'none'))
#        
        
        

