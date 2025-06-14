class User:

    def __init__(self, name, lastname):
        self.first_name = name
        self.last_name = lastname

    def sayName(self):
        print("Мое имя ", self.first_name)

    def sayLastName(self):
        print("Моя фамилия ", self.last_name)

    def sayFullName(self):
        print("Меня зовут", self.first_name, self.last_name)
