import math
def d2b(n):
    if(n == 0):
        return [0,0,0]
    l = []
    while(n!=0):
        l.append(n%2)
        n//=2;
    while(len(l) < 3):
        l.append(0)
    return l

def obscured_function(a,b,c):
    #write the himmelblau function here in terms of a,b,c and return the result
    return (a**2 + b - 11)**2 + (a + b**2 - 7)**2 + c**2 
def minl(l):
    m = 0
    for i in range(len(l)):
        if l[i] <l[m]:
    return m
# Example usage:
nsteps = 1000000;
p = [1,1,1]
e = 0.01
for h in range(nsteps):
    l1 = [p]
    l2 = [obscured_function(p[0] , p[1] , p[2])]
    for i in range(8):
        tempcord = p.copy()
        binl = d2b(i)
        for j in range(len(binl)):
            if(binl[j] == 0):
                tempcord[j] +=e
            else:
                tempcord[j]-=e
        l1.append(tempcord)
        l2.append(obscured_function(tempcord[0] , tempcord[1] , tempcord[2] ))
    m = minl(l2)
    if(m == 0):
        break
    else:
        p = l1[m]
print(p , obscured_function(p[0] , p[1] , p[2]))

