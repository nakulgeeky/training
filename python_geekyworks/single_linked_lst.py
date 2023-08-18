# linked list  [single linked list]
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Linked_list:
    def __init__(self):
        self.head = None

    def print_linked(self):
        if self.head is None:
            print("empty linked list")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        # now we need to check linked list is empty or not
        if self.head is None:
            self.head = new_node
        # process of going to last node , n variable lete usko check krte jate jab tk uska ref 0 nhi ho jata
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
        # ye check krne k baad hum n.ref ko new node le lete

    def add_after_element(self, data,
                          x):  # we are taking x because x tells ki kis node k baad entre krna hai.....[x position (index nahi hai direct no hai)]
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("The node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before_element(self, data, x):
        n = self.head
        if self.head is None:
            print("the Linked list is empty")
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            print("Linked list is not empty")

    # now for deleting the kinked list

    def delete_begin(self):
        if self.head is None:
            print("linked list is empty so we can't delete the node")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("linked list is empty so we can't delete the node")
        elif self.head.ref is None:
            print("The Linked List only contain one element so cannot be removed")

        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("linked list is empty so we can't delete the node")
        if x == self.head.data:
            self.head = self.head.ref
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Nod is not present")
        else:
            n.ref = n.ref.ref

    # LL1 =Linked_list()

    # ll1 = Linked_list()

    def callmain(self):

        while True:
            print("Select an operation:")
            print("1. Create single linked list")
            print("2. Add element at the beginning")
            print("3. Add element at the end")
            print("4. Add element after an element")
            print("5. Add element before an element")
            print("6. Delete the first element")
            print("7. Delete the last element")
            print("8. Delete element by value")
            print("9. Display the list")
            print("10. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 10:
                print("Exiting...")
                break
            elif choice == 1:
                num_elements = int(input("Enter the number of elements in the linked list: "))
                ll1 = Linked_list()
                for _ in range(num_elements):
                    data = int(input("Enter element: "))
                    ll1.add_end(data)
                ll1.print_linked()
            elif choice == 2:
                data = int(input("Enter element to add at the beginning: "))
                ll1.add_begin(data)
            elif choice == 3:
                data = int(input("Enter element to add at the end: "))
                ll1.add_end(data)
            elif choice == 4:
                data = int(input("Enter element to add: "))
                x = int(input("Enter the element after which to add: "))
                ll1.add_after_element(data, x)
            elif choice == 5:
                data = int(input("Enter element to add: "))
                x = int(input("Enter the element before which to add: "))
                ll1.add_before_element(data, x)
            elif choice == 6:
                ll1.delete_begin()
            elif choice == 7:
                ll1.delete_end()
            elif choice == 8:
                x = int(input("Enter the element to delete: "))
                ll1.delete_by_value(x)

            elif choice == 9:
                ll1.print_linked()
            # ... other operations ...
            else:
                print("Invalid choice")