def calculator():
    print("\n🔢 Welcome to Simple Calculator 🔢")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            op = '+'
        elif choice == '2':
            result = num1 - num2
            op = '-'
        elif choice == '3':
            result = num1 * num2
            op = '*'
        elif choice == '4':
            if num2 == 0:
                print("❗ Cannot divide by zero.")
                return
            result = num1 / num2
            op = '/'
        else:
            print("❗ Invalid operation choice.")
            return

        print(f"\n✅ Result: {num1} {op} {num2} = {result}")
    
    except ValueError:
        print("❗ Invalid input. Please enter numbers only.")

# Run the calculator
calculator()
