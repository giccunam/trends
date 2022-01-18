#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

import random

class People:
    age = 0
    religion = 'none'
    
    def __init__(self, age, religion):
        self.age = age
        self.religion = religion

    #               x
    #!-----!----------------!-------------!
    #0 A  rp[0]    B   rp[0]+rp[1]  C    1.0
    def vote(self, rp):
        x = random.random()
        if (x < rp[0]):
            return 'A'
        elif ((x >= rp[0]) and (x < (rp[0]+rp[1]))):
            return 'B'
        else:
            return 'C'
              
