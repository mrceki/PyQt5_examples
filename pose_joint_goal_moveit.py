# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pose_joint_goal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from threading import Thread
import sys
import rclpy
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.node import Node

from pymoveit2 import MoveIt2
from pymoveit2.robots import sr80
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 201)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        font.setItalic(False)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setSuffix(" m")
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMinimum(-3.0)
        self.doubleSpinBox.setMaximum(3.0)
        self.doubleSpinBox.setSingleStep(0.005)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_2.addWidget(self.doubleSpinBox, 0, 0, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        font.setItalic(False)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setSuffix("")
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setMinimum(-3.0)
        self.doubleSpinBox_4.setMaximum(3.0)
        self.doubleSpinBox_4.setSingleStep(0.005)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 0, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        font.setItalic(False)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setSuffix(" m")
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setMinimum(-3.0)
        self.doubleSpinBox_2.setMaximum(3.0)
        self.doubleSpinBox_2.setSingleStep(0.005)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_2.addWidget(self.doubleSpinBox_2, 1, 0, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        font.setItalic(False)
        self.doubleSpinBox_5.setFont(font)
        self.doubleSpinBox_5.setSuffix("")
        self.doubleSpinBox_5.setDecimals(3)
        self.doubleSpinBox_5.setMinimum(-3.0)
        self.doubleSpinBox_5.setMaximum(3.0)
        self.doubleSpinBox_5.setSingleStep(0.005)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 1, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        font.setItalic(False)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setSuffix(" m")
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setMinimum(-3.0)
        self.doubleSpinBox_3.setMaximum(3.0)
        self.doubleSpinBox_3.setSingleStep(0.005)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_2.addWidget(self.doubleSpinBox_3, 2, 0, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        font.setItalic(False)
        self.doubleSpinBox_6.setFont(font)
        self.doubleSpinBox_6.setSuffix("")
        self.doubleSpinBox_6.setDecimals(3)
        self.doubleSpinBox_6.setMinimum(-3.0)
        self.doubleSpinBox_6.setMaximum(3.0)
        self.doubleSpinBox_6.setSingleStep(0.005)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_2.addWidget(self.doubleSpinBox_6, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab, clicked= lambda: self.main())
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(12)
        font.setItalic(False)
        self.doubleSpinBox_7.setFont(font)
        self.doubleSpinBox_7.setSuffix("")
        self.doubleSpinBox_7.setDecimals(3)
        self.doubleSpinBox_7.setMinimum(-3.0)
        self.doubleSpinBox_7.setMaximum(3.0)
        self.doubleSpinBox_7.setSingleStep(0.005)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_2.addWidget(self.doubleSpinBox_7, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_3.setMinimum(-100)
        self.spinBox_3.setMaximum(100)
        self.spinBox_3.setSingleStep(1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_4.addWidget(self.spinBox_3, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy)
        self.horizontalSlider_3.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: rgb(255, 140, 0);\n"
"    border: 0px solid #424242; \n"
"    height: 6px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: white; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 8px; \n"
"}\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 204, 116)\n"
"}")
        self.horizontalSlider_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider_3.setMinimum(-100)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setPageStep(0)
        self.horizontalSlider_3.setTracking(False)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setInvertedAppearance(False)
        self.horizontalSlider_3.setInvertedControls(False)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_3.setTickInterval(0)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_4.addWidget(self.horizontalSlider_3, 2, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setMinimum(-100)
        self.spinBox.setMaximum(100)
        self.spinBox.setSingleStep(1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_4.addWidget(self.spinBox, 0, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: rgb(255, 140, 0);\n"
"    border: 0px solid #424242; \n"
"    height: 6px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: white; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 8px; \n"
"}\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 204, 116)\n"
"}")
        self.horizontalSlider.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(0)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_4.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setMinimum(-100)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_4.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: rgb(255, 140, 0);\n"
"    border: 0px solid #424242; \n"
"    height: 6px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: white; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 8px; \n"
"}\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 204, 116)\n"
"}")
        self.horizontalSlider_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider_2.setMinimum(-100)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setPageStep(0)
        self.horizontalSlider_2.setTracking(False)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setInvertedAppearance(False)
        self.horizontalSlider_2.setInvertedControls(False)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_2.setTickInterval(0)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_4.addWidget(self.horizontalSlider_2, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_4.setMinimum(-100)
        self.spinBox_4.setMaximum(100)
        self.spinBox_4.setSingleStep(1)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_5.addWidget(self.spinBox_4, 0, 0, 1, 1)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_6.setSizePolicy(sizePolicy)
        self.horizontalSlider_6.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: rgb(255, 140, 0);\n"
"    border: 0px solid #424242; \n"
"    height: 6px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: white; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 8px; \n"
"}\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 204, 116)\n"
"}")
        self.horizontalSlider_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider_6.setMinimum(-100)
        self.horizontalSlider_6.setMaximum(100)
        self.horizontalSlider_6.setPageStep(0)
        self.horizontalSlider_6.setTracking(False)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setInvertedAppearance(False)
        self.horizontalSlider_6.setInvertedControls(False)
        self.horizontalSlider_6.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_6.setTickInterval(0)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout_5.addWidget(self.horizontalSlider_6, 2, 1, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy)
        self.horizontalSlider_4.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: rgb(255, 140, 0);\n"
"    border: 0px solid #424242; \n"
"    height: 6px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: white; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 8px; \n"
"}\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 204, 116)\n"
"}")
        self.horizontalSlider_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider_4.setMinimum(-100)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setPageStep(0)
        self.horizontalSlider_4.setTracking(False)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setInvertedAppearance(False)
        self.horizontalSlider_4.setInvertedControls(False)
        self.horizontalSlider_4.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_4.setTickInterval(0)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout_5.addWidget(self.horizontalSlider_4, 0, 1, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_6.setMinimum(-100)
        self.spinBox_6.setMaximum(100)
        self.spinBox_6.setSingleStep(1)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_5.addWidget(self.spinBox_6, 2, 0, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_5.setMinimum(-100)
        self.spinBox_5.setMaximum(100)
        self.spinBox_5.setSingleStep(1)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_5.addWidget(self.spinBox_5, 1, 0, 1, 1)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_5.setSizePolicy(sizePolicy)
        self.horizontalSlider_5.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: rgb(255, 140, 0);\n"
"    border: 0px solid #424242; \n"
"    height: 6px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: white; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 8px; \n"
"}\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 204, 116)\n"
"}")
        self.horizontalSlider_5.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider_5.setMinimum(-100)
        self.horizontalSlider_5.setMaximum(100)
        self.horizontalSlider_5.setPageStep(0)
        self.horizontalSlider_5.setTracking(False)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setInvertedAppearance(False)
        self.horizontalSlider_5.setInvertedControls(False)
        self.horizontalSlider_5.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_5.setTickInterval(0)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout_5.addWidget(self.horizontalSlider_5, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Lt")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_8.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.horizontalSlider.sliderMoved['int'].connect(self.spinBox.setValue) # type: ignore
        #self.horizontalSlider.sliderReleased.connect(self.slider_zero) # type: ignore
        self.spinBox.valueChanged['int'].connect(self.horizontalSlider.setValue) # type: ignore
        self.horizontalSlider_2.sliderMoved['int'].connect(self.spinBox_2.setValue) # type: ignore
        #self.horizontalSlider_2.sliderReleased.connect(self.slider_zero_2) # type: ignore
        self.spinBox_2.valueChanged['int'].connect(self.horizontalSlider_2.setValue) # type: ignore
        self.horizontalSlider_3.sliderMoved['int'].connect(self.spinBox_3.setValue) # type: ignore
        #self.horizontalSlider_3.sliderReleased.connect(self.slider_zero_3) # type: ignore
        self.spinBox_3.valueChanged['int'].connect(self.horizontalSlider_3.setValue) # type: ignore
        self.horizontalSlider_4.sliderMoved['int'].connect(self.spinBox_4.setValue) # type: ignore
        #self.horizontalSlider_4.sliderReleased.connect(self.slider_zero_4) # type: ignore
        self.horizontalSlider_5.sliderMoved['int'].connect(self.spinBox_5.setValue) # type: ignore
        #self.horizontalSlider_5.sliderReleased.connect(self.slider_zero_5) # type: ignore
        self.horizontalSlider_6.sliderMoved['int'].connect(self.spinBox_6.setValue) # type: ignore
        #self.horizontalSlider_6.sliderReleased.connect(self.slider_zero_6) # type: ignore
        self.spinBox_6.valueChanged['int'].connect(self.horizontalSlider_6.setValue) # type: ignore
        self.spinBox_5.valueChanged['int'].connect(self.horizontalSlider_5.setValue) # type: ignore
        self.spinBox_4.valueChanged['int'].connect(self.horizontalSlider_4.setValue) # type: ignore
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.doubleSpinBox.setPrefix(_translate("MainWindow", "x = "))
        self.doubleSpinBox_4.setPrefix(_translate("MainWindow", "x = "))
        self.doubleSpinBox_2.setPrefix(_translate("MainWindow", "y = "))
        self.doubleSpinBox_5.setPrefix(_translate("MainWindow", "y = "))
        self.doubleSpinBox_3.setPrefix(_translate("MainWindow", "z = "))
        self.doubleSpinBox_6.setPrefix(_translate("MainWindow", "z = "))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.doubleSpinBox_7.setPrefix(_translate("MainWindow", "w = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pose"))
        self.label_2.setText(_translate("MainWindow", "L2"))
        self.label_3.setText(_translate("MainWindow", "L3"))
        self.label.setText(_translate("MainWindow", "L1"))
        self.label_7.setText(_translate("MainWindow", "L6"))
        self.label_6.setText(_translate("MainWindow", "L5"))
        self.label_5.setText(_translate("MainWindow", "L4"))
        self.pushButton_2.setText(_translate("MainWindow", "Go"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Joint"))
    def slider_zero(self):
        if self.horizontalSlider.value != 0:
                self.horizontalSlider.setValue(0)
                self.spinBox.setValue(0)
    def slider_zero_2(self):
        if self.horizontalSlider_2.value != 0:
                self.horizontalSlider_2.setValue(0)
                self.spinBox_2.setValue(0)
    def slider_zero_3(self):
        if self.horizontalSlider_3.value != 0:
                self.horizontalSlider_3.setValue(0)
                self.spinBox_3.setValue(0)
    def slider_zero_4(self):
        if self.horizontalSlider_4.value != 0:
                self.horizontalSlider_4.setValue(0)
                self.spinBox_4.setValue(0)
    def slider_zero_5(self):
        if self.horizontalSlider_5.value != 0:
                self.horizontalSlider_5.setValue(0)
                self.spinBox_5.setValue(0)
    def slider_zero_6(self):
        if self.horizontalSlider_6.value != 0:
                self.horizontalSlider_6.setValue(0)
                self.spinBox_6.setValue(0)

    def main(self, args=None):

        rclpy.init(args=args)#args=args

        # Create node for this example
        node = Node("ex_pose_goal")
        # Create callback group that allows execution of callbacks in parallel without restrictions
        callback_group = ReentrantCallbackGroup()
        # Create MoveIt 2 interface
        moveit2 = MoveIt2(
                node=node,
                joint_names=sr80.joint_names(),
                base_link_name=sr80.base_link_name(),
                end_effector_name=sr80.end_effector_name(),
                group_name=sr80.MOVE_GROUP_ARM,
                callback_group=callback_group,
        )

        # Spin the node in background thread(s)
        executor = rclpy.executors.MultiThreadedExecutor(2)
        executor.add_node(node)
        executor_thread = Thread(target=executor.spin, daemon=True, args=())
        executor_thread.start()

        # Get parameters
        position = [self.doubleSpinBox.value(), self.doubleSpinBox_2.value(), self.doubleSpinBox_3.value()] #node.get_parameter("position").get_parameter_value().double_array_value
        quat_xyzw = [self.doubleSpinBox_4.value(), self.doubleSpinBox_5.value(), self.doubleSpinBox_6.value(), self.doubleSpinBox_7.value()] #node.get_parameter("quat_xyzw").get_parameter_value().double_array_value
        #cartesian = node.get_parameter("cartesian").get_parameter_value().bool_value

        # Move to pose
        node.get_logger().info(
                f"Moving to {{position: {list(position)}, quat_xyzw: {list(quat_xyzw)}}}"
        )
        moveit2.move_to_pose(position=position, quat_xyzw=quat_xyzw)
        moveit2.wait_until_executed()
        rclpy.shutdown()
        #exit(0)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #ui.main()
    sys.exit(app.exec_())
