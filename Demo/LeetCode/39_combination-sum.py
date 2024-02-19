class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        startIndex = 0
        sum = 0
        path = []
        self.backtracking(candidates, target, result, startIndex, sum, path)
        return result

    def backtracking(self, candidates, target, result, startIndex, sum, path):
        if sum > target:
            return
        if sum == target:
            result.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            sum += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, result, i, sum, path)
            sum -= candidates[i]
            path.pop()


s = Solution()
print(s.combinationSum([2,3,6,7],7))