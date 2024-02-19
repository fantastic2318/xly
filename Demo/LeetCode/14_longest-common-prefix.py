class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # 最小单元两个比较、然后用比较结果和第三个字符串比较
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.lcp(strs[i], prefix)
            if not prefix:
                break
        return prefix

    def lcp(self, str1, str2):
        length = min(len(str1), len(str2))
        index = 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str2[:index]

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
