__author__ = 'Jie'
"""
136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""
from collections import defaultdict
class Solution:
    def singleNumber(self, nums) -> int:
        # iteration O(n2)
        new=[]
        for elem in nums:
            if elem not in new:
                new.append(elem)
            else:
                new.remove(elem)
        return new.pop()

    def singleNumber_1(self,nums):
        # hash-table, time complexity is O(n)
        hash_table=defaultdict(int)
        for elem in nums:
            hash_table[elem] +=1
        for i in hash_table:
            if hash_table[i]==1:
                return i
    def singleNumber_2(self,nums):
        # math:  2*(a+b+c)-(a+a+b+b+c)=c
        return 2*sum(set(nums))-sum(nums)


solution=Solution()
nums=[4,1,2,1,2]
ans=solution.singleNumber_2(nums)
print (ans)



