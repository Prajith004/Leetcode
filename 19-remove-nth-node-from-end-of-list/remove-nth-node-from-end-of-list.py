# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_h=ListNode()
        current=dummy_h
        count=0
        temp=head

        while temp:
            count+=1
            temp=temp.next
        if count>1:
            while head:
                if count!=n:
                    val=head.val
                    current.next= ListNode(val)
                    current=current.next
                head=head.next
                count-=1
        return dummy_h.next

        