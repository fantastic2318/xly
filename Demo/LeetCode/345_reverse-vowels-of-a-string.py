# 反转字符串中的元音
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'u', 'o', "A", "E", "I", "U", "O"]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                #self.reverse1(s, left, right)
                left += 1
                right -= 1
            elif s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                return "".join(s)
        return "".join(s)

s = Solution()
#print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
