class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ---------------- INSERTIONS ---------------- #

    def append(self, data):
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

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        new_node.next = self.head
        last.next = new_node
        self.head = new_node

    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            print("Position out of bounds")
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current.next != self.head and count < pos - 1:
            current = current.next
            count += 1

        if count != pos - 1:
            print("Position out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    # ---------------- DELETIONS ---------------- #

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        self.head = self.head.next
        last.next = self.head

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

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
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

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None

        while True:
            if current.data == value:
                if current == self.head:
                    self.delete_at_beginning()
                else:
                    prev.next = current.next
                return

            prev = current
            current = current.next

            if current == self.head:
                break

        print(f"{value} not found")

    # ---------------- DISPLAY ---------------- #

    def display(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")


cll = CircularLinkedList()

cll.append(10)
cll.append(20)
cll.append(30)

cll.insert_at_beginning(5)
cll.insert_at_position(2, 15)

cll.display()

cll.delete_at_beginning()
cll.delete_at_end()
cll.delete_by_value(20)

cll.display()
