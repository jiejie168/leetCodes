__author__ = 'Jie'
# coding=utf8
"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        #Kadane algorithm
        max_end_here=nums[0]
        max_so_far=nums[0]
        for x in nums[1:]:
            max_end_here=max(x,max_end_here+x)
            max_so_far=max(max_so_far,max_end_here)
        return max_so_far

    def maxSubArray_1(self,nums,l,r):
        # using divide and conquer algorithm
        # l,r is the index of left end and right end of nums
            #1) Divide the given array in two halves
            #2) Return the maximum of following three
            #.a) Maximum subarray sum in left half (Make a recursive call)
            #.b) Maximum subarray sum in right half (Make a recursive call)
            #.c) Maximum subarray sum such that the subarray crosses the midpoint
        # the base case, only one element in nums.
        if l==r:
            return nums[l]
        mid=(l+r)//2
        return max(self.maxSubArray_1(nums,l,mid),self.maxSubArray_1(nums,mid+1,r),self.maxCrossSubArray(nums,l,mid,r))

    def maxCrossSubArray(self,nums,l,m,r):
        # include element on the left part of mid
        sm=0
        left_sum=-10000
        for i in range(m,l-1,-1):
            sm=sm+nums[i]
            if sm>left_sum:
                left_sum=sm
        sm=0
        right_sum=-10000
        for i in range(m+1,r+1):
            sm=sm+nums[i]
            if sm>right_sum:
                right_sum=sm
        return left_sum+right_sum


nums=[-2,1,-3,4,-1,2,1,-5,4]
solution=Solution()
# max1=solution.maxSubArray(nums)
max2=solution.maxSubArray_1(nums,0,len(nums)-1)
print (max2)


