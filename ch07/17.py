# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

count_win = 0
count_draw = 0
count_total = 0.0
first = True

while True:
    print("\nGame start")
    result = play_once(first)
    if result == -1:
        print("You win!")
        count_win += 1
    elif result == 0:
        print("Game drawn!")
        count_draw += 1
    elif result == 1:
        print("I win!")
    first = not first
    count_total += 1.0
    print("\nSCORES:\nWins: {0}\tDraws: {1}\n".format(count_win, count_draw))
    print("Win percentage: {0:.2f}%\n".format(count_win*100/count_total))
    stay = input("Do you want to play again? (y/n)\n")
    while not (stay == "y" or stay == "n"):
        stay = input("Invalid input. Do you want to play again? (y/n)\n")
    if stay == "n":
        break

print("Goodbye")
