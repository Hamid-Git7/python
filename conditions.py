import random

if True:
    print("Ce message s'affichera toujours")

if False:
    print("Ce message ne s'affichera jamais")

number1 = random.randint (0, 10)
number2 = random.randint (0, 10)

print(f'{number1 = }')
print(f'{number2 = }')

if number1 < number2:
    print("La valeur de number1 est plus petite que number2")

else: #number1 >= number2
    print("La variable de number1 est plus grande ou égale que number2")

if number1 >= number2:
    print( "La variable number1 est plus petite que number2")

elif number1 > number2:
        print("La variable number1 est plus grande que number2")

else:
        print("les deux vairiables number1 et number2 sont égales")

#elif == else if

#block if4
#réécriture du block if3 aces des if imbriqués

if number1 >= number2:
    print( "La variable number1 est plus petite que number2")

elif number1 > number2:
    print("La variable number1 est plus grande que number2")

else:
    print("les deux vairiables number1 et number2 sont égales")

    #opérateurs boléens

    #négation
    print(not True)
    print(not False)

#Table de vérité de l'opérateur de négation
#A   not A
#True False
#False True

#OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Table de vérité de l'opérateur OU logique

# A     B       A or B
#True   True    True
#True   False   True
#False  True    True
#False  False   False

# pour retrouver la table, remplacez :
# - A par " j'ai du cash"
# - B par " j'ai une cb"
# - A or B" puis-je faire mes courses?""

#ET logique
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# table de vérité de l'opérateur ET logique
# A     B       A and B
#True   True    True
#True   False   False
#False  True    False
#False  False   False

# pour retrouver la table, remplacez:
# - A par "j'ai coupé l'électricité"
# - B par "j'ai coupé l'eau"
# - A and B par "puis-je partir 3 mois à l'étranger ?"

# table de vérité de l'opérateur NAND (not and)
# A     B       A and B
#True   True    False
#True   False   True
#False  True    True
#False  False   True


