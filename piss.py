from PyQt5.QtWidgets import *

class PISS:
    """
    Python Image Selection Saver is a PyQt GUI based program which lets the user
    load up a collection of images from a folder, providing a preview of the
    images, an easy way to browse them (left/right arrow buttons) and finally
    let him save the images he likes with a simple press of the spacebar.
    """

    # Variables (Numbers, Strings, Lists)
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

    def __init__(self):
        """
        Init the PISS variables needed beforehand
        """

        pass

    def create_main_window(self):
        """
        Creates the main window.
        First it defines the window and it's properties, then it creates all
        the elements and forms it has to display and finally
        it adds everything together.
        """

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

    def start_app(self):
        """
        Starts the execution of the application.
        """

        self.APP.exec_()

    def create_set_input_path_button(self):
        """
        Creates a button which opens a dialog to let the user select the
        input folder. It also gets added to the layout of the application
        window.
        """

        self.btn_set_input_path = QPushButton(self.VIEWER)
        self.btn_set_input_path.setText("Select input folder")
        self.btn_set_input_path.clicked.connect(self.set_input_path)
        self.LAYOUT.addWidget(self.btn_set_input_path)

    def create_set_output_path_button(self):
        """
        Creates a button which opens a dialog to let the user select the
        output folder. It also gets added to the layout of the application
        window.
        """

        self.btn_set_output_path = QPushButton(self.VIEWER)
        self.btn_set_output_path.setText("Select output folder")
        self.btn_set_output_path.clicked.connect(self.set_output_path)
        self.LAYOUT.addWidget(self.btn_set_output_path)

    def create_label_input_path(self):
        """
        Creates a text label that displays the currently set path of the
        input directory.
        """

        self.lbl_input_path = QLabel(self.VIEWER)
        self.lbl_input_path.setText("Input-Path: " + self.INPUT_PATH)
        self.LAYOUT.addWidget(self.lbl_input_path)

    def create_label_output_path(self):#
        """
        Creates a text label that displays the currently set path of the
        output directory.
        """

        self.lbl_output_path = QLabel(self.VIEWER)
        self.lbl_output_path.setText("Output-Path: " + self.OUTPUT_PATH)
        self.LAYOUT.addWidget(self.lbl_output_path)

    def update_label_input_path(self):
        """
        Updates the label of the input path.
        """

        self.lbl_input_path.setText("Input-Path: " + self.INPUT_PATH)

    def update_label_output_path(self):
        """
        Updates the label of the output path.
        """

        self.lbl_output_path.setText("Output-Path: " + self.OUTPUT_PATH)

    def set_input_path(self):
        """
        Opens a dialog form that lets the user choose the input directory.
        """

        self.INPUT_PATH = QFileDialog().getExistingDirectory(None, "Select Input Folder")
        self.update_label_input_path()
        print(f"INPUT_PATH set to {self.INPUT_PATH}")

    def set_output_path(self):
        """
        Opens a dialog form that lets the user choose the output directory.
        """

        self.OUTPUT_PATH = QFileDialog().getExistingDirectory(None, "Select Output Folder")
        self.update_label_output_path()
        print(f"OUTPUT_PATH set to {self.OUTPUT_PATH}")

# Starts the program!
if __name__ == '__main__':
    print("Start PISS")
    piss = PISS()
    piss.create_main_window()
    piss.start_app()
