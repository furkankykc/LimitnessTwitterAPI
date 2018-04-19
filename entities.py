import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table

class user(Model):
    __keyspace__ = 'k1'
    username = columns.Text(primary_key=True)
    password = columns.Text()
    twitter_api_token = columns.Text()
    twitter_api_token_secret = columns.Text()
    reset_time =columns.Date()

class userapp(Model):
    __keyspace__ = 'k1'
    author_id = columns.Text(primary_key=True)
    apptoken = columns.Text()
    appsecret = columns.Text()

class dataset(Model):
    __keyspace__ = 'k1'
    creator_id = columns.Text(primary_key=True)
    description = columns.Text()

class tweets(Model):
    __keyspace__='k1'
    id = columns.Text(primary_key=True)
    author_id = columns.Text(primary_key=True)
    text = columns.Text()
    date = columns.Date()

