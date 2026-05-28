class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initialize window
        l, r = 0, k - 1

        # max res array that you maintain
        maxElements = []

        # loop through windows keep track of max at each step and update
        for r in range(len(nums)):
            while (r - l + 1) > k:
                curMax = float("-inf")
                for i in range(l, r):
                    if nums[i] > curMax:
                        curMax = nums[i]
                maxElements.append(curMax)
                l += 1

        curMax = float("-inf")
        for i in range(len(nums) - k, len(nums)):
                if nums[i] > curMax:
                    curMax = nums[i]
        maxElements.append(curMax)

        return maxElements


