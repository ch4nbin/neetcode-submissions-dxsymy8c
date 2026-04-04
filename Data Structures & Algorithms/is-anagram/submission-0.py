class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seen = {}
        for c in s:
            seen[c] = seen.get(c, 0) + 1
        
        for c in t:
            if c not in seen:
                return False
            elif seen[c] == 0:
                return False
            else:
                seen[c] = seen.get(c) - 1

        return True 