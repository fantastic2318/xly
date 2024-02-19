class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) > 12:
            return []
        startIndex = 0
        pointNum = 0
        self.backtracking(s, startIndex, pointNum, res)
        return res

    def backtracking(self, s, startIndex, pointNum, res):
        if pointNum == 3:
            if self.isValid(s, startIndex, len(s)-1):
                res.append(s)
            return
        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, pointNum+1, res)
                s = s[:i+1] + s[i+2:]
            else:
                continue

    def isValid(self, s, start, end):
        if start > end:
            return False
        if s[start] == "0" and start != end:
            return False
        for i in range(start, end + 1):
            if s[i] > '9' or s[i] < "0":
                return False
        if not 0 <= int(s[start: end+1]) <= 255:
            return False
        return True


s = Solution()
print(s.restoreIpAddresses("25525511135"))