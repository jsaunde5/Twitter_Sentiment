#Jordan Saunders          ***  EXTRA CREDIT  ***

#This program is intended to work on a timer from timer.py
#This program is a combination of twitterstream.py and
#tweet_sentiment with alterations to both files

#twitterstream.py was taken from Bill Howe at University of Washington and
# he used this assignment in the Coursera Data Science course.

import oauth2 as oauth
import urllib2 as urllib
import sys
import json
import datetime 

#createSent(sent_file)
#creates dict from sentiment file
#code taken from class site
def createSent(sent_file):
  scores = {} # initialize an empty dictionary
  for line in sent_file:
    term, score  = line.split("\t")  # The file is tab-delimited.
    scores[term] = int(score)  # Convert the score to an integer.

  return scores


#tweetParse(tweet_file, scores)
#takes in a file of tweets, reads the file tweet by tweet (from list)
# and compares it to the scores dictionary to count the sentiment
# of each tweet. Then adds the sentiment value of each tweet and finally
# gets the average of the 100 tweets sentiment score. Prints the
# current time and average sentiment score.
def tweetParse(tweetsArr, scores):
  count = 0  #only do 100 tweets
  avg = 0
  sent = 0  #add sentiment scores

  for tweet in tweetsArr:

    response = json.loads(tweet)  #create dict object

  #elements of actual tweets will have lang key
  #only read tweets of english language                     ONLY 100 TWEEETS
    if (response.get('lang') and response['lang'] == 'en' and count < 100): 
   
      tweet = response['text'].lower() #get value of tweet & convert lower
      tweetArr = tweet.split()  #create array of words in tweet

    #add sentiment count word by word in tweet
      for word in tweetArr:
        sent = sent + searchSent(word, scores)
      
      count = count + 1  #increment count by 1

  #we have 100 tweets -> calculate avg, time and print
    elif(count == 100):
      avg = str(sent/ float(100))
      time = str(datetime.datetime.now())
      print 'Time: ' + time + '   Average Sentiment: ' + avg
      return

  #not a valid line (either not a true tweet or not in english)
    else:
      pass


#searchSent(word, scores)
#searches for the word in sentiment dictionary
#if word is found -> return sentiment value
#if word is not found -> return zero
def searchSent(word, scores):
  if(scores.get(word)):
    return scores[word]

  else:
    return 0


#****************************************************************************
#most of the code below is copied from twitterstream.py
#from this point until main, I only altered fetchsamples()

#you may enter your own Twitter Developer credentials below in quotes.
#I took out my own credentials since uploading to GitHub.

creds = open('credentials.txt', 'r')

api_key = creds.readline().rstrip('\n')
api_secret = creds.readline().rstrip('\n')
access_token_key = creds.readline().rstrip('\n')
access_token_secret = creds.readline().rstrip('\n')

########

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

#use existing code from twitterstream.py with the following alterations
#  - create out list and append each line from stream to list
#  - only read 1200 tweets -> we will select valid tweets in tweetParse
#        valid tweets are ones that have tweet text and in English
#  - once we reach 1200 tweets, return out and break back to main
def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  count = 0
  out = []
  for line in response:
    if (count<1200):
      out.append(line.strip())
      count = count + 1
    else:
      return out
      break

#  ***  ***  ***  ***  ***  ***  ***  ***  ***  ***  ***  ***  
# fetch 1200 samples from the live stream
# hard-coded opening of the sentiment file
# creating scores dictionary from sentiment file
# send 1200 tweets and scores dictionary to tweetParse
def main():
  tweet_file = fetchsamples()
  sent_file = open('AFFIN-111.txt')

  scores = createSent(sent_file)
  tweetParse(tweet_file, scores)

if __name__ == '__main__':
  main()

