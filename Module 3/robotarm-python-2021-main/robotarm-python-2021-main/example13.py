from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

tiles = 1
infiniteloop = 1
while infiniteloop == 1:
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == str(""):
        break
    else:
        for x in range(tiles):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(tiles):
            robotArm.moveLeft()
        tiles = tiles + 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()