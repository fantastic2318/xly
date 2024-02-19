class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []
        startIndex = 0
        self.backtracking(s, path, startIndex, res)
        return res

    def backtracking(self, s, path, startIndex, res):
        if startIndex == len(s):
            res.append(path[:])
            return
        for i in range(startIndex, len(s)):
            if self.isPalindrame(s, startIndex, i):
                path.append(s[startIndex:i+1])
            else:
                continue
            self.backtracking(s, path, i+1, res)
            path.pop()

    def isPalindrame(self, s, left, right) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


s = Solution()
print(s.partition("aab"))