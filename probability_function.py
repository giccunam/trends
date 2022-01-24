#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

import people
import population

class P_function:

    P = {}
        
    def __init__(self, filename, noptions):
        with open(filename) as fp:
            lines = fp.readlines()
        data=[]            
        for line in lines:
            if not line.startswith("#"):
                data.append(line)
        for line in data:
            row = line.split(',')
            #print(row)
            self.P[int(row[0])] = [float(row[1]),float(row[2]),float(row[3])]
    
    def get_range(self,age):
        return self.P[age]
