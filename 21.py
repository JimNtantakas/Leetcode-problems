# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        current=dummy=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                current.next=ListNode(list1.val)
                list1=list1.next
            else:
                current.next=ListNode(list2.val)
                list2=list2.next
            current=current.next

        #Check if one of the lists has remaining nodes , if yes add them to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
                
        return dummy.next
    
"""   
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(8)
l1.next.next.next=ListNode(9)
l1.next.next.next.next=ListNode(11)
l1.next.next.next.next.next=ListNode(12)

l2=ListNode(3)
l2.next=ListNode(4)

solution_instance=Solution()
head=solution_instance.mergeTwoLists(l1,l2)

while head:
    print(head.val)
    head=head.next
    
"""