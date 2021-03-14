# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):

        answer = ListNode(-1)
        tmp = answer
        up = 0
        exp = 0
        while True:

            if l1 == None and l2 == None:
                if up == 1:
                    tmp.next = ListNode(up)
                break
            elif l1 == None and l2 != None:
                val = l2.val + up
                l2 = l2.next
            elif l2 == None and l1 != None:
                val = l1.val + up
                l1 = l1.next
            else:
                val = l1.val + l2.val + up
                l1 = l1.next
                l2 = l2.next

            if val >= 10:
                up = 1
                val -= 10
            else:
                up = 0

            if tmp.val == -1:
                tmp.val = val
            else:
                tmp.next = ListNode(val)
                tmp = tmp.next

            exp += 1

        return answer
