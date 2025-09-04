import board
import digitalio
import adafruit_max31865
import time

class PT100Reader():
    def __init__(self):
        spi = board.SPI()
        cs = digitalio.DigitalInOut(board.D5)
        self.sensor = adafruit_max31865.MAX31865(spi, cs, wires=4, rtd_nominal=100.0, ref_resistor=430.0)

    def get_temperature(self):
        temperature = self.sensor.temperature
        temperature = round(temperature, 2)

        if temperature < 100:
            return temperature

        else:
            return 0


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