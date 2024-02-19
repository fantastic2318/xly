class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        self.backtracking(res, path, used, nums)
        return res

    def backtracking(self, res, path, used, nums):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i] and used[i-1] == False:
                continue
            if used[i] == False:
                used[i] = True
                path.append(nums[i])
                self.backtracking(res, path, used, nums)
                used[i] = False
                path.pop()


s = Solution()
print(s.permuteUnique([1,1,2]))
