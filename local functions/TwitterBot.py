import tweepy
from CreateMergedImage import create
import os
import sys
consumer_key = "4bWloDC6KEkiQ0InIcZh1x9db"
consumer_secret = "BWhQObA39V3U3S3wa9jlchUaMZFzVYDL2RjgdoW5KekaAitPo6"
access_token = "1368648177478299650-2gRaRznc8Qz9l1vRDrHGH9lxnw5zPL"
access_token_secret = "B3AhDcxrvRRZ9RURPhNvZsgXOTjgQZJS9wiGArLmeYL3s"

# resource used ttps://realpython.com/twitter-bot-python-tweepy/
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


def execute(color1, color2, color3, color4, color5, color6, text):
    oauth = OAuth()
    api = tweepy.API(oauth)
    create(color1, color2, color3, color4, color5, color6)
    media = api.media_upload(resource_path('myImageColor.png'))
    tweet = text
    api.update_status(status=tweet, media_ids=[media.media_id])

def executefavorites(img, text):
    oauth = OAuth()
    api = tweepy.API(oauth)
    media = api.media_upload(img)
    tweet = text
    api.update_status(status=tweet, media_ids=[media.media_id])


def resource_path( relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)