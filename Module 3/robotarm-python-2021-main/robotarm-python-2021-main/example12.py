from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

tiles = 9
while tiles > 0:
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == str("red"):
        for x in range(tiles):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(tiles):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    tiles = tiles - 1
    robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
