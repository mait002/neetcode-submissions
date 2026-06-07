class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        


    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        #if list was empty
        if self.tail == None:
            self.tail = new_node

        self.length += 1


        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.length > 0:
            self.tail.next = new_node
        
        self.tail = new_node

        if self.head == None:
            self.head = new_node
        
        self.length += 1
        

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        
        #remove head
        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next

            #remove tail
            if curr.next == self.tail:
                self.tail = curr

            #remove from the middle
            else:
                curr.next = curr.next.next

        self.length -= 1
        return True

    
    
    def getValues(self) -> List[int]:
        lst = []
        curr = self.head
        for _ in range(self.length):
            lst.append(curr.val)
            curr = curr.next

            
        return lst
        
