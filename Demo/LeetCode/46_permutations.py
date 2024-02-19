class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        used = [False for _ in range(len(nums))]
        path = []
        self.backtracking(res, used, path, nums)
        return res

    def backtracking(self, res, used, path, nums):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] == True:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(res, used, path, nums)
            used[i] = False
            path.pop()


s = Solution()
print(s.permute([1, 2, 3]))


