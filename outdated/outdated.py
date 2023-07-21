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
        