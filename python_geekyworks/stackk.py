class Stack:
    def __init__(self):
        self.stack = []

    def push(self):
        element = int(input("Enter element: "))
        self.stack.append(element)
        print("Stack after pushing:", self.stack)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            self.stack.pop()
            print("Stack after popping:", self.stack)

    def delete_element(self):
        if not self.stack:
            print("Stack is empty")
            return

        element = int(input("Enter element to delete: "))
        if element in self.stack:
            self.stack.remove(element)
            print("Stack after deleting element:", self.stack)
        else:
            print("Element not found in the stack")

    def display(self):
        print("Current stack:", self.stack)

    def callmain(self):
        while True:
            print("Select an operation:")
            print("1. Push")
            print("2. Pop")
            print("3. Delete element")
            print("4. Display stack")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.push()
            elif choice == 2:
                self.pop()
            elif choice == 3:
                self.delete_element()
            elif choice == 4:
                self.display()
            elif choice == 5:
                break
            else:
                print("Invalid choice")


#st1 = Stack()
#st1.callmain()
