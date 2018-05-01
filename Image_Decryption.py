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
#使用文字檔處理會比較模糊 所以我改讀取圖片
"""
k1 = np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\k1.txt")
k2 = np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\k2.txt")
E  = np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\eprime.txt")
Eprime=np.loadtxt("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\eprime.txt")
I = imageio.imread("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\I.png")
"""
k1 = imageio.imread("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\key1.png")
k2  = imageio.imread("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\key2.png")
E = imageio.imread("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\E.png")
Eprime =imageio.imread("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\Eprime.png")
I = imageio.imread("G:\學校課堂資料\東華大三下\機器學習\ML_2018_410421236\data\I.png")

#print(I)
#==================================================================================================#



weight = np.random.rand(3)#讓權重有隨機的初始值
#Weight[0],weight[1],weight[2]

learning_rate=0.000001#當我嘗試調高學習率時，直接不能跑

MaxIterLimit=10


L = 400#data的length

W = 300#data的width

print(">初始 Random Weight:",weight)#看一下還沒訓練的隨機權重



#==================================================================================================#

#np.any() is  if ndarray have any true value and nonzero value ，return 0
#np.absolute() absolute value
def find_weight():
    Epoch = 1
    while (Epoch==1 or Epoch<MaxIterLimit and np.any(np.absolute(weight[1]-weight[0])>learning_rate)):
   
        for i in range(0,W):
        
            temp0=0
        
            for j in range(0,L):
                temp1 = weight[0]*k1[i][j]+ weight[1]*k2[i][j]+weight[2]*I[i][j]
            #被解密的照片的第[i][j]位置
                temp0 = E[i][j]-temp1 
            #變異量
                weight[0]=weight[0]+learning_rate*temp0*k1[i][j]
                weight[1]=weight[1]+learning_rate*temp0*k2[i][j]
                weight[2]=weight[2]+learning_rate*temp0*I[i][j]
                if(j%300==0 and i%300==0):
                    print(weight)
        print(">Epoch = ",Epoch)
        print(">Difference is:",temp0)
    
        Epoch += 1
    
    return weight


#=================================================================================================#
weight=find_weight()

print("After training weight =",weight)

ans_picture= (Eprime - (weight[0]*k1)-(weight[1]*k2))/weight[2]
           
plt.imshow(ans_picture,cmap="gray")

plt.savefig('G:\\學校課堂資料\\東華大三下\\機器學習\\ML_2018_410421236\\pic\\ans_picture',bbox_inches='tight')
plt.show()

    
          
           
        










