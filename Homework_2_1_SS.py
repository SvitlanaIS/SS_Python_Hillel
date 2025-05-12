#Variant 1
number_user_1 = int(input ("Please enter a 4-digit number from the keyboard: "))
n1 = number_user_1 // 1000
n2 = number_user_1  % 1000 // 100
n3 = (number_user_1  % 100) // 10
n4 = number_user_1  % 10

print (n1)
print (n2)
print (n3)
print (n4)

#Variant 2

number_user_1 = int(input ("Please enter a 4-digit number from the keyboard: "))
print (number_user_1 // 1000)
print (number_user_1  % 1000 // 100)
print ((number_user_1  % 100) // 10)
print (number_user_1  % 10)