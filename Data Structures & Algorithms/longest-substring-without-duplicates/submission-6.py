class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        maxSub = 0
        l, r = 0, 1

        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxSub = max(maxSub, len(seen))
            r += 1
        return maxSub


