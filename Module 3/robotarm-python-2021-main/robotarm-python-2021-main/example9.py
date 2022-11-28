from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for y in range(10):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(4):
        robotArm.moveLeft()
    if y==1 or (y>=3 and y<5) or y>=6:
        print('ja')
        robotArm.moveLeft()
robotArm.wait()

    
         
