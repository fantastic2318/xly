class Solution:
    def isPalindrome(self, s: str) -> bool:
        oriLength = len(s)
        s = list(s.lower().strip())
        tmp = []
        for i in s:
            if (i >= "A" and i <= "Z") or (i >= "a" and i <= "z") or (i >= "0" and i <= "9"):
                tmp.append(i)
        if len(tmp) == 0:
            return True
        left = 0
        right = len(tmp) - 1
        while left < right:
            if tmp[left] == tmp[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

s = Solution()
#print(s.isPalindrome(" A man, a plan, a canal: Panama    "))
print(s.isPalindrome("a."))
