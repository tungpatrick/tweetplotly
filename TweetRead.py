from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

# credentials
with open('your_twitter_credentials.json', 'r') as f:
    credentials = json.load(f)

# create your own app to get consumer key and secret
CONSUMER_KEY = credentials['CONSUMER_KEY']
CONSUMER_SECRET = credentials['CONSUMER_SECRET']
ACCESS_TOKEN = credentials['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']


class CustomListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          tweet = json.loads(data)
          print(tweet["text"].encode("utf-8"))
          self.client_socket.send(tweet["text"].encode("utf-8"))
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

  api = Stream(auth, CustomListener(c_socket))
  api.filter(languages=["en"], track=["instagram", "facebook", "twitter"])

if __name__ == "__main__":
  s = socket.socket()
  host = "127.0.0.1"
  port = 9999
  s.bind((host, port))

  print("Listening on port:", port)

  s.listen(5)
  c, addr = s.accept()

  print("Received request from: "+str(addr))

  sendData(c)
