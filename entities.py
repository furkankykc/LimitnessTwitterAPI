import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table

class user(Model):
    id = columns.UUID(primary_key=True)
    username = columns.Text()
    password = columns.Text()
    twitter_api_token = columns.Text()
    twitter_api_token_secret = columns.Text()
    limit = columns.Integer()
    reset_time =columns.Date()


class dataset(Model):
    id = columns.UUID(primary_key=True)
    creator_id = columns.Text(primary_key=True)
    description = columns.Text()

class tweets(Model):
    __keyspace__='k1'
    id = columns.Text(primary_key=True)
    author_id = columns.Text(primary_key=True)
    text = columns.Text()
    date = columns.Date()

