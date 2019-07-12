

#n1->n2->n3

def reverseList(head):
    if not head or not head.next:
        return head
    n = reverseList(head)
    head.next.next = head
    head.next = None
    return n
