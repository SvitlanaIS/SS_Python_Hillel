import random
list = [random.randint(0,9) for i in range(random.randint(3, 10))]
print(list, " == ", end=" ")
print ([list[0], list[2], list[-2]])

list = [1, 2, 3, 4, 5, 6, 7, 9]
print(list, " == ", end=" ")
#list1 = list [0: 2:-2]
print ([list[0], list[2], list[-2]])

list = [1, 1, 2, 1]
print(list, " == ", end=" ")
#list1 = list [0: 2:-2]
print ([list[0], list[2], list[-2]])

list = [6, 3, 7]
print(list, " == ", end=" ")
#list1 = list [0: 2:-2]
print ([list[0], list[2], list[-2]])