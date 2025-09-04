import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import board
import adafruit_tca9548a
import time
from numpy import interp

class PressureReader():
    def __init__(self, input_i2c_port : int):
        i2c = board.I2C()
        tca = adafruit_tca9548a.TCA9548A(i2c)
        self.ads = ADS.ADS1015(tca[input_i2c_port])

    def get_voltage_value(self):
        read = AnalogIn(self.ads, ADS.P0)
        voltage_value = read.voltage
        # pressure_value = read.value
        
        return voltage_value

    def get_pressure_value(self):

        constant_psi2bar = 0.0689476
        psi_value = round(interp(self.get_voltage_value(),[0.002,5.006],[0,200]),2)
        bar_value = round(psi_value * constant_psi2bar, 2)

        return bar_value
        

def main():
    pr = PressureReader(4)
    while True:
        print(vr.get_pressure_value())
        time.sleep(1)

if __name__ == "__main__":
    main()
