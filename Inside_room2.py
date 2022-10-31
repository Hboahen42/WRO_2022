#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor
import Dropping
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
robot = DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=170)

def ls_following(proportional_gain = 1.4,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 30:

        # Calculate the deviation from the threshold.

        deviation = left_sensor.reflection() - 30

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

def rs_following(proportional_gain = 1.4,drive_speed = 600):
    while right_sensor.reflection() > 30:

        # Calculate the deviation from the threshold.

        deviation = 30 - right_sensor.reflection()

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.stop()
        right_motor.run(100)
    robot.stop()
    left_motor.brake()
    right_motor.brake()



def pid_line(proportional_gain = 1.4,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 20:

        # Calculate the deviation from the threshold.

        deviation = right_sensor.reflection() - left_sensor.reflection()

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

def inside_room2():

    # #turn to room
    # robot.stop()
    # robot.settings(0,0,900,900)
    # robot.turn(99)

    #move straight
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(280)

    turn_to_lundary()
        
    #lift first lundary
    lift(300,-280)
    lift(300,280)


def drop_water(water_position):
    inside_room2()
    return(Dropping.drop_water_position(water_position))


def game(turn=-65):
    inside_room2()
    
    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-71)

    #move to ball
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-128)


    #lift ball
    lift(350,-170)

    #move to drop in basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(70)

    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-95)

    #move to basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-147)

    #drop ball
    lift(350,110)

    #move away from basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(125)

    #move out of bottle
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(68)

    #out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(300)

    lift(350,50)

    ls_following(proportional_gain=0, drive_speed=100)
    rs_following(proportional_gain=0, drive_speed=100)

def lift(rotation=160,angle=200):
    large_motor.run_angle(rotation,angle,then=Stop.BRAKE)


def turn_to_lundary():

    #turn to bottle
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-95)

    #move back to pick bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-40 )


def led_indicator():
    output_color = color_2.color()
    ev3.light.on(output_color)