class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end="<-->")
            current = current.next
            if current == self.head:
                break
        print("(head)")

    def add_to_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        # Find the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Rearrange pointers
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty!")
            return

        if self.head.next == self.head:
            # Only one node
            self.head = None
            return

        # Find the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Point last node to the new head
        current.next = self.head.next
        self.head = self.head.next

    def insert_at_position(self, data, pos):
        new_node = Node(data)

        # Case 1: insert at head
        if pos == 0:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = new_node
                new_node.next = self.head
                self.head = new_node
            return

        # Case 2: insert at given pos
        current = self.head
        count = 0

        while current.next != self.head and count < pos - 1:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None

        while True:
            if current.data == value:
                # Case 1: deleting head
                if current == self.head:
                    # only one node
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = self.head.next
                        self.head = self.head.next
                else:
                    prev.next = current.next
                return

            prev = current
            current = current.next

            if current == self.head:
                break

        print(f"{value} not found")

    def delete_at_position(self, pos):
        if self.head is None:
            print("Empty list")
            return

        if pos == 0:
            self.delete_at_beginning()
            return

        current = self.head
        count = 0

        while current.next != self.head and count < pos - 1:
            current = current.next
            count += 1

        if current.next == self.head:
            print("Position out of bounds")
            return

        current.next = current.next.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head


cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.add_to_beginning(5)
cll.print_list()
cll.delete_at_beginning()
cll.print_list()
cll.delete_at_position(2)
cll.print_list()

