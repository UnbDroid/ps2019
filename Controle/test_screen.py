import os
import time

def clear_screen():
    os.system("clear")

ang = 45
vel = "000"

def number_print(number):
    try:
        import texts
    except:
        pass    
    number = str(number)

    for i in range(1, 8):
        for digit in number:
            func_name = 'print_'+str(digit)+'_'+str(i)
            func = getattr(texts, func_name)
            result = func()
        print("")

def update_screen_info(ang, vel):
    try:
        import texts
    except:
        pass
    clear_screen()

    texts.print_ship()
    texts.print_vel()
    # print_1_1()
    number_print(vel)
    print("")
    print("")
    print("")

    texts.print_angle()
    number_print(ang)

    time.sleep(1)

while True:
    update_screen_info(ang, vel)
    ang = ang+1
    vel = str(int(vel) + 1)
