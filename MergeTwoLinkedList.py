__author__ = 'Jie'
'''
# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        curr=ListNode(0)
        dummy=curr
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        curr.next=l1 or l2
        return dummy.next

#### this is only for test on your own computuer
def myPrintList(l):
    while True:
        print(l.val)
        if l.next is not None:
            l = l.next
        else:
            break
##### when test on your own computer,  the create of the linked list.
##### this is important for you to understand more about the data structure of linked list.
def main():
    #     # 342 + 465 = 807
    l1=[1,2,3]
    l2=[4,5,6]
    l1_1 = ListNode(l1[0])
    l1_2 = ListNode(l1[1])
    l1_3 = ListNode(l1[2])
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(l2[0])
    l2_2 = ListNode(l2[1])
    l2_3 = ListNode(l2[2])
    l2_1.next = l2_2
    l2_2.next = l2_3

    l3 = Solution().mergeTwoLists(l1_1,l2_1)
    myPrintList(l3)
    myPrintList(l3)

if __name__ == '__main__':
    main()
