import tkinter as tk
from tkinter import *


class MenuComponent(tk.Frame):
    def __init__(self, master, root, extra=None):
        tk.Frame.__init__(self, master)

        if extra is None:
            extra = {}

        self.root = root
        self.grid()
        self.config(padx=5, pady=5)
        label = Label(self, text="Menu")
        label.grid(row=0, column=0)
        button = Button(self, text="Alunos", command=self.alunos)
        button.grid(row=0, column=1)
        button = Button(self, text="Professores", command=self.professores)
        button.grid(row=0, column=2)
        button = Button(self, text="Disciplinas", command=self.disciplinas)
        button.grid(row=0, column=3)
        button = Button(self, text="Turmas", command=self.turmas)
        button.grid(row=0, column=4)
        button = Button(self, text="Notas", command=self.notas)
        button.grid(row=0, column=5)

    def alunos(self):
        self.root.show_frame("AlunosIndex")

    def professores(self):
        print("Professores")

    def disciplinas(self):
        print("Disciplinas")

    def turmas(self):
        print("Turmas")

    def notas(self):
        print("Notas")
