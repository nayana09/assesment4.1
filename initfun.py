class person:

    #init method or constructor
    '''here name and age are the 2 parameters'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #sample method
    def my_fun(self):
        print("My name is " + self.name)

p1 = person ("Ram", 40)
p2 = person ("sham", 33)
p3 = person ("kamala", 50)

p1.my_fun()
p2.my_fun()
p3.my_fun()


class person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname

person = person("Mrs", "Suray",  "Prakash")
print(person.title)
print(person.name)
print(person.surname)



