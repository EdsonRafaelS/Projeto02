import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.title('Ofertas de Disciplinas')
root.geometry('1075x450') #Tamanho principal da tela
root.resizable(False,False) #Não permite 

#Label do ano
label_ano = ttk.Label(root, text='Ano:') #Nome que ira ficar encima do button
label_ano.grid(column=0, row=0) #Posicionando o elemento

#Combobox do ano
button_ano = ttk.Combobox(root) #Combobox é o botão que possui opções
button_ano['values'] = ('2021', '2022', '2023', '2024') #Cria a lista de seleção
button_ano.current(2)  #Define o item que ira ser selecionado automatico
button_ano.grid(column=0, row=1) #Posicionando o button

#Label de semestre
label_semestre = ttk.Label(root, text='Semestre:') #Nome que ira ficar encima do button
label_semestre.grid(column=2, row=0) #Posicionando o elemento

#Combobox do semestre
button_semestre = ttk.Combobox(root) #Combobox é o botão que possui opções
button_semestre['values'] = (1, 2) #Cria a lista de seleção
button_semestre.current(0) #Define o item que ira ser selecionado automatico
button_semestre.grid(column=2, row=1) #Posicionando o button

#Label da disciplina
label_disciplina = ttk.Label(root, text='Disciplina:')
label_disciplina.grid(column=3, row=0)

#Combobox de disciplina
button_disciplina = ttk.Combobox(root)
button_disciplina['values'] = ('Banco de Dados', 'Projeto Integrador', 'Algoritmos')
button_disciplina.current(0)
button_disciplina.grid(column=3, row=1)

#Label do Nível de Ensino
label_NivelDeEnsino = ttk.Label(root, text='Nível de Ensino')
label_NivelDeEnsino.grid(column=4, row=0)

#Combobox do Nível de Ensino
button_NivelDeEnsino = ttk.Combobox(root)
button_NivelDeEnsino['values'] = ('Superior', 'Técnico')
button_NivelDeEnsino.current(1)
button_NivelDeEnsino.grid(column=4, row=1)

#Treelview
colunas = ('Ano', 'Semestre', 'Disciplina', 'Nível')

# Crie o TreeView com colunas e cabeçalhos
treeview_conteudo = ttk.Treeview(root, columns=colunas, show='headings')

# Configurar os cabeçalhos das colunas
for coluna in colunas:
    treeview_conteudo.heading(coluna, text=coluna)

# Exibir o TreeView
treeview_conteudo.grid(columnspan=4, row=3, padx=10, pady=10, sticky=tk.N)


root.grid_columnconfigure(4, weight=1)

root.mainloop()