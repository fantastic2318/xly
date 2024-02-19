class MyStack:
    def __init__(self):
        self.__queueA = []
        self.__queueB = []

    def isEmpty(self):
        if self.__queueA is None and self.__queueB is None:
            return True
        else:
            return False

    def push(self, x):
        self.__queueA.append(x)

    def pop(self) -> int:
        if self.isEmpty():
            return None
        for _ in range(len(self.__queueA)-1):
            self.__queueB.append(self.__queueA.pop(0))
        self.__queueB, self.__queueA = self.__queueA, self.__queueB
        return self.__queueB.pop(0)

    def top(self):
        res = self.pop()
        self.__queueA.append(res)
        return res


s = MyStack()
s.push(1)
s.push(2)
print(s.top())
print(s.pop())
print(s.isEmpty())


