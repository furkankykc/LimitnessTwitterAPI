import types
import warnings
from twitterRest import TwitterClient
import os

import googletrans
import tweepy
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table, log
import uuid
import Myauth

from entities import tweets, dataset

# OAuth process, using the keys and tokens

# Creation of the actual interface, using authentication

apiL= []
api = None



class limitnessTwitter():


    def __init__(self,accList=[]):

        self.cluster = None
        self.connectCluster()
        self.api = None
        self.apiL = []
        self.login(accList)
        self.currMachine = 0


    def connectCluster(self):
        cluster = Cluster()
        session = cluster.connect('k1')
        connection.setup(['127.0.0.1'], 'k1')
        sync_table(tweets)

    def login(self,accList):
        loginedAcc = "Login successful for :\n"
        try:
            for acc in accList:
                self.apiL.append([TwitterClient(auth=acc),0])
                loginedAcc+="\t"+acc.get_username()+"\n"
            self.api = self.apiL[0][0]
            return loginedAcc
        except Exception:
            raise Exception("Error when login acc")




    def makinaSec(self):
        self.apiL[self.currMachine % (len(apiL) + 1)][1]=1
        self.currMachine+=1
        if(self.apiL[self.currMachine % (len(apiL) + 1)][1]==0):
            self.api = self.apiL[self.currMachine%(len(apiL)+1)][0]
        else:
            print('TÜM MAKİNALAR LİMİTE ULAŞTI')
            raise tweepy.TweepError("AZ BEKLE")

        print("Makina değiştrildi")



    def makina(self,username, page_id, count=90):
        try:
            stuff = api.getTweetsFrom(username, count=count, page=page_id)
        except tweepy.RateLimitError:
            self.makinaSec()
        dataset.create(id=uuid.uuid1(),creator_id=api.auth.username,description=username+"|"+str(len(stuff))+"*"+str(page_id))
        [tweets.create(id=str(status.id),text=status.text,author_id=status.author.screen_name,date=status.created_at) for status in stuff]


    def tweetGetir(self,username='furkankykc', count=200, cpt=90):
        max_page = int(count / cpt) + 1
        c = count
        for i in range(1, max_page):
            self.makina(username,i, i, cpt)
            c -= cpt



    def getProfile(self,who,cpt=20):
        l = []
        count = self.api.getUserTweetCount(who)
        if(count!=0 and count<cpt):
            pageCount=1
        elif(count>cpt):
            pageCount= round(count/cpt)+1
        c = count
        for i in range(pageCount):
            try:
                l.append(self.api.getTweetsFrom(who, count=cpt,page=i))
            except tweepy.RateLimitError:
                self.makinaSec()
            c -= cpt
            print(c)
        return l

    def getHashtag(self,who,cpt=90):
        l = []
        count = self.api.getUserTweetCount(who)
        if(count!=0 and count<cpt):
            pageCount=1
        elif(count>cpt):
            pageCount= round(count/cpt)+1
        c = count
        for i in range(pageCount):
            self.makinaSec()
            l.append(self.api.getTweetsFromHashtag(who, count=cpt,page=i))
            c -= cpt
            print(c)
        return l
