from PyQt5.QtWidgets import *

class PISS:

    # Variables
    WIDTH = 1920
    HEIGHT = 1080
    INPUT_PATH = ''
    OUTPUT_PATH = ''
    VIEWER = None
    APP = None

    def __init__(self, width=800, height=600):
        self.WIDTH = width
        self.HEIGHT = height

    def create_main_window(self):
        self.APP = QApplication([])
        self.VIEWER = QWidget()
        self.VIEWER.setWindowTitle("Python Image Selection Saver")
        #
        #
        # STUFF
        self.create_label_input_path()
        #
        self.VIEWER.show()
        self.APP.exec_()

    def create_set_path_button(self):
        btn_set_path = Button(self.VIEWER, text="Set up input directory", width=25, callback=set_input_path)

    def create_label_input_path(self):
        lbl_input_path = QLabel(self.VIEWER)
        lbl_input_path.setText("Input-Path: " + self.INPUT_PATH)

    def create_label_output_path(self):
        lbl_output_path = QLabel(self.VIEWER, text="Output-Path: " + self.OUTPUT_PATH)

    def set_input_path(self):
        self.INPUT_PATH = "Test"

if __name__ == '__main__':
    print("Start PISS")
    piss = PISS(width=1920, height=1080)
    piss.create_main_window()
