__author__ = 'Jie'
'''
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip(" ")
        s=list(s.split(" "))
        leng=len(s[-1])
        return leng

solution=Solution()
s="nihao wo shi shui ? "
leng=solution.lengthOfLastWord(s)
print (leng)

