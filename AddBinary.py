__author__ = 'Jie'

"""
67. Add Binary
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # str[:::]=>  str[start,end,step]
        result, carry,val="",0,0  # val is the added value of current loop
        for i in range(max(len(a),len(b))):
            val=carry
            if i<len(a):
                val+=int(a[-(i+1)])
            if i<len(b):
                val+=int(b[-(i+1)])
            carry,val=val//2,val%2
            result+=str(val)
        if carry:
            result+=str(1)
        return result[::-1]

a="1010"
b="1"
solution=Solution()
result=solution.addBinary(a,b)
print(result)

