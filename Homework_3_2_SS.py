list = [12, 3, 4, 10, 8]
print(list, " => ", end=" ")
if len(list) > 0:
    list.insert(0, list[-1])
    list.pop ()
print(list)

list = [12, 3, 4, 10]
print(list, " => ", end=" ")
if len(list) > 0:
    list.insert(0, list[-1])
    list.pop ()
print(list)

list = [1]
print(list, " => ", end=" ")
if len(list) > 0:
    list.insert(0, list[-1])
    list.pop ()
print(list)

list = [ ]
print(list, " => ", end=" ")
if len(list) > 0:
    list.insert(0, list[-1])
    list.pop ()
print(list)
