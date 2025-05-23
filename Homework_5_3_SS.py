import string

user_text = str(input ("Please enter text: "))
print (user_text, " -> ", end=" ")
user_text = user_text.title()
for symbol in user_text:
    if symbol in string.punctuation+" ":
        user_text = user_text.replace(symbol, "")
user_text = "#"+user_text
print(user_text[0:140])
