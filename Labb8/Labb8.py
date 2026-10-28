from linkedQFile2 import LinkedQ
import unittest

class Syntaxfel(Exception):
    pass

class SyntaxTest(unittest.TestCase):

    def testGroup(self):
        self.assertEqual(syntax_test("H"), "rätt syntax!")
        self.assertEqual(syntax_test("P21"), "rätt syntax!")
        self.assertEqual(syntax_test("Fe12"), "rätt syntax!")
        self.assertEqual(syntax_test("8"), "fel syntax!")
        self.assertEqual(syntax_test("a"), "fel syntax!")
        
def group(q): 
    atom(q)
    if q.is_empty() == False:
        number(q)
    return

def atom(q):
    biggie(q)
    if q.is_empty() == False:
        smallie(q)
    return
    
def biggie(q):
    letter = q.peek()
    if letter.isupper():
        q.dequeue()
        return
    else:
        raise Syntaxfel ("Saknad stor bokstav vid radslutet ")
    
def smallie(q):
    letter = q.peek()
    if letter.islower():
        q.dequeue()
        return
    else:
        return
    
def number(q):
    rest = ""
    if int(q.peek()) == 0:
        q.dequeue()
        raise Syntaxfel ("För litet tal vid radslutet ")
    while q.is_empty() == False:
        if q.peek().isnumeric():
            rest += q.peek()
            q.dequeue()
    if int(rest) < 2:
        raise Syntaxfel ("För litet tal vid radslutet ")
    else:
        return

def syntax_test(mol):
    q = LinkedQ()
    for i in mol:
        q.enqueue(i)
    try:
        group(q)
        if q.is_empty():
            return ("Formeln är syntaktiskt korrekt")
    except Syntaxfel as fel:
        return str(fel) + str(q)
        

def main():
    mol = input()
    while mol != "#" and mol:
        result = syntax_test(mol)
        print(result)
        mol = input()
if __name__ == "__main__":
    main()


