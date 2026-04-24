class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack of times that you look at from closest to target
        # at any point if the time to reach target of a rear fleet
        # is less than time of fleet infront you pop that cause it
        # becomes part of the front fleet

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            time = target - p
            time = time / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)