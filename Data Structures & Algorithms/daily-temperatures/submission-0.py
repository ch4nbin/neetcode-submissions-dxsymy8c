class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain stack and pop when a larger value shows up
        res = [0] * len(temperatures)
        s = [] # store (temp, i)

        for i in range(len(temperatures)):
            while s and temperatures[i] > s[-1][0]:
                temp, index = s.pop()
                res[index] = (i - index)
            s.append((temperatures[i], i))
        return res