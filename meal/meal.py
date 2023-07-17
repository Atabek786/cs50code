def main():
    time = input("What time is it? ")
    converted = convert(time)

    if 7.0 <= converted <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted <= 13.0:
        print("lunch time")
    elif 18.0 <= converted <= 19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(':')
    float_time = float(hours) + float(minutes) / 60
    return float_time

if __name__ == "__main__":
    main()