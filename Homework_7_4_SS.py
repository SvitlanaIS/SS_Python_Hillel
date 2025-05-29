def common_elements():
    list1 = [i for i in range (0, 100) if i % 3 == 0]
    list2 = [i for i in range (0, 100) if i % 5 == 0]
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return intersection

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
