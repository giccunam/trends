#!/usr/bin/env python3
# by: Jazmin Lopez (ENES Morelia UNAM)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def A_fun(x):
    return 1/9.8e3*(x-31)**2+0.08

def B_fun(x):
    ya = A_fun(x)
    yb =(-1/7.45e2*(x-50)**2+5)/7
    if yb>1-ya:
        yb=abs(ya-yb/yb)        
    return yb

def C_fun(x):
    ya = A_fun(x)
    yb = B_fun(x)
    return 1-ya-yb

x = np.array(range(18,111))

yA = A_fun(x)

yB = np.array([B_fun(i) for i in x])

yC = np.array([C_fun(i) for i in x])

plt.plot(x,yA,'r',label="A")
plt.plot(x,yB,'g',label="B")
plt.plot(x,yC,'b',label="C")
plt.plot(x,yA+yB+yC,'k', label="A+B+C")
plt.legend(loc=2)
plt.show()

V = pd.DataFrame(index=x)
V['A']=yA
V['B']=yB
V['C']=yC

V.to_csv('votePerc.csv')
