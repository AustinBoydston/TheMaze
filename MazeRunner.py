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
    
    if DifficultySetting == 1:
        length = random.randint(20, 40)
    elif DifficultySetting == 2:
        length = random.randint(60, 120)
    elif DifficultySetting == 3:
        length = random.randint(200, 500)
    elif DifficultySetting == 4:
        length = random.randint(600, 1000)

    for i in range(length):
        temp.append(0)
    for i in range(length):
        MDataL.append(temp)
    return MDataL, length



def GenerateMaze(DiffucultySetting):
    return



#########################################Call Methods and Run Game########################

MazeLayoutData, Length = InitMazeStorage(MazeLayoutData, Difficulty)




