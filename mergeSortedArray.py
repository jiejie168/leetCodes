__author__ = 'Jie'

"""
88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
"""
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[m-1+n]=nums2[n-1]
                n=n-1
            else:
                # all put the largest digit on the farest right place,
                # use 0 replace the original place
                nums1[m-1],nums1[m-1+n]=nums1[m-1+n],nums1[m-1]
                m=m-1
        if m==0 and n>0:
            nums1[:n]=nums2[:n]
        return nums1

nums1 = [6,8,9,0,0,0,0,0]
m = 3
nums2 = [1,2,5,6,8]
n = 5
solution=Solution()
result=solution.merge(nums1,m,nums2,n)
print (result)



