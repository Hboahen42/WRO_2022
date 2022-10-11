#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)
color_1 = ColorSensor(Port.S3)
color_2 = ColorSensor(Port.S2)
large_motor = Motor(Port.D)
robot = DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=170)
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

def lift(rotation=160,angle=200):
    large_motor.run_angle(rotation,angle,then=Stop.BRAKE)


def inside_room():
    #pid
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(50)

    pid_line(0.5,200)

    # robot.stop()
    # robot.settings(900,900,0,0)
    # robot.straight(10)

    wait(300)


    #turn to room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-94)

    #move straight
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(250)

    output_color = color_1.color()
    #lundary id here
    if output_color is not None:
        led_indicator()

        turn_to_lundary()
        
        #lift first lundary
        lift(300,-250)
        lift(300,250)
    return(output_color)


def water():
    if inside_room() is None:
        turn_to_lundary()

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-20)

    #move back to drop bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(115)
    
    #lift drop bottle
    lift(300,-180)

    #move back to release bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-170)

    #lift remaining water
    lift(300,180)

    #turn go to out of room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(116.5)

    #move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(260)

    lift(300,20)

def game():
    if inside_room() is None:
        turn_to_lundary()
    
    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(65)

    #move to ball
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-123)


    #lift ball
    lift(350,-150)

    #move to drop in basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(70)

    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(95)

    #move to basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-130)

    #drop ball
    lift(350,100)

    #move away from basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(105)

    #move out of bottle
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-66)

    #out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(300)

    lift(350,50)


def turn_to_lundary(): 
    #move straight
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(50)

    #turn to bottle
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(93.5)

    #move back to pick bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-50)


def led_indicator():
    output_color = color_1.color()
    ev3.light.on(output_color)