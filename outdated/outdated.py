months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    prompt = input("Date: ")
    try:
        month, day, year = prompt.split('/')
        if (int(month) >=1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            str_month, str_day, year = prompt.split(" ")

            for i in range(len(months)):
                if str_month == months[i]:
                    month = i + 1
            day = str_day.replace(",","")

            if (int(month) >=1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass




print(f"{year}-{int(month):02}-{int(day):02}")