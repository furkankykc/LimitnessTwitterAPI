import uuid

from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

import Myauth
from entities import tweets,dataset
from twitterRest import TwitterClient
from twitterRest import *
import twitterimpl

# def getir(user = "furkankykc"):
#     api = TwitterClient(auth=Myauth.fake())
#     print (api.getUsername())
#     return api.getProfile(user)
#
# def getirProfil(user = "furkankykc"):
#     return twitterimpl.profilGetir(user)
#cluster = Cluster()
#session = cluster.connect('k1')
#connection.setup(['127.0.0.1'],'k1')
#sync_table(tweets)
#def queryTweet(tweet):
 #   stmt = session.prepare("INSERT INTO tweets (id, text, author_id,date)VALUES (?, ?, ?,?) IF NOT EXISTS")

  #  [session.execute(stmt, [uuid.uuid1(),status.text,status.author.screen_name,status.created_at])for status in tweets]

#tweets.create(id=uuid.uuid1(),text="deneme",author_id='author.screen_name')

