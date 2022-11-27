from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 1

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for stapel in range(7):
        robotArm.grab()
        for blok in range(8):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(8):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()