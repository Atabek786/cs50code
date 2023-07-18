prompt = input("Input: ")

words = ['A', 'E', 'I', 'O', 'U', ']

converted = prompt

for word in words:
    converted = converted.replace(word, '')

print(converted)
