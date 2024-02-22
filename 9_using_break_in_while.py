# here is the example to understand breaks in while loop
# we will consider a game logic
# enemy will attack on player and his hp will be decreased

import random

playerhp = 260              # player hp
enmyhph = 80                # enemy high power
enmyhpl = 60                # enemy low power

while playerhp > 0:
    dmg = random.randrange(enmyhpl, enmyhph)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
        print("Enemy strikes for ", dmg, "points of damage. Your current hp is", playerhp )

    if playerhp == 30:
        print("You have low health. Your are teleported to nearest inn.")
        break

# if we don't use break here it will continue infinite
