import unicodedata
# import re


class Strings:

    def __init__(self):
        self.string = None

    def add_string(self, string: str):
        self.string = string

    def remove_non_ascii(self) -> str:
        return self.string.encode('ascii', 'ignore').decode('utf8').casefold()

    def remove_non_ascii_normalized(self) -> str:
        normalized = unicodedata.normalize('NFD', self.string)
        return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

    # def remove_combining_regex(string: str) -> str:
    #     normalized = unicodedata.normalize('NFD', string)
    #     return re.sub(r'[\u0300-\u036f]', '', normalized).casefold()

    # def remove_combining_fluent(string: str) -> str:
    #     normalized = unicodedata.normalize('NFD', string)
    #     return ''.join(
    #         [l for l in normalized if not unicodedata.combining(l)]
    #     ).casefold()


if __name__ == '__main__':

    string = 'Atenção \N{SNAKE}'
    # string = 'áéíóú'

    s1 = Strings()

    s1.add_string(string)

    print(string)
    print(s1.remove_non_ascii())
    print(s1.remove_non_ascii_normalized())
