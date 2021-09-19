# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        nodes = list()

        cursor = head

        while cursor != None:
            nodes.append(cursor)
            cursor = cursor.next

        if len(nodes) < 2:
            return head
        else:
            real_k = k % len(nodes)

            start = nodes[ (-1) * real_k ]
            nodes[-1].next = nodes[0]
            nodes[(-1)*real_k - 1].next = None
            

            return start