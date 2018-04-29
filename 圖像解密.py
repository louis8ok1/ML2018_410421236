# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 22:57:32 2018

@author: louis
"""
import keras
import numpy as np

#load_data

test=np.loadtxt("eprime.txt")



test.flatten("F")

print(test)
test=np.savetxt("test.txt",test)











