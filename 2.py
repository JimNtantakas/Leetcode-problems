class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        llist=ListNode()
        while l1.next!=None and l2.next!=None:
            print("compared: ",l1.val,l2.val)
            if l1.val<=l2.val:
               llist.val=l1.val
               l1=l1.next
               llist.next=ListNode()
               #print(llist.val)
               llist=llist.next
            elif l1.val>l2.val:
               llist.val=l2.val
               l2=l2.next
               llist.next=ListNode()
               #print(llist.val)
               llist=llist.next
        
        while llist:
            print(llist.val)
            llist=llist.next
            
    
    
        
    
num1=ListNode()
num1.val=2
num2=ListNode()
num1.next=num2
num2.val=66
num3=ListNode()
num2.next=num3
num3.val=999
#num2.next=None

num4=ListNode()
num5=ListNode()
num4.val=5
num4.next=num5
num5.val=89
num6=ListNode()
num3.next=num6
num6.val=8898
#num4.next=None

solution=Solution()
solution.addTwoNumbers(num1,num4)
