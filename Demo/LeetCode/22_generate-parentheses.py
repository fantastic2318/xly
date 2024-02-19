class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []
        left = n
        right = n
        self.dfs(res, left, right, path)
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append("".join(path))
            return
        if left > 0:
            path.append("(")
            self.dfs(res, left-1, right, path)
            path.pop()
        if left < right:
            path.append(")")
            self.dfs(res, left, right-1, path)
            path.pop()

s = Solution()
print(s.generateParenthesis(3))