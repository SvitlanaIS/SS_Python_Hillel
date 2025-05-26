user_number = str(input ("Please enter number: "))

if not user_number.isnumeric():
    print("Incorrect number format")
else:
    user_number = int(user_number)
    print (user_number, " -> ", end=" ")
    number = user_number
    while number>=10:
       mult=1
       while number > 0:
            mult = mult * (number % 10)
            number = (number // 10)
       number = mult
       if number == 0:
        break
    print(number)
