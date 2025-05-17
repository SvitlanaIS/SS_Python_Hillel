list = [1, 2, 3, 4, 5, 6]
print(list, " => [", end=" ")
p=(len(list)//2) + len(list) % 2
print(list[:p], ", ", end=" ")
print(list[p:], "]")

list = [1, 2, 3]
print(list, " => [", end=" ")
p=(len(list)//2) + len(list) % 2
print(list[:p], ", ", end=" ")
print(list[p:], "]")

list = [1, 2, 3, 4, 5]
print(list, " => [", end=" ")
p=(len(list)//2) + len(list) % 2
print(list[:p], ", ", end=" ")
print(list[p:], "]")

list = [1]
print(list, " => [", end=" ")
p=(len(list)//2) + len(list) % 2
print(list[:p], ", ", end=" ")
print(list[p:], "]")

list = [ ]
print(list, " => [", end=" ")
p=(len(list)//2) + len(list) % 2
print(list[:p], ", ", end=" ")
print(list[p:], "]")
