#!/usr/bin/env pybricks-micropython
from runWRO_subfolder.variable_initiation import *
from runWRO_subfolder import (lundary_sorting,dropping_water,starting_room,move_to_next_room)

# Write your program here.

# pick bottle

def say_color():
    output_color = str(color_1.color()).split(".")
    ev3.speaker.set_speech_options('en','f3',150,75)
    ev3.speaker.set_volume(100,which='PCM')
    ev3.speaker.say(str(output_color[1]))

def move_out_mid_drop(turn=97, straight=220):

    #turn go to out of room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(int(turn))

    #move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(int(straight))

    lift_down()

    ls_following(proportional_gain=0, drive_speed=100)
    rs_following(proportional_gain=0, drive_speed=100)

def move_out_right_drop(turn=70,straight=220):

    #turn go to out of room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(int(turn))

    #move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(straight)

    lift_down()

    ls_following(proportional_gain=0, drive_speed=100)
    rs_following(proportional_gain=0, drive_speed=100)

    

def move_out_left_drop(turn=122,straight=220):

    #turn go to out of room
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(int(turn))

    # move out of room
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(straight)

    lift_down()

    ls_following(proportional_gain=0, drive_speed=100)
    rs_following(proportional_gain=0, drive_speed=100)

def start_orientation(position=49):
    # # turn to bottle
    robot.stop()
    robot.settings(0,0,5000,5000)
    robot.turn(position)


def end_orientation(position=-50):
    # # turn to bottle
    robot.stop()
    robot.settings(0,0,5000,5000)
    robot.turn(position)

def move_to_water_bottle():
    # #move forward
    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(150)

    #pid
    pid_line(1.05,300)

    #move forward
    robot.settings(600,600,0,0)
    robot.straight(60)

    #lift bottle
    lift_down()



#Write your program here.



while True:
    if Button.CENTER in ev3.buttons.pressed():
        wait(500)

        
        start_position={'a':-46,'b':49,'c':144,'d':-141.5}
        start_orientation(start_position['a'])

        move_to_water_bottle()

        starting_room.start_at_yellow_room()

        drop_status = {'left': True, 'right': True, 'mid': True}

        # color = laundry_block_color_covertion()

        print(color)
        if (color == 'GREEN'):

            enter_room_a()
            turn_to_lundary()
            play_game_a()

        elif (color == 'WHITE'):
            enter_room_a()
            turn_to_lundary()
            for key,value in drop_status.items():
                if value == True:
                    drop_status[key] = dropping_water.drop_water_position(water_position=key)
                    if key == 'mid':
                        move_out_mid_drop(straight=215)
                    elif key == 'right':
                        move_out_right_drop()
                    elif key == 'left':
                        move_out_left_drop(straight=210)
                    break
        print(drop_status)

        move_to_next_room.move_to_blue_room()

        color = laundry_block_color_covertion()
        print(color)

        if (color == 'GREEN'):
            enter_room_b()
            turn_to_lundary(turn_value=-95,straight_value=-40)
            play_game_b(turn_to_ball=-71,turn_to_basket=-95,turn_out_of_room=68)

        elif (color == 'WHITE'):
            enter_room_b()
            turn_to_lundary(turn_value=-95,straight_value=-40)
            for key,value in drop_status.items():
                if value == True:
                    drop_status[key] = dropping_water.drop_water_position(water_position=key)
                    if key == 'mid':
                        move_out_mid_drop(turn=-97, straight=210 )
                    elif key == 'right':
                        move_out_right_drop(turn=-123)
                    elif key == 'left':
                        move_out_left_drop(turn=-71, straight=210)
                    break
        print(drop_status)  

        move_to_next_room.move_to_green_room()

        color = laundry_block_color_covertion()
        print(color)
        if (color == 'GREEN'):

            enter_room_a(straight_value=-2)
            turn_to_lundary()
            play_game_a(move_to_ball=-124,turn_out_of_room=-62)

        elif (color == 'WHITE'):
            enter_room_a()
            turn_to_lundary()
            for key,value in drop_status.items():
                if value == True:
                    drop_status[key] = dropping_water.drop_water_position(water_position=key)
                    if key == 'mid':
                        move_out_mid_drop()
                    elif key == 'right':
                        move_out_right_drop(straight=200)
                    elif key == 'left':
                        move_out_left_drop(straight=210)
                    break
        print(drop_status)

        move_to_next_room.move_to_red_room()

        color = laundry_block_color_covertion()
        print(color)

        if (color == 'GREEN'):
            enter_room_b(straight_value=-145)
            turn_to_lundary(turn_value=-95,straight_value=-50)
            play_game_b(turn_to_ball=-71,turn_to_basket=-95,turn_out_of_room=68)

        elif (color == 'WHITE'):
            enter_room_b(straight_value=-144)
            turn_to_lundary(turn_value=-95,straight_value=-50)
            for key,value in drop_status.items():
                if value == True:
                    drop_status[key] = dropping_water.drop_water_position(water_position=key)
                    if key == 'mid':
                        move_out_mid_drop(turn=-97)
                    elif key == 'right':
                        move_out_right_drop(turn=-121)
                    elif key == 'left':
                        move_out_left_drop(turn=-71, straight=200)
                    break
        print(drop_status)

        
        move_to_next_room.move_to_laundry_basket()

        push_laundry_blocks()
        
        lundary_sorting.backwards_basket_scanning()

        basket_colors = {'basket_1': None, 'basket_2': None, 'basket_3': None}
        print(basket_colors)

        basket_colors['basket_1'] = lundary_sorting.basket_scanning()
        basket_color_1 = basket_colors['basket_1']
        print(basket_color_1)

        lundary_sorting.laundry_check(basket_color_1)

        pid_line(proportional_gain=0.2,drive_speed=150)

        basket_colors['basket_2'] = lundary_sorting.basket_scanning()
        basket_color_1 = basket_colors['basket_2']
        print(basket_color_1)

        lundary_sorting.laundry_check(basket_color_1)
        
        basket_colors['basket_3'] = lundary_sorting.basket_scanning()  
        basket_color_1 = basket_colors['basket_3']
        print(basket_color_1)

        lundary_sorting.laundry_check(basket_color_1)                   

        robot.stop()
        robot.settings(900,900,0,0)
        robot.straight(-190)

        print(basket_colors)

        lundary_sorting.lundary_sorting(basket_colors)
        

        robot.stop()
        robot.settings(900,900,0,0)
        robot.straight(40)

        robot.stop()
        robot.settings(0,0,900,900)
        robot.turn(90)

        pid_distance(0.5,200,160)

        robot.stop()
        robot.settings(900,900,0,0)
        robot.straight(218)

        ending_position={'a':50,'b':-50,'c':-150,'d':140}
        end_orientation(ending_position['c'])
        print(drop_status)
        
        for key,value in drop_status.items():
            if value == True:

                robot.stop()
                robot.settings(900,900,0,0)
                robot.straight(100)

                lift_up()

                robot.stop()
                robot.settings(900,900,0,0)
                robot.straight(-100)

                lift_down()
                break



