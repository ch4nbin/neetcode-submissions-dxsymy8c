class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # half of the array is always sorted
        # if target is not in current half cut it off

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            val = nums[mid]

            if target == val:
                return mid
            elif nums[l] <= val:
                if target < nums[l] or target > val:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < val or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1