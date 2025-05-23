while True:
   number1 = int(input ("Please enter a first number from the keyboard: "))
   number2 = int(input ("Please enter a second number from the keyboard: "))
   operation = str(input ("Please enter a mathematical operation (+, -, *, /):"))
   match operation:
        case "+":
           result = number1 + number2
           print(result)
        case "-":
            result = number1 - number2
            print(result)
        case "*":
            result = number1 * number2
            print(result)
        case "/":
            if number2 != 0:
                result = number1 / number2
                print(result)
            else:
                print("Division by 0 is impossible")
        case _:
             print("Invalid operator entered")

   user_input = input("Please enter 'y' to continue: ")
   if user_input != "y":
      break

