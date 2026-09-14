class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

def putta(p, newvalue):
    if p == None:
        return Node(newvalue)
    else:
        if newvalue < p.value:
            p.left = putta(p.left, newvalue)
        elif newvalue > p.value:
            p.right = putta(p.right, newvalue)
    return p

# Funktion som gör själva jobbet att stoppa in en ny nod

def finns(p, value):
    if p:
        if value == p.value:
            return True
        elif value < p.value:
            return finns(p.left, value)
        else:
            return finns(p.right, value)
    else:
        return False
    
# Funktion som gör själva jobbet att söka efter ett värde

def skriv(p):
    if p:
        skriv(p.left)
        print(p.value)
        skriv(p.right)

# Funktion som gör själva jobbet att skriva ut trädet