'''
import time
timeOpen = 0

while True:
  f = open("test.txt","w")
  f.write(str(timeOpen))
  f.close()
  time.sleep(5)
  timeOpen += 5
'''
import time
import datetime
today = datetime.datetime.now()
data = now.strftime("%Y-%m-%d %H:%M:%S")
f = open("test.txt","w")
#f.write(str(time.time()))
f.write(data)
f.close()
