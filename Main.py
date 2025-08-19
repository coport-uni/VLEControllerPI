from SegmentController import SegmentController
from PT100Reader import PT100Reader
import time

def main():
    sc = SegmentController(0)
    pr = PT100Reader()

    while True:
        temperature = pr.get_temperature()
        print("Temperature is " + str(temperature) + "\n")
        sc.run_number_display(temperature * 10, True)
        time.sleep(1)

if __name__ == "__main__":
    main()