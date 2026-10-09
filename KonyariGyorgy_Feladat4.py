from sense_hat import SenseHat
import matplotlib.pyplot as plt
from time import sleep

sense = SenseHat()

def exercise_1():
    calibration = True
    def stop():
        nonlocal calibration
        calibration = False
    sense.stick.direction_middle = stop
    x_list = []
    y_list = []
    while calibration:
        magnet = sense.get_compass_raw()
        x_list.append(magnet['x'])
        y_list.append(magnet['y'])
        sleep(0.1)
    plt.figure()
    plt.scatter(x_list, y_list, c='blue', marker='o', label='Mag X-Y')
    plt.title('Magnetometer X-Y Scatter Plot')
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.axhline(0, color='grey', linewidth=0.5)
    plt.axvline(0, color='grey', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

def exercise_2():
    sense.clear()
    x = 4
    y = 4
    for _ in range(50):
        orientation = sense.get_orientation()
        pitch = orientation["pitch"]
        if pitch > 180:
            pitch -= 360
        if pitch < -5 and x > 0:
            x -= 1
        elif pitch > 5 and x < 7:
            x += 1
        sense.clear()
        sense.set_pixel(x, y, (255, 0, 0))
        sleep(0.2)
    sense.clear()

def exercise_3():
    y_col = (255, 255, 0)
    o = (0, 0, 0)
    pacman_open = [
        o, o, y_col, y_col, y_col, y_col, o, o,
        o, y_col, y_col, y_col, y_col, y_col, y_col, o,
        y_col, y_col, y_col, y_col, y_col, y_col, y_col, y_col,
        y_col, y_col, y_col, o, o, o, y_col, y_col,
        y_col, y_col, o, o, o, o, o, y_col,
        y_col, y_col, y_col, o, o, o, y_col, y_col,
        y_col, y_col, y_col, y_col, y_col, y_col, y_col, y_col,
        o, y_col, y_col, y_col, y_col, y_col, y_col, o
    ]
    pacman_closed = [
        o, o, y_col, y_col, y_col, y_col, o, o,
        o, y_col, y_col, y_col, y_col, y_col, y_col, o,
        y_col, y_col, y_col, y_col, y_col, y_col, y_col, y_col,
        y_col, y_col, y_col, y_col, y_col, y_col, y_col, y_col,
        y_col, y_col, y_col, y_col, y_col, y_col, y_col, y_col,
        y_col, y_col, y_col, y_col, y_col, y_col, y_col, y_col,
        y_col, y_col, y_col, y_col, y_col, y_col, y_col, y_col,
        o, y_col, y_col, y_col, y_col, y_col, y_col, o
    ]
    for _ in range(20):
        sense.set_pixels(pacman_open)
        sleep(0.3)
        sense.set_pixels(pacman_closed)
        sleep(0.3)
    sense.clear()

if __name__ == "__main__":
    choice = input()
    if choice == '1':
        exercise_1()
    elif choice == '2':
        exercise_2()
    elif choice == '3':
        exercise_3()