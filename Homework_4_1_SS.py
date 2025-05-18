list = [0, 1, 0, 12, 3]
print (list, " -> ", end=" ")
x = list.count (0)
for i in range(1, x+1):
   list.remove (0)
   list.append (0)
print (list)

list = [0]
print (list, " -> ", end=" ")
x = list.count (0)
for i in range(1, x+1):
   list.remove (0)
   list.append (0)
print (list)

list = [1, 0, 13, 0, 0, 0, 5]
print (list, " -> ", end=" ")
x = list.count (0)
for i in range(1, x+1):
   list.remove (0)
   list.append (0)
print (list)

list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print (list, " -> ", end=" ")
x = list.count (0)
for i in range(1, x+1):
   list.remove (0)
   list.append (0)
print (list)