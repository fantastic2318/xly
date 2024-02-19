def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    k = m + n - 1
    m = m - 1
    n = n - 1
    while n >= 0 and m >= 0:
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
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

