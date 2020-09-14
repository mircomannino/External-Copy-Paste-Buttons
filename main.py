from personal_controller import PersonalController
from setup import load_setup()
import serial
import time
import os

if __name__ == '__main__':
    # Setup
    port_name, baud_rate = load_setup()
    os.system('sudo chmod 666 /dev/{}'.format(port_name))
    serial_port = serial.Serial('/dev/ttyACM0', baudrate=baud_rate)
    controller = PersonalController()
    print('Connected to: ', serial_port.name)

    while True:
        command = serial_port.read().decode('ASCII')
        if command == 'C':
            controller.copy()
            print('copied')
        elif command == 'V':
            controller.paste()
            print('pasted')

    # Close connection
    serial_port.close()
