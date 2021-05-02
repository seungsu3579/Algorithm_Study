# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):

        cursor = head
        count = 0
        tmp = []

        while cursor != None:
            
            count += 1
            tmp.append(cursor)
            cursor = cursor.next
        
        if n == 1:
            tmp[count - 1].next = None
        elif count - n > 0:
            tmp[count - n - 1].next = tmp[count - n + 1]
        elif count - n == 0:
            head = head.next
        
        return tmp[0]

        