from linkedQFile import LinkedQ

def create_list():
    nytt_q = LinkedQ()
    kort = input("")
    kortlista = kort.split(" ")
    for kort in range(len(kortlista)):
        nytt_q.enqueue(kortlista[kort])
    return nytt_q, kortlista

def algoritm(nytt_q, kortlista):
    output = ""
    for i in range(len(kortlista)): 
        temp = nytt_q.dequeue()
        nytt_q.enqueue(temp)
        temp2 = nytt_q.dequeue()
        output = output + str(temp2) + " "
    return output

def main():
    nytt_q, kortlista = create_list()
    output = algoritm(nytt_q, kortlista)
    print(output)
main()

'''
---------------------GAMMAL TESTKOD------------------
from array import array
colors = ["Blue", "Red", "Purple"]
print(colors)
add_color = input("Which color do you want to add to the list: ")
colors.append(add_color)
print(colors)
new_color = input("Choose another color: ")
position = int(input("Where do you want to insert the color? Enter the position number: "))
colors.insert(position, new_color)
print(colors)
remove_color = input("Which color do you want to remove from this list? : ")
for i in colors:
    if remove_color == i:
        colors.remove(remove_color)
print(colors)
remove_position = int(input("Enter the position number of the color you want to remove: "))
colors.pop(remove_position)
print(colors)
numbers = array("i", [1, 2, 3, 4, 5])  # How to create an array

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

q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")
'''


