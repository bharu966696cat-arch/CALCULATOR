def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def modulo(a, b):
    if b == 0:
        return "Error! Modulo by zero."
    return a % b


def main():
    while True:
        print("\n====== SIMPLE CALCULATOR ======")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "6":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice! Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            print("Result:", add(a, b))

        elif choice == "2":
            print("Result:", subtract(a, b))

        elif choice == "3":
            print("Result:", multiply(a, b))

        elif choice == "4":
            print("Result:", divide(a, b))

        elif choice == "5":
            print("Result:", modulo(a, b))


if __name__ == "__main__":
    main()