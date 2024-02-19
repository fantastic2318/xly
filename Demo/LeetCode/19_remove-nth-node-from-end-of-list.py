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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next=head)
        slowIndex = dummy_head
        fastIndex = dummy_head
        for _ in range(n+1):
            fastIndex = fastIndex.next
        while fastIndex != None:
            slowIndex = slowIndex.next
            fastIndex = fastIndex.next
        slowIndex.next = slowIndex.next.next
        return dummy_head.next

linklist = LinkList()
for i in [1]:
    linklist.append(i)
print(linklist.nodes_list())
s = Solution()
print(linklist.get_head().next.val)
head = s.removeNthFromEnd(linklist.get_head().next, 1)
res = []
cur = head
while cur:
    res.append(cur.val)
    cur = cur.next
print(res)




