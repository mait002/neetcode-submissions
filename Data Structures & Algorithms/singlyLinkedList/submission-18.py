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
        i = 0
        if self.head != None:
            curr = self.head
            while curr != None and i < self.length:
                if i == index:
                    return curr.val
                else:
                    i += 1
                    curr = curr.next
                    
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
        self.length += 1


        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        
        if self.head != None:
            if index == 0:
                self.head = self.head.next
                self.length -=1
                return True
            else:
                i = 0
                curr = self.head
                while curr != None:
                    if i == index - 1:
                        if index == self.length -1:
                            curr.next = None
                            self.tail = curr
                            self.length -=1
                            return True
                        else: 
                            curr.next = curr.next.next
                            self.length -=1
                            return True
                        return False
                    else:
                        curr = curr.next
                        i += 1
                
        return False


        

    def getValues(self) -> List[int]:
        lst = []
        if self.head != None:
            curr = self.head
            while curr != None:
                lst.append(curr.val)
                curr = curr.next
            
        return lst
        
