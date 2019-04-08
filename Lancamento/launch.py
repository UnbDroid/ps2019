from termcolor import colored, cprint
from os import system
import texts
import time


def number_print(number):
    number = str(number)

    for i in range(1, 8):
        for digit in number:
            func_name = f'print_{digit}_{i}'
            func = getattr(texts, func_name)
            result = func()
        print("")

def print_menu(speed, angle):
    system('clear')

    texts.print_ship()
    texts.print_vel()
    # print_1_1()
    number_print(speed)
    print("")
    print("")
    print("")

    texts.print_angle()
    number_print(angle)

if __name__ == "__main__":
    clear = lambda: system('clear')

    for i in range(0, 100):
        time.sleep(0.05)
        print_menu(i, i)



    while(True):
        pass
