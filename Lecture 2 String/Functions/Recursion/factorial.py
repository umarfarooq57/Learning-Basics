def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n* fact(n-1)             # factorial formula =>     n!=(n-1)n     5!==4!x5==1x2x3x4x5

print(fact(5 )) 