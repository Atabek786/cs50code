def main():
    while True:
        height = int(input("Height: "))
        if height >= 1 and height <= 8:
            break

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

