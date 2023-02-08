from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for x in range(7):
    robotArm.moveRight()
for y in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    # if y < 7:    
    #     robotArm.moveLeft()
    #     robotArm.moveLeft()

    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
