import customtkinter
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional
from core.tools.suite_runner.suite_runner import TestSuite


run = TestSuite()


class Execute(ABC):

    @abstractmethod
    def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> None:
        ...


@dataclass
class App(Execute):

    root = customtkinter.CTk()
    frame = customtkinter.CTkFrame(master=root)
    label = customtkinter.CTkLabel(master=frame, text='Cellenium', font=("Roboto", 24))
    button_1 = customtkinter.CTkButton(master=frame, text='Suite', text_color='white', font=('Roboto', 20))
    button_2 = customtkinter.CTkButton(master=frame,
                                       text='Run',
                                       text_color='white',
                                       font=('Roboto', 20),
                                       command=...)

    def __post_init__(self) -> None:
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')
        self.root.geometry('500X350')
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)
        self.label.pack(padx=10, pady=12)
        self.button_1.pack(padx=10, pady=12)
        self.button_2.pack(padx=10, pady=12)

    @property
    def button_event(self) -> None:
        return ...

    def execute(self) -> None:
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.execute()
