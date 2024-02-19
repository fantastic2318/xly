class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    # def __init__(self, node=None):
    #     self.__head = node
    #     self.__length = 0
    def __init__(self):
        self.__head = LinkNode()
        self.__length = 0

    def isEmpty(self):
        if self.__length == 0:
            return True
        else:
            return False

    def get(self, index: int) -> int:
        if index > self.__length or index < 0:
            return -1
        cur = self.__head
        for i in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = LinkNode(val)
        if self.__head.next:
            node.next = self.__head.next
            self.__head.next = node
        else:
            self.__head.next = node
        self.__length += 1

    def addAtTail(self, val: int) -> None:
        node = LinkNode(val)
        if self.__head.next:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.__head.next = node
        self.__length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.__length:
            return None
        elif index == self.__length:
            self.addAtTail(val)
        elif index <= 0:
            self.addAtHead(val)
        else:
            cur = self.__head
            node = LinkNode(val)
            for _ in range(index):
                cur = cur.next
            node.next = cur.next
            cur.next = node
            self.__length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.__length or index < 0:
            return None
        cur = self.__head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList(LinkNode())
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# param_1 = obj.get(1)
# print(param_1)
# obj.deleteAtIndex(1)
# param_2 = obj.get(1)
# print(param_2)

#["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
#[[],[1],[3],[1,2],[1],[1],[1]]

#["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
#[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3, 0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
param_1 = obj.get(4)
obj.addAtHead(4)
obj.addAtIndex(5, 0)
obj.addAtHead(6)
print(param_1)
# obj.deleteAtIndex(1)
# param_2 = obj.get(1)
# print(param_2)