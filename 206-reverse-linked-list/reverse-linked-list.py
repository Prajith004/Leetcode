# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_h=ListNode()
        current=dummy_h
        lst=[]
        while head:
            ele=head.val
            lst.append(ele)
            head=head.next
        lst.reverse()
        for i in lst:
            newnode=ListNode(i)
            current.next=newnode
            current=current.next
        return dummy_h.next



        