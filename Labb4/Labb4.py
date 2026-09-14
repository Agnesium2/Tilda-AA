from bintreeFile import Bintree
from linkedQFile import LinkedQ

def makechildren(q, svenska, gamla, ord, slutord):
    alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
    bokstav = list(ord)
    for j in range(len(bokstav)):
        current = bokstav[j]
        for i in range(29):
            bokstav[j] = alfabet[i]
            testord = "".join(bokstav)
            if testord in svenska:
                if testord not in gamla:
                    q.enqueue(testord)
                    gamla.put(testord)
                    if testord == slutord:
                        return True
        bokstav[j] = current

def main():
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet not in svenska:
                svenska.put(ordet)             # in i sökträdet

    q = LinkedQ()
    gamla = Bintree()

    hittad = False

    startord = input("Startord: ")
    slutord = input("Slutord: ")

    if startord in svenska:
        gamla.put(startord)
        q.enqueue(startord)

    while not q.is_empty():
        ord = q.dequeue()
        hittad = makechildren(q, svenska, gamla, ord, slutord)
        if hittad == True:
            break

    if hittad == True:
        print("Det finns en väg till: ", slutord)
    else: 
        print("Nej det fanns ingen väg till", slutord)

main()