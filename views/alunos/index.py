import tkinter as tk
from tkinter import *
from views import MenuComponent


# alunos index view
class IndexView(tk.Frame):
    def __init__(self, master, extra=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.config(padx=10, pady=10)
        MenuComponent(self, master).grid(row=0, column=0)

        alunos = [
            {"id": 1, "nome": "João", "matricula": "123"},
            {"id": 2, "nome": "Maria", "matricula": "456"},
            {"id": 3, "nome": "José", "matricula": "789"},
        ]

        # forms para adicionar aluno
        self.nome = StringVar()
        self.matricula = StringVar()

        Label(self, text="Nome").grid(row=1, column=0)
        Entry(self, textvariable=self.nome).grid(row=1, column=1)

        Label(self, text="Matrícula").grid(row=2, column=0)
        Entry(self, textvariable=self.matricula).grid(row=2, column=1)

        Button(self, text="Adicionar", command=self.add_aluno).grid(row=3, column=0, columnspan=2, pady=10)

        # tabela de alunos
        Label(self, text="Lista de alunos").grid(row=4, column=0, columnspan=2, pady=10)

        # cabeçalho da tabela
        Label(self, text="ID").grid(row=5, column=0)
        Label(self, text="Nome").grid(row=5, column=1)
        Label(self, text="Matrícula").grid(row=5, column=2)

        # corpo da tabela
        for i, aluno in enumerate(alunos):
            Label(self, text=aluno["id"]).grid(row=i+6, column=0)
            Label(self, text=aluno["nome"]).grid(row=i+6, column=1)
            Label(self, text=aluno["matricula"]).grid(row=i+6, column=2)
            Button(self, text="Excluir", command=lambda id=aluno["id"]: self.delete_aluno(id)).grid(row=i+6, column=3)


    def add_aluno(self):
        print("Adicionar aluno")
        print("Nome:", self.nome.get())
        print("Matrícula:", self.matricula.get())

    def delete_aluno(self, id):
        print("Excluir aluno", id)
