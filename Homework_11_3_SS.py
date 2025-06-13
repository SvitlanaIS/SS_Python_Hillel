#Variant 1
def is_even(number):
     last_digit = str(abs(number))[-1]
     return last_digit in '02468'

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(8) == True, 'Test4'
assert is_even(7) == False, 'Test5'
print('OK')

#Variant 2

def is_even(number):
    return (number & 1) == 0

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(8) == True, 'Test4'
assert is_even(7) == False, 'Test5'
print('OK')