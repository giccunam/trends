#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

from probability_function import P_function

class Montecarlo:
    P_by_age = P_function()
    population = Population()
    poll = {}
    
    def __init__(self, P, population):
        self.P_by_age = P
        self.population = population
        self.poll['A'] = 0
        self.poll['B'] = 0
        self.poll['C'] = 0
        
        
    def vote(self):
        for person in self.population:
            range_of_probability = self.P_by_age.get_range(person.age)
            candidate = person.vote(range_of_probability)
            self.poll[candidate] = self.poll[candidate] + 1            
        return self.poll

    

