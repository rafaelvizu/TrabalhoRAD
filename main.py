import tkinter as tk
from tkinter import *
from views.home import HomeView
from views.alunos.index import IndexView as AlunosIndexView


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main App")
        self.geometry("600x600")
        self.resizable(False, False)
        self.frames = {
            "Home": HomeView,
            "AlunosIndex": AlunosIndexView,
        }
        self.show_frame("Home")
        self.extra = {}

    def show_frame(self, page_name):
        # remover o frame atual
        for widget in self.winfo_children():
            widget.destroy()

        frame = self.frames[page_name](self)
        frame.tkraise()

    def set_extra(self, key, value):
        self.extra[key] = value

    def get_extra(self, key):
        return self.extra[key]

    def remove_extra(self, key):
        del self.extra[key]

    def get_all_extra(self):
        return self.extra

    def clear_all_extra(self):
        self.extra.clear()


MainApp().mainloop()
