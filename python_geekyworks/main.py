
from double_linked_lst import *
from stackk import *
from single_linked_lst import*
from queuee import *
from binary_searchtree import *



if __name__ == '__main__':
    while True:
        print("Select an operation:")
        print("1. for Stack")
        print("2. for Single linked list")
        print("3. for Double linked list")
        print("4. for Queue")
        print("5. for Binary search Tree")
        print("6. terminate the code")

       # choice = int(input("Enter your choice: "))
        choice = int(input("entre choice: "))

        if choice == 1:
            st1 = Stack()
            st1.callmain()


        elif choice == 2:
            ll1 = Linked_list()
            ll1.callmain()

        elif choice == 3:
            dl1 = double_list()
            dl1.callmainn()

        elif choice == 4:

            q1 = Queue()
            q1.callmain()

        elif choice == 5:
            bst = BinarySearchTreee()
            bst.callmain()

        elif choice == 6:
            exit()

        else:
            print("invalid choice")
