def is_palindrome(text):
   import string
   for symbol in text:
      if symbol in string.punctuation+" ":
       text = text.replace(symbol, "")
   text = text.lower()
   text1 = text[::-1]
   return text1 == text

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
