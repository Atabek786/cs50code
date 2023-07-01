while height < 1 and height > 8:
    height = int(input("Height: "))

for row in range(height):
    for space in range(height - row - 1):
        print(' ')
    for cols in range(rows):
        print('#')
    print('  ')
    for cols in range(rows):
        print('#')
