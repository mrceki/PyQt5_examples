# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 568)
        self.output_label = QtWidgets.QLabel(MainWindow)
        self.output_label.setGeometry(QtCore.QRect(10, 20, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.output_label.setFont(font)
        self.output_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_label.setScaledContents(False)
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.percentButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.clearButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("C"))
        self.clearButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.arrowButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.seven = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("7"))
        self.seven.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("8"))
        self.eight.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("9"))
        self.nine.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.multipleButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("*"))
        self.multipleButton.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multipleButton.setFont(font)
        self.multipleButton.setObjectName("multipleButton")
        self.four = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("4"))
        self.four.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("5"))
        self.five.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("6"))
        self.six.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.minusButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.one = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("1"))
        self.one.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("2"))
        self.two.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("3"))
        self.three.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.plusButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(280, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.plus_minusButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.plus_minus_it())
        self.plus_minusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plus_minusButton.setFont(font)
        self.plus_minusButton.setObjectName("plus_minusButton")
        self.zero = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.press_it("0"))
        self.zero.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.dotButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.dot_it())
        self.dotButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dotButton.setFont(font)
        self.dotButton.setObjectName("dotButton")
        self.equalButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(280, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def dot_it(self):
        screen = self.output_label.text()
        if "." in screen:
            pass
        else:
            self.output_label.setText(f'{screen}.')
    
    def remove_it(self):
        screen = self.output_label.text()
        #REMOVE LAST ITEM IN LIST
        screen = screen[:-1]
        #output back screen
        self.output_label.setText(screen)

    def press_it(self, pressed):
        if pressed == "C":
            self.output_label.setText("0")
        else:#0 ile başlıyor mu?
            if self.output_label.text() == "0":
                self.output_label.setText("")
            self.output_label.setText(f'{self.output_label.text()}{pressed}')

    def plus_minus_it(self):
        screen = self.output_label.text()
        if "-" in screen:
            self.output_label.setText(screen.replace("-",""))
        else:
            self.output_label.setText(f'-{screen}')

    # Math
    def math_it(self):
        screen = self.output_label.text()
        #do the math
        try:
            answer = eval(screen)
            #output
            self.output_label.setText(str(answer))
        except:
            self.output_label.setText("ERROR!!")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.multipleButton.setText(_translate("MainWindow", "x"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.plus_minusButton.setText(_translate("MainWindow", "+/-"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
