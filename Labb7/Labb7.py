import csv

class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, nyckel, data):
        self.dict[nyckel] = data

    def __contains__(self, nyckel):
        return self.dict[nyckel]

    def search(self, nyckel):
        finns  = self.dict.__contains__(nyckel)
        if finns == True:
            return self.dict[nyckel]
        else:
            print("det fanns inte kdrama som heter så")

    def __str__(self):
        return self.name + ":" + self.year  


""" dramadict.store("Hej", 5)
dramadict.store("Då", 8)
dramadict.store("så", 10)
pris = dramadict.search("Då")
print(pris) """

def filereader(filename, dramadict):
    with open(filename, mode="r") as csvfile:
        csvfile = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvfile:
            dramadict.store(row[0],int(row[7]))
        return dramadict

def main():
    dramadict = DictHash()
    filereader("kdrama.csv", dramadict)
    q = input("vad letar du efter: ")
    data = dramadict.search(q)
    print("Den kom ut: ", data)
main()
