class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letterMap = ["", "", "abc", "def", "ghi", 'jkl', "mno", "pqrs", "tuv", "wxyz"]
        index = 0
        result = []
        s = ""
        self.backtracking(digits, s, index, result, letterMap)
        return result

    def backtracking(self, digits, s, index, result, letterMap):
        if len(digits) == 0:
            return [""]
        if index == len(digits):
            result.append(s)
            return
        digit = int(digits[index])   # 转化成数字
        letter = letterMap[digit]   # 找到对应的字符串
        for i in range(len(letter)):
            s += letter[i]
            self.backtracking(digits, s, index+1, result, letterMap)
            s = s[0:-1]
        return result


s = Solution()
print(s.letterCombinations("23"))
