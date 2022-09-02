import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Boxes")
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Hello!!")
        my_label.setFont(qtg.QFont("Arial", 20))
        self.layout().addWidget(my_label)

        my_text = qtw.QTextEdit(self,
            acceptRichText = True,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,           #change size of textbox
            placeholderText="Hello World",
            readOnly=False)
        self.layout().addWidget(my_text)

        my_button = qtw.QPushButton("Press Me",
            clicked = lambda : press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f'You Typed {my_text.toPlainText()}')
            my_text.setPlainText("You pressed the button!")


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()


