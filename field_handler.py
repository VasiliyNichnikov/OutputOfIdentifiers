import typing
from config import KEYWORDS


class FieldHandler:
    @property
    def name(self) -> str:
        return self.__name

    def __init__(self, words: typing.List):
        self.__field = words
        self.__name = self.__get_name()

    def __get_name(self) -> str:
        for word in self.__field:
            if word not in KEYWORDS:
                for i in range(len(word)):
                    if word[i] == '=' or word[i] == ';':
                        return word[:i]
                return word
        return ""
