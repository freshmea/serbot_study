from pop import LiDAR, Pilot
lidar = LiDAR.Rplidar()
bot = Pilot.SerBot()

lidar.connect()
lidar.startMotor()
bot.setSpeed(10)


while True:
    no_collisions = True
    vectos = lidar.getVectors()
    for v in vectos:
        degree = v[0]
        distance = v[1]
        print(v)
        if degree <= 60 or degree >= 300:
            if destance <= 500:
                no_collision = False
    if no_collisions:
        bot.setSpeed(10)
        bot.forward()
    else:
        bot.setSpeed(5)
        bot.turnLeft()
        