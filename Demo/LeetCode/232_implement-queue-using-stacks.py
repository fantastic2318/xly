class Myqueue:
    def __init__(self):
        self.__stackA = []
        self.__stackB = []

    def isEmpty(self):
        if self.__stackA is None or self.__stackB is None:
            return True
        else:
            return False

    def push(self, x):
        self.__stackA.append(x)

    def pop(self):
        if self.isEmpty():
            return None
        if self.__stackB:
            return self.__stackB.pop()
        else:
            for _ in range(len(self.__stackA)):
                self.__stackB.append(self.__stackA.pop())
            return self.__stackB.pop()

    def peek(self):
        res = self.pop()
        self.__stackB.append(res)
        #print(self.__stackB)
        return res


q = Myqueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.isEmpty())