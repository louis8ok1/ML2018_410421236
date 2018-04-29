# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 22:57:32 2018

@author: louis
"""
import numpy as np
from PIL import Image
import math

#---------------------------------------------------------#
#load_data and preparing

k1 = Image.open("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\key1.png") 
k2 = Image.open("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\key2.png") 
I  = Image.open("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\I.png")
E  = Image.open("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\Eprime.png")
#k1.save("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\Check_k1_gray.png")

k1 = list(k1.getdata())
k2 = list(k2.getdata())
I  = list(I.getdata())
E  = list(E.getdata())

print(I)

learning_rate = 0.00001
Epoch = 1

w=np.random.rand(3)

print (w)



#=============================================================#





















