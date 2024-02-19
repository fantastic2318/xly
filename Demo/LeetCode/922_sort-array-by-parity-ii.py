class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        i = 0
        while i < len(nums):
            if (self.is_odd(i) == True and self.is_odd(nums[i]) == True) or \
                (self.is_odd(i) == False and self.is_odd(nums[i]) == False):
                i += 1
            elif self.is_odd(i) == True:
                tmp = i
                while self.is_odd(nums[i]) == False:
                    i += 1
                nums[tmp], nums[i] = nums[i], nums[tmp]
                i = tmp + 1
            elif self.is_odd(i) == False:
                tmp = i
                while self.is_odd(nums[i]) == True:
                    i += 1
                nums[tmp], nums[i] = nums[i], nums[tmp]
                i = tmp + 1
        return nums


    def is_odd(self, i):
        if i % 2 != 0:
            return False
        return True


s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))
print(s.sortArrayByParityII([2,3]))

# 方法二

def sortArrayByParityII2(self, nums: list[int]) -> list[int]:
    result = len(nums) * [0]
    oddIndex = 1
    evenIndex = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result[evenIndex] = nums[i]
            evenIndex += 2
        else:
            result[oddIndex] = nums[i]
            oddIndex += 2
    return result