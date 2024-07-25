class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
	# When you create a node like node1 = Node(data="banana"), node1 holds the data "banana" and has its next attribute initially set to None.



class LinkedList:
    def __init__(self):
        self.head = None # Address reference (not data value) to the first node, which is blank when a linked list is first created.
	# The Node class doesn't need self.head because each node is only responsible for storing its own data and the reference to the next node. The LinkedList class, on the other hand, manages the entire sequence of nodes, so it needs self.head to keep track of the first node.


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)



    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count



    def insert_at_beginning(self, data):
        node = Node(data, self.head) # Create a new node, and makes the new node's "next" value equal to the original self.head, which is paving the way so we can create a new self.head value below with:

        self.head = node 



    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None) # Set "next" == None because it is the last node.
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None) # Sets the "next" value of the current last node to equal the new node that will take the place of the final node, and this final node will now have "None" as the "next" value.



    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1



    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1



    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next



    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()