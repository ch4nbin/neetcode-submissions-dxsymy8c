"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # use a hashmap and map cur nodes to copies so you can
        # index vals easily. 2 pass appoach first pass
        # you just create all the copies and map to hash
        # second pass you do all the pointers by using hash indexes

        copyDict = { None : None }

        cur = head
        while cur:
            copyDict[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = copyDict[cur]
            copy.next = copyDict[cur.next]
            copy.random = copyDict[cur.random]
            cur = cur.next

        return copyDict[head]
