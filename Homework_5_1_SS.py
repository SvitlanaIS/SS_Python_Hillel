import string
import keyword

my_punctuation = string.punctuation.replace("_", " ")
user_text = str(input ("Please enter text: "))

if (user_text[0] in string.digits or
    user_text != user_text.lower() or
    user_text.count("__") >= 1 or
    user_text in keyword.kwlist):
    print(False)
else:
    bad_text = False
    for symbol in user_text:
        if symbol in my_punctuation:
            bad_text = True
            break
    if bad_text:
        print(False)
    else:
        print (True)

# test_data = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value", "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]
#
# for user_text in test_data:
#     print(user_text, " => ", end=" ")
#     if (user_text[0] in string.digits or
#     user_text != user_text.lower() or
#     user_text.count("__") >= 1 or
#     user_text in keyword.kwlist):
#         print(False)
#     else:
#         bad_text = False
#         for symbol in user_text:
#             if symbol in my_punctuation:
#                 bad_text = True
#                 break
#         if bad_text:
#             print(False)
#         else:
#             print (True)