from tkinter.filedialog import askopenfile
import tkinter as tk
import auth

import db
from twitterimpl import TwitterClient, limitnessTwitter

listeAdi = ""
taslakAdi = ""

root = tk.Tk()
keyLabel=tk.Label(root, text="search").grid(row=0)
key_secretLabel=tk.Label(root, text="Tweet").grid(row=1)
userLabel=tk.Label(root, text="username ").grid(row=2)
user = tk.StringVar()
keyText = tk.StringVar()
password = tk.StringVar()
key_secretText = tk.StringVar()
e3 = tk.Entry(root,textvariable=keyText)
e4 = tk.Entry(root,textvariable=key_secretText)
e5 = tk.Entry(root,textvariable=user)
e6 = tk.Entry(root,textvariable=password)
e3.grid(row=0, column=1)
e4.grid(row=1, column=1)
e5.grid(row=2, column=1)
e6.grid(row=3, column=1)
twitter = limitnessTwitter()


def login(username,password):
    global twitter
    if(db.login(username,password)):
        twitter = limitnessTwitter([auth.getAuth(db.getUser(username))])
    else:
        raise Exception("username veya password yanlış")



def yolla():
    print("key = "+e3.get()+"\n key_secret = "+e4.get());
    twitter.getProfile(e3.get())


def btnLogin():
    login(e5.get(),e6.get())
tk.Button(root, text='KAYDET', command=yolla).grid(row=5, column=3, sticky=tk.W, pady=4)
tk.Button(root, text='LOGIN', command=btnLogin).grid(row=5, column=2, sticky=tk.W, pady=4)


root.mainloop()