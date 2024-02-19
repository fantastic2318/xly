class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left)/2)
            print(mid)
            if nums[mid] == target:
                start = mid
                end = mid
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end < len(nums)-1 and nums[end+1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]


s = Solution()
print(s.searchRange(nums = [1], target = 1))
