class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        path = []
        result = []
        startIndex = 1
        sum = 0
        self.backtracking(k, n, startIndex, sum, path, result)
        return result

    def backtracking(self, k, n, startIndex, sum, path, result):
        if len(path) == k:
            if sum == n:
                result.append(path[:])
            return
        for i in range(startIndex, 10):
            sum += i
            path.append(i)
            self.backtracking(k, n, i+1, sum, path, result)
            sum -= i
            path.pop()


s = Solution()
#print(s.combinationSum3(3, 7))

print(s.combinationSum3(3, 9))

print(s.combinationSum3(4, 1))
