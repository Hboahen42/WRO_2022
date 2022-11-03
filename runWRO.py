#!/usr/bin/env pybricks-micropython
from runWRO_subfolder.variable_initiation import *
from runWRO_subfolder import inside_room1,inside_room2,inside_room3,inside_room4,lundary_sorting,dropping_water,starting_room

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
    lift_up()



#Write your program here.



while True:
    if Button.CENTER in ev3.buttons.pressed():
        wait(500)

        
        start_position={'a':-46,'b':49,'c':149,'d':-141}
        start_orientation(start_position['a'])

        move_to_water_bottle()

        starting_room.start_at_yellow_room()

        drop_status = {'left': True, 'right': True, 'mid': True}
        color = str(color_1.color()).split(".")[1]
        print(color)
        if (color == 'GREEN'):

            enter_room_a()
            turn_to_lundary()
            play_game()

        elif (color == 'WHITE'):
            enter_room_a()
            turn_to_lundary()
            for key,value in drop_status.items():
                print(key)
                if value == True:
                    drop_status[key] = dropping_water.drop_water_position(water_position=key)
                    if key == 'mid':
                        move_out_mid_drop(straight=215)
                    elif key == 'right':
                        move_out_right_drop()
                    elif key == 'left':
                        move_out_left_drop(straight=210)
                    break
                
                    
        # #     print(drop)
        # #     ev3.light.off()
 
        



        # # # # go back
        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(70)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(94.5)

        # # ls_following(proportional_gain=0.7,drive_speed=100)
        # # wait(50)

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(7)

        # # color2 = color_1.read('COLOR')
        # # print(color2)

        # # robot.stop()
        # # robot.settings(-900,-900,0,0)
        # # robot.straight(-142)

        # # #turn to room*
        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(-94)

        # # if (color2[0] in range(0,5)) or (color2[0] in range(11,14)):

        # #     # game()
        # #     Inside_room2.game()
        # #     ev3.light.off()
        # # elif (color2[0] in range (14,19)):
            
        # #     for key,value in drop.items():
        # #         print(key)
        # #         if value == True:
        # #             drop[key] = inside_room2.drop_water(water_position=key)
        # #             if key == 'mid':
        # #                 move_out_mid_drop(turn=-97, straight=210 )
        # #             elif key == 'right':
        # #                 move_out_right_drop(turn=-123)
        # #             elif key == 'left':
        # #                 move_out_left_drop(turn=-71, straight=210)
        # #             break
                    
        # #     print(drop)
        # #     ev3.light.off()

        # # # 55
        # # # go back
        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(45)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(-90)

        

        # # pid_line(proportional_gain= 0.6, drive_speed=200)

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(45)

        # # pid_line(proportional_gain= 0.1, drive_speed=200)

        # # robot.stop()
        # # right_motor.run_angle(500,270)

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(45)

        # # robot.stop()
        # # left_motor.run_angle(500,274.8)


        # # ls_following(proportional_gain=0, drive_speed=500)

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(35)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(90)

        # # pid_line(proportional_gain= 0.6, drive_speed=200)

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(45)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(-90)

        # # pid_line(proportional_gain= 0.1, drive_speed=200)

        

        # # color = color_1.read('COLOR')
        # # print(color)
        # # if (color[0] in range(0,5)) or (color[0] in range(11,14)):

        # #     # game()
        # #     Inside_room3.game()
        # #     ev3.light.off()
        # # elif (color[0]in range (14,19)):
        # #     for key,value in drop.items():
        # #         print(key)
        # #         if value == True:
        # #             drop[key] = inside_room3.drop_water(water_position=key)
        # #             if key == 'mid':
        # #                 move_out_mid_drop()
        # #             elif key == 'right':
        # #                 move_out_right_drop(straight=200)
        # #             elif key == 'left':
        # #                 move_out_left_drop(straight=210)
        # #             break
                    
        # #     print(drop)
        # #     ev3.light.off()

        # #  # go back
        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(70)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(94.5)

        # # ls_following(proportional_gain=1,drive_speed=100)
        # # wait(50)

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(7)

        # # color2 = color_1.read('COLOR')
        # # print(color2)

        # # robot.stop()
        # # robot.settings(-900,-900,0,0)
        # # robot.straight(-144)

        # # #turn to room*
        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(-94)

        # # if (color2[0] in range(0,5)) or (color2[0] in range(11,14)):

        # #     # game()
        # #     Inside_room4.game()
        # #     ev3.light.off()
        # # elif (color2[0] in range (14,19)):
            
        # #     for key,value in drop.items():
        # #         print(key)
        # #         if value == True:
        # #             drop[key] = inside_room4.drop_water(water_position=key)
        # #             if key == 'mid':
        # #                 move_out_mid_drop(turn=-97)
        # #             elif key == 'right':
        # #                 move_out_right_drop(turn=-121)
        # #             elif key == 'left':
        # #                 move_out_left_drop(turn=-71,straight=200)
        # #             break
                    
        # #     print(drop)
        # #     ev3.light.off()

            
        # # # go back
        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(49)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(-96)

        # # pid_distance(0.25,800,470)


        # # robot.settings(0,0,900,900)
        # # robot.turn(38)

        # # ls_following(proportional_gain=0, drive_speed=300)

        # # # straight to lundary
        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(15)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(60)

        # # pid_line(1,300)

        # # # push lundary
        # # robot.stop()
        # # robot.settings(700,700,0,0)
        # # robot.straight(130)

        # # # push lundary
        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(-80)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(93.5)

        # # pid_distance(1.05,200,80)

        # # basket_colors = {'basket_1': None, 'basket_2': None, 'basket_3': None}
        # # # print(basket_colors)

        # # basket_colors['basket_1'] = lundary_sorting.basket_scanning()
        
        # # robot.stop()
        # # robot.settings(700,700,0,0)
        # # robot.straight(-130)

        
        # # basket_colors['basket_2'] = lundary_sorting.basket_scanning()

        # # robot.stop()
        # # robot.settings(700,700,0,0)
        # # robot.straight(-110)

        
        # # basket_colors['basket_3'] = lundary_sorting.basket_scanning()

        # # pid_line(0.4,300)

        # # # print(basket_colors)

        # # lundary_sorting.lundary_sorting(basket_colors)
        

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(40)

        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(90)

        # # pid_distance(1,200,160)

        # # robot.stop()
        # # robot.settings(900,900,0,0)
        # # robot.straight(218)


        # # # a = 50
        # # # b = -50
        # # # c = -150
        # # # d = 140
        # # robot.stop()
        # # robot.settings(0,0,900,900)
        # # robot.turn(140)
