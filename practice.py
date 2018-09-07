import random

print 'Do you wanna roll dice homie G ?'
yes = True
answer = raw_input('yes or no: ')
if (answer == 'yes'):
    while(yes):
        print random.randint(1,6)
        print 'Do you wanna roll again  ?'
        answer = raw_input('yes or no: ')
        # print(answer)
        if (answer == 'yes'):
            yes = True
        else:
            yes = False
else:
    print 'leave me alone'

if(yes == False):
    print 'leave me alone'