import requests
flags = ["read", "write", "append", "url"]

class MyFile:
    def __init__(self, name, flag):
        if flag not in flags:
            print("Недопустимый флаг")
        if not name:
            print("Пустое имя")
        self.name = name
        self.flag = flag

    def read(self):
        if self.flag not in ["read", "write", "append"]:
            print("Неправильный флаг")
        try:
            f = open(self.name, mode = 'r')
        except FileNotFoundError:
            return "Несуществующий файл"
        a = f.read()
        f.close()
        return a
    
    def write(self, string):
        if self.flag not in ["write", "append"]:
            print("Неправильный флаг")
        if self.flag == "write":
            f = open(self.name, mode = 'w')
        elif self.flag == "append":
            f = open(self.name, mode = 'a')
        f.write(string)
        f.close()
    
    def read_url(self):
        if self.flag != "url":
            return "Неправильный флаг"
        try:
            s = requests.get(self.name)
            s.close()
            return s.text
        except requests.ConnectionError:
            return "Сайт не найден"
    
    def count_urls(self):
        if self.flag != "url":
            return "Неправильный флаг"
        try:
            s = requests.get(self.name)
            text = s.text
            count = text.count('href=')
            s.close()
            return count
        except requests.ConnectionError:
            return "Сайт не найден"
    
    def write_url(self, name):
        if self.flag != "url":
            return "Неправильный флаг"
        try:
            f = open(name, mode = 'w')
            s = requests.get(self.name)
            f.write(s.text)
            f.close()
            s.close()
        except requests.ConnectionError:
            print("Сайт не найден")