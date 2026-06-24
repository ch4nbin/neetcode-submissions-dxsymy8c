# at every step you have 2 choices take 2 back and cur or one back
# take the max

class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        maxVal = 0
        twoBack = 0
        oneBack = 0

        for n in nums:
            maxVal = max(twoBack + n, oneBack)
            twoBack = oneBack
            oneBack = maxVal
        
        return maxVal

