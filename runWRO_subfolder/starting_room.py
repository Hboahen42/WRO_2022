from runWRO_subfolder.variable_initiation import *
from runWRO_subfolder import lundary_sorting,dropping_water

def start_at_yellow_room():

    # #turn to rooms
    robot.stop()
    robot.settings(0,0,5000,5000)
    robot.turn(-34)
    # -460.5
    #go back
    robot.stop()
    robot.settings(5000,5000,0,0)
    robot.straight(-450.5)

    # #turn to room line
    robot.stop()
    robot.settings(0,0,5000,5000)
    robot.turn(123)
    
    #left sensor following
    ls_following(proportional_gain=0.7,drive_speed=100)
    # pid_line2(proportional_gain=0.9)

    #forward
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(20)

    #left sensor following
    ls_following(proportional_gain=0.7,drive_speed=100)
    # pid_line(proportional_gain=0.1,drive_speed=100)

def start_at_green_room():
    pass