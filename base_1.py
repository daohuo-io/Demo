#!/usr/bin/python
# encoding=UTF-8

'''
@author: cloud
@contact: 
@file: base_1.py
@time: 2020/10/18 4:37 PM
@desc: data_type
'''
#Assignment operation
width = 20
height = 5 * 9
print(width * height)

#string index
word = 'python'
print(word[5])

#string slice
word = 'python'
print(word[2:4])



#List splicing
squares = [1, 4, 9, 16, 25]
squares + [26, 49, 64, 81]



#list index
squares = [1, 4, 9, 16, 25]
print(squares[-2])


#list slice
squares + [26, 49, 64, 81]
print(squares[3:6])


#斐波那契数列
a, b = 0, 1
while a < 300:
    print(a, end=',')  #加End换行
    a, b = b, a+b


