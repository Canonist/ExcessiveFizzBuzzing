import datetime
import time
'''

This script has been created by KriminaaliSM, under no copyright.
It is done for fun. You should edit it to do something fun.
It's not efficient or optimized, it is artistic.


'''
''' This block is needed, if tnow and tplex are required outside the timefuzzer
#tnow = datetime.datetime.now()

#tplex = tnow.hour*10000 + tnow.minute*100 + tnow.second
'''

#allow mode selection
mode = input(f'Select mode: 1) fuzzbizzer: \n '
             f'            2) timefuzzer:')

i = 1
#define incremental fuzzbizzer
def fuzzbizzer(i):
    if i % 3 == 0 and l % 5 == 0:
        print(f'Step {i} is fizzbuzzable')
        return(i)
    elif i % 3 == 0:
        print(f'Step {i} is fizzable')
        return(i)
    elif i % 5 == 0:
        print(f'Step {i} is buzzable')
        return(i)

#define clock-based timefuzzer
def timefuzzer():
    #find current time
    tnow = datetime.datetime.now()
    #print current time
    print(f'Time as it currently stands is {tnow.time()}')
    #"timeplexing" into an integer
    tplex = tnow.hour * 10000 + tnow.minute * 100 + tnow.second
    #test and comment on fizzbuzzability
    if tplex % 3 == 0 and tplex % 5 == 0:
        print(f'The current time is fizzbuzzing')
    elif tplex % 3 == 0:
        print(f'The current time is fizzing')
    elif tplex % 5 == 0:
        print(f'The current time is buzzing')
    else:
        print(f'The current time is not fizzbuzzable')

#if mode 1, fuzzbizzer is selected
if mode == "1" or mode == "fuzzbizzer":
    l = int(input("Enter your number for fuzzbizzing:"))
    while i < l:
        time.sleep(0.1)
        i += 1
        fuzzbizzer(i)
#check for mode 2, timefuzzing
elif mode == "2" or mode == "timefuzzer":
    while i > 0:
        time.sleep(1)
        i += 1
        timefuzzer()
