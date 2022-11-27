from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
for i in range(0,8):
    robotArm.moveRight()
for i in range(1,9):
    robotArm.grab()
    scan = robotArm.scan()
    if scan == "red":
        for c in range(0,i):
            robotArm.moveRight()
        robotArm.drop() 
        for c in range(0,i):
            robotArm.moveLeft()  
    else:
        robotArm.drop()
    robotArm.moveLeft()
robotArm.wait()
