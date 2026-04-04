class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for n in nums:
            res[n] = res.get(n, 0) + 1

        arr = []
        for n, c in res.items():
            arr.append([c, n])
        arr.sort()

        count = 0
        out = []
        while(count < k):
            out.append(arr.pop()[1])
            count += 1
        return out




