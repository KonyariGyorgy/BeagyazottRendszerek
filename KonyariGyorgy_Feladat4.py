
from sense_hat import SenseHat
from math import sqrt
from time import sleep


def run_exercise_1():
    print("\n--- Running Exercise 1: Magnetometer Scatter Plot ---")
    sense = SenseHat()
    calibration = True

    def stop():
        nonlocal calibration
        calibration = False

    sense.stick.direction_middle = stop
    x_list = []
    y_list = []

    print("Start rotating the Sense HAT around the z-axis. Press the joystick to stop.")
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


def run_exercise_2():
    print("\n--- Running Exercise 2: LED Matrix Dot Movement (Pitch Angle) ---")
    print("Tilt the Sense HAT left or right. Press Ctrl+C in terminal to exit.")
    sense = SenseHat()
    sense.clear()

    x = 4
    y = 4

    try:
        while True:
            orientation = sense.get_orientation()
            pitch = orientation["pitch"]

            if pitch > 180:
                pitch -= 360

            if pitch < -5 and x > 0:
                x -= 1
            elif pitch > 5 and x < 7:
                x += 1

            sense.clear()
            sense.set_pixel(x, y, (255, 0, 0))  # Red dot
            sleep(0.2)
    except KeyboardInterrupt:
        sense.clear()
        print("Exited Exercise 2.")


def run_exercise_3():
    print("\n--- Running Exercise 3: Pac-Man Animation ---")
    print("Press Ctrl+C in terminal to exit.")
    sense = SenseHat()

    yellow = (255, 255, 0)
    black = (0, 0, 0)

    pacman_open = [
        black, black, yellow, yellow, yellow, yellow, black, black,
        black, yellow, yellow, yellow, yellow, yellow, yellow, black,
        yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
        yellow, yellow, yellow, black, black, black, yellow, yellow,
        yellow, yellow, black, black, black, black, black, yellow,
        yellow, yellow, yellow, black, black, black, yellow, yellow,
        yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
        black, yellow, yellow, yellow, yellow, yellow, yellow, black
    ]

    pacman_closed = [
        black, black, yellow, yellow, yellow, yellow, black, black,
        black, yellow, yellow, yellow, yellow, yellow, yellow, black,
        yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
        yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
        yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
        yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
        yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
        black, yellow, yellow, yellow, yellow, yellow, yellow, black
    ]

    try:
        while True:
            sense.set_pixels(pacman_open)
            sleep(0.3)
            sense.set_pixels(pacman_closed)
            sleep(0.3)
    except KeyboardInterrupt:
        sense.clear()
        print("Exited Exercise 3.")


def main():
    print("=== Sense HAT Lab Menu ===")
    print("1. Exercise 1: Magnetometer Scatter Plot")
    print("2. Exercise 2: LED Matrix Dot Movement via Pitch")
    print("3. Exercise 3: Pac-Man Animation")

    choice = input("Select an exercise to run (1, 2, or 3): ").strip()

    if choice == '1':
        run_exercise_1()
    elif choice == '2':
        run_exercise_2()
    elif choice == '3':
        run_exercise_3()
    else:
        print("Invalid choice. Please run the script again and select 1, 2, or 3.")


if __name__ == '__main__':
    main()