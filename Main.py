from SegmentController import SegmentController
from PT100Reader import PT100Reader
from PumpController import PumpController
from PressureReader import PressureReader
import time

def main():
    pr100 = PT100Reader()
    sc_temp_1 = SegmentController(0)
    sc_pres = SegmentController(1)
    pc = PumpController(3)
    pr = PressureReader(4)

    pc.run_command_start("off")
    time.sleep(3)
    pc.run_command_start("on")


    while True:
        temperature_1 = pr100.get_temperature()
        pressure = pr.get_pressure_value()
        print("Temperature is " + str(temperature_1) + "\n")
        sc_temp_1.run_number_display(temperature_1, True)
        print("Pressure is " + str(pressure) + "\n")
        sc_pres.run_number_display(pressure, True)
        time.sleep(1)

if __name__ == "__main__":
    main()