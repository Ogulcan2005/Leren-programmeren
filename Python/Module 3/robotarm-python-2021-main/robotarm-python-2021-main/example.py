from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 1

# Jouw python instructies zet je vanaf hier:
for b in range(1,5):
    for f in range(b):
        robotArm.grab()
        for c in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for d in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
