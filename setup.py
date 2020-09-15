'''
File used to configure the serial connection
Change the variables values with your preferences
'''

def load_setup_linux():
    PORT_NAME = '/dev/ttyACM0'
    BAUD_RATE = 9600
    return PORT_NAME, BAUD_RATE

def load_setup_windows():
    PORT_NAME = 'COM3'
    BAUD_RATE = 9600
    return PORT_NAME, BAUD_RATE
