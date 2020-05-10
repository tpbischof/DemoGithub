import sys

import requests

print(sys.executable)
print(sys.version)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return self.first_name + " " + self.last_name


p = Person("tom", "bischof")
print(p)
print(p.fullname)
print(p.fullname())
print(Person.fullname)
print(Person.fullname(p))

r = requests.get("https://google.de")
print(r.status_code)

i = input("Please enter your name: ")
print("Hello,", i)
