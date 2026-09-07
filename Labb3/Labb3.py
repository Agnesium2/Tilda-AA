from bintreeFile import Bintree
'''
def makeTree():
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

def main():
    tree = makeTree()
    searches(tree)
    tree.write()

main()
'''

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

engelska = Bintree()
with open("engelska.txt", "r") as engelskfil:
    for rad in engelskfil:
        ordrad = rad.strip().split(" ")               # Ett trebokstavsord per rad
        for ord in ordrad:
            if ord not in engelska:
                engelska.put(ord)  
                if ord in svenska:
                    print(ord, end = " ")       # in i sökträdet
engelska.write()
print("\n")