# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = True
        if head == None or head.next == None:
            return head
        else:
            answer = head.next
            cursor = head
            prev = None
            
            while cursor.next != None:
                next = cursor.next
                
                if flag:
                    
                    cursor.next = next.next
                    next.next = cursor
                    if prev != None:
                        prev.next = next
                    
                    prev = next
                    cursor = cursor

                    flag = False
                else:
                    
                    flag = True
                
                    prev = cursor
                    cursor = next
            
            return answer
