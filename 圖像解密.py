# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:13:24 2018

@author: louis
"""
import imageio
import numpy as np
import matplotlib.pyplot as plt

#==================================================================================#
#load_data

#用np.loadtxt來讀取數值
k1 = np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\k1.txt", dtype=int)
k2 = np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\k2.txt", dtype=int)
E  = np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\eprime.txt", dtype=int)


#發現i.txt只有一個數值，所以就處理相片來獲取資料
I = imageio.imread("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\I.png")
Eprime=np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\eprime.txt", dtype=int)
print(I)
print("---------------------")
print(Eprime)
Epoch = 10
#讓權重有隨機的初始值
weight = np.random.rand(3)

learning_rate=0.00001

L = 400

W = 300

print("Random Weight:",weight)

while True:
    
    for i in range(W):
        
        temp_weight=weight.sum()
        
        temp0=0
        
        for j in range(L):
            temp1 = weight[0]*k1[i][j]+ weight[1]*k2[i][j]+weight[2]*I[i][j]
            temp2 = E[i][j]-temp1 
            
            weight[0]=weight[0]+learning_rate*temp2*k1[i][j]
            weight[1]=weight[1]+learning_rate*temp2*k2[i][j]
            weight[2]=weight[2]+learning_rate*temp2*k1[i][j]
        
    Epoch += 1
   
    if Epoch >=3:
           
           p= (E - (weight[0]*k1)-(weight[1]*k2))/weight[2]
           
           plt.imshow(p,cmap="gray")
           plt.show()
           
           ap= (Eprime - (weight[0]*k1)-(weight[1]*k2))/weight[2]
           
           plt.imshow(ap,cmap="gray")
           plt.show()
          
          
           
        










