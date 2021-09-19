# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        else:
            answer = head
            for i in range(k-1):
                answer = answer.next
            cursor = head
            prev = None
            idx = 0
            
            stack = list()
            while cursor != None:
                
                if idx % k == k-1:
                    stack.append(cursor)
                    next = cursor.next
                    
                    start = stack[-1]
                    end = stack[0]

                    if prev != None:
                        prev.next = start

                    for i in range(1, k):
                        stack[i].next = stack[i-1]

                    end.next = next
                    prev = end

                    stack = []
                    cursor = next
                    
                    
                else:
                    stack.append(cursor)
                    
                    cursor = cursor.next
                
                idx += 1
            
            return answer
