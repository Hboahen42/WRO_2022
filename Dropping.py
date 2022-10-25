 #!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)
color_1 = Ev3devSensor(Port.S3)
color_2 = ColorSensor(Port.S2)
large_motor = Motor(Port.D)
drop_motor = Motor(Port.A)
robot = DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=170)   



def lift(rotation=160,angle=200):
    large_motor.run_angle(rotation,angle,then=Stop.BRAKE)
    
    
    
    
def mid_drop():

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(124)

    #lift drop bottle
    lift(300,-160)

    #move back to release bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-170)

    #lift remaining water
    lift(300,160)

    #turn go to out of room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(95)

    #move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(265)

    lift(300,20)

def right_drop():

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(26)

    #move back to drop bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(110)
    
    #lift drop bottle
    lift(300,-160)

    #move back to release bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-170)

    #lift remaining water
    lift(300,160)

    #turn go to out of room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(70)

    #move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(265)

    lift(300,20)

def left_drop():

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-26)

    #move back to drop bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(111)
    
    #lift drop bottle
    lift(300,-160)

    #move back to release bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-135)

    #lift remaining water
    lift(300,160)

    #turn go to out of room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(122)

    # move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(265)

    lift(300,20)

def drop_water_position(water_position):
    if water_position.lower() == 'left':
        left_drop()
        return False

    elif water_position.lower() == 'right':
        right_drop()
        return False
        
    elif water_position.lower() == 'mid':
        mid_drop()
        return False