import tkinter as tk
from tkinter import *
from views import MenuComponent


class HomeView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.grid()
        MenuComponent(self, master).grid(row=0, column=0)

