user_number = int(input ("Please enter number: "))

if ((user_number)<0 or (user_number)>8640000):
    print("Incorrect number format")
else:
    days = user_number // 86400
    days_rem = user_number % 86400
    hours = days_rem // 3600
    hours_rem = days_rem % 3600
    minutes = hours_rem // 60
    seconds = hours_rem % 60

    if days in (11, 12, 13, 14) or (days % 10) in (0, 5, 6, 7, 8, 9):
        days1 = "днів"
    elif days % 10 == 1:
         days1 = "день"
    else:
         days1 = "дні"

    print(str(days) +" " + days1 +" "+ str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
