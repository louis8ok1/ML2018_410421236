# Machine Learning 2018,NDHU #
## 參數設定 ##
>Epoch = 1
>>
>weight=[random_value,random_value,random_value]
>>
>MaxIterLimit = 10
>>
>Learning_rate=0.000001
>>
>temp0=E[i][j]-temp1
>變化量
## 經過訓練的權重 ##
>weight[0]=0.2497264 
>>
>weight[1]=0.66036318
>>
>weight[2]=0.08956617
## 如何把圖片讀入model ##
>使用imageio模組來讀圖片
## 成果 ##
  解密後的照片
>>
![](https://raw.githubusercontent.com/louis8ok1/ML2018_410421236/master/ans_picture.png)
## 心得 ##
這次的作業我認為對我的幫助非常大，從一開始完全沒頭緒如何讓程式讀照片到最後解碼後的照片被順利解出來時，中間學習到非常多的知識。像是學習率一開始絕對不能調太高，學習率就像是我們自己在學習時如果太自信滿滿認為已經學過的話，那train出來的成果一定非常差。一開始在讀入data時，我是使用numpy來讀文字檔，可是不知道為什麼最後權重訓練得不好導致圖片很不清楚，之後就換用imageio來讀照片當作data。

