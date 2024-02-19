def sortedSquares(nums: list[int]) -> list[int]:
    k = len(nums)-1
    i = 0
    j = len(nums)-1
    res = [0]*len(nums)
    while i <= j:
        if nums[i]*nums[i] < nums[j]*nums[j]:
            res[k] = nums[j]*nums[j]
            j -= 1
        else:
            res[k] = nums[i]*nums[i]
            i += 1
        k -= 1
    return res

#print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))
