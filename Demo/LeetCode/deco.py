def wrapper3(f3):
    print("in the wrapper3")
    def inner3(*args, **kwargs):
        print("in inner3")
        ret = f3(*args, **kwargs)
        print("333")
        return ret
    return inner3

def wrapper2(f2):
    print("in the wrapper2")
    def inner2(*args, **kwargs):
        print("in inner2")
        ret = f2(*args, **kwargs)
        print("222")
        return ret
    return inner2

def wrapper1(f1):
    print("in the wrapper1")
    def inner1(*args, **kwargs):
        print("in inner1")
        ret = f1(*args, *kwargs)
        print("111")
        return ret
    return inner1


@wrapper3
@wrapper2
@wrapper1
def func():
    print("in func")

func()

#1 func = wrapper3(func) --> f3 = func -->打印in wrapper3 --> func = inner3
# 2 func = wrapper2(func)即 func = wrapper2(inner3) -->f2 = inner3 --> 打印in wrapper2 --> func = inner2