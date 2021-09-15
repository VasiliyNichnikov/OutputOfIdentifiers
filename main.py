"""
    Данный скрипт парсит простые файлы java и выводит имена классов, методов и полей.
"""

from parsing import Parsing

if __name__ == '__main__':
    path: str = 'JavaScript.java'
    reading_java: Parsing = Parsing(path)
    reading_java.output()
