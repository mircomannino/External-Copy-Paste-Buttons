from pynput.keyboard import Key, Controller
import time

class PersonalController:
    def __init__(self):
        self.keyboard = Controller()

    def copy(self):
        self.keyboard.press(Key.ctrl.value)
        self.keyboard.press('c')
        self.keyboard.release('c')
        self.keyboard.release(Key.ctrl.value)

    def cut(self):
        self.keyboard.press(Key.ctrl.value)
        self.keyboard.press('x')
        self.keyboard.release('x')
        self.keyboard.release(Key.ctrl.value)

    def paste(self):
        self.keyboard.press(Key.ctrl.value)
        self.keyboard.press('v')
        self.keyboard.release('v')
        self.keyboard.release(Key.ctrl.value)

    def manage_input(command):
        if command == 'C' or command == 'c':
            self.copy()
            return
        if command == 'V' or command == 'v':
            self.paste()
            return
        if command == 'X' or command == 'x':
            self.cut()
            return 
