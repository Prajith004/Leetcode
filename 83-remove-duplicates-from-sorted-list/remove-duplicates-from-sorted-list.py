# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        dummy_h=ListNode()
        current=dummy_h
        while head:
            ele=head.val
            if ele not in lst:
                current.next=ListNode(ele)
                current=current.next
                lst.append(ele)
            head=head.next

        return dummy_h.next

            
            

        return dummy_h
        