# double linked list operation
class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None


class double_list:
    def __init__(self):
        self.head = None

    def print_linked_forward(self):
        if self.head is None:
            print("empty linked list\n")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.nref

    def print_linked_reverse(self):
        if self.head is None:
            print("empty linked list\n")
        else:
            n = self.head
            while n.nref is not None:
                # print(n.data, end = " ")     ye hum print nahi krenge kyki reverse hain isse last mai jayenge fir pref se piche picche aayenge
                n = n.nref
            while n is not None:
                print(n.data, end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("given none is not present in Linkes List")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n.pref
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("given none is not present in Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("double linked list is empty so it can't be deleted")
            return
        if self.head.nref is None:
            self.head = None
            print("double link list is empty after deleting the node")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("double linked list is empty so it can't be deleted")
            return
        if self.head.nref is None:
            self.head = None
            print("double link list is empty after deleting the node")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("double linked list is empty so it can't be deleted")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("print X is not present in Double linked list")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("x is not present in Double Linked List")

    # dl1 = double_list()

    def callmainn(self):
        while True:
            print("Select an operation:")
            print("1. Create double linked list")
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
                dl1 = double_list()
                for _ in range(num_elements):
                    data = int(input("Enter element: "))
                    dl1.add_end(data)
                dl1.print_linked_reverse()
            elif choice == 2:
                data = int(input("Enter element to add at the beginning: "))
                dl1.add_begin(data)
            elif choice == 3:
                data = int(input("Enter element to add at the end: "))
                dl1.add_end(data)
            elif choice == 4:
                data = int(input("Enter element to add: "))
                x = int(input("Enter the element after which to add: "))
                dl1.add_after(data, x)
            elif choice == 5:
                data = int(input("Enter element to add: "))
                x = int(input("Enter the element before which to add: "))
                dl1.add_before(data, x)
            elif choice == 6:
                dl1.delete_begin()
            elif choice == 7:
                dl1.delete_end()
            elif choice == 8:
                x = int(input("Enter the element to delete: "))
                dl1.delete_by_value(x)

            elif choice == 9:
                dl1.print_linked_forward()

            else:
                print("Invalid choice")