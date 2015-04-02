#                ******   EXTRA CREDIT  ******

#Jordan Saunders

#This program is a timer to execute scrpit3.py every 5 minutes
#to execute the program, type the following command
#  $ timer.py


import time, stream3


while True:
  stream3.main()
  time.sleep(280)


#280 seconds is used, since the program takes about 20 seconds
#to run. This should give data intervals very close to 5 minutes
