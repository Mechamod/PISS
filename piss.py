from PyQt5.QtWidgets import *

class PISS:

    # Variables
    MINIMUM_HEIGHT = 600
    MINIMUM_WIDTH = 800
    MAXIMUM_WIDTH = 1920
    MAXIMUM_HEIGHT = 1080
    INPUT_PATH = ''
    OUTPUT_PATH = ''

    # Components (not neccessary, but good to have a look)
    VIEWER = None
    APP = None
    LAYOUT = None
    btn_set_input_path = None
    btn_set_output_path = None
    lbl_input_path = None
    lbl_output_path = None

    def __init__(self, width=800, height=600):
        self.WIDTH = width
        self.HEIGHT = height

    def create_main_window(self):

        # Define window
        self.APP = QApplication([])
        self.VIEWER = QWidget(minimumHeight=self.MINIMUM_HEIGHT, minimumWidth=self.MINIMUM_WIDTH, maximumHeight=self.MAXIMUM_HEIGHT, maximumWidth=self.MAXIMUM_WIDTH)
        self.VIEWER.setWindowTitle("Python Image Selection Saver")
        self.LAYOUT = QVBoxLayout()

        # Decorate window
        ## Labels
        self.create_label_input_path()
        self.create_label_output_path()

        ## Buttons
        self.create_set_input_path_button()
        self.create_set_output_path_button()

        # Start app
        self.VIEWER.setLayout(self.LAYOUT)
        self.VIEWER.show()
        self.APP.exec_()

    def create_set_input_path_button(self):
        self.btn_set_input_path = QPushButton(self.VIEWER)
        self.btn_set_input_path.setText("Select input folder")
        self.btn_set_input_path.clicked.connect(self.set_input_path)
        self.LAYOUT.addWidget(self.btn_set_input_path)

    def create_set_output_path_button(self):
        self.btn_set_output_path = QPushButton(self.VIEWER)
        self.btn_set_output_path.setText("Select output folder")
        self.btn_set_output_path.clicked.connect(self.set_output_path)
        self.LAYOUT.addWidget(self.btn_set_output_path)

    def create_label_input_path(self):
        self.lbl_input_path = QLabel(self.VIEWER)
        self.lbl_input_path.setText("Input-Path: " + self.INPUT_PATH)
        self.LAYOUT.addWidget(self.lbl_input_path)

    def create_label_output_path(self):
        self.lbl_output_path = QLabel(self.VIEWER)
        self.lbl_output_path.setText("Output-Path: " + self.OUTPUT_PATH)
        self.LAYOUT.addWidget(self.lbl_output_path)

    def update_label_input_path(self):
        self.lbl_input_path.setText("Input-Path: " + self.INPUT_PATH)

    def update_label_output_path(self):
        self.lbl_output_path.setText("Output-Path: " + self.OUTPUT_PATH)

    def set_input_path(self):
        self.INPUT_PATH = QFileDialog().getExistingDirectory(None, "Select Input Folder")
        self.update_label_input_path()
        print(f"INPUT_PATH set to {self.INPUT_PATH}")

    def set_output_path(self):
        self.OUTPUT_PATH = QFileDialog().getExistingDirectory(None, "Select Output Folder")
        self.update_label_output_path()
        print(f"OUTPUT_PATH set to {self.OUTPUT_PATH}")

if __name__ == '__main__':
    print("Start PISS")
    piss = PISS(width=1920, height=1080)
    piss.create_main_window()
