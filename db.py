from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from entities import *

def connectCluster():
    cluster = Cluster()
    session = cluster.connect('k1')
    connection.setup(['127.0.0.1'], 'k1')
    sync_table(user)

connectCluster()



def createUser(username,password,api_token,api_secret):
    user.create(username =username,password=password,twitter_api_token=api_token,twitter_api_token_secret=api_secret)
    print (user)

def getUser(username):
    return user.objects().filter(username=username).first()

def getApp(author):
    return userapp.objects().filter(author_id=author).first()

def createApp(author,token,secret):
    userapp.create(author_id =author,apptoken=token,appsecret=secret)
    print (userapp)

def getUsers():
    return user.objects().all()
def login(username,password):
    user = getUser(username)
    if password == user.password:
        return True
    else:
        return False



print(login('furkankykc','1234'))