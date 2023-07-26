import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    # Check if the time is in the 12-hour format (hh:mm AM/PM)
    if re.match(r"\b(1[0-2]|0?[1-9]):[0-5][0-9] [APap][Mm]\b", s):
        # Convert to 24-hour format (HH:MM)
        time_obj = datetime.datetime.strptime(s, "%I:%M %p")
        return time_obj.strftime("%H:%M")

    # Check if the time is in the 24-hour format (HH:MM)
    elif re.match(r"\b(?:2[0-3]|[01]?[0-9]):[0-5][0-9]\b", s):
        # Convert to 12-hour format (hh:mm AM/PM)
        time_obj = datetime.datetime.strptime(s, "%H:%M")
        return time_obj.strftime("%I:%M %p")

    else:
        return "Format not supported"




if __name__ == "__main__":
    main()