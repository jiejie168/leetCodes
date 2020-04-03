__author__ = 'Jie'
"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:

        def to_bst(nums,start,end):
            if start>end:
                return None
            mid=(start+end)//2
            node=TreeNode(nums[mid])
            node.left=to_bst(nums,start,mid-1)
            node.right=to_bst(nums,mid+1,end)
            return node
        return to_bst(nums,0,len(nums)-1)

