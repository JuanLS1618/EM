# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:48:27 2023

@author: lemas
"""


import matplotlib.pyplot as plt
import numpy as np
import math as mt


def EM(pos_x):
    E_naught =8
    k = 5
    omega = 6
    j = 0 
    t= 1
    re = []
    while j < len(pos_x):
        m = E_naught*mt.cos(omega*t - pos_x[j] *k)
        re.append(m)
        j+=1
        
    j = 0 
    im = []
    while j < len(pos_x):
        m = E_naught*mt.sin(omega*t - pos_x[j] *k)
        im.append(m)
        j+=1
    complex_array = np.array([re,im],dtype = complex)
    return complex_array

pos_x = []
i =0
while i < 90: #x coordinate list
    pos_x.append(i)
    i+= 12
    

xpoints = pos_x
ypoints = EM(pos_x)[1]
plt.plot(xpoints, ypoints)
plt.show()
