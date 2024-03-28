import os


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
        break
    except:
        pass

#Clear the terminal screen (just to make less typing for me)
def CL():
    os.system('cls')

