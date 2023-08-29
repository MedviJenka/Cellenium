import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk
from core.infrastructure.modules.executor import Executor


@dataclass
class Window(Executor):

    window: tk = tk.Tk()

    def __post_init__(self) -> None:
        self.window.geometry('800x800')
        self.window.title('Cellenium')

    def execute(self) -> None:
        self.window.mainloop()


@dataclass
class App(Window):

    def __post_init__(self) -> None:
        self.table = ttk.Treeview(self.window, columns=('name', 'type', 'element'), show='headings')
        self.header_list = ['name', 'type', 'element']
        self.headers_display = [self.table.heading(each, text=each) for each in self.header_list]
        self.table.pack(fill='both', expand=True)
        self.table.bind('<<TreeviewSelect>>', lambda event: print(self.table.selection()))
        self.table.insert(parent='', index=tk.END, values=['button', 'NAME', 'btnK'])


app = App()
if __name__ == '__main__':
    app.execute()
