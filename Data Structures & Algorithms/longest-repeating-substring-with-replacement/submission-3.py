class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #
        #
        #
        freqs = {}
        l = 0

        res = 0
        curFreq = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            curFreq = max(curFreq, freqs[s[r]])

            while (r - l + 1) - curFreq > k:
                freqs[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        return res
