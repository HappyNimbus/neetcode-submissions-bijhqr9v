# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tempNode = None
        curr = head

        while curr:
            temp1 = curr.next
            curr.next = tempNode

            tempNode = curr
            curr = temp1
        
        return tempNode
