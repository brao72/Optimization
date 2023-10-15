#importing the math library
import math

#defining a function which takes into parameter a number and returns a list of 3 elements which are the binary representation of the number
def d2b(n):
    if(n == 0):
        return [0,0,0]
    l = []
    while(n!=0):
        l.append(n%2)
        n//=2;
    while(len(l) < 3):
        l.append(0)
    l = l[::-1]
    return l

#defining a 3 variable obscured function(blackbox)
def obscured_function(a,b,c):
    #defining the himmelblau function here in terms of a,b,c 
    return (a**2 + b - 11)**2 + (a + b**2 - 7)**2 + c**2 

#definig a function to return the index of the minimum element in a list
def minl(l):
    m = 0
    for i in range(len(l)):
        if l[i] <l[m]:
    return m

#intializing the number of steps , the starting point and the step size
nsteps = 1000000;
p = [1,1,1]
e = 0.01

#iterating through every step
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
    #the list l1 contains the inital cordinates and the cordinates of 8 points in it's neighbourhood while the list l2 contains the value of the obscured function at these 9 points
    m = minl(l2)

    #continuing the loop with the intial point out of the 8 being the one whose mapping in the pbscured function is minimum , if the value of the image of the eight points in the neighbourhood is more that the current point , we declare the current point to be the local minimum.
    if(m == 0):
        break
    else:
        p = l1[m]

#printinf the point of minima and the minimum value of the obscured function
print(p , obscured_function(p[0] , p[1] , p[2]))

