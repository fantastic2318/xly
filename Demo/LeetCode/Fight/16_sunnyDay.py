# import heapq
# def topFrequent(nums, k):
#     map = {}
#     for i in range(len(nums)):
#         map[nums[i]] = map.get(nums[i], 0) + 1
#
#     pri_que = []
#
#     for key, freq in map.items():
#         heapq.heappush(pri_que, (freq, key))
#         if len(pri_que) > k:
#             heapq.heappop(pri_que)
#
#     result = [0] * k
#     for i in range(k-1, -1, -1):
#         result[i] = heapq.heappop(pri_que)[1]
#
#     return result

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right):  # 从左向右
                if len(ans) < len(matrix) * len(matrix[0]):
                    ans.append(matrix[top][i])
            for j in range(top, bottom):  # 从上向下
                if len(ans) < len(matrix) * len(matrix[0]):
                    ans.append(matrix[j][right])
            for i in range(right, left, -1):  # 从右向左
                if len(ans) < len(matrix) * len(matrix[0]):
                    ans.append(matrix[bottom][i])
            for j in range(bottom, top, -1):  # 从下向上
                if len(ans) < len(matrix) * len(matrix[0]):
                    ans.append(matrix[j][left])
            top += 1
            right -= 1
            bottom -= 1
            left += 1
        if len(matrix) == len(matrix[0]) and len(matrix) % 2 ==1:
            ans.append(matrix[len(matrix) // 2][len(matrix) // 2])
        return ans

s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print(s.spiralOrder([[6,9,7]]))