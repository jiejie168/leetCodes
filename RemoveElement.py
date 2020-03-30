__author__ = 'Jie'

"""
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
"""

class Solution:
    def removeElement(self, nums, val: int) -> int:

        if nums is None:
            return 0

        leng=len(nums)
        count=0

        for i in range(leng):
            if nums[i]!=val:
                nums[count]=nums[i]  #  noted that we can not creat a new array. So just use the same array nums.
                count+=1
        return count