from bintreeFile import Bintree
from linkedQFile import LinkedQ
from linkedQFile import ParentNode
from linkedQFile import SolutionFound

def readfile(filename):
    svenska = Bintree()
    with open(filename, "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet not in svenska:
                svenska.put(ordet)             # in i sökträdet
    return svenska

def writechain(slutordsnod):
    if slutordsnod != None:
        writechain(slutordsnod.get_parent())
        print(slutordsnod)

def makechildren(q, svenska, gamla, ord, slutord):
    alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
    bokstav = list(str(ord))
    for j in range(len(bokstav)):
        current = bokstav[j]
        for i in range(29):
            bokstav[j] = alfabet[i]
            testord = "".join(bokstav)
            if testord in svenska and testord not in gamla:
                gamla.put(testord)
                testord = ParentNode(testord)
                testord.make_parent(ord)
                q.enqueue(testord)

                if str(testord) == slutord:
                    slutordsnod = testord
                    writechain(slutordsnod)
                    return True
        bokstav[j] = current

def sök(startord, slutord, svenska, gamla, q):
    if startord in svenska:
        gamla.put(startord)
        startord = ParentNode(startord)
        q.enqueue(startord)

    while not q.is_empty():
        ord = q.dequeue()
        hittad = makechildren(q, svenska, gamla, ord, slutord)
        if hittad == True:
            return True

def main():
    svenska = readfile("word3.txt")

    q = LinkedQ()
    gamla = Bintree()

    hittad  = False
    
    startord = input("Startord: ")
    slutord = input("Slutord: ")

    hittad = sök(startord, slutord, svenska, gamla, q)

    if hittad == True:
        print("Det finns en väg till: ", slutord)
    else: 
        print("Nej det fanns ingen väg till", slutord)

main()