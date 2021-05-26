class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head) 
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
    
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    
    def insert(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, after, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == after:
                itr.next = Node(data, itr.next) 
                return
            itr = itr.next
            count += 1
        raise Exception("The data don't exist")
    
    def remove_by_value(self, data, stop_count = None):
        count = 0
        itr= self.head
        while itr:
            if count == stop_count:
                itr.next = itr.next.next
                return
            if itr.data == data:
                return self.remove_by_value(data, count - 1)
            
            itr = itr.next
            count += 1
        raise Exception("Wrong input")

    def print(self):
        if self.head is None:
            print(" ")
            return
        
        itr = self.head
        listStr = ""
        while itr:
            listStr += str(itr.data) + ","
            itr = itr.next
        
        print(listStr)

if __name__ == '__main__':
    Li = LinkedList()
    Li.insert_at_beginning(5)
    Li.insert_at_beginning(3674)
    Li.insert_at_end(90)
    Li.insert_at_end(89)
    Li.insert_values(["cool", "joback", "pratham"])
    print(Li.length())
    Li.print()
    Li.remove(1)
    Li.insert(0, "lime")
    Li.insert(2, "mango")
    Li.insert_after_value("mango", "banana")
    Li.insert(3, "banana")
    Li.print()
    Li.remove_by_value("banana")
    Li.print()
    Li.remove_by_value("banana")
    Li.print()
    # Li.remove_by_value("banana")
    # Li.insert_after_value("mango0", "banana")
    # Li.remove(9)
