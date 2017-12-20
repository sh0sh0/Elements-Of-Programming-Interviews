#define the new class for ListNode
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


# convert lst to a linked list, and return that
def genList(lst):
    R = None
    for i in range(len(lst)-1, -1, -1):
        R = ListNode(lst[i], R)
    return R

# combining two linked list into one
def combine(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next

def main():
    L1 = genList([1, 5])
    L2 = genList([4])
    print(L1)
    print(L2)
    LR = combine(L1, L2)
    print(LR)
    

if __name__ == "__main__":
    main()
    
