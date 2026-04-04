class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            if n not in seen:
                seen[n] = i + 1

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in seen:
                return [i + 1, seen[diff]]