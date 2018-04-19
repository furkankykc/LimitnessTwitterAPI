import tweepy

import db


def getAuth(user,username='furkankykc'):
    app = db.getApp(username)
    auth = tweepy.OAuthHandler(app.appToken, app.appSecret)
    auth.set_access_token(user.twitter_api_token, user.twitter_api_token_secret)
    return auth