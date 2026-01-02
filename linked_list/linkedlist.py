# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# class LinkedList():
#     def __init__(self):
#         self.head = None
        
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
            
#     def print(self):
#         current = self.head
#         while current:
#             print(current.data,end="-->")
#             current = current.next
#         print("None")
        
#     def add_to_beggining(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
        
#     def delete_at_beggining(self):
#         if self.head is None:
#             print("No linkedlist Exists!!")
#         else:
#             self.head = self.head.next
        
#     def delete_at_position(self, pos):
        
#         if self.head is None:
#             print("List is empty!!")
#             return
#         if pos == 0:
#             self.head = self.head.next
#             return

#         current = self.head
#         count = 0
        
#         while current and count < pos-1:
#             current = current.next
#             count+=1
            
#         if current is None or current.next is None:
#             print("Position out of bounds!!")
#             return
        
#         current.next = current.next.next
        
#     def insert_by_position(self,pos,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         if pos == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return
        
#         current = self.head
#         count = 0
        
#         while current is not None and count < pos - 1:
#             current = current.next
#             count+=1
            
#         if current is None:
#             print("Index out of bounds.\n")
#             return
        
#         new_node.next = current.next
#         current.next = new_node 
        

#     def delete_by_value(self,value):
#         if self.head is None:
#             print("No LinkedList found!!")
#             return
        
#         if self.head.data == value:
#             self.head = self.head.next
#             return
        
#         current = self.head    
#         while current.next and current.next.data != value:
#             current = current.next
            
#         if current.next is None:
#             print("Value not found")
#             return
        
#         current.next = current.next.next
        
#     def reverse(self):
#         if self.head is None:
#             print("No LinkedList found")
#             return
        
#         current = self.head
#         prev = None
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev

#     def length(self):
#         current = self.head
#         count = 0
#         while current:
#             count+=1
#             current = current.next
#         return count

#     def search_by_value(self,value):
#         current = self.head
#         index = 0
#         while current:
#             if current.data == value:
#                 return f"Value {value} found at index {index}"
#             current = current.next
#             index+=1
#         return f"Value {value} not found"
 
# ll = LinkedList()
# ll.append(20)
# ll.append(30)
# ll.append(40)
# ll.append(50)
# ll.add_to_beggining(10)
# ll.print()
# ll.delete_at_beggining()
# ll.print()
# ll.delete_at_position(2)
# ll.print()
# ll.insert_by_position(1,5)
# ll.print()
# ll.delete_by_value(20)
# ll.print()
# ll.reverse()
# ll.print()
# print(ll.length())
# print(ll.search_by_value(30))


###########################################################################################################################
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def print(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        
        current = self.head
        while current:
            print(current.data,end = "->")
            current = current.next
        print("None")
        
    def insert_at_the_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insert_at_position(self, pos, data):
        new_node = Node(data)
        if self.head is None:
            print("No LinkedList Exists!")
            return
        
        if pos == 0:
            return self.insert_at_the_beginning(data)
            return
        
        current = self.head
        count = 0
        while current is not None and count < pos -1:
            current = current.next
            count+=1
            
        if current is None:
            print("Index out of bounds!")
            return
        
        new_node.next = current.next
        current.next = new_node
        
    def delete_at_position(self,pos):
        if self.head is None:
            print("No linkedlist exists!")
            return
        
        if pos == 0:
            self.head = self.head.next
            return
        
        current = self.head 
        count = 0 
        while current is not None and count < pos -1:
            current = current.next
            count+=1
            
        if current is None or current.next is None:
            print("Postion out of bound!")
            return
        
        current.next = current.next.next
            
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
    def length(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count
        
        
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.print()
ll.insert_at_the_beginning(5)
ll.print()
ll.insert_at_position(2,15)
ll.print()
ll.delete_at_position(2)
ll.print()
ll.reverse()
ll.print()
print(ll.length())


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
            
    
    def print(self):
        if self.head is None:
            print("No linkedlist exists")
            return
        current = self.head
        while current:
            print(current.data,end = "<-->")
            current = current.next
        print("None")
        
    def insert_by_position(self,pos,data):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0 
        while current and count < pos-1:
            current = current.next
            count+=1
        
        if current is None:
            print("out of bound")
            return
            
        new_node.next = current.next
        current.next = new_node
            
    def delete_by_position(self,pos):
        if pos == 0:
            self.head = self.head.next
            return
        
        current = self.head
        count = 0 
        while current and count < pos-1:
            current = current.next
            count+=1 
        
        if current is None and current.next is None:
            print("Position out of bound")
            return
        
        current.next = current.next.next
        
    def delete_by_value(self,value):
        if self.head is None:
            print("No linkedlist exists!")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return  
        
        current = self.head
        count = 0 
        
        if current.next and current.next.data != value:
            current = current.next
            count+=1
            
        if current.next is None:
            print("Value not found")
            return
        
        current.next = current.next.next
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete_at_beginning(self):
        if self.head is None:
            print("No linkedlist exists")
            return
        if self.head:
            self.head = self.head.next
            return
        
    def delete_at_end(self):
        if self.head is None:
            print("No linkedlist exists")
            return
        if self.head.next is None:
            self.head = None
            return 
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def remove_middle(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.print()
ll.insert_by_position(2,25)
ll.print()
ll.delete_by_position(3)
ll.print()
ll.delete_by_value(30)
ll.print()
ll.insert_at_beginning(0)
ll.print()
ll.delete_at_beginning()
ll.print()
ll.delete_at_end()
ll.print()
ll.reverse()
ll.print()
        




































class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self,data):
        new_node = Node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
            return
        
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head is None:
            return "No LinkedList exists!!"
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print(None)
        
    def insert_at_index(self,pos,data):
        new_node = Node(data)
        if pos == 0:
            self.prepend(data)
            return
        
        current = self.head
        count = 0
        while current and count < pos-1:
            current = current.next
            count+=1
            
        if current is None:
            print("Index out of Bound")
            return
            
        new_node.next = current.next
        current.next = new_node
        
    def delete_head(self):
        if self.head is None:
            print("No LinkedList Exists")
            return 
        self.head = self.head.next
        
    def delete_tail(self):
        if self.head is None:
            print("No LinkedList Exists")
            return 
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        
    def delete_at_pos(self,pos):
        if self.head is None:
            print("No LinkedList Exists")
            return
        
        if pos == 0:
            self.head = self.head.next
            return
        
        current = self.head
        count = 0 
        
        while current and count < pos-1:
            current = current.next
            count+=1
        
        if current is None or current.next is None:
            print("Index Out Of Bound")
            return
        
        current.next = current.next.next
        
    def search(self,value):
        if self.head is None:
            print("No LinkedList Exists")
            return
        current = self.head
        pos = 0
        while current:
            if current.data == value:
                print(f"Value {value} found at position {pos}")
                return
            current = current.next
            pos+=1
        print(f"Value {value} NOT found in the LinkedList")

    def reverse(self):
        if self.head is None:
            print("No LinkedList Exists")
            return
        current = self.head
        prev = None
        while current:
            temp = current.next 
            current.next = prev 
            prev = current 
            current = temp
        self.head = prev
        
    def reverse_recursive(self,node):
        if node is None or node.next is None:
            return node
            
        new_head = self.reverse_recursive(node.next)
        node.next.next = node
        node.next = None 
        
        return new_head
        
    def find_middle(self):
        if self.head is None:
            print("No LinkedList Exists!")
            return
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        return
        
    def has_cycle(self):
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False


    def remove_duplicates_sorted(self):
        if self.head is None:
            print("No LinkedList Exists!")
            return
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        
    def remove_duplicates(self):
        if self.head is None:
            print("No LinkedList Exists!")
            return
        current = self.head
        seen = set()
        prev = None 
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next
        
        
ll = LinkedList()
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(6)
ll.append(6)
ll.append(8)
ll.append(9)
ll.append(5)
ll.print()
ll.prepend(1)
ll.print()
result = ll.insert_at_index(10, 100)
ll.print()
ll.delete_head()
ll.print()
ll.delete_tail()
ll.print()
ll.delete_at_pos(1)
ll.print()
ll.search(6)
ll.search(100)
ll.reverse()
ll.print()
ll.head = ll.reverse_recursive(ll.head)
ll.print()
ll.find_middle()
ll.print()
print(ll.has_cycle())
ll.remove_duplicates_sorted()
ll.print()
ll.remove_duplicates()