class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        startIndex = 0
        self.backtracking(nums, res, path, startIndex)
        return res

    def backtracking(self, nums, res, path, startIndex):
        if len(path) >= 2:
            res.append(path[:])
        set_list = set()
        for i in range(startIndex, len(nums)):
            if (len(path) and nums[i] < path[-1]) or nums[i] in set_list:
                continue
            path.append(nums[i])
            set_list.add(nums[i])
            self.backtracking(nums, res, path, i+1)
            path.pop()


s = Solution()
print(s.findSubsequences([4, 6, 7, 7]))