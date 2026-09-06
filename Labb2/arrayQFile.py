from array import array
class ArrayQ:
    def __init__(self):
        self.__array = []

    def enqueue(self,item):
        self.__array.append(item)

    def dequeue(self):
        item = self.__array.pop(0)
        return item
    
    __array = array
    
    def __str__(self):
        return str(self.__array[0])
