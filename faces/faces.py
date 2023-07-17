def main():
    text = input()
    converted = convert(text)
    print(converted)

def convert(text):
    smile = text.replace(':)', '🙂')

    sad = smile.replace(':(', '🙁')

    return sad;
main()