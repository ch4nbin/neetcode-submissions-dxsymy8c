class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # only two possibilities at a given index either the 
        # chars match or they dont if they do inrecement both
        # indexes if not you take the max of the 2 spawned 
        # subranches where you opnly increment one of the strings
        # since its bottom pu recursion the highest count match
        # from all the spawned threads will end up at the current level
        # you just memoized and by the time you reach the top level
        # itll be the very highest val
        memo = {}
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + helper(i + 1, j + 1)
            else:
                memo[(i,j)] = max(helper(i + 1, j), helper(i, j + 1))
            return memo[(i,j)]
        
        return helper(0,0)