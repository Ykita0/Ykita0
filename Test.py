#-*-coding:Latin-1 -*-
 
from Tkinter import *
import os
 
def ouvrir():
    if (entree.get() == "Aucun fichier"):
        entree.delete(0, END)
        a="Aucun fichier"
        entree.insert(0,str(a))
    elif (entree.get() != ''):
        if (os.path.isfile(entree.get()) == True):
            text.delete(0., END)
            text.insert(1.,open(entree.get(),'r').read())
        else:
            entree.delete(0, END)
            a="Aucun fichier"
            entree.insert(0,str(a))
    else:
        entree.delete(0, END)
        a="Aucun fichier"
        entree.insert(0,str(a))
 
def sauvegarder():
    if (entree.get() == "Aucun fichier"):
        entree.delete(0, END)
        a="Aucun fichier"
        entree.insert(0,str(a))
    elif (entree.get() != ''):
        open(entree.get(), "w").write(text.get(0., END))
    else:
        entree.delete(0, END)
        a="Aucun fichier"
        entree.insert(0,str(a))
     
def python ():
    open("tempo.py", "w").write(text.get(0., END))
    execfile("tempo.py")
    os.system("del tempo.py")
 
fen = Tk()
fen.title('Editeur Python')
 
fileMenu = Menubutton(fen, text ='Fichier')
fileMenu.grid(row =0, column =0)
# Partie "déroulante" :
me1 = Menu(fileMenu)
me1.add_command(label ='Ouvrir', underline =0, command = ouvrir)
me1.add_command(label ='Sauvegarder', underline =0, command = sauvegarder)
me1.add_command(label ='Python', underline =0, command = python)
me1.add_command(label ='Terminer', underline =0, command = fen.quit)
# Intégration du menu :
fileMenu.configure(menu = me1)
 
text = Text()
text.grid(row=1, column=0, columnspan=25, sticky=N, padx=2, pady=2)
Label(fen, text='Fichier :').grid(row =2, column =0)
entree = Entry(fen)
entree.grid(row = 2, column=1)
 
fen.mainloop()