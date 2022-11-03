from runWRO_subfolder.variable_initiation import *

def move_to_blue_room():
    # # go back
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(70)

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(94.5)

    ls_following(proportional_gain=0.7,drive_speed=100)
    wait(50)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(7)

def move_to_green_room():
    # go back
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(45)

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-90)

    

    pid_line(proportional_gain= 0.6, drive_speed=200)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(45)

    pid_line(proportional_gain= 0.1, drive_speed=200)

    robot.stop()
    right_motor.run_angle(500,270)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(45)

    robot.stop()
    left_motor.run_angle(500,274.8)


    ls_following(proportional_gain=0, drive_speed=500)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(35)

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(90)

    pid_line(proportional_gain= 0.6, drive_speed=200)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(45)

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-90)

    pid_line(proportional_gain= 0.1, drive_speed=200)                           

def move_to_red_room():
    # go back
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(70)

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(94.5)

    ls_following(proportional_gain=1,drive_speed=100)
    wait(50)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(7)

def move_to_laundry_basket():
    # go back
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(49)

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-96)

    pid_distance(0.25,800,470)


    robot.settings(0,0,900,900)
    robot.turn(38)

    ls_following(proportional_gain=0, drive_speed=300)

    # straight to lundary
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(15)

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(60)
