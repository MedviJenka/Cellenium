class App:

    class SubApp:

        def __init__(self, name):
            self.name = name

        def get_name(self) -> str:
            return self.name


app = App()
a = app.SubApp("jenia")
print(a.get_name())
