class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # append to stack and when you come across operator pop 2

        ops = set()
        ops.add('-')
        ops.add('+')
        ops.add('*')
        ops.add('/')

        stack = []

        for t in tokens:
            if len(stack) >= 2 and t in ops:
                first = int(stack.pop())
                second = int(stack.pop())
                if t == '+':
                    stack.append(second + first)
                elif t == '-':
                    stack.append(second - first)
                elif t == '*':
                    stack.append(second * first)
                elif t == '/':
                    stack.append(int(second / first))
            else:
                stack.append(int(t))
        return stack.pop()

