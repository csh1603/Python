from random import *

count = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[O] {0}th passenger (time: {1} minutes)".format(i, time))
        count+=1
    else:
        print("[ ] {0}th passenger (time: {1} minutes)".format(i, time))

print("Total passengers : {0}".format(count))