import csv
class HashNode:
    def __init__(self, key = "", data = None):
        self.key = key
        self.data = data

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def __str__(self):
        return str(self.key)  
    

class Hashtable:  
    def __init__(self, size):
        self.size = size
        self.list = [None] * size * 2

    def store(self, key, data):
        start_pos = self.hashfunction(key)
        plats = start_pos
        nod_obj = HashNode(key)
        nod_obj.set_data(data)
        while plats != self.size:
            if self.list[plats] is None:
                self.list[plats] = nod_obj
                return
            if self.list[plats].key == key:
                self.list[plats].set_data(data)
                return
            
            plats = (plats + 1) % self.size
            if plats == start_pos:
                break

    def search(self, key):
        start_pos = self.hashfunction(key)

        position = start_pos
        while self.list[position] is not None:
            if self.list[position].key == key:
                return self.list[position].data
            position = (position + 1) % self.size
            if position == start_pos:
                break
        raise KeyError("Invalid namn: Dramat du gav fanns inte, eller du shar stavat fel;)")
        
    def hashfunction(self, key):
        total = 0
        for char in key:
            total += 31* ord(char) # ascii
        return total % self.size
    
def filereader(filename, dramadict):
    with open(filename, mode="r") as csvfile:
        csvfile = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvfile:
            dramadict.store(row[0],row)
        return dramadict
    
def get_size(filename):
    with open(filename, mode="r") as csvfile:
        csvfile = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        size = 1
        for row in csvfile:
            size += 1
        return size 

# def main():
#     # s = get_size("kdrama.csv")
#         hash = Hashtable(s)
#     # filereader("kdrama.csv", hash)
#     # sök_efter = input("Ge ett drama namn och få året: ")
#     # p = hash.search(sök_efter)
#     # print(p)
#     # hash.store("Hej", ["bla", 2])
#     # sök_efter2 = input("Ge ett drama namn och få året: ")
#     # h = hash.search(sök_efter2)
#     # print(h)

# main()