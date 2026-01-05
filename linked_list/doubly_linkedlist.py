class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ---------------- INSERTIONS ---------------- #

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        count = 0

        while current and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    # ---------------- DELETIONS ---------------- #

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next:
            current = current.next

        current.prev.next = None

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 0:
            self.delete_at_beginning()
            return

        current = self.head
        count = 0

        while current and count < pos:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        if current.next is None:
            self.delete_at_end()
            return

        current.prev.next = current.next
        current.next.prev = current.prev

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        if current.data == value:
            self.delete_at_beginning()
            return

        while current and current.data != value:
            current = current.next

        if current is None:
            print("Value not found")
            return

        if current.next is None:
            self.delete_at_end()
            return

        current.prev.next = current.next
        current.next.prev = current.prev

    # ---------------- DISPLAY ---------------- #

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


dll = DoublyLinkedList()

dll.append(20)
dll.append(30)
dll.append(40)

dll.insert_at_beginning(10)
dll.insert_at_position(2, 25)

dll.display_forward()
dll.display_backward()

dll.delete_at_beginning()
dll.delete_at_end()
dll.delete_by_value(25)

dll.display_forward()
