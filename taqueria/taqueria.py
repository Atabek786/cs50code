


def get_int(prompt, item, total):
    while True:
        x = input(prompt)
        try:
            if x in menu:
                total += menu[item]
            return total
        except EOFError:
            return True
        except KeyError:
            pass

if __name__ == "__main__":
    main()
