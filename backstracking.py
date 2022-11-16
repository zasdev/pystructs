#recursive approach to generating all the possible permutations of 
#a given string, s, of agiven length n: 

def bitStr(n, s):
    if n == 1: 
        return s   

    return [ digit + bits for digit in bitStr(1,s) for bits in bitStr(n- 1,s)]

print(bitStr(4,'abcd'))

#Tiene el problema de que consume demasiada memoria