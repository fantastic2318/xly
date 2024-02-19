# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = list1
        while list1.next and list2:
            if list1.next.val < list2.val:
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                node.next = list1.next
                list1.next = node
                list2 = list2.next
        if list1 and list1.next:
            list1.next = list2
        return head

