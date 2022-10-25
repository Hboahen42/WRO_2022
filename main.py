#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor
import Inside_room
import Inside_room2
import Inside_room3
import Inside_room4

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



# Write your program here.
def pid_line(proportional_gain = 1.05,drive_speed = 600):
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


def ls_following(proportional_gain = 1.4,drive_speed = 600):
    while left_sensor.reflection() + right_sensor.reflection() > 20:

        # Calculate the deviation from the threshold.

        deviation = left_sensor.reflection() - 30

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
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
# pick bottle

def say_color():
    output_color = str(color_1.color()).split(".")
    ev3.speaker.set_speech_options('en','f3',150,75)
    ev3.speaker.set_volume(100,which='PCM')
    ev3.speaker.say(str(output_color[1]))

def lift(rotation=160,angle=200):
    large_motor.run_angle(rotation,angle,then=Stop.BRAKE)








#Write your program here.

while True:
    if Button.CENTER in ev3.buttons.pressed():
        wait(500)

        # # turn to bottle
        # #  a = -46
        # #  b = 46
        # robot.stop()
        # robot.settings(0,0,5000,5000)
        # robot.turn(48)

        # # #move forward
        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(150)

        # #pid
        # pid_line(1.05,300)

        # #move forward
        # robot.settings(600,600,0,0)
        # robot.straight(60)

        # #lift bottle
        # lift(180,270)

        # # #turn to rooms
        # robot.stop()
        # robot.settings(0,0,5000,5000)
        # robot.turn(-34)

        # #go back
        # robot.stop()
        # robot.settings(5000,5000,0,0)
        # robot.straight(-460.5)

        # # #turn to room line
        # robot.stop()
        # robot.settings(0,0,5000,5000)
        # robot.turn(123)
        
        # #pid
        # pid_line2()

        # #forward
        # wait(50)

        # #pid
        # pid_line()


        # #insert room_id here
        
        
        drop = {'left': True, 'right': True, 'mid': False}
        color = color_1.read('COLOR')
        print(color)
        # if (color[0] in range(3,5)) or (color[0] == 13):

        #     # game()
        #     Inside_room.game()
        #     ev3.light.off()
        # else:
        #     for key,value in drop.items():
        #         print(key)
        #         if value == True:
        #             drop[key] = Inside_room.drop_water(water_position=key)
        #             break
        #     print(drop)
        #     ev3.light.off() 



        # # go back
        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(17)

        # robot.stop()
        # robot.settings(0,0,900,900)
        # robot.turn(94)

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(43.5)

        # robot.stop()
        # robot.settings(-900,-900,0,0)
        # robot.straight(-137)

        # #turn to room*
        # robot.stop()
        # robot.settings(0,0,900,900)
        # robot.turn(-97)

        if (color[0] in range(3,5)) or (color[0] == 13):

            # game()
            Inside_room2.game()
            ev3.light.off()
        else:
            for key,value in drop.items():
                print(key)
                if value == True:
                    drop[key] = Inside_room2.drop_water(water_position=key)
                    break
            print(drop)
            ev3.light.off() 


        # go back
        robot.stop()
        robot.settings(900,900,0,0)
        robot.straight(55)

        robot.stop()
        robot.settings(0,0,900,900)
        robot.turn(-90)

        pid_distance(0.7,800,550)

        # cross to room
        robot.stop()
        robot.settings(900,900,0,0)
        robot.straight(400)


        robot.stop()
        right_motor.run_angle(500,220)

        robot.stop()
        left_motor.run_angle(500,220)

        ls_following(0.5,200)

        robot.stop()
        left_motor.run_angle(500,200)

        robot.stop()
        right_motor.run_angle(500,200)



        pid_line()
        wait(50)

        if (color[0] in range(3,5)) or (color[0] == 13):

            # game()
            Inside_room3.game()
            ev3.light.off()
        else:
            for key,value in drop.items():
                print(key)
                if value == True:
                    drop[key] = Inside_room3.drop_water(water_position=key)
                    break
            print(drop)
            ev3.light.off() 

        # go back
        robot.stop()
        robot.settings(900,900,0,0)
        robot.straight(50)

        robot.stop()
        robot.settings(0,0,900,900)
        robot.turn(-90)

        pid_line(0.8,200)

        if color_2.color() == Color.GREEN:
            Inside_room.led_indicator()
            # water()
            # Inside_room4.water()
            for key,value in drop.items() :
                if value == True:
                    drop[key] = Inside_room4.water(drop)
                    break
                
            ev3.light.off()
        else:
            Inside_room.led_indicator()
            # game()
            Inside_room4.game()
            ev3.light.off()

            
        # # go back
        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(55)

        # robot.stop()
        # robot.settings(0,0,900,900)
        # robot.turn(-90)

        # pid_distance(1.4,800,470)


        # robot.settings(0,0,900,900)
        # robot.turn(35)

        # # straight to lundary
        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(433)

        # robot.stop()
        # robot.settings(0,0,900,900)
        # robot.turn(70)

        # pid_line(1,300)

        # # push lundary
        # robot.stop()
        # robot.settings(700,700,0,0)
        # robot.straight(130)

        # # push lundary
        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(-90)

        # robot.stop()
        # robot.settings(0,0,900,900)
        # robot.turn(93.5)

        # pid_distance(1.05,200,60)

        # robot.stop()
        # left_motor.run_angle(500,40)


        # print(color_1.color())

        # wait (300)

        # robot.stop()
        # robot.settings(700,700,0,0)
        # robot.straight(-110)

        # print(color_1.color())

        # wait (300)

        # robot.stop()
        # robot.settings(700,700,0,0)
        # robot.straight(-110)

        # print(color_1.color())

        # wait (300)

        # pid_line(0.6,300)

        # # if basket 1

        # # push lundary
        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(-40)

        # robot.stop()
        # drop_motor.run_angle(900,200)
    
        # robot.stop()
        # drop_motor.run_angle(-900,200)

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(40)



        # # if basket 2

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(80)

        # robot.stop()
        # drop_motor.run_angle(900,200)
    
        # robot.stop()
        # drop_motor.run_angle(-900,200)

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(-80)

        # # if basket 3

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(180)

        # robot.stop()
        # drop_motor.run_angle(900,200)
    
        # robot.stop()
        # drop_motor.run_angle(-900,200)

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(-180)

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(40)

        # robot.stop()
        # robot.settings(0,0,900,900)
        # robot.turn(90)

        # pid_distance(1.5,200,160)

        # robot.stop()
        # robot.settings(900,900,0,0)
        # robot.straight(215)


        # # a = 50
        # # b = -50
        # # c = -150
        # # d = 140
        # robot.stop()
        # robot.settings(0,0,900,900)
        # robot.turn(140)
