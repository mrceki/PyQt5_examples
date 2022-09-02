import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World!")

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create A Label 
        my_label = qtw.QLabel("Pick something from the list!")
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)
        
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Create a combo box
        my_combo = qtw.QComboBox(self,
        # bu satırları girerek combobox'ı editable yapabiliyoruz ve elle yeni veri girebiliyoruz
            editable=True,                           
            insertPolicy=qtw.QComboBox.InsertAtTop)
        my_combo.addItem("Pepperoni", "Something") #İkinci veri 'Data'
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom",qtw.QWidget)
        my_combo.addItem("Peppers")
        my_combo.addItem("ZartZurt")
        my_combo.addItems(["1", "2", "3"])
        my_combo.insertItem(2,"Third Thing")

        self.layout().addWidget(my_combo)

        # Create a  button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            # Add name to label
            my_label.setText(f'You picked {my_combo.currentText()}!') #Currentdata ile 21. satırdaki veri , currentIndex ise dizideki kaçıncı veri olduğunu verir
        

app = qtw.QApplication([])
mw = MainWindow()
app.exec()

"""    """
