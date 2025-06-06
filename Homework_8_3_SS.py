def find_unique_value(some_list):
  unique_numbers = []
  for number in some_list:
    if some_list.count(number) == 1:
      unique_numbers.append(number)
  if len(unique_numbers) == 1:
    return unique_numbers[0]
  else:
    return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([]) is None, 'Test4'
assert find_unique_value([1, 2]) is None, 'Test5'
print("ОК")
