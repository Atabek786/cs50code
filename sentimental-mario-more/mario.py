def main():
    while True:
        height_str = input("Height: ")
        if height_str.isdigit():
            height = int(height_str)
            if height >= 1 and height <= 8:
                break
        print("Invalid input. Please enter a numeric value between 1 and 8.")

    for row in range(height):
        for space in range(height - row - 1):
            print(" ", end="")
        for cols in range(row + 1):
            print("#", end="")
        print("  ", end="")
        for cols in range(row + 1):
            print("#", end="")
        print()

if __name__ == "__main__":
    main()

