__author__ = 'Jie'

'''
28. Implement strStr()
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        leng=len(haystack)
        if needle=="":
            return 0

        for i in range(leng-len(needle)+1):
                if haystack[i:i+len(needle)] ==needle:
                    return i
        return -1
haystack="aaabbb"
needle="bb"

solution=Solution()
val=solution.strStr(haystack,needle)
print(val)