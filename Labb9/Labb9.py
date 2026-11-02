from linkedQFile3 import LinkedQ
import unittest

class Syntaxfel(Exception):
    pass

class SyntaxTest(unittest.TestCase):

    def testGroup(self):
        self.assertEqual(syntax_test("Na"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(syntax_test("H2O"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(syntax_test("Si(C3(COOH)2)4(H20)7"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(syntax_test("Na332"), "Formeln är syntaktiskt korrekt")

atom_list = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", 
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", 
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", 
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", 
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", 
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

def formel(q):
    mol(q)
    if q.is_empty() == False:
        group(q)

def mol(q):
    group(q)
    if q.is_empty() == False and q.peek() != ")":
        mol(q)
    return

def group(q): 
    if q.is_empty():
        raise Syntaxfel ("Felaktig gruppstart vid radslutet ")
    
    start = q.peek()
    if start == "(":
        q.dequeue() #tar bort öppningasparantes
        mol(q)
        if q.is_empty():
            raise Syntaxfel ("Saknad högerparentes vid radslutet ")
        slut = q.peek()
        if slut != ")":
            raise Syntaxfel ("Saknad högerparentes vid radslutet ")
        else:
            q.dequeue() #tar bort stängningsparantes
            if q.is_empty() == False and q.peek().isnumeric():
                number(q)
            else:
                raise Syntaxfel ("Saknad siffra vid radslutet ")
    elif start.isalpha():
        atom(q)
        if q.is_empty() == False and q.peek().isnumeric():
            number(q)
    else:
        raise Syntaxfel ("Felaktig gruppstart vid radslutet ")
    return

def atom(q):
    atom_str = ""
    biggie(q)
    atom_str += str(q.dequeue())
    if q.is_empty() == False:
        if smallie(q) == True:
            atom_str += str(q.dequeue())
    if atom_str not in atom_list:
        raise Syntaxfel ("Okänd atom vid radslutet ")
    return
    
def biggie(q):
    letter = q.peek()
    if letter.isupper():
        return
    else:
        raise Syntaxfel ("Saknad stor bokstav vid radslutet ")
    
def smallie(q):
    letter = q.peek()
    if letter.islower():
        return True
    else:
        return False
    
def number(q):
    rest = ""
    if int(q.peek()) == 0:
        q.dequeue()
        raise Syntaxfel ("För litet tal vid radslutet ")

    while q.is_empty() == False and q.peek().isnumeric():
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
        formel(q)
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


