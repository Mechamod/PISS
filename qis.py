from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pathlib import Path
from PyQt5.QtCore import *
import sys

class Utility:
    """
    Provides helper functions
    """

    def cut_long_string(string):
        """
        If the input string is too long (20 characters or more) it gets
        shortened and '...' is put infornt of it, indicating that there
        was more. The returned string has a length of 20.
        """

        if len(string) >= 20:
            return "..."+string[-17:]
        else:
            return string

    def path_exists(directory_path):
        """
        Checks if the given path exists. True iff yes.
        """

        from os import path
        return path.exists(directory_path)

    def start_saving(image_path_list, selected_image_indizes, output_path):
        """
        Starts to copy images from the given path list to the output path if
        the index is in the selected list.
        """

        print("Start saving!")
        from shutil import copy2
        for index in selected_image_indizes:
            input_path = str(image_path_list[index])
            print(f"Copy from '{input_path}' to '{output_path}'.")
            copy2(input_path, output_path)

        return True


class PISS_UI(object):
    """
    Python Image Selection Saver is a PyQt GUI based program which lets the user
    load up a collection of images from a folder, providing a preview of the
    images, an easy way to browse them (left/right arrow buttons) and finally
    let him save the images he likes with a simple press of the spacebar.
    """

    # Variables (Numbers, Strings, Lists)
    MINIMUM_HEIGHT = 800 # Minimum height, standard value
    MINIMUM_WIDTH = 1600 # minimum width, standard value

    MAXIMUM_HEIGHT = 1080 # Maximum height
    MAXIMUM_WIDTH = 1920 # Maximum width

    WINDOW_HEIGHT = 600 # Actual window height, initialized with standard value
    WINDOW_WIDTH = 800 # Actual window width, initialized with standard value

    INPUT_PATH = ''
    OUTPUT_PATH = ''

    IMAGE_PATH_LIST = ['Homescreen.png']
    SELECTED_IMAGE_INDIZES = []
    IMAGE_INDEX = 0

    # Components (not neccessary, but good to have a look)
    VIEWER = None
    APP = None
    LAYOUT = None

    btn_set_input_path = None
    btn_set_output_path = None
    btn_go = None

    lbl_input_path = None
    lbl_output_path = None
    lbl_index = None
    lbl_list_length = None
    lbl_number_selected = None

    def __init__(self):
        """
        Init the PISS variables needed beforehand
        """
        pass

    def setupUI(self, MainWindow):
        """
        Creates the main window.
        First it defines the window and it's properties, then it creates all
        the elements and forms it has to display and finally
        it adds everything together in a QGridLayout.
        """

        # Define window
        MainWindow.setObjectName("Python Image Selection Saver")
        self.VIEWER = QWidget(MainWindow)
        self.setCentralWidget(self.VIEWER)
        self.LAYOUT = QGridLayout()

        # Decorate window
        ## Labels
        self.create_label_input_path()
        self.create_label_output_path()
        self.create_image_label()
        self.initialize_image_label()
        self.create_label_index()
        self.create_label_list_length()
        self.create_label_number_selected()

        ## Buttons
        self.create_set_input_path_button()
        self.create_set_output_path_button()
        self.create_button_go()

        # Start app
        self.VIEWER.setLayout(self.LAYOUT)
        self.VIEWER.show()

        # Resize
        self.resize(self.MINIMUM_WIDTH, self.MINIMUM_HEIGHT)

    def check_background(self):
        if self.IMAGE_INDEX in self.SELECTED_IMAGE_INDIZES:
            self.setStyleSheet("background-color: lightgray;")
        else:
            self.setStyleSheet("background-color: white;")

    def create_button_go(self):
        """
        Create the button used to start the saving process.
        """

        self.btn_go = QPushButton(self.VIEWER)
        self.btn_go.setText("Save selected")
        self.btn_go.clicked.connect(self.start_saving)
        self.btn_go.setFocusPolicy(Qt.NoFocus)
        self.LAYOUT.addWidget(self.btn_go, 7,9,1,2)

    def start_saving(self):
        """
        Starts the saving process
        """

        if Utility.start_saving(self.IMAGE_PATH_LIST, self.SELECTED_IMAGE_INDIZES, self.OUTPUT_PATH):
            print("Copying done!")
            sys.exit()

    def create_label_number_selected(self):
        self.lbl_number_selected = QLabel(self.VIEWER)
        self.lbl_number_selected.setText(f"# of selected images: {len(self.SELECTED_IMAGE_INDIZES)}")
        self.LAYOUT.addWidget(self.lbl_number_selected, 6, 9, 1, 1)

    def update_label_number_selected(self):
        self.lbl_number_selected.setText(f"# of selected images: {len(self.SELECTED_IMAGE_INDIZES)}")

    def create_label_list_length(self):
        """
        Creates the label which shows the number of images loaded.
        """

        self.lbl_list_length = QLabel(self.VIEWER)
        self.lbl_list_length.setText(f"# of images: {len(self.IMAGE_PATH_LIST)}")
        self.LAYOUT.addWidget(self.lbl_list_length, 5, 9, 1, 1)

    def update_label_list_length(self):
        """
        Updates the label which shows the number of images.
        """

        self.lbl_list_length.setText(f"# of Images: {len(self.IMAGE_PATH_LIST)}")

    def create_label_index(self):
        """
        Creates a label which is going to indicate which index the user is on.
        """

        self.lbl_index = QLabel(self.VIEWER)
        self.lbl_index.setText(f"Actual image number: {self.IMAGE_INDEX+1}")
        self.LAYOUT.addWidget(self.lbl_index, 4, 9, 1, 1)

    def update_label_index(self):
        self.lbl_index.setText(f"Actual image number: {self.IMAGE_INDEX+1}")

    def create_set_input_path_button(self):
        """
        Creates a button which opens a dialog to let the user select the
        input folder. It also gets added to the layout of the application
        window.
        """

        self.btn_set_input_path = QPushButton(self.VIEWER)
        self.btn_set_input_path.setText("Select input folder")
        self.btn_set_input_path.clicked.connect(self.set_input_path)
        self.btn_set_input_path.setFocusPolicy(Qt.NoFocus)
        self.LAYOUT.addWidget(self.btn_set_input_path, 1, 9, 1, 1)

    def create_set_output_path_button(self):
        """
        Creates a button which opens a dialog to let the user select the
        output folder. It also gets added to the layout of the application
        window.
        """

        self.btn_set_output_path = QPushButton(self.VIEWER)
        self.btn_set_output_path.setText("Select output folder")
        self.btn_set_output_path.clicked.connect(self.set_output_path)
        self.btn_set_output_path.setFocusPolicy(Qt.NoFocus)
        self.LAYOUT.addWidget(self.btn_set_output_path, 3, 9, 1, 1)

    def create_label_input_path(self):
        """
        Creates a text label that displays the currently set path of the
        input directory.
        """

        self.lbl_input_path = QLabel(self.VIEWER)
        self.lbl_input_path.setText("Input-Path: " + self.INPUT_PATH)
        self.LAYOUT.addWidget(self.lbl_input_path, 0, 9, 1, 1)

    def create_label_output_path(self):
        """
        Creates a text label that displays the currently set path of the
        output directory.
        """

        self.lbl_output_path = QLabel(self.VIEWER)
        self.lbl_output_path.setText("Output-Path: " + self.OUTPUT_PATH)
        self.LAYOUT.addWidget(self.lbl_output_path, 2, 9, 1, 1)

    def create_image_label(self):
        """
        Creates the image display
        """

        self.image_label = QLabel(self.VIEWER)
        self.image_label.setMaximumWidth(1600)
        self.image_label.setMaximumWidth(1280)
        self.LAYOUT.addWidget(self.image_label, 0, 0, 9, 9)

    def initialize_image_label(self):
        """
        Initizlaizes the image display with the homescreen
        """

        qpixmap = QPixmap('Homescreen.png').scaledToHeight(self.WINDOW_HEIGHT)
        self.image_label.setPixmap(qpixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

    def update_image_label(self):
        """
        Updates the image display by the actual index in the path list
        of images.
        """

        path = str(self.IMAGE_PATH_LIST[self.IMAGE_INDEX])
        qpixmap = QPixmap(path).scaledToHeight(self.WINDOW_HEIGHT)
        self.image_label.setPixmap(qpixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

    def update_label_input_path(self):
        """
        Updates the label of the input path.
        """

        longness_checked_input_string = Utility.cut_long_string(self.INPUT_PATH)
        self.lbl_input_path.setText("Input-Path: " + longness_checked_input_string)

    def update_label_output_path(self):
        """
        Updates the label of the output path.
        """

        longness_checked_output_string = Utility.cut_long_string(self.OUTPUT_PATH)
        self.lbl_output_path.setText("Output-Path: " + longness_checked_output_string)

    def set_input_path(self):
        """
        Opens a dialog form that lets the user choose the input directory.
        """

        self.INPUT_PATH = str(QFileDialog().getExistingDirectory(None, "Select Input Folder"))
        self.update_label_input_path()
        print(f"INPUT_PATH set to {self.INPUT_PATH}")
        self.btn_set_input_path.setEnabled(False)
        self.load_input_images()

    def set_output_path(self):
        """
        Opens a dialog form that lets the user choose the output directory.
        """

        self.OUTPUT_PATH = str(QFileDialog().getExistingDirectory(None, "Select Output Folder"))

        if Utility.path_exists(self.OUTPUT_PATH):
            self.update_label_output_path()
            self.btn_set_output_path.setEnabled(False)
            print(f"OUTPUT_PATH set to {self.OUTPUT_PATH}")
        else:
            print("Path does not exists!")

    def load_input_images(self):
        """
        Loads the paths to the images from the input path as a list.
        """

        # Resets existing List and Index
        self.IMAGE_PATH_LIST = []
        self.IMAGE_INDEX = 0

        # Loads paths
        types = ['jpg', 'jpeg', 'png']
        for type in types:
            for path in Path(self.INPUT_PATH).rglob(f"*.{type}"):
                self.IMAGE_PATH_LIST.append(path)

        # Update length and its label
        self.update_label_list_length()

        # Update image view
        self.update_image_label()

    def change_image_index(self, mode):
        """
        Increases or decreases the image index.
        """

        if mode == "INCREASE" and self.IMAGE_INDEX < len(self.IMAGE_PATH_LIST)-1:
            self.IMAGE_INDEX+=1
        elif mode == "DECREASE" and self.IMAGE_INDEX > 0:
            self.IMAGE_INDEX-=1

    def shift_image(self):
        """
        Adds or removes an image, depending if it is already in the list or not.
        """

        if self.IMAGE_INDEX in self.SELECTED_IMAGE_INDIZES:
            print(f"Remove {self.IMAGE_INDEX}")
            self.SELECTED_IMAGE_INDIZES.remove(self.IMAGE_INDEX)
        else:
            print(f"Add {self.IMAGE_INDEX}")
            self.SELECTED_IMAGE_INDIZES.append(self.IMAGE_INDEX)

        self.update_label_number_selected()

class MainWindow(QMainWindow, PISS_UI):

    # Starts the window
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setWindowTitle("Python Image Selection Saver") # Names the window
        #self.setGeometry(0, 0, 500, 300)  # Resizes the window
        self.setupUI(self)

    # Gets key press events
    def keyPressEvent(self, e):
        pressed_key = e.key()

        if pressed_key == Qt.Key_Shift:
            self.shift_image()
        elif pressed_key == Qt.Key_Left:
            self.change_image_index("DECREASE")
        elif pressed_key == Qt.Key_Right:
            self.change_image_index("INCREASE")

        self.update_image_label()
        self.update_label_index()
        self.check_background()

# Starts the program!
if __name__ == '__main__':
    print("Start PISS")
    app = QApplication([])
    piss_main_window = MainWindow()
    piss_main_window.show()
    app.exec_()
