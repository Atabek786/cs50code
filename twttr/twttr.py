prompt = input("Input: ")

words = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']


for word in words:
    prompt = prompt.replace(word, '')

print(prompt)
