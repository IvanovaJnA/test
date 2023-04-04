class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def myfunc(self):
        print('Привет, меня зовут ' + self.name)
        print('Привет, меня зовут %s' % self.name)
ob1 = Person('Anna', 15)
ob1.myfunc()
