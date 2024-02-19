def mySqrt(x):
    left = 0
    right = x
    while left <= right:
        mid = left + int((right-left)/2)
        if x > mid * mid:
            left = mid + 1
        elif x < mid * mid:
            right = mid - 1
        else:
            return mid
    return right

#print(mySqrt(4))
print(mySqrt(12))