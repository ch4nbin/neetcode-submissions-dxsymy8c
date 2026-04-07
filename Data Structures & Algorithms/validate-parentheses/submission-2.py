class Solution:
    def isValid(self, s: str) -> bool:
        # create dict of mappings
        # when you encounter an opneing paren append it to stack
        # when you come across a closing paren pop it and check

        mappings = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for c in s:
            if c in mappings:
                if stack and stack.pop() == mappings[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False

        return True