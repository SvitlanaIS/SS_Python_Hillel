def add_one(some_list):
    some_list = int(''.join(map(str, some_list)))
    some_list = some_list + 1
    some_list = list(map(int, str(some_list)))
    return some_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


def add_one_1(some_list):
  for i in range(len(some_list), 0, -1):
    if some_list[i-1] < 9:
        some_list[i-1] += 1
        break
    else:
        some_list[i-1] = 0
        if i == 1:
          some_list.insert(0, 1)
          break
  return some_list

assert add_one_1([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one_1([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one_1([0]) == [1], 'Test3'
assert add_one_1([9]) == [1, 0], 'Test4'
print("ОК")

