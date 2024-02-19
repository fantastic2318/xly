def isHappy(n: int) -> bool:
    res = set()
    while True:
        n = func(n)
        if n == 1:
            return True
        if n in res:
            return False
        else:
            res.add(n)


def func(n):
    sum = 0
    while n!= 0:
        sum += (n % 10) * (n % 10)
        n = n // 10
    return sum


#print(isHappy(19))
print(isHappy(2))