import os
import random

MazeLayoutData = []
Length = 0

print("_________          _______    _______  _______  _______  _______ ")
print("\\__   __/|\\     /|(  ____ \\  (       )(  ___  )/ ___   )(  ____ \\")
print("   ) (   | )   ( || (    \\/  | () () || (   ) |\\/   )  || (    \\/")
print("   | |   | (___) || (__      | || || || (___) |    /   )| (__    ")
print("   | |   |  ___  ||  __)     | |(_)| ||  ___  |   /   / |  __)   ")
print("   | |   | (   ) || (        | |   | || (   ) |  /   /  | (      ")
print("   | |   | )   ( || (____/\\  | )   ( || )   ( | /   (_/\\| (____/\\")
print("   )_(   |/     \\|(_______/  |/     \\||/     \\|(_______/(_______/")
print()
print()


print("                   Select Difficulty")
print("             =============================")
print("                    1: easy")
print("                    2: medium")
print("                    3: hard")
print("                    4: Endless")


#Get Difficulty from user
while(True):
    try:   
        Difficulty = int(input())
        CL()
        break
    except:
        pass

#Clear the terminal screen (just to make less typing for me)
def CL():
    os.system('cls')


#Create the empty maze
def InitMazeStorage(MDataL, DifficultySetting):
    #Temporary matrix to add to the main marix later
    temp = []
    
    # Walls is an array that has entries 0 - 3 representing the walls. 0 is north, 1 is east, 2 is south, 3 is west
    # 4 states if it has been visited by the maze generation, 
    # 5 gives the type of the cell, (empty, exit, stairs, encounter[value 100-200])
    walls = []
    
    if DifficultySetting == 1:
        length = random.randint(20, 40)
    elif DifficultySetting == 2:
        length = random.randint(60, 120)
    elif DifficultySetting == 3:
        length = random.randint(200, 500)
    elif DifficultySetting == 4:
        length = random.randint(600, 1000)

    for i in range(7):
        walls.append(1)
    for i in range(length):
        temp.append(walls)
    for i in range(length):
        MDataL.append(temp)
    return MDataL, length



def GenerateMaze(DiffucultySetting, len):
    RandomStartNode = random.randint(1, len - 2)
    


    return



#########################################Call Methods and Run Game########################

MazeLayoutData, Length = InitMazeStorage(MazeLayoutData, Difficulty)
