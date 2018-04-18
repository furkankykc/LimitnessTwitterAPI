from tkinter.filedialog import askopenfile
import tkinter as tk

import twitterRest
from test import getir
from twitterimpl import tweetGetir


listeAdi = ""
taslakAdi = ""

root = tk.Tk()
keyLabel=tk.Label(root, text="KEY").grid(row=0)
key_secretLabel=tk.Label(root, text="KEY-SECRET").grid(row=1)
userLabel=tk.Label(root, text="username ").grid(row=2)
user = tk.StringVar()
keyText = tk.StringVar()
key_secretText = tk.StringVar()
e3 = tk.Entry(root,textvariable=keyText)
e4 = tk.Entry(root,textvariable=key_secretText)
e5 = tk.Entry(root,textvariable=user)
e3.grid(row=0, column=1)
e4.grid(row=1, column=1)
e5.grid(row=2, column=1)

def yolla():
    print("key = "+e3.get()+"\n key_secret = "+e4.get());
    tweetGetir(username="furkankykc",count=100, cpt=20)


def gel():
    for i in (getir(e5.get())):
        print(i)

tk.Button(root, text='KAYDET', command=yolla).grid(row=5, column=3, sticky=tk.W, pady=4)
tk.Button(root, text='SORGULA', command=gel).grid(row=5, column=2, sticky=tk.W, pady=4)


root.mainloop()