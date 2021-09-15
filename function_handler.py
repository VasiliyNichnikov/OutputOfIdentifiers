import typing


class FunctionHandler:
    @property
    def name(self) -> str:
        return self.__name

    @property
    def parameters(self) -> str:
        return self.__parameters

    def __init__(self, words: typing.List[str]):
        self.__words = words
        self.__parts_of_function = self.__get_name_and_parameters()
        self.__name = self.__get_name()
        self.__parameters = self.__get_parameters()

    def __get_name_and_parameters(self) -> typing.List[str]:
        opening_parenthesis: bool = False
        closing_parenthesis: bool = False
        result: typing.List[str] = []

        for word in self.__words:
            if '(' in word:
                opening_parenthesis = True
            elif ')' in word:
                closing_parenthesis = True
            result.append(word)

            if opening_parenthesis and closing_parenthesis:
                return result
        return result

    def __get_name(self) -> str:
        func: str = ' '.join(self.__parts_of_function)
        name: str = ""
        for letter in func:
            if letter not in [' ', '(']:
                name += letter
            else:
                return name
        return name

    def __get_parameters(self) -> str:
        func: str = ' '.join(self.__parts_of_function)
        parameters: str = ""
        opening_parenthesis: bool = False
        closing_parenthesis: bool = False

        for letter in func:
            if letter == ')':
                closing_parenthesis = True

            if opening_parenthesis and not closing_parenthesis:
                parameters += letter

            if letter == '(':
                opening_parenthesis = True

            if opening_parenthesis and closing_parenthesis:
                return parameters
        return parameters
