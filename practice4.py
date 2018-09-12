from datetime import datetime
import time
   #random.randint(1,60)


odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]


while(True):
    right_this_minute = datetime.today()
    print(right_this_minute.strftime("%I:%M"))
    if right_this_minute.minute in odds:
        print("this minute seems a little odd.  ")
    else:
        print(" Not an odd minute. ")
    time.sleep(60)



#challenge complete