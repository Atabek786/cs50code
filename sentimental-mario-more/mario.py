height = int(input("Height: "))
if height < 1 or height > 8:
    print("give an integer between 1 and 8")

for row in height:
    for space in (height - row):
        print(' ')
    for cols in range(row + 1):
        print('#')
    print('  ')
    for cols in range(row + 1):
        print('#')
