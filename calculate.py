import pandas as pd
import numpy as np
from math import log, factorial, exp
from parameters import matches, clubs

teams = pd.Series.tolist(clubs['name'])

def getHUB (club1, club2):
    res = [0.4018, 0.12033, 1.0478] # results from trained model in parameters.py
    
    spi1 = clubs.loc[clubs['name'] == club1, 'spi'].iloc[0]
    spi2 = clubs.loc[clubs['name'] == club2, 'spi'].iloc[0]
    
    lam1 = (res[0]+res[1])*exp(res[2]*(spi1/spi2))
    lam2 = (res[0])*exp(res[2]*(spi2/spi1))
    
    g1 = [lam1**0*exp(-lam1)/factorial(0), lam1**1*exp(-lam1)/factorial(1), lam1**2*exp(-lam1)/factorial(2), lam1**3*exp(-lam1)/factorial(3), lam1**4*exp(-lam1)/factorial(4), lam1**5*exp(-lam1)/factorial(5)]
    g2 = [lam2**0*exp(-lam2)/factorial(0), lam2**1*exp(-lam2)/factorial(1), lam2**2*exp(-lam2)/factorial(2), lam2**3*exp(-lam2)/factorial(3), lam2**4*exp(-lam2)/factorial(4), lam2**5*exp(-lam2)/factorial(5)]
    
    h=0
    u=0
    b=0
    for i in range(5):
        for j in range(5):
            if i > j:
                h += g1[i]*g2[j]
            elif i == j:
                u += g1[i]*g2[j]
            else:
                b += g1[i]*g2[j]
    
    #return [g1, g2], [h, u, b]
    return [h, u, b]
    #return str(h)