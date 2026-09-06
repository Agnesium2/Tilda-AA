svenska = Bintree()             # Skapa ett trädobjekt
svenska.put("gurka")		    # Sortera in "gurka" i trädet	


if "gurka" in svenska:          # Kolla om "gurka" finns i trädet
                                # (Operatorn in anropar metoden __contains__ 
                                # som du ska implementera i din Bintree-klass)
    
svenska.write()                 # Skriver alla trädobjektets ord i bokstavsordning