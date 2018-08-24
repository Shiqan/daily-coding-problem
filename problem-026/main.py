#!/usr/bin/env python
""" Problem 26 daily-coding-problem.com """


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return " -> ".join([str(i.value) for i in self])

    def __iter__(self):
        cur = self
        while cur is not None:
            yield cur
            cur = cur.next


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return " -> ".join([str(i.value) for i in self.head])

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def remove_element(self, k):
        main_ptr = self.head
        ref_ptr = self.head 
     
        count  = 0
        while(count < k):  
            ref_ptr = ref_ptr.next
            count += 1
 
        while(ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next

        return main_ptr.value


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):
        ll.push(i)
    
    assert ll.remove_element(2) == 1
