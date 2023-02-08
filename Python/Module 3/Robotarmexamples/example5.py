from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1
for x in range(7):
    robotArm.moveRight()
for x in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
