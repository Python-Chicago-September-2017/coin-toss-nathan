import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(5001):
        coin = random.randint(0,1)
        if coin == 0:
            heads += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        else:
            tails += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

coin_toss()
        