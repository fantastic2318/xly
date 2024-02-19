class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        minValue = float("inf")
        nums.sort()
        for i in range(len(nums)):
            # if (i > 0 and nums[i] == nums[i - 1]):
            #     continue
            left = i+1
            right = len(nums)-1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == target:
                    return target
                if abs(threeSum - target) < abs(minValue - target):
                    minValue = threeSum
                if threeSum - target < 0:
                    left += 1
                else:
                    right -= 1
        return minValue

s = Solution()
#print(s.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(s.threeSumClosest(nums = [0,0,0], target = 1))