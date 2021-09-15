import typing
from config import KEYWORDS
from function_handler import FunctionHandler
from field_handler import FieldHandler


class Parsing:
    def __init__(self, path: str) -> None:
        self.__path = path
        self.__words: typing.List[str] = self.__get_words()

        self.__classes: typing.List[str] = []
        self.__functions: typing.List[FunctionHandler] = []
        self.__fields: typing.List[FieldHandler] = []

        self.__word_handler()

    def __get_words(self) -> typing.List[str]:
        with open(self.__path, 'r') as file:
            words: typing.List[str] = file.read().split()
        return words

    def __word_handler(self) -> None:
        for i in range(len(self.__words)):
            word: str = self.__words[i]
            if word == "class":
                class_name: str = self.__words[i + 1]
                self.__classes.append(class_name)
            elif word == "void":
                func_h: FunctionHandler = FunctionHandler(self.__words[i + 1:])
                self.__functions.append(func_h)

            elif word in KEYWORDS:
                is_field, number_end = self.__is_field(self.__words[i:])
                if is_field:
                    field_h = FieldHandler(self.__words[i: number_end + i])
                    self.__fields.append(field_h)
                elif self.__is_func(self.__words[i + 1: number_end + i]):
                    func_h: FunctionHandler = FunctionHandler(self.__words[i + 1: number_end + i])
                    self.__functions.append(func_h)

    @staticmethod
    def __is_field(words: typing.List[str]) -> (bool, int):
        for i in range(len(words)):
            if '=' in words[i] or ';' in words[i]:
                return True, i + 1
            if ')' in words[i]:
                return False, i + 1
        return False, 0

    @staticmethod
    def __is_func(words: typing.List[str]) -> bool:
        func: str = ' '.join(words)
        return '(' in func and ')' in func

    def output(self):
        print(f"Кол-во классов: {len(self.__classes)}. Имена классов:")
        for c in self.__classes:
            print(f"Имя: {c};")
        print()
        print(f"Кол-во методов: {len(self.__functions)}. Имена и параметры методов:")
        for func in self.__functions:
            parameters: str = func.parameters
            if len(parameters) == 0:
                parameters = "нет"
            print(f"Имя: {func.name}; Параметры: {parameters};")
        print()
        print(f"Кол-во полей: {len(self.__fields)}. Имена полей:")
        for field in self.__fields:
            print(f"Имя: {field.name}")

