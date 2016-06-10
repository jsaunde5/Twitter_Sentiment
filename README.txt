Jordan Saunders
Twitter Sentiment
Big Data
March 9 2015

                           ********    README    ********
						   
						   
This Project was taken from Bill Howe from University of Washington and was
assigned in our Big Data Class at Eastern University taught by William Sverdlik.


*** Problem 1 ***

Open problem_1_submission.txt




*** Problem 2 ***

To run the program use the following command (.py):
$ python tweet_sentiment.py AFINN-111.txt output.txt

The first argument should be the sentiment file
The second argument should be output from twitterstream.py
	The program handles all lines from the twitterstream.
		If the line is not a true tweet, it will pass that line
		If the line is not in English, it will pass that line
		Also works on output.json 
		
		
		
		
*** Problem 3 (extra credit) ***

YOU NEED YOUR OWN TWITTER DEVELOPER CREDENTIALS TO RUN THIS
PROGRAM. I TOOK MY CREDENTIALS OUT OF SCRIPT3.PY FOR
CONFIDENTIALITY WHEN PUSHED TO GITHUB	

To run the program use the following command:
$ python timer.py

timer.py then calls script3.py and sleeps for 300 seconds
then calls script3.py again... will repeat until manually
stopped (ctrl + c). I have made slight alterations from
twitterstream.py and tweet_sentiment.py to make this work.

NOTE: No need to put any parameters; I hard-coded AFINN-111.txt
into script3.py and the program then gets a stream and executes
the proper functions to calculate the average sentiment of 100 tweets
in English ONLY. 

