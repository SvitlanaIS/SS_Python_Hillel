import string

user_text = str(input ("Please enter text: "))

if (((len(user_text) !=3) or
    (user_text[1] != "-") or
    not (user_text[0].isalpha()) or
    not (user_text[2]).isalpha())):
    print("Incorrect text format")
else:
    start=string.ascii_letters.index(user_text[0])
    end=string.ascii_letters.index(user_text[2])
    if end < start:
       print(string.ascii_letters[end: start+1][::-1])
    else:
        print(string.ascii_letters[start:end+1])
