#fonction qui cree une pile vide
def pile():
    '''
    cree une pile vide
    '''
    #coeur de la fonction
    return [ ]
#jeu d'auto test
assert pile() == []

#fonction qui retourne la taille de la pile
def Taille(P):
    '''
    retourne la taille de la pile
    @P : list
    '''
    #pre-condition
    assert type(P) == list, 'P nest pas une liste'
    #coeur de la fonction
    return len(P)
#jeu d'auto test
assert Taille([1]) == 1
assert Taille([ ]) == 0
assert Taille([1, 2, 3, 4]) == 4

#fonction qui verifie si la piel est vide
def Est_Vide(P):
    '''
    verifie si la liste est vide
    @P : list
    '''
    #pre-condition
    assert type(P) == list, 'P nest pas une liste'
    #coeur de la fonction
    if Taille(P) == 0:
        return True
    else:
        return False
#jeu d'auto test
assert Est_Vide([1]) == False
assert Est_Vide([ ]) == True
assert Est_Vide([1, 2, 3, 4]) == False

#fonction qui empiler un nouvel élément x sur la pile P
def Empiler(P, x):
    '''
    Empiler un nouvel élément x sur la pile P
    @P : list
    @x : int
    '''
    #pre-condition
    assert type(x) == int or type(x) == float, 'x doit etre un int ou float'
    assert type(P) == list, 'P nest pas une liste'
    #coeur de la fonction
    P.append(x)
    return P
#jeu d'auto test
assert Empiler([1], 2) == [1, 2]
assert Empiler([ ], 6) == [6]
assert Empiler([1, 2, 3, 4], 1) == [1, 2, 3, 4, 1]

# fonction qui dépiler un élément de la pile P
def Depiler(P):
    '''
    Dépiler un élément de la pile P et le renvoi
    @P : list non vide
    '''
    #pre-condition
    assert type(P) == list, 'P nest pas une liste'
    assert Est_Vide(P) == False, 'P ne peu pas etre vide'
    #coeur de la fonction
    x = P.pop()
    return x
#jeu d'auto test
assert Depiler([1]) == 1
assert Depiler([1, 2]) == 2
assert Depiler([1, 2, 3, 4]) == 4

#fonction qui retourne la valeur au sommet de la pile P
def Lire_Sommet(P):
    '''
    Lire la valeur au sommet de la pile P
    @P : list non vide
    '''
    #pre-condition
    assert type(P) == list
    assert Est_Vide(P) == False
    #coeur de la fonction
    return P[-1]
#jeu d'auto test
assert Lire_Sommet([1]) == 1
assert Lire_Sommet([1, 2]) == 2
assert Lire_Sommet([1, 2, 3, 4]) == 4