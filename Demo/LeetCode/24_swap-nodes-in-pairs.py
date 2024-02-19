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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next != None and cur.next.next != None:
            tmp = cur.next
            tmp1 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = tmp
            cur.next.next.next = tmp1
            cur = cur.next.next
        return dummy_head.next


linklist = LinkList()
for i in [1,2,3,4]:
    linklist.append(i)
print(linklist.nodes_list())

s = Solution()
head = s.swapPairs(linklist.get_head().next)
cur = head
res = []
while cur:
    res.append(cur.val)
    cur = cur.next
print(res)






