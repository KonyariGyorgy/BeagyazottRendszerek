from KonyariGyorgy_Feladat4 import KonyariGyorgy_Feladat4
from time import sleep
from random import randint
import time

sense = KonyariGyorgy_Feladat4()


def exercise_1():
    up_arrow = [
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 1, 0, 0, 1, 1, 0,
        1, 1, 0, 0, 0, 0, 1, 1,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0
    ]
    down_arrow = [
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 1, 1,
        0, 1, 1, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0
    ]
    left_arrow = [
        0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 1, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0
    ]
    right_arrow = [
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 1, 1, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0
    ]
    w = (255, 255, 255)
    n = (0, 0, 0)
    up_img = [w if v == 1 else n for v in up_arrow]
    down_img = [w if v == 1 else n for v in down_arrow]
    left_img = [w if v == 1 else n for v in left_arrow]
    right_img = [w if v == 1 else n for v in right_arrow]

    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    sense.set_pixels(up_img)
                elif event.direction == "down":
                    sense.set_pixels(down_img)
                elif event.direction == "left":
                    sense.set_pixels(left_img)
                elif event.direction == "right":
                    sense.set_pixels(right_img)
                sleep(0.5)
                sense.clear()


def exercise_2():
    o = (0, 0, 0)
    b = (0, 0, 255)
    patterns = {
        1: [o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, o, o, o, o, o, o, b,
            b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o],
        2: [o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, o, o, o, o, o, o, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o,
            o, o, o, o, o, b, b, o, o, o, o, o, o, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o],
        3: [o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, o, o, o, o, o, o, b, b, o, o, o, o, b, b, o, o, o, o, o, o, b,
            b, o, o, o, o, b, b, o, o, o, o, o, o, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o],
        4: [o, o, o, o, o, o, o, o, o, b, b, o, o, b, b, o, o, b, b, o, o, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o,
            o, o, o, o, o, b, b, o, o, b, b, o, o, b, b, o, o, b, b, o, o, o, o, o, o, o, o, o],
        5: [o, b, b, o, o, b, b, o, o, b, b, o, o, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, o, o, o, o, o, o, b,
            b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, o, o, b, b, o, o, b, b, o, o, b, b, o],
        6: [o, b, b, o, o, b, b, o, o, b, b, o, o, b, b, o, o, o, o, o, o, o, o, o, o, b, b, o, o, b, b, o, o, b, b, o,
            o, b, b, o, o, o, o, o, o, o, o, o, o, b, b, o, o, b, b, o, o, b, b, o, o, b, b, o]
    }

    def roll(event):
        if event.action == "pressed":
            t0 = time.time()
            while time.time() - t0 < 3:
                val = randint(1, 6)
                sense.set_pixels(patterns[val])
                time.sleep(0.1)
            final_val = randint(1, 6)
            sense.set_pixels(patterns[final_val])
            time.sleep(2)
            sense.clear()

    sense.stick.direction_middle = roll
    while True:
        pass


def exercise_3():
    n = (0, 0, 0)
    b = (0, 0, 255)
    pixels = [n] * 64
    while True:
        pixels = [n] * 56 + pixels[:8]
        col = randint(0, 7)
        pixels[col] = b
        sense.set_pixels(pixels)
        sleep(0.5)


def exercise_4():
    state = 0
    halted = False
    r = (255, 0, 0)
    g = (0, 255, 0)
    y = (255, 255, 0)
    n = (0, 0, 0)
    red = [n, n, n, r, r, n, n, n] * 2 + [n] * 48
    red_yellow = [n, n, n, r, r, n, n, n] * 2 + [n] * 16 + [n, n, n, y, y, n, n, n] * 2 + [n] * 24
    yellow = [n] * 24 + [n, n, n, y, y, n, n, n] * 2 + [n] * 24
    green = [n] * 48 + [n, n, n, g, g, n, n, n] * 2

    def set_state():
        nonlocal state
        if not halted:
            if state < 3:
                state += 1
            elif state == 3:
                state = 0

    def button_event(event):
        nonlocal halted
        if event.action == 'released':
            halted = not halted

    sense.stick.direction_middle = button_event

    while True:
        if not halted:
            if state == 0:
                sense.set_pixels(red)
                sleep(3)
            elif state == 1:
                sense.set_pixels(red_yellow)
                sleep(1)
            elif state == 2:
                sense.set_pixels(green)
                sleep(2)
            elif state == 3:
                sense.set_pixels(yellow)
                sleep(1)
            set_state()
        else:
            sense.set_pixels(yellow)
            sleep(0.5)
            sense.clear()
            sleep(0.5)


if __name__ == "__main__":
    choice = input()
    if choice == '1':
        exercise_1()
    elif choice == '2':
        exercise_2()
    elif choice == '3':
        exercise_3()
    elif choice == '4':
        exercise_4()