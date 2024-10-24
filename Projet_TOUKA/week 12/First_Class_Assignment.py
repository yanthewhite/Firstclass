#Assignment 5

def plus_grand_de_trois():
    """
    Cette fonction détermine et affiche le plus grand de trois entiers saisis par l'utilisateur.
    """
    try:
        # Saisir les trois entiers
        A = int(input("Entrez le premier entier (A): "))
        B = int(input("Entrez le deuxième entier (B): "))
        C = int(input("Entrez le troisième entier (C): "))

        # Déterminer le plus grand entier
        if A >= B and A >= C:
            plus_grand = A
        elif B >= A and B >= C:
            plus_grand = B
        else:
            plus_grand = C

        # Afficher le plus grand entier
        print(f"Le plus grand des trois entiers est: {plus_grand}")

    except ValueError:
        print("Veuillez entrer des entiers valides.")

# Appel de la fonction
plus_grand_de_trois()



#Assignment 4

def pair_ou_impair():
    """
    Cette fonction détermine si un nombre entier saisi par l'utilisateur est pair ou impair.
    """
    try:
        # Saisir un nombre entier
        nombre = int(input("Entrez un nombre entier: "))

        # Déterminer si le nombre est pair ou impair
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impair.")

    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction
pair_ou_impair()


# Assignment 3

def echanger_entiers():
    """
    Cette fonction permet d'échanger le contenu de deux entiers saisis par l'utilisateur
    et affiche ces entiers après l'échange.
    """
    try:
        # Saisir les deux entiers
        A = int(input("Entrez le premier entier (A): "))
        B = int(input("Entrez le deuxième entier (B): "))

        # Afficher les valeurs avant l'échange
        print(f"Avant l'échange: A = {A}, B = {B}")

        # Échanger les valeurs
        A, B = B, A

        # Afficher les valeurs après l'échange
        print(f"Après l'échange: A = {A}, B = {B}")

    except ValueError:
        print("Veuillez entrer des entiers valides.")

# Appel de la fonction
echanger_entiers()


#Assignment 2

def display_product():
    """
    This function prompts the user to enter two numbers
    and then displays their product.
    """
    try:
        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the product
        product = num1 * num2

        # Display the product
        print(f"The product of {num1} and {num2} is {product}.")

    except ValueError:
        print("Please enter valid numbers.")
# Call the function
display_product()


# Assignment 1

from datetime import datetime

def Hello_new_programmer(name, dob):
    """
    This function greets the new programmer and calculates their age.
    :param name: str : User's name
    :param dob: str : User's date of birth in mm/dd/yyyy format
    :return: None
    """
 # Check if the name has at least 3 characters
    if len(name) < 3:
        print("Error: The name must contain at least 3 characters.")
        return

# Convert the date of birth from string to datetime object
    try:
        birth_date = datetime.strptime(dob, '%m/%d/%Y')
    except ValueError:
        print("Error: The date of birth must be in mm/dd/yyyy format.")
        return

# Calculate the age
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Check if the user is at least 10 years old
    if age < 10:
        print("Error: The minimum age to learn programming is 10 years old.")
        return

 # Print the greeting message
    print(f"Hello {name}! Welcome to learning Python.")
    print(f"You are {age} years old today.")


# Test the function
Hello_new_programmer("Alice", "04/15/2005")

