#Jordan Saunders    E00202285
#Big Data
#March 9 2015

#This program takes in a .json file from Twitter consisting of a stream
#of tweets and a sentiment library (tab delimited). The program creates 
#a Python dictionary from the sentiment library and uses it to calculate
#the sentiment of each tweet in the .json file. We then print the 
#sentiment value of each tweet, line by line.

#I attached a sample output that was created from the twitter stream 
# named output.txt


import sys
import json

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
#takes in a file of tweets, reads the file line by line
# and compares it to the scores dictionary to count the sentiment
# of each tweet. Then prints the sentiment value of each tweet
def tweetParse(tweet_file, scores):

 #iterate through file line by line
  for line in tweet_file: 

    sent = 0  #initialize sentiment count for tweet
    response = json.loads(line)  #create dict object

  #lines of actual tweets will have lang key
  #only read tweets of english language
    if (response.get('lang') and response['lang'] == 'en' ): 
   
      tweet = response['text'].lower() #get value of tweet & convert lower
      tweetArr = tweet.split()  #create array of words in tweet

    #add sentiment count word by word in tweet
      for word in tweetArr:
        sent = sent + searchSent(word, scores)
      
      print sent  #print the sentiment value for tweet

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

########################################

def main():
  #open each file
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

  #create dict of sentiment and sent to tweetParse
    scores = createSent(sent_file)
    tweetParse(tweet_file, scores)

if __name__ == '__main__':
    main()

