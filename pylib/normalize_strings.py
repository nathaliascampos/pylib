import unicodedata


def remove_non_ascii(string) -> str:
    return string.encode('ascii', 'ignore').decode('utf8').casefold()


def remove_non_ascii_normalized(string) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()


if __name__ == '__main__':

    string = 'Atenção \N{SNAKE}'
    # string = 'áéíóú'

    print(string)
    print(remove_non_ascii(string))
    print(remove_non_ascii_normalized(string))
