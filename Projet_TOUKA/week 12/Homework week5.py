# DSC 510
# Week 4
# Programming Assignment Week 5
# Author TOUKA
# 9/25/2024

# Calculation program with loops and functions

def perform_calculation(operation):
    """Performs an arithmetic operation on two numbers."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero.")
                return
        else:
            print("Invalid operation.")
            return

        print(f"The result of {num1} {operation} {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")


def calculate_average():
    """Calculates the average of several numbers entered by the user."""
    try:
        count = int(input("How many numbers do you want to enter? "))
        if count <= 0:
            print("Error: Number must be greater than zero.")
            return

        total = 0
        for i in range(count):
            num = float(input(f"Enter the number {i + 1}: "))
            total += num

        average = total / count
        print(f"The average of the numbers entered is: {average}")
    except ValueError:
        print("Error: Please enter valid numbers.")


def main():
    """Main program loop."""
    while True:
        print("\nOptions:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Calculate the average")
        print("6. To leave")

        choice = input("Choose an option: ")

        if choice == '1':
            perform_calculation('+')
        elif choice == '2':
            perform_calculation('-')
        elif choice == '3':
            perform_calculation('*')
        elif choice == '4':
            perform_calculation('/')
        elif choice == '5':
            calculate_average()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again..")


if __name__ == "__main__":
    main()