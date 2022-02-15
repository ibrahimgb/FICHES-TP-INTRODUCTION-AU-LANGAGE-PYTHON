



#Écrire votre propre programme qui affiche en sortie : Mon premier programme en Python


print("Mon premier programme en Python")


#Créer des variables et les afficher


nom = "Asimo"
date = 2000
print ("La première version d’ASIMO est finalisée en "+ str(date) +",")


#Demander à l'utilisateur d'entrer des données et s'en servir.


name = input("Enter your robot name: ")
type = input("Enter your robot type: ")
print("the robot name is " + name + " and the robot type is " + type + ".")


#. Opérations sur les nombres:


a = 17
b = 55
print("a = "+ str(a))
print("b = "+ str(b))
print("a + b = "+ str(a+b))
print("a - b = "+ str(a-b))
print("a * b = "+ str(a*b))
print("a / b = "+ str(a/b))


#Calculer la distance entre 2 points A(x1,y1) et B(x2,y2) e


#A = type('point', (object,  ), dict(X=16, Y=12))
#print(A.X)
x1=int(input("enter x1 : "))
y1=int(input("enter y1 : "))

x2=int(input("enter x2 : "))
y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
print("distance entre",(x1,x2),"and",(y1,y2),"is : ",result)

if result < 2000:
    print("Proche")
else:
    print("loin")

# Ecrire un programme qui calcule l'aire de différentes figures : disque, triangle, rectangle


import math
choise = input('Enter  1 pour disque 2 pour triangle 3 pour rectangle: ')  
print("choise : ",choise)

if (choise == 3):
    side = float(input('Enter la longer de diagonall: ')) 
    Area = side*side
    print("Aire du rectangle est:"+str(Area))    

elif (choise == 2):
    # base et hauteur
    base = float(input('Enter la base: '))  
    hauteur = float(input('Enter hauteur: '))  
    area = (base * hauteur) / 2  
  
    # calculate the area   
    print('Aire du triangle est: %0.2f' %area)     
elif (choise == 1):
    
    R = int(input("Enter the radius of the circle: "))
    
    area = math.pi * R * R
    print('Aire du disque est: %0.2f' %area) 
 

# Liste des diviseurs d'un entier


n = float(input("entrez l'entier que vous voulez obtenir ses diviseurs:"))              
root = math.ceil(math.sqrt(n))
divisors = []

for i in range(1, root+1):
    if n % i == 0:
        divisors.append(i)
print(divisors)  


#



# Partie 3: les fonctions 
#Exercice 1 : Palindromes, un exo pour les cracs....

def checkForPalindromes(input):
    length = len(input)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
           if(input[first]==input[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break 
    if(status):
        print("c'est un palindrome ")
    else:
        print("c'est pas un palindrome")            
        

input = input("entrez le nom que vous voulez détecter si c'est un palindrom:")
checkForPalindromes(input)


#Écrire une fonction qui calcule la distance entre 2 points A(x1,y1) et B(x2,y2).

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
a = point(4,8)
b = point(9,6)
        
a.x=int(input("enter x-axis de a : "))
a.y=int(input("enter y-axis de a : "))
b.x=int(input("enter x-axis de b : "))
b.y=int(input("enter y-axis de b : "))

result= ((((a.x - b.x )**2) + ((a.y-b.y)**2) )**0.5)
print("distance entre A et B est : ",result)


import turtle
wn=turtle.Screen()
wn.bgcolor("blue")
wn.setup(width-800 , height-600)
wn.tracer(800) 
for i in range(120, 140, 10):
    turtle.circle(i,360)
while True:
    wn.update() 
 
    
