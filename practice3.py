import random
Urabum = random.randint(1,100)
print 'Guess a number between 1 and 100! :'
#print (Urabum)
yes = True

while(yes):
    answer = raw_input('enter a number: ')
    answer = int(answer)
    if answer > Urabum:
        print'your answer is to high'
    elif answer < Urabum:
        print' Sorry your guess is to low'
    else:
        print' Correct that is  the right number!'
        break
    print'Would you like to guess again?'
    answer = raw_input()
    if (answer == "yes"):
        continue
    else:
        print 'later bye!'
        break






   # print'Thats exactly my number too'

#else:
    #print'sorry the numbers do not match '

#if(response == 'yes' ):
 #if(Urabum != answer):
   # print 'Would you like to guess again?'
