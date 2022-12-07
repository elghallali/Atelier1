# Fonction qui renvoie la puissance d'un nombre X

def puissance(X,n):
    if ( X == 0 and n == 0):
        return "La puissance n'existe pas"
    else:
        power = 1
        for i in range(n):
            power *= X
        return power
