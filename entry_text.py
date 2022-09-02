import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # Add a title
        self.setWindowTitle("Hello World")

        # Set vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # Create Label
        my_label = qtw.QLabel("Hello, What's your name?")
        
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)

        # Create an empty box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a button
        my_button = qtw.QPushButton("PressMe",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        # Add name to label
        def press_it():
            my_label.setText(f'Hello {my_entry.text()}!')
            
        # Clear the entry box
        my_entry.setText("")

        
        
app = qtw.QApplication([])
mw = MainWindow()

app.exec()
