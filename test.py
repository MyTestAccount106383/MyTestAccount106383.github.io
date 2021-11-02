import time
timeOpen = 0

while True:
  f = open("test.txt","w")
  f.write(timeOpen)
  f.close()
  time.wait(5)
  timeOpen += 5
