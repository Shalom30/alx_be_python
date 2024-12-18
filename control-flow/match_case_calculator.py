num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the  second number: "))
operation = input("Choose the operator (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by 0.")
            exit()
        else:
            result = num1 / num2

print("The result of the calculation is " + str(result))


