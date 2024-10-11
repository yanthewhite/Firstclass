# Variable Assignment
# Print the values of both A and B
A=5
print(A)
B=A+5
print(B)

#Conditional Execution
" Write a python program that makes decisions based on variable values"
num=7
if num>=10:
    print("True")
else:
    print("num is not greater than 10")

#Combining Conditions
"Use multiple conditions to control the flow of a program"
x=5
y=7
print(x+y)
print(x-y)
print(x/y)
print(x*y)
if (x+y)>=0:
    print("Both are positive")
if (x-y)<0:
    print("only one is positive")
if (x/y)>0:
    print ("neither is positive")
if (x*y)>0:
    print("Both are positive")

# Nested Conditionals

D=75
if D>=90:
    print("Grade: A")
if 80<D<89:
        print("Grade: B")
if 70<D<79:
         print("Grade: C")
else:
        print("Grade: F")

#une function qui va prendre une chaine d'occurence

def compter_occurrences(chaine):
    occurences = {}
    for caractere in chaine:
        if caractere in occurences:
            occurences[caractere] += 1
        else:
            occurences[caractere] = 1
    return occurences

# Exemple d'utilisation
chaine = "bonjour"
resultat = compter_occurrences(chaine)
print(resultat)


