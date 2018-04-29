# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 22:57:32 2018

@author: louis
"""
import keras
import numpy as np

#load_data

test=np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\eprime.txt")



test.flatten("F")

print(test)
test=np.savetxt("test.txt",test)











