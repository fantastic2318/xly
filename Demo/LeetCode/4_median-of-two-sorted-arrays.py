class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = m + n -1
        m = m - 1
        n = n - 1
        nums1 = nums1 + nums2
        print(nums1)
        # 先合并两个数组、然后偶数取中间两个数相加然后除2、奇数取中间的数
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
                k -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
                k -= 1
        while n >= 0:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1
        print(nums1)
        a = int(len(nums1) / 2)
        if len(nums1) % 2 == 0:
            return (nums1[a-1]+nums1[a]) / 2
        else:
            return nums1[a]




s = Solution()
print(s.findMedianSortedArrays([100001], [100000]))