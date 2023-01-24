'''
Author: JIAlonglong
Date: 2023-01-24 22:34:40
LastEditors: JIAlonglong 2495477531@qq.com
LastEditTime: 2023-01-24 23:29:46
FilePath: /d_learn_ws/src/dp_myself/chapter1_numpy_network/test.py
Description: 

Copyright (c) 2023 by JIAlonglong 2495477531@qq.com, All Rights Reserved. 
'''
import numpy as np
import matplotlib.pyplot as plt

def draw_scatter(x,y):
    plt.scatter(x.ravel(),y.ravel())
    plt.show()

def layer(in_dim,out_dim):
    weights=np.random.normal(loc=0,scale=0.1,size=[in_dim,out_dim])
    bias=np.full([1,out_dim],0.1)
    return{"w":weights,"b":bias}
    
#data
x=np.linspace(-1,1,10)[:,None]#主要用来创建等差数列
y=np.random.normal(loc=0,scale=0.2,size=[10,1])+x#生成一个以Y轴来进行正态分布，scale表示

draw_scatter(x,y)##绘制散点图
