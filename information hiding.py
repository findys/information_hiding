# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 17:45:56 2016

@author: findys
"""

import random
import numpy as np
from scipy.misc import imsave
 
size = 600
a = np.random.randint(0,255,size = [size,size])
print a
imsave('original.jpg', a)
print '\n'

delta = 20    # delta-B的值
n = 10       #总的帧数
location = 300
#生成用delta-B调制过的帧

def fun(i):
    for j in range(size):
        if i % 2 == 0:
            a[location][j] -= delta
            b = a
        else:
            a[location][j] += delta
            b = a
    return b
    

for k in range(10):
    print fun(k)
    print '\n'

imsave('zhen9.jpg', fun(9))
imsave('zhen10.jpg', fun(10))

#初始化sum为全零数组
sum = np.zeros([size,size])
print sum
print '\n'

# S(x,y)实现
for k in range(10):
    if (k % 2 == 0):
        sum -= fun(k)
    else:
        sum += fun(k)

print sum


imsave('test.jpg', sum)
