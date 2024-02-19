# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.__head = ListNode(0)
        self.__length = 0

    def get_head(self):
        return self.__head

    def append(self, val):
        node = ListNode(val)
        cur = self.__head
        if self.__head.next:
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.__head.next = node
        self.__length += 1

    def nodes_list(self):
        res = []
        cur = self.__head
        while cur.next:
            res.append(cur.next.val)
            cur = cur.next
        return res


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

#head = [1,2,3,4,5]

linklist = LinkList()
for i in [1,2,3,4,5]:
    linklist.append(i)
print(linklist.nodes_list())
s = Solution()
pre = s.reverseList(linklist.get_head().next)
res = []
while pre:
    res.append(pre.val)
    pre = pre.next
print(res)
