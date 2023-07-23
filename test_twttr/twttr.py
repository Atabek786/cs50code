def main():
    prompt = input("Input: ")
    result = shorten(prompt)
    print(result)


def shorten(word):
    words = ['a', 'e', 'i', 'o', 'u']
    for w in words:
        word = word.replace(w, '')
    return word

if __name__ == "__main__":
    main()