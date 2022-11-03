from runWRO_subfolder.variable_initiation import *
from runWRO_subfolder import inside_room1,inside_room2,inside_room3,inside_room4,dropping,starting_room




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


   

    pid_distance(1.05,200,80)

def backwards_basket_scanning():
    robot.stop()
    robot.settings(0,0,900,900)
    robot.turn(93.5)

    robot.stop()
    robot.settings(900,900,0,0)
    robot.straight(-130)

    basket_color_1 = str(color_1.color()).split(".")[1]

    return basket_color_1



def lundary_sorting(basket_colors):
    basket_done = {'basket_1_done': False, 'basket_2_done': False, 'basket_3_done': False}
    # for key,value in basket_done.items():
    #     if value == False:
    # for x in range(4):
    x = 1
    
    while x <= len(basket_colors):
        for k,v in basket_done.items():
            for key,value in basket_colors.items():
                lundary_color = str(color_2.color()).split(".")[1]
                if str(value) == str(lundary_color):
                    if (key == 'basket_1') and (k == 'basket_1_done' and v == False) :
                        basket_done['basket_1_done'] = move_to_basket_1()
                        break
                        # move_to_basket_1()
                    elif key == 'basket_2' and (k == 'basket_2_done' and v == False):
                        basket_done['basket_2_done'] = move_to_basket_2()
                        break
                        # move_to_basket_2()
                    elif key == 'basket_3' and (k == 'basket_3_done' and v == False):
                        basket_done['basket_3_done'] = move_to_basket_3()
                        break
                # else:
                #     out_of_basket_color()                     

                wait(100)

        print(basket_done)
        x += 1

        
def out_of_basket_color():
    robot.stop()
    drop_motor.run_angle(900,200)

    robot.stop()
    drop_motor.run_angle(-900,200)     

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


