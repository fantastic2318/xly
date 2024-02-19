# import heapq
# class Solution:
#     def GetLeastNumbers_Solution(self , input: list[int], k: int) -> list[int]:
#         # write code here
#         pri_que = []
#         for i in input:
#             heapq.heappush(pri_que, i)
#             if len(pri_que) > k:
#                 heapq.heappop(pri_que)
#         res = [0] * k
#         for i in range(k):
#             res[i] = heapq.heappop(pri_que)
#         return res
#
# s = Solution()
# print(s.GetLeastNumbers_Solution([1,2,3,4,5,6,7,8], 4))

import heapq
class Solution:
    def GetLeastNumbers_Solution(self , input: list[int], k: int) -> list[int]:
        # write code here
        pri_que = []
        for i in input:
            heapq.heappush(pri_que, -i)
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        res = []
        for i in range(k-1, -1, -1):
            res.append(-pri_que[i])
        return res



s = Solution()
print(s.GetLeastNumbers_Solution([1,2,3,4,5,6,7,8], 4))