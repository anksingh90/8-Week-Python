
class List:
    def __init__(self, val=0, next=None):
        # val hold present value of the list
        # next : hold next value in the list
        self.val = val
        self.next = next
        
    # Dunder method to print object value
    def __repr__(self):
        result = []         # list to hold values
        current = self      # counter to point present/new value
        while current is not None:
            result.append(current.val)      # adding value into new list
            current = current.next
        return str(result)                  # returning value in string format

class Soln:
    def mergeTwoLists(self, lst1, lst2):
        x = List()
        temp = x

        while lst1 and lst2:
            if lst1.val < lst2.val:
                temp.next = lst1
                lst1 = lst1.next
            else:
                temp.next = lst2
                lst2 = lst2.next
            temp = temp.next

        if lst1:
            temp.next = lst1
        else:
            temp.next = lst2

        return x.next


# main()
# Building lst1 : (The chain: 1 -> 2 -> 4)

node_a3 = List(4)       # variable node_a3 holds - 4
node_a2 = List(2, node_a3)  # variable node_a2 holds - 2 & points next node to node_a3
lst1 = List(1, node_a2)     # declared list lst1 : hold first value - 1 & points next node to node_a2

# Same Building lst2: 1 -> 3 -> 4
# node_b3 = List(4) (Creates the tail)
# node_b2 = List(3, node_b3) (Creates the middle link, points it to the tail)
# lst2 = List(1, node_b2) (Creates the head, points it to the middle link)

node_b3 = List(4)
node_b2 = List(3, node_b3)
lst2 = List(1, node_b2)

obj = Soln()            # obj created for Soln()
merged = obj.mergeTwoLists(lst1, lst2)      # called mergeTwoLists and passed (lst1, lst2)

print(f"Merged List : {merged}")       # output - Merged List : [1, 1, 2, 3, 4, 4]
