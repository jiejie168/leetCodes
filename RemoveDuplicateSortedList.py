__author__ = 'Jie'
"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current=head
        while current:
            runner=current.next
            while runner and current.val==runner.val:
                runner=runner.next
            current.val=runner
            current=runner # adjust the pointer to the current
        return head



