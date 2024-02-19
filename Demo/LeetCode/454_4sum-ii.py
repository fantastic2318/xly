def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    hashmap = {}
    count = 0
    for i in nums1:
        for j in nums2:
            if i+j in hashmap:
                hashmap[i+j] += 1
            else:
                hashmap[i+j] = 1

    for i in nums3:
        for j in nums4:
            if 0-i-j in hashmap:
                count += hashmap[-i-j]
    return count


print(fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
print(fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))


