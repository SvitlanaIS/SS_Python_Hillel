number_user_2 = int(input ("Please enter a 5-digit number from the keyboard: "))
n1 = number_user_2 // 10000
n2 = number_user_2 % 10000 // 1000
n3 = (number_user_2 % 1000) // 100
n4 = (number_user_2 % 1000) % 100 //10
n5 = number_user_2 % 10

result = n5 * 10000 + n4 *1000 + n3 *100 + n2 *10 + n1
print (result)