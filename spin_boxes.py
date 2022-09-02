import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spin Boxes")
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Hello")
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        my_spinbox = qtw.QDoubleSpinBox(self, #QSpinbox
            value = 10,
            maximum = 100,
            minimum = 0,
            singleStep = 5.2, #her basışta kaçar artacak/azalacak
            prefix="#",        #Before value in box
            suffix=" Order")   #After value iin box
        # Change font size 
        my_spinbox.setFont(qtg.QFont("Times New Roman", 15))
        self.layout().addWidget(my_spinbox)

        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f'You entered {my_spinbox.value()}')

app = qtw.QApplication([])
mw = MainWindow()
app.exec()



