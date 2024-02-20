class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        current=dummy=ListNode()    
        remainder=0
        while l1 and l2:
            sum=l1.val+l2.val+remainder
            if sum>9:
                remainder=1
                sum-=10
            else:
                remainder=0
     
            current.next=ListNode(sum)
            l1=l1.next
            l2=l2.next
            current=current.next

        #Check if one of the lists has remaining nodes, if yes add them 
        if l1 or l2:
            while l1 or l2:
                if l1:
                    sum=l1.val+remainder
                    l1=l1.next
                else:
                    sum=l2.val+remainder 
                    l2=l2.next
                if sum>9:
                    remainder=1
                    sum-=10
                else:
                    remainder=0
                current.next=ListNode(sum) 
                current=current.next    
        
        if remainder==1:
            current.next=ListNode(1)
        return dummy.next
    
   
""" 
l1=ListNode(9)
l1.next=ListNode(9)
l1.next.next=ListNode(9)
l1.next.next.next=ListNode(9)
l1.next.next.next.next=ListNode(9)
l1.next.next.next.next.next=ListNode(9)
l1.next.next.next.next.next.next=ListNode(9)

l2=ListNode(9)
l2.next=ListNode(9)
l2.next.next=ListNode(9)
l2.next.next.next=ListNode(9)

solution_instance=Solution()
head=solution_instance.addTwoNumbers(l1,l2)

while head:
    print(head.val)
    head=head.next

"""