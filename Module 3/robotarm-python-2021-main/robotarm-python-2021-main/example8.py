from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for stapel in range(7):
        robotArm.moveRight()
        robotArm.grab()
        for blok in range(8):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(9):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()