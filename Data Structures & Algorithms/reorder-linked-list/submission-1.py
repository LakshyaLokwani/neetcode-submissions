# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = slow.next
        slow.next = None

        current = second
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            
        second = previous



        while first is not None and second is not None:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
            

    
        