class Solution:

    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k = k % len(nums)
        print id(nums)
        nums = nums[k:] + nums[:k]
        print id(nums)
        return nums

s = Solution()
l = [
    [[1], 0],
    [range(7), 3],
    [range(7)[::-1], 3],
]
for nums, k in l:
    print s.rotate(nums, k)
