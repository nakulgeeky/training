class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self):
        element = int(input("Enter element: "))
        self.queue.append(element)
        print("Queue after enqueuing:", self.queue)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            self.queue.pop(0)
            print("Queue after dequeuing:", self.queue)

    def delete_element(self):
        if not self.queue:
            print("Queue is empty")
            return

        element = int(input("Enter element to delete: "))
        if element in self.queue:
            self.queue.remove(element)
            print("Queue after deleting element:", self.queue)
        else:
            print("Element not found in the queue")

    def display(self):
        print("Current queue:", self.queue)

    def callmain(self):
        while True:
            print("Select an operation:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Delete element")
            print("4. Display queue")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.enqueue()
            elif choice == 2:
                self.dequeue()
            elif choice == 3:
                self.delete_element()
            elif choice == 4:
                self.display()
            elif choice == 5:
                break
            else:
                print("Invalid choice")

#q1 = Queue()
#q1.callmain()
""""
class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, element):
        if len(self.queue) >= self.max_size:
            print("Queue is full. Cannot enqueue more elements.")
            return
        self.queue.append(element)
        print("Queue after enqueuing:", self.queue)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            self.queue.pop(0)
            print("Queue after dequeuing:", self.queue)

    def display(self):
        print("Current queue:", self.queue)

    def callmain(self):

        max_queue_size = int(input("Enter the maximum size of the queue: "))
        q1 = Queue(max_queue_size)
        while True:
            print("Select an operation:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Display queue")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.enqueue()
            elif choice == 2:
                self.dequeue()
            elif choice == 3:
                self.display()
            elif choice == 4:
                break
            else:
                print("Invalid choice")
"""


