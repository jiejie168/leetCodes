__author__ = 'Jie'

"""
100. Same Tree
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # pre order traversal tree
        # recusion
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        return False

    def isSameTree_1(self,p,q):
        # utilize the iteration method
        def check(p,q):
            if p is None and q is None:
                return True
            if not p  or not q:
                return False
            if p.val!=q.val:
                return False
            return True

        de=deque([(p,q),])
        while de:
            p,q=de.popleft()
            if not check(p,q):
                return False
            if p:
                de.append([(p.left,q.left),])
                de.append([(p.right,q.right),])
        return True






# de=deque([1,2,3])
# de.append(4)
# print (de)
# de.appendleft(0)
# print (de)
# de.pop()
# print (de)
# de.popleft()
# print (de)


