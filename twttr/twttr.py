
def main():
    result = shorten(word)
    



def shorten(word):
    prompt = input("Input: ")
    words = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    converted = prompt
    for word in words:
        converted = converted.replace(word, '')


