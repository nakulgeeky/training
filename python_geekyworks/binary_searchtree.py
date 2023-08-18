class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTreee:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self._insert_recursive(root.left, key)
            else:
                root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.val, end=" ")
            self._inorder_recursive(root.right)

# Create a binary search tree
#bst = BinarySearchTree()

    def callmain(self):

        while True:
            print("Select an operation:")
            print("1. Insert element")
            print("2. Search element")
            print("3. In-order traversal")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 4:
                print("Exiting...")
                break
            elif choice == 1:
                data = int(input("Enter element to insert: "))
                bst.insert(data)
            elif choice == 2:
                data = int(input("Enter element to search: "))
                if bst.search(data):
                    print(f"{data} found in the tree.")
                else:
                    print(f"{data} not found in the tree.")
            elif choice == 3:
                print("In-order traversal:")
                bst.inorder_traversal()
                print()
            else:
                print("Invalid choice")
