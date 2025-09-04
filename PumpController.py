import board
import adafruit_mcp4728
import adafruit_tca9548a
import time

class PumpController():
    def __init__(self, input_i2c_port : int):
        i2c = board.I2C()
        tca = adafruit_tca9548a.TCA9548A(i2c)
        self.pump_controller = adafruit_mcp4728.MCP4728(tca[input_i2c_port])
        self.max_number = 65535

    def run_command_speed(self, input_percent : int):
        self.pump_controller.channel_a.value = int(self.max_number / 100 * input_percent)
    
    def run_command_start(self, input_start : str):
        if input_start == "on":
            self.pump_controller.channel_b.value = self.max_number * 0

        elif input_start == "off":
            self.pump_controller.channel_b.value = self.max_number

    def run_command_direction(self, input_start : str):
        if input_start == "cw":
            self.pump_controller.channel_c.value = self.max_number * 0

        elif input_start == "ccw": 
            self.pump_controller.channel_c.value = self.max_number

def main():
    pc = PumpController(1)

    pc.run_command_start("off")
    time.sleep(3)
    pc.run_command_start("on")

    for i in range(50):
        pc.run_command_speed(i)
        pc.run_command_direction("cw")
        time.sleep(0.5)

    for i in range(51,100):
        pc.run_command_speed(i)
        pc.run_command_direction("ccw")
        time.sleep(0.5)

    pc.run_command_start("off")

if __name__ == "__main__":
    main()
