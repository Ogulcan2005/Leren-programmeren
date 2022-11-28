from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
for i in range(9,0,-1):
    robotArm.grab()
    scan = robotArm.scan()
    if scan != "red":
        robotArm.drop() 
        robotArm.moveRight()
    else:
        for c in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(i-1):
            robotArm.moveLeft()
robotArm.wait()

