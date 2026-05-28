class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # if t (key str) is empty return 0
        if t == "":
            return 0

        # initialize hashmaps for freq of chars in t and curWindow
        countT, curWindow = {}, {}

        # populate initial hash for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # keep track of comparison values (need = len(countT))
        # because thats how many unique chars there are in t
        have, need = 0, len(countT)

        # keep track of res
        resWindow = [0, 0]
        minLength = float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]

            # add new char to window (update window step)
            curWindow[c] = 1 + curWindow.get(c, 0)

            # check if c is in t if the count of c in t
            # equals count of c in cur window (see if condition
            # is satistfied)
            if c in countT and curWindow[c] == countT[c]:
                have += 1

            # if we found new res update res stores and 
            # the window
            while have == need:
                # update result if its a new min
                if (r - l + 1) < minLength:
                    resWindow = [l, r]
                    minLength = (r - l + 1)

                c = s[l]
            
                # update window
                curWindow[c] -= 1
                if c in countT and curWindow[c] < countT[c]:
                    have -= 1
                l += 1
        
        # retrive vals
        l, r = resWindow

        return s[l:r+1] if minLength != float("infinity") else ""

            

        
