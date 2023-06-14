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

# OU EXCLUSIF

print( True ^ True)
print( True ^ False)
print( False ^ True)
print( False ^ False)


# A     B       A xor B
#True   True    False
#True   False   True
#False  True    True
#False  False   False


# exo course (opérateur OU logique)
#affichez :
# - "je peux aller faire les courses" si on a au moins un moyen de paiement
# - "je ne peux pas aller faire les courses" si je n'ai aucun moyen de paiement
has_cash = bool(random.randint(0,1))
has_cb = bool(random.randint(0,1))

print(f'{has_cash = }')
print(f'{has_cb}')

if has_cash == True or has_cash == True:
    print("je peux aller faire les courses")
else:
    print("je ne peux pas aller faire les courses")

# exo courses (opérateur ET logique)

if has_cash == False and has_cb == False:
    print("je ne peux pas faire les courses")
else:
    print("je peux aller faire les courses")
if not has_cash and not has_cash:
    print("je ne peux pas aller faire les courses")
else:
    print("je peux aller faire les courses")

# Combinaison d'opérateurs AND et OR

user_level = 3
user_score = 0
user_credit = 0

if (user_level >= 3 and user_score >= 100) or user_credit >= 10:
    print("le joueur peut acheter du matériel")
else:
    print("le joueur ne peut pas acheter de matériel")

# exo carte de reduction 
#déterminez la carte de reduction auquelle le a droit:
# - entre 0 et 11 ans (inclus),le voyageur a droit à la gratuité
# - entre 12 et 25 ans (inclus), le voyageur a droit à une réduction de 50%
# -entre 26 et 64 ans (inclus), le voyageur a droit à une réduction de 10%
# - au delà de 65 ans (inclus), le voyageur a droit à une réduction de 50%

age = random.randint(0, 99)

if age >= 0 and age <= 11:
    print("le voyageur a droit à la gratuité")
elif age >= 12 and age <=25 or age >=65 and age <=99:
    print("le voyageur a droit à une réduction de 50%")
elif age >= 26 and age <= 64:
    print("le voyageur a droit à une réduction de 10%")
elif age >=65 and age <=99:
    ("le voyageur a droit à une réduction de 50%")