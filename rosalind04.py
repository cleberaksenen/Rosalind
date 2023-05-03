n = int(input("Digite o número de meses: "))
k = int(input("Digite o número de pares de coelhos gerados por par de adulto: "))

def coelhos(n,k):
    if n == 0:
        return(0) # coelhos(0,k) == 0
    if n == 1:
        return(1) # coelhos(1,k) == 1
    else:
        return(coelhos(n-1,k) + k*coelhos(n-2,k))
       
print(coelhos(n,k))

# n = int(input("Digite o número de meses: "))
# k = int(input("Digite o número de pares de coelhos gerados por par de adulto: "))

# if n == 0:
#     return(0) # coelhos(0,k) == 0
# if n == 1:
#     return(1) # coelhos(1,k) == 1
# else:
#     return(coelhos(n-1,k) + k*coelhos(n-2,k))








