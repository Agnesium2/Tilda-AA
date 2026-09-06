class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self,next_node):
        self.next=next_node

    def get_next(self):
        return self.next

    def __str__(self):
        return str(self.value)
    
class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def is_empty(self):
        return self.__first == None

    def enqueue(self, item):
        temp = Node(item)

        if self.__first == None:
            self.__first = temp
            self.__last = temp

        else:
            self.__last.set_next(temp)
            self.__last = temp
        
    def dequeue(self):
        temp1 = self.__first
        self.__first = self.__first.next
        return temp1.value
    
    def __str__(self):
        return str(self.__first)
