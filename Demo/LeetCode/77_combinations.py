class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []
        startIndex = 1
        self.backtracking(n, k, startIndex, path, result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n+1):
            path.append(i)
            self.backtracking(n, k, i+1, path, result)
            path.pop()


s = Solution()
print(s.combine(4, 2))
