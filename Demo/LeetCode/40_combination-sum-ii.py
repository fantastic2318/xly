class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []
        used = [False for _ in range(len(candidates))]
        sum = 0
        startIndex = 0
        candidates.sort()
        self.backtracking(candidates, target, result, path, sum, used, startIndex)
        return result

    def backtracking(self, candidates, target, result, path, sum, used, startIndex):
        if sum == target:
            result.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            if sum + candidates[i] > target:
                return
            if i > 0 and candidates[i-1] == candidates[i] and used[i-1] == False:
                continue
            sum += candidates[i]
            path.append(candidates[i])
            used[i] = True
            self.backtracking(candidates, target, result, path, sum, used, i+1)
            sum -= candidates[i]
            path.pop()
            used[i] = False


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

