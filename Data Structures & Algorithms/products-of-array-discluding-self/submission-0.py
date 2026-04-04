class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_count = 0
        product = 1
        for n in nums:
            if n != 0:
                product *= n
            else:
                zero_count += 1

        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
        elif zero_count > 1:
            return [0] * len(nums)
        else:
            for i in range(len(nums)):
                nums[i] = product//nums[i]

        return nums
