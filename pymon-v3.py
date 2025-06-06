import random
import os
import time

# set the score to 1 and the level to 1 
level = 1
score = 1
# loop beings 
while True:

    # set the list to compare to the pattern we need to match
    p1 = []    

    # randomly generates a pattern with numbers 1 - 4, every round the length of the patter goes up by 1
    pattern = random.choices(range(1,5), k = level)
    print(pattern) #prints pattern you have to copy
    time.sleep(1) #ensures patter is only shown for 1 second
    os.system("cls" if os.name == 'nt' else 'clear') #clears screen 
    #game logic
    for i in pattern:
        play = int(input(":")) #after ever number press enter, do not write the full pattern then press enter
        p1.append(play) #adds our input of the patter to the list to be compared to
    # if we hit the correct pattern the level and score go up & game continues
    if p1 == pattern: 
        level += 1
        score = level
        continue
    #if were wrong we lose and we get told our score
    else: 
        print("You Lose!")
        print(f"Your score was {score}")
        #Game asks if we want to play again
        replay = input("Would you like to play again? (Y/N)").upper()
        #if not game quits if yes game loops back again
        if replay != "Y":
            break
        # when we select we want to play again the score is set back to level 1 score 1 and game continues
        else:
            level = 1
            score = 1