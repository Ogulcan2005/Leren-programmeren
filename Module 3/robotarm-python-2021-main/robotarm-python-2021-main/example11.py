from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:

tiles = 1
for right in range(1,10):
    robotArm.moveRight()
while tiles <= 10:
    robotArm.grab()
    robotArm.scan()   
    if robotArm.scan() == str("white"):
        robotArm.moveRight()
        robotArm.drop()
        for right in range(2):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
    tiles = tiles + 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()