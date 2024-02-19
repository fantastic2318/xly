# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        lenA = 0
        lenB = 0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        reA = headA
        reB = headB
        if lenA > lenB:
            for _ in range(lenA-lenB):
                reA = reA.next
        else:
            for _ in range(lenB-lenA):
                reB = reB.next
        while reA != reB:
            reB = reB.next
            reA = reA.next
        return reA

