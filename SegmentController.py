import board
from adafruit_ht16k33.segments import BigSeg7x4
import adafruit_tca9548a
import time

class SegmentController():
    def __init__(self, input_i2c_port : int):
        i2c = board.I2C()
        tca = adafruit_tca9548a.TCA9548A(i2c)
        # self.display = BigSeg7x4(i2c)

        self.display = BigSeg7x4(tca[input_i2c_port], address = 0x71)
        self.display.brightness = 1.0
        self.display.blink_rate = 0

    def run_number_display(self, input_number : float, input_colons : bool):
        self.display.colons[0] = input_colons
        number_array = list(map(int, str(int(input_number * 100))))
        if len(number_array) == 3:
            self.display[0] = "0"

            for i in range(len(number_array)):
                self.display[i+1] = str(number_array[i])

        elif len(number_array) == 4:
            for i in range(len(number_array)):
                self.display[i] = str(number_array[i])

        else: 
            print("value_error")
            
    def run_string_display(self, input_string : str):
        self.display.print(input_string)

def main():
    sc = SegmentController(0)
    number = 0

    for number in range(1000):
        sc.run_number_display(number, False)
        print(number)
        time.sleep(0.05)

if __name__ == "__main__":
    main()

# display.print("ABCD")
# display.print(1234)
# display.print("12:34")

# display.ampm = True
# display.top_left_dot = True
# display.bottom_left_dot = True
# display.colons[0] = True
# display.colons[1] = True
# display.print("12.34")