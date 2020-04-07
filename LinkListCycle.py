__author__ = 'Jie'
"""
141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # utilize the hash_table method
        new_has=set() # create a non-key dictionary, every element occurs once
        while head:
            if head in new_has:
                return True
            new_has.add(head)
            head=head.next
        return False
    def hasCycle_1(self,head):
        # use the two pointers method
        fast,slow=head,head
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
            if fast==slow:
                return True
        return False

aa=set()
list1=[1,2,3,4,5,6,6]
for elm in list1:
    aa.add(elm)
print (aa)
b=int(0)
if b not in aa:
    print (True)

