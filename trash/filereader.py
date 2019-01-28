import sys




class FileReader:

    def __init__(self, arg):
        self.arg = sys.argv[1]

    def read(self):
        try:
            with open(self.arg, "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return "Отсутствует файл для чтения по адресу : {}".format(self.arg)
        except IsADirectoryError:
            return "Указана только директория. Укажите полный путь до файла."
        except IndexError:
            print("Отсутствует путь до файла для чтения")


try:
    reader = FileReader(sys.argv[1])
    print(reader.read())
except IndexError:
    print("Отсутствует путь до файла для чтения")
