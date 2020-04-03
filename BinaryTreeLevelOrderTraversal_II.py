__author__ = 'Jie'

"""
107. Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        # just use the in order to print out each node
        if root is None:
            return []
        result,current=[],[root]
        while current:
            next_level,vals=[],[]  # vals for the restore of current values
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                current=next_level
            result.append(vals)
        return result[::-1]  # output of results in the reversed sequence.


