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




# print(lundary_color)

def basket_scanning():

    basket_lundary_color = {'BLACK':[0,3,11,12,13,14,15,16,17],'RED':[1,7,8,9,10],'YELLOW':[5,6]}
    
    wait(350)   
    basket_color_1 = color_1.read('COLOR')[0]


    # converting hitech color sensor
    for key,value in basket_lundary_color.items():
        if basket_color_1 in value:
            basket_color_1 = key
            break
    
    return basket_color_1




def lundary_sorting(basket_colors):
    basket_done = {'basket_1_done': False, 'basket_2_done': False, 'basket_3_done': False}    
    # for key,value in basket_done.items():
    #     if value == False:
    for x in range(4):
        for key,value in basket_colors.items():
            lundary_color = str(color_2.color()).split(".")[1]

            if str(value) == str(lundary_color):
                if key == 'basket_1':
                    basket_done['basket_1_done'] = move_to_basket_1()
                    break
                elif key == 'basket_2':
                    basket_done['basket_2_done'] = move_to_basket_2()
                    break
                elif key == 'basket_3':
                    basket_done['basket_3_done'] = move_to_basket_3()
                    break
                # elif (lundary_color is not RED) or (lundary_color is not YELLOW) or (lundary_color is not BLACK):
                #     robot.stop()
                #     drop_motor.run_angle(900,200)

                #     robot.stop()
                #     drop_motor.run_angle(-900,200)
                #     break

            wait(100)
        
        

def move_to_basket_3():

    # push lundary
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-40)

    robot.stop()
    drop_motor.run_angle(900,200)

    robot.stop()
    drop_motor.run_angle(-900,200)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(40)

    return True

def move_to_basket_2():

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(80)

    robot.stop()
    drop_motor.run_angle(900,200)

    robot.stop()
    drop_motor.run_angle(-900,200)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-80)

    return True

def move_to_basket_1():

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(195)

    robot.stop()
    drop_motor.run_angle(900,200)

    robot.stop()
    drop_motor.run_angle(-900,200)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-195)
    
    return True


