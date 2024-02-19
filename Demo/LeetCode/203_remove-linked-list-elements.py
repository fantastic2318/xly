# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self, node=None):
        self.__head = node
        self.__length = 0

    # 因为是私有变量、所以需要单独写一个函数
    def get_head(self):
        return self.__head

    def isEmpty(self):
        if self.__length == 0:
            return True
        else:
            return False

    def append(self, val):
        node = ListNode(val)
        if self.__head:
            cur = self.__head
            while cur.next:
                cur = cur.next
            # 让当前的尾节点的指针域指向node
            cur.next = node
        else:
            self.__head.next = node
            # 链表的长度+1
        self.__length += 1

    def add(self, val):
        # 往链表的头部添加一个节点,值为val
        # 新建一个节点node
        node = ListNode(val)
        # None.prev
        if self.isEmpty():
            self.__head.next = node
        else:
            # 先让node指向当前链表中的头结点
            node.next = self.__head.next
            # 再让链表的head指向当前node节点
            self.__head.next = node
        # 添加节点之后,链表的长度加1
        self.__length += 1

    def nodes_list(self):
        # 返回链表中的所有节点的值组成的列表
        res = []
        cur = self.__head
        while cur.next:
            res.append(cur.next.val)
            cur = cur.next
        return res


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next


s = Solution()
head = ListNode()
linklist = LinkList(head)
for i in [1, 2, 3, 4, 5, 6]:
    linklist.append(i)
s.removeElements(linklist.get_head(), 6)
print(linklist.nodes_list())
