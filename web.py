import flask

import auth
import db
from test import *
from flask import Flask, request, render_template, redirect
from twitterimpl import limitnessTwitter
app = Flask("Limitness Twitter API")

def gel(username='furkankykc'):
    a = ""
    renk =["red","blue"]
    count=1
    loginList = [auth.getAuth(i) for i in db.getUsers()]
    lt=limitnessTwitter(loginList)
    for i in lt.getProfile(username):
        if i != None:
            for j in i:
                tweets.create(id=str(j.id), text=j.text, author_id=j.author.screen_name,
                               date=j.created_at)

                a += "<font color=\""+renk[count%2]+"\">"+j.text + "</font><br/>"
                count+=1
    return "Bu kullanıcının tweet sayısı : "+str(count)+"<br/>"+a

@app.route('/')
def index():
    return redirect('/tweets')

@app.route('/tweets/',methods=['GET','POST'])
def mytweets():
    if request.method == "POST":
        text = request.form['text']
        return gel(text)
    else:
        return render_template("tweets.html")


if __name__ == '__main__':
    app.run()
    #print(gel('furkankykc'))
