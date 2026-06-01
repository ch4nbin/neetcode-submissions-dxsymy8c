class Solution:
    def findMin(self, nums: List[int]) -> int:
        # one half of the array is always sorted
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l) // 2

            if nums[mid] > nums [r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]