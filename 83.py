class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def deleteDuplicates(head):
    start=head
    while head and head.next:
        if head.val==head.next.val:
            head.next=head.next.next
        else:
            head=head.next
    return start

"""
head=ListNode(1)
head.next=ListNode(1)
head.next.next=ListNode(2)
head.next.next.next=ListNode(3)

head=deleteDuplicates(head)

while head:
    print(head.val)
    head=head.next
"""
