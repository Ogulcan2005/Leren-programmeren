from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.moveRight()
robotArm.moveRight()
for x in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
