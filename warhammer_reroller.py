import random
def roll(dice, DC, mod, rr):
    rolls = []
    success = 0
    for die in range(dice):
        dice_roll = random.randint(1,5) + mod
        if dice_roll >=1 :
            rolls.append(dice_roll)
    for result in rolls:
        if result >= DC:
            success += 1
        elif result >= rr and result < DC:
            re_roll = random.randint(1,5) + mod
        if result >= DC:
            success += 1  
    if success == 1:
        print ("you rolled {} success".format(success))
    else:
        print ("you rolled {} successes".format(success))

roll (10, 5, 0, 3)