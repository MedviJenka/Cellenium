import customtkinter
from dataclasses import dataclass
from core.infrastructure.modules.executor import Executor


@dataclass
class App(Executor):

    root = customtkinter.CTk()
    frame = customtkinter.CTkFrame(master=root)
    label = customtkinter.CTkLabel(master=frame, text='Cellenium', font=("Roboto", 24))
    button_1 = customtkinter.CTkButton(master=frame, text='Edit Suite', text_color='white', font=('Roboto', 20))

    def __post_init__(self) -> None:
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')
        self.root.geometry('500X350')
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)
        self.label.pack(padx=10, pady=12)
        self.button_1.pack(padx=10, pady=12)

    @property
    def button_event(self) -> str:
        return "ok"

    def execute(self) -> None:
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.execute()
