# Advanced Calculator

def show_menu():
    print("\n====== Advanced Calculator ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Modulus (%)")
    print("7. Percentage")
    print("8. View History")
    print("9. Exit")


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")


def calculator():
    history = []

    while True:
        show_menu()
        choice = input("Choose an option (1-9): ")

        if choice == '9':
            print("Exiting calculator. Goodbye!")
            break

        elif choice == '8':
            print("\n--- Calculation History ---")
            if history:
                for item in history:
                    print(item)
            else:
                print("No history yet.")
            continue

        elif choice in ['1','2','3','4','5','6','7']:
            num1, num2 = get_numbers()

            if choice == '1':
                result = num1 + num2
                operation = f"{num1} + {num2} = {result}"

            elif choice == '2':
                result = num1 - num2
                operation = f"{num1} - {num2} = {result}"

            elif choice == '3':
                result = num1 * num2
                operation = f"{num1} * {num2} = {result}"

            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero")
                    continue
                result = num1 / num2
                operation = f"{num1} / {num2} = {result}"

            elif choice == '5':
                result = num1 ** num2
                operation = f"{num1} ^ {num2} = {result}"

            elif choice == '6':
                result = num1 % num2
                operation = f"{num1} % {num2} = {result}"

            elif choice == '7':
                result = (num1 / num2) * 100 if num2 != 0 else None
                if result is None:
                    print("Error: Division by zero")
                    continue
                operation = f"{num1} is {result}% of {num2}"

            print("Result:", result)
            history.append(operation)

        else:
            print("Invalid choice. Try again.")


# Run program
calculator()