from dataclasses import dataclass


@dataclass
class App:

    name: str = ""

    @property
    def person(self):
        return self.name

    @person.setter
    def set_name(self, name):
        self.name = name


app = App("jenia")
a = app.set_name()
print(a)