#!/usr/bin/env pybricks-micropython
from runWRO_subfolder.variable_initiation import *
from runWRO_subfolder import lundary_sorting,dropping_water,starting_room
    
    
    
    
def mid_drop():

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(124)

    #lift drop bottle
    lift(300,-170)

    #move back to release bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-105)

    #lift remaining water
    lift(300,170)


def right_drop():

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(26)

    #move back to drop bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(98)
    
    #lift drop bottle
    lift(300,-170)

    #move back to release bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-105)

    #lift remaining water
    lift(300,170)



def left_drop():

    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(-26)

    #move back to drop bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(98)
    
    #lift drop bottle
    lift(300,-170)

    #move back to release bottle
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-105)

    #lift remaining water
    lift(300,170)



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