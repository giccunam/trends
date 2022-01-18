#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx


#people1 = People(18,'catolico')
#people2 = People(19,'musulman')
#people = [people1,people2]
#population_test = Population(people)

from population import Population
from probability_function import P_function
from montecarlo import Montecarlo
import people

print('Creating Population')
mexico = Population('/home/vdelaluz/data/inegi2020/INEGI_exporta_11_1_2022_10_12_31.txt',100)
print('Creating P_by_age Function')
P_by_age = P_function('/home/vdelaluz/data/surveys/vote_by_age.csv',3)
print('Creating Montecarlo')
ballot_2020_mx = Montecarlo(P_by_age,mexico) 
print('Voting...')
result_of_ballot = ballot_2020_mx.vote()
print('Results')
print(result_of_ballot)
