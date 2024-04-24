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

#Clear the terminal screen (just to make less typing for me)
def CL():
    os.system('cls')

#Get Difficulty from user
while(True):
    try:   
        Difficulty = int(input())
        CL()
        break
    except:
        pass




#Create the empty maze
def InitMazeStorage(MDataL, DifficultySetting):
    #Temporary matrix to add to the main marix later
    temp = []
    
    # Walls is an array that has entries 0 - 3 representing the walls. 0 is north, 1 is east, 2 is south, 3 is west
    # 4 states if it has been visited by the maze generation, 
    # 5 gives the type of the cell, (empty, exit, stairs, encounter[value 100-200])
    walls = []
    
    if DifficultySetting == 1:
        length = random.randint(10, 10)
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



def GenerateMaze(Maze, DiffucultySetting, len):

    #Choose a random pair of coordinates for maze to start its generation from.
    RandomStartNodex = random.randint(1, len - 2)
    RandomStartNodey = random.randint(1, len - 2)

    #Stack is the stack for implementing back tracking. it stores a list of maze nodes, x coordinate, and y coordinate
    Stack = []
    AllNotVisited = True
    Stack.append([tuple(Maze[RandomStartNodex][RandomStartNodey]), RandomStartNodex, RandomStartNodey])
    

    while(AllNotVisited):
        #get the current node off the top of the stack
        Current = Stack.pop()

        #Set node to visited
        print()
        print(Current[1]," : ", Current[2])
        print(Maze[Current[1]][Current[2]][4])
        Maze[Current[1]][Current[2]][4] = 0
        print(Maze[Current[1]][Current[2]][4])
        Available = 0
        
        #Index for the wall from the other side.
        ReverseWall = 0

        #Check frontier items if they are valid and have not been visited yet
        #check north
        north = CheckFontier(Maze, Current[1], Current[2] + 1, len)
        if north:
            Available = Available + 1
        #check east
        east = CheckFontier(Maze, Current[1] + 1 , Current[2], len)
        if east:
            Available = Available + 1
        #check south
        south = CheckFontier(Maze, Current[1], Current[2] - 1, len)
        if south:
            Available = Available + 1
        #check west
        west = CheckFontier(Maze, Current[1] - 1, Current[2], len)
        if west:
            Available = Available + 1
        #Choose a random direction to try to go in
        #If no available frontier, back track
        
        if Available == 0:
            
            if( not Stack):
                AllNotVisited = False
                break
        else:
            #Push current back onto the stack if it still has frontier next to it.
            Stack.append(Current)
            while(True):
                ChooseRandomDirection = random.randint(0, 3)
                #print("The stack is: ", Stack)
                match ChooseRandomDirection:
                    case 1:
                        if(north):
                            ReverseWall = 2
                            #Set the wall in the next node that is between this node and it to air (this prevents one way passages)
                            Maze[Current[1]][Current[2]+1][ReverseWall] = 0
                            Stack.append([Maze[Current[1]][Current[2]+1], Current[1], Current[2]+1])
                            break
                    case 2:
                        if(east):
                            ReverseWall = 3
                            #Set the wall in the next node that is between this node and it to air (this prevents one way passages)
                            Maze[Current[1]+1][Current[2]][ReverseWall] = 0
                            Stack.append([Maze[Current[1]+1][Current[2]], Current[1]+1, Current[2]])
                            break
                    case 3:
                        if(south):
                            ReverseWall = 0
                            #Set the wall in the next node that is between this node and it to air (this prevents one way passages)
                            Maze[Current[1]][Current[2]-1][ReverseWall] = 0
                            Stack.append([Maze[Current[1]][Current[2]-1], Current[1], Current[2]-1])
                            break
                    case 4:
                        if(west):
                            ReverseWall = 1
                            #print()
                            #print(Current[1])
                            #print(Current[2])
                            #Set the wall in the next node that is between this node and it to air (this prevents one way passages)
                            Maze[Current[1]-1][Current[2]][ReverseWall] = 0
                            Stack.append([Maze[Current[1]-1][Current[2]], Current[1]-1, Current[2]])
                            break
            #Set the wall in the chosen direction to air on the current node's side
            Maze[Current[1]][Current[2]][ChooseRandomDirection] = 0

            
            

       



        

    return Maze

#Check if the entry of the maze is a valid fontier item
def CheckFontier(Maze, coordx, coordy, len):
    try:
        M_obj = Maze[coordx][coordy]
        #if coordx == 0 or coordy == 0 or coordx == len-1 or coordy == len-1:
           # return False, 1
        #Check if node has been visited already
        if M_obj[4] != 1:
            return False#, 2
        return True#, 0
    except:
        return False#, 3


#########################################Call Methods and Run Game########################

MazeLayoutData, Length = InitMazeStorage(MazeLayoutData, Difficulty)
MazeLayoutData = GenerateMaze(MazeLayoutData, Difficulty, Length)
print(MazeLayoutData)
