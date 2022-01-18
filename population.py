#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

from people import People
import random

class Population:

    population = []
    stat_population = {}

    def __init__(self, population):
        self.population = population
        
    def __init__(self, filename, npeople):
        total_population = 0
        probability_age = {}
        with open(filename) as fp:
            lines = fp.readlines()
        data=[]            
        for line in lines:
            if not line.startswith("#"):
                data.append(line)
        for line in data:
            row = line.split()
            self.stat_population[int(row[0])] = float(row[2])
            total_population = total_population + float(row[2])
        for i in range(86):
            probability_age[i] = self.stat_population[i] / total_population

        print(probability_age)
        x = random.random()
        age = 0

        for j in range(npeople): 
            while age < 18:
                a = b = 0
                for i in range(85):
                    a = b
                    b = b + probability_age[i+1]
                    if ((a <= x) and (x < b)):
                        age = i
                        break
            self.population.append(People(age,'none'))
        
        
        

