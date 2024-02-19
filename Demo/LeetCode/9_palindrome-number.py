class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) == 0:
            return False
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] == x[right]:
                left += 1
                right -= 1
            return False
        return True
s = Solution()
print(s.isPalindrome(-121))