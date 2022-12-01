# La fonction qui convertir le nombre decimal en nombre binaire

def decimalToBinary(n):
    res =  ""
    
    while(n > 0):
        r = n%2
        res = str(r)+res
        n //= 2
    return int(res)


