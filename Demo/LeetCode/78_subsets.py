class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        startIndex = 0
        path = []
        self.backtracking(res, startIndex, path, nums)
        return res

    def backtracking(self,res, startIndex, path, nums):
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(res, i+1, path, nums)
            path.pop()


s = Solution()
print(s.subsets([1,2,3]))


