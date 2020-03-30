__author__ = 'Jie'

import numpy as np
from matplotlib import pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
from scipy.optimize import fminbound
from sympy import Symbol, Derivative
from sympy import *
import csv
import matplotlib.transforms
import matplotlib as mpl
import matplotlib.animation as animation
from matplotlib.widgets import  Slider
from matplotlib.widgets import TextBox

# L=100
# w0m=10
# s=0.01
# num=8.9868   # nL=8.986
# x=np.linspace(-0.5,0.5,200)
# w0=s/15.7*(1+8.9868**2/8-(num*x)**2/2-np.cos(num*x)/np.cos(8.9868/2))

# w0_cos=s*np.cos(np.pi*x)
#
# plt.plot(x,w0,'k-',linewidth=2)
# plt.plot(x,w0_cos,linewidth=2)
# ax=plt.gca()
# ax.set_ylim(0,)
# ax.xaxis.set_ticks(np.arange(-0.5,0.55,0.1))
#
# ax=plt.gca()
# ax.set_xlabel("Normalized pipe length")
#
# xmajorFormatter = mpl.ticker.FormatStrFormatter('%3.1f')
# ymajorFormatter=mpl.ticker.FormatStrFormatter('%4.3f')
# ax.xaxis.set_major_formatter(xmajorFormatter)
# ax.yaxis.set_major_formatter(ymajorFormatter)
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_position(('data',0))
# ax.tick_params(left=False,right=False,top=False,bottom=True,direction='out',pad=4,labelsize=10)
#
# ax.set_ylabel("Imperfection amplitude")
# ax.set_yticklabels([])
#
#
# plt.show()

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if l1==None:
#             return l2
#         if l2==None:
#             return l1
#
#         carry=0
#         dummy=ListNode(0)
#         p=dummy
#
#         while l1 and l2:
#             p.next=ListNode((l1.val+l2.val+carry)%10)
#             carry=(l1.val+l2.val+carry)//10
#             l1=l1.next
#             l2=l2.next
#             p=p.next
#         if l2:
#             while l2:
#                 p.next=ListNode((l2.val+carry)%10)
#                 carry=(l2.val+carry)//10
#                 l2=l2.next
#                 p=p.next
#         if l1:
#             while l1:
#                 p.next=ListNode((l1.val+carry)%10)
#                 carry=(l1.val+carry)//10
#                 l1=l1.next
#                 p=p.next
#         if carry==1:
#             p.next=ListNode(1)
#         return dummy.next
#
# def myPrintList(l):
#     while True:
#         print(l.val)
#         if l.next is not None:
#             l = l.next
#         else:
#             break
#
# def main():
#     #     # 342 + 465 = 807
#     l1_1 = ListNode(3)
#     l1_2 = ListNode(4)
#     l1_3 = ListNode(2)
#     l1_1.next = l1_2
#     l1_2.next = l1_3
#
#     l2_1 = ListNode(4)
#     l2_2 = ListNode(6)
#     l2_3 = ListNode(5)
#     l2_1.next = l2_2
#     l2_2.next = l2_3
#
#     l3 = Solution().addTwoNumbers(l1_1, l2_1)
#     myPrintList(l3)
#
# if __name__ == '__main__':
#     main()

# def longestCommonPrefix(strs):
#     def commonPrefix(left,right):
#         min_len = min(len(left), len(right))
#         for i in range(min_len):
#             if left[i] != right[i]:
#                 return left[:i]
#         return left[:min_len]
#
#     def find_longestCommonPrefix(strs, left_index, right_index):
#         if left_index == right_index:
#             return strs[left_index]
#         # recursive call
#         else:
#             mid_index = (left_index + right_index)//2
#             lcpLeft = find_longestCommonPrefix(strs,left_index, mid_index)
#             lcpRight = find_longestCommonPrefix(strs,mid_index+1,right_index)
#             return commonPrefix(lcpLeft,lcpRight)
#
#     if not strs: return ""
#     return find_longestCommonPrefix(strs, 0, len(strs)-1)
#
# strs=["flower","flow","flight"]
# a=longestCommonPrefix(strs)
# print (a)

# def commonfix(left,right):
#     min_len=min(len(left),len(right))
#     for i in range(min_len):
#         if left[i]!=right[i]:
#             return left[:i]
#     return left[:min_len]
#
# left="flow"
# right="a1"
# aa=commonfix(left,right)
# print (aa)

# str_input="[{"
# s={']':"[",'}':'{',')':'('}
# stack=[]
#
# for elem in str_input:
#
#     if elem in s:
#         print (elem)
#         if stack:
#             pop=stack.pop()
#         else:
#             '#'
#         if s[elem]!=pop:
#             print (False)
#     else:
#         stack.append(elem)

import turtle as p

def drawFace(x,y):
    p.pencolor('red')
    p.fillcolor('red')
    p.begin_fill()
    p.circle(50)
    p.end_fill()

# drawFace(0,0)
x1,x2=Symbol('x1'),Symbol('x2')
y=x1**2+x2*x1+x1**3
y_prime=y.diff(x1)
print (y_prime)