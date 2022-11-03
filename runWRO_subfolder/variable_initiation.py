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
color_1 = ColorSensor(Port.S3)
color_2 = ColorSensor(Port.S2)
large_motor = Motor(Port.D)
drop_motor = Motor(Port.A)
robot = DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=170)

def pid_line(proportional_gain = 1.05,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 20:

        # Calculate the deviation from the threshold.

        deviation = right_sensor.reflection() - left_sensor.reflection()

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()
    left_motor.stop()
    right_motor.stop()


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

def ls_following2(proportional_gain = 1.4,drive_speed = 600):
    while (right_sensor.color() is not Color.BLACK):

        # Calculate the deviation from the threshold.

        deviation = left_sensor.reflection() - 30

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

def rs_following2(proportional_gain = 1.4,drive_speed = 600):
    while right_sensor.reflection() > 20:

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

    

def pid_distance(proportional_gain = 1.4,drive_speed = 600, distance = 20):
    robot.reset()
    while robot.distance() <= distance:

        # Calculate the deviation from the threshold.

        deviation = right_sensor.reflection() - left_sensor.reflection()

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()


def pid_line2(proportional_gain = 1.05,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 20:

        # Calculate the deviation from the threshold.

        deviation = right_sensor.reflection() - left_sensor.reflection()

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)

def lift(rotation=160,angle=200):
    large_motor.run_angle(rotation,angle,then=Stop.BRAKE)

def lift_up():
    large_motor.run_until_stalled(speed=-500,then=Stop.BRAKE,duty_limit=30)

def lift_down():
    large_motor.run_until_stalled(speed=500,then=Stop.BRAKE,duty_limit=30)

def enter_room_a(straight_value=7,turn_value=-94):
    #pid
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(50)

    pid_line(0.1,200)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(straight_value)

    wait(300)


    #turn to room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(turn_value)

    #move straight
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(300)

def enter_room_b(straight_value=-142):
    robot.stop()
    robot.settings(-900,-900,0,0)
    robot.straight(straight_value)

    #turn to room*
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-94)

    #move straight
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(280)

def turn_to_lundary(turn_value=94.5,straight_value=-50):

    #turn to bottle
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(turn_value)

    #move back to pick bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(straight_value)

    #lift first lundary
    lift_up()
    lift_down()

def play_game_a(move_to_ball=-122.5,turn_to_basket=95,turn_out_of_room=-65):

    
    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(67)

    #move to ball
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(move_to_ball)


    #lift ball
    lift(500,-170)

    #move away from ball
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(60)

    #turn to basket
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(turn_to_basket)

    #move to basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-145)

    #drop ball
    lift(500,110)

    #move away from basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(128)

    #turn outside the room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(turn_out_of_room)

    #move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(250)

    lift_down()

    ls_following(proportional_gain=0, drive_speed=100)
    rs_following(proportional_gain=0, drive_speed=100)

def play_game_b(turn_to_ball=-65, move_to_ball=-126,turn_to_basket=-97,turn_out_of_room=68):
    inside_room2()
    
    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(turn_to_ball)

    #move to ball
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(move_to_ball)


    #lift ball
    lift(350,-170)

    #move to drop in basket
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(70)

    #turn to ball
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(turn_to_basket)

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
    robot.turn(turn_out_of_room)

    #out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(250)

    
    lift_down()

    ls_following(proportional_gain=0, drive_speed=100)
    rs_following(proportional_gain=0, drive_speed=100)


def push_laundry_blocks():
    pid_line(1,300)

    # push lundary
    robot.stop()
    robot.settings(700,700,0,0)
    robot.straight(130)

    # push lundary
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-80)

