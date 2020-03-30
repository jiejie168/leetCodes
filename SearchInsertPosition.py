__author__ = 'Jie'

'''
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1
'''

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # method 1
        nums.append(target)
        nums.sort()
        for i,elem in enumerate(nums):
            if elem==target:
                return i

    def searchInset_2(self,nums,target):
        # method 2
        if target>nums[-1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i]>=target:
                return i


nums=[1,3,5,6]
target=5.5
solution=Solution()
index=solution.searchInsert(nums,target)
index1=solution.searchInset_2(nums,target)
print (index1)



