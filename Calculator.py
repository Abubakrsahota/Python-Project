print("For exponentiation both numbers should be Same.")
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("+ For addition \n- For subtraction \n* For multiplication \n/ For division \n** For exponentiation")
    operator = input("Enter the operator: ")

    match operator:
        case "+":
            print(f"The result of {a} + {b} is: {a + b}")
        case "-":
            print(f"The result of {a} - {b} is: {a - b}")
        case "*":
            print(f"The result of {a} * {b} is: {a * b}")
        case "/":
            if b == 0:
                print("Division by zero is not allowed.")
            else:
                print(f"The result of {a} / {b} is: {a / b}")
        case "**":
            print(f"The result of {a} ** {b} is: {a ** b}")  # Exponentiation
        case _:
            print("Invalid operator. Please use +, -, *, /, or **.")

except Exception as e:
    print("An error occurred:", e)