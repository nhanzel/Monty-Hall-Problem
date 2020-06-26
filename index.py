import random
import time

#Monty Hall Problem Simulation
def game_show(s):
    #DOOR OBJECT
    #First parameter: if the door has a car
    #Second parameter: if that door is revealed
    #Third parameter: if we selected that door
    doors = [[False, False, False], [False, False, False], [False, False, False]]

    #get the door with the car and the contestant selection
    car_door = random.randint(0, 2)
    init_selection = random.randint(0, 2)
    doors[car_door][0] = True
    doors[init_selection][2] = True

    #reveal one of the other doors
    for i in range(len(doors)):
        if doors[i][0] == False and doors[i][2] == False:
            doors[i][1] = True
            break

    selection = init_selection
    #account for the switch
    if s:
        counter = 0
        for i in range(len(doors)):
            if doors[i][1] == False and doors[i][2] == False:
                doors[0][2] = False
                doors[1][2] = False
                doors[2][2] = False

                doors[i][2] = True

                selection = counter
                break
            counter += 1

    #USE THIS LINE TO MAKE THE NUMBER OF GAMES GO BY SLOWLY
    #(FOR DRAMATIC EFFECT)
    time.sleep(.00125)

    if car_door == selection:
        return True
    else:
        return False

num_games = 1000
wins = 0
losses = 0
#CASES WITH NO SWITCHING
print("NO SWITCHING\n")
for i in range(num_games):
    r = game_show(False)
    if r:
        wins += 1
    else:
        losses += 1
    print("Game " + str(i+1) + " of " + str(num_games), end="\r", flush=True)
print("\nWins: " + str(wins) + "    Losses: " + str(losses) + "\n\n\n")

#CASES WITH SWITCHING
wins = 0
losses = 0

print("SWITCHING\n")
for i in range(num_games):
    r = game_show(True)
    if r:
        wins += 1
    else:
        losses += 1
    print("Game " + str(i+1) + " of " + str(num_games), end="\r", flush=True)
print("\nWins: " + str(wins) + "    Losses: " + str(losses) + "\n\n\n")













