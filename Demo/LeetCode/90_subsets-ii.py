class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        used = [False for _ in range(len(nums))]
        startIndex = 0
        path = []
        res = []
        nums.sort()
        self.backtracking(nums, startIndex, path, used, res)
        return res

    def backtracking(self, nums, startIndex, path, used, res):
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            if i > 0 and used[i-1] == False and nums[i-1] == nums[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, i+1, path, used, res)
            path.pop()
            used[i] = False


s = Solution()
print(s.subsetsWithDup([4,4,4,1,4]))



