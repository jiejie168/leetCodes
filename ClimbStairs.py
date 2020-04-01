__author__ = 'Jie'
"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        #  it is a fiponacci series
        prev,curr=0,1
        for i in range(n):
            prev,curr=curr,curr+prev
        return curr

    def climbStairs_1(self,n):
        # use an array restoring all  fiponacci series
        # dp algorithm
        array_=np.array([None]*(n+2))
        array_[0]=0
        array_[1]=1
        for i in range(2,n+2):
            array_[i]=array_[i-1]+array_[i-2]
        return array_[n+1]

    def climStaires_2(self,n):
        # recuisive method
        return self.fob(n+1)

    def fob(self,n):
        if n<=1:
            return n
        return self.fob(n-1)+self.fob(n-2)



solution=Solution()
# n=solution.climbStairs(3)
# n=solution.climbStairs_1(3)
n=solution.climStaires_2(6)
print (n)

