class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length=0
        current=head
        while current:   #calculate the length of the linked list
            length+=1
            current=current.next
        position=length-n+1
        
        current=head
        i=1
        while i<=length and current:
            if i==position==1:  #if we want to remove the 1st node, just move the head to the next node
                head=current.next
                break
            elif i==position==length-1:  # if we want to remove the last node, just remove the next node from the node positioned before the last node
                current.next=None
                break
            elif i==position-1:    # if we want to remove any node except the first and last
                current.next=current.next.next
                break
            i+=1         
            current=current.next
        return head 



"""
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

n=5

solution_instance=Solution()

result=solution_instance.removeNthFromEnd(head,n)

while result:
    print(result.val)
    result=result.next
"""