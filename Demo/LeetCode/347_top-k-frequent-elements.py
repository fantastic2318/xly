import heapq


def topkFrequent(nums, k):
    hashmap = dict()
    pri_que = []
    for i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

    for key, v in hashmap.items():
        heapq.heappush(pri_que, (v, key))
        if len(pri_que) > k:
            heapq.heappop(pri_que)

    res = [0] * k
    for i in range(k-1, -1, -1):
        res[i] = heapq.heappop(pri_que)[1]

    return res


print(topkFrequent([1,1,1,2,2,3], 2))
