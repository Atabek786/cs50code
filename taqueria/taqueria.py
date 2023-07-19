def main():
    ...



def get_int(prompt, item, total):
    while True:
        x = input(prompt)
        try:
            if x in menu:
                total += menu[item]



menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

if __name__ == "__main__":
    main()
