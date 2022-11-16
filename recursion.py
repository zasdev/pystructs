#Ejercicio sobre recursion 

def Factorial(n):
    #Pruaba del caso base
    if (n == 0):
        return 1

    #Hace los cálculos y regresa el valor
    f= n*Factorial(n-1)
    print(f)
    return(f)

print(Factorial(8))