from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1, 21)
users = list(users)

shuffle(users)
winners = sample(users, 4)
print("-- announcement of the winners --\n")
print("Chicken Winner: {0}".format(winners[0]))
print("\nCoffee Winner: {0}".format(winners[1:]))
print("\n-- Congratulation --")
