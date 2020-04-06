__author__ = 'Jie'

"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None :
            return True
        s="".join(ele for ele in s if ele.isalnum())
        s=s.lower()
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True

solution=Solution()
s="A man, a plan, a canal: Panama"
ans=solution.isPalindrome(s)
print (ans)