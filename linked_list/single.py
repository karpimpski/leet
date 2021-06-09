class MyLinkedList:
    def __init__(self):
        self.val = None
        self.nextNode = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.get_node(index)
        if node == None:
            return -1
        return node.val

    def get_node(self, index):
        """
        Get the index-th node.
        """
        node = self
        for i in range(0, index):
            node = node.nextNode
        if node == None:
            return None
        else:
            return node

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:
            self.val = val
        else:
            newNode = MyLinkedList()
            newNode.val = self.val
            newNode.nextNode = self.nextNode
            self.val = val
            self.nextNode = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:
            self.addAtHead(val)
        else:
            node = self
            newNode = MyLinkedList()
            newNode.addAtHead(val)
            while node.nextNode != None:
                node = node.nextNode
            node.nextNode = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        else:
            node = self.get_node(index - 1)
            if node != None:
                newNode = MyLinkedList()
                newNode.val = val
                newNode.nextNode = node.nextNode
                node.nextNode = newNode

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.get_node(index)
        if node == None:
            pass
        elif node.nextNode == None:
            self.get_node(index - 1).nextNode = None
        elif node != None:
            node.val = node.nextNode.val
            node.nextNode = node.nextNode.nextNode

    def show(self):
        """
        Displays all values in the List.
        """
        node = self
        result = "["
        while node.nextNode != None:
            result += str(node.val) + ", "
            node = node.nextNode
        result += str(node.val) + "]"
        print(result)


list = MyLinkedList()
list.addAtHead(0)
list.addAtTail(1)
list.addAtTail(2)
list.addAtTail(3)
list.addAtTail(4)
list.show()