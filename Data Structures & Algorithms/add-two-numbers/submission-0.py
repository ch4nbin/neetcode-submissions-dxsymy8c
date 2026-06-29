# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 3 pass? 1 for each list to accululate digits into a
        # respective string and then last pass to build
        # the output linked list should be N time for all of them
    
        cur = l1
        string1 = ""
        while cur:
            curVal = cur.val
            string1 = str(curVal) + string1
            cur = cur.next

        cur = l2
        string2 = ""
        while cur:
            curVal = cur.val
            string2 = str(curVal) + string2
            cur = cur.next
        
        sumVal = str(int(string1) + int(string2))

        seen = {}
        amount = len(str(sumVal)) - 1
        while (amount > -1):
            seen[amount] = ListNode(int((sumVal[amount])))
            amount -= 1


        amount = len(str(sumVal)) - 1
        while amount > -1:
            cur = seen[amount]
            if amount > 0:
                temp = amount - 1
                cur.next = seen[temp]
            amount -= 1

        return seen[len(str(sumVal)) - 1]

