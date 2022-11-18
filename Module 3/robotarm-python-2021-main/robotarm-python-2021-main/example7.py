from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
robotArm.moveRight()

for stack in range(1,6):
    # move blok 1
    for block in range(1,7):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()

    # move to next stack
    robotArm.moveRight()
    robotArm.moveRight()
 
  


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()