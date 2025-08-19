# RaspiMultiSensor 프로젝트
## Setup
* 라즈베리파이에 PT100 센서, 압력 센서, 펌프 제어를 하는 것이 목표
* PT100
	* https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier/python-circuitpython
* I2C Multiplexer
	* https://learn.adafruit.com/adafruit-tca9548a-1-to-8-i2c-multiplexer-breakout/circuitpython-python
* ADC(압력 센서)
	* https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython
* DAC(펌프 제어)
	* https://learn.adafruit.com/adafruit-mcp4728-i2c-quad-dac
* Segment 1.2인치
	* https://learn.adafruit.com/adafruit-led-backpack/1-2-inch-7-segment-backpack
```bash 
# pwd
mkdir workspace && cd workspace
mkdir VLEControllerPi && cd VLEControllerPi

# Setup venv
python -m venv .venv
source .venv/bin/activate

# Install Dependency
cd .venv/bin && pip3 install adafruit-circuitpython-tca9548a adafruit-circuitpython-ads1x15 adafruit-circuitpython-max31865 adafruit-circuitpython-ht16k33 adafruit-circuitpython-mcp4728
sudo apt-get install pillow 
```
## Code
```python title:Main.py
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
```


```python title:PT100Reader.py
import board
import digitalio
import adafruit_max31865
import time

class PT100Reader():
    def __init__(self):
        spi = board.SPI()
        cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
        self.sensor = adafruit_max31865.MAX31865(spi, cs, wires=4, rtd_nominal=100.0, ref_resistor=430.0)

    def get_temperature(self):
        temperature = self.sensor.temperature
        temperature = round(temperature, 2)

        return temperature

    def get_resistance(self):
        resistance = self.sensor.resistance
        resistance = round(resistance, 2)

        return resistance

def main():
    pr = PT100Reader()

    while True:
        print("Temperature is " + str(pr.get_temperature()) + "\n")
        print("Resistance is " + str(pr.get_resistance()))
        time.sleep(0.1)

if __name__ == "__main__":
    main()
```


```python title:SegmentController.py
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

    def run_number_display(self, input_number : int , input_colons : bool):
        self.display.colons[0] = input_colons
        self.display.print(str(input_number).zfill(4))

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
```
## Result
![[SegmentTest.mp4]]
![[PT100withSegment.mp4]]