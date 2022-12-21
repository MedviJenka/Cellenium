from dataclasses import dataclass


@dataclass
class App:

    __x: int = 2


app = App()
print(app._App__x)
