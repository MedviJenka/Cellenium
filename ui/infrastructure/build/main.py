import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk


@dataclass
class Window:

    window: tk = tk.Tk()

    def __post_init__(self) -> None:
        self.window.geometry('800x800')
        self.window.title('Cellenium')


@dataclass
class Main(Window):

    def __post_init__(self) -> None:
        self.table = ttk.Treeview(self.window, columns=('name', 'type', 'element'), show='headings')
        header_list = ['name', 'type', 'element']
        self.headers_display = [self.table.heading(each, text=each) for each in header_list]
        self.table.pack(fill='both', expand=True)
        self.table.bind('<<TreeviewSelect>>', lambda event: print(self.table.selection()))
        self.table.insert(parent='', index=tk.END, values=['button', 'NAME', 'btnK'])
        self.window.mainloop()


if __name__ == '__main__':
    Main()
