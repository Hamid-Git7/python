#import du module ramdom
import random 

# arithmétique
a = 123 + 42
a = 123 - 42
a = 123 * 42
a = 123 / 42

# division entière, integer division
a = 123 // 42
print (a)

#modulo entière, integer division

#opérateurs composés
b = 0

#incrémentation
# b = b + 1
b = b + 1
b += 1
print (b)

#soustraction
b = b - 1
b -= 1
print (b)

#multiplication
c = 3
# c = c * 2
c *= 2
print (c)

#division
d = 10
# d = d / 3
d /= 3
print (d)

#division entière
d = 10
# d = d // 3
d //= 3
print (d)

#opérateur d'inclusion
text1 = "Lorem ipsum"

result ="e" in text1
print (result)

list1 = ["Lorem", "ipsum"]
print ("e" in list1)

#comparaison avec des nombres aléatoires
e = random.randint (0,100)
f = random.randint (0,100)

print(f'{e = }')
print(f'{f = }')

result = e == f
print(result)

result = e < f
print(result)

# est une expression
# 1 + 1 -> 2
# (100 + 2) * 3 -> 102 * 3 -> 306
# 1 + 1 > (100 + 2) * 3 -> 2 > 306 -> False

# n'est pas une expression
#print(100)