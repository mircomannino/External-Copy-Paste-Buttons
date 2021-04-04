from personal_controller import PersonalController
from pynput.keyboard import Key, Controller
from setup import load_setup_linux
import time
import serial
import os

if __name__ == '__main__':
    # Setup
    port_name, baud_rate = load_setup_linux()
    os.system('sudo chmod 666 {}'.format(port_name))
    serial_port = serial.Serial(port_name, baudrate=baud_rate)
    controller = PersonalController()
    print('Connected to: ', serial_port.name)
    
    # Main part
    while True:
        command = serial_port.read().decode('ASCII')
        controller.manage_input(command)

    # Close connection
    serial_port.close()
