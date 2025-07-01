# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlpctl.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1135, 957)
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalFrame_2 = QFrame(self.centralwidget)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMouseTracking(True)
        self.horizontalFrame_2.setAutoFillBackground(False)
        self.horizontalFrame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.video_layout = QVBoxLayout()
        self.video_layout.setObjectName(u"video_layout")
        self.label = QLabel(self.horizontalFrame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)

        self.video_layout.addWidget(self.label)

        self.video_frame = QLabel(self.horizontalFrame_2)
        self.video_frame.setObjectName(u"video_frame")

        self.video_layout.addWidget(self.video_frame)

        self.line_2 = QFrame(self.horizontalFrame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.video_layout.addWidget(self.line_2)

        self.line_3 = QFrame(self.horizontalFrame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.video_layout.addWidget(self.line_3)

        self.video_slider = QSlider(self.horizontalFrame_2)
        self.video_slider.setObjectName(u"video_slider")
        self.video_slider.setOrientation(Qt.Horizontal)

        self.video_layout.addWidget(self.video_slider)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play = QPushButton(self.horizontalFrame_2)
        self.play.setObjectName(u"play")

        self.horizontalLayout.addWidget(self.play)

        self.pause = QPushButton(self.horizontalFrame_2)
        self.pause.setObjectName(u"pause")

        self.horizontalLayout.addWidget(self.pause)

        self.replay = QPushButton(self.horizontalFrame_2)
        self.replay.setObjectName(u"replay")

        self.horizontalLayout.addWidget(self.replay)

        self.capture = QPushButton(self.horizontalFrame_2)
        self.capture.setObjectName(u"capture")

        self.horizontalLayout.addWidget(self.capture)

        self.pushButton = QPushButton(self.horizontalFrame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalFrame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.load_bitmask = QPushButton(self.horizontalFrame_2)
        self.load_bitmask.setObjectName(u"load_bitmask")

        self.horizontalLayout.addWidget(self.load_bitmask)


        self.video_layout.addLayout(self.horizontalLayout)

        self.video_layout.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.video_layout)

        self.line = QFrame(self.horizontalFrame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.tool_layout = QVBoxLayout()
        self.tool_layout.setObjectName(u"tool_layout")
        self.tabWidget = QTabWidget(self.horizontalFrame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.video_filters = QWidget()
        self.video_filters.setObjectName(u"video_filters")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video_filters.sizePolicy().hasHeightForWidth())
        self.video_filters.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.video_filters)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.blur_grid = QGridLayout()
        self.blur_grid.setObjectName(u"blur_grid")
        self.checkBox_4 = QCheckBox(self.video_filters)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.blur_grid.addWidget(self.checkBox_4, 0, 1, 1, 1)

        self.label_11 = QLabel(self.video_filters)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setPointSize(8)
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.blur_grid.addWidget(self.label_11, 0, 0, 1, 1)

        self.line_8 = QFrame(self.video_filters)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.blur_grid.addWidget(self.line_8, 1, 0, 1, 2)

        self.horizontalSlider_7 = QSlider(self.video_filters)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.blur_grid.addWidget(self.horizontalSlider_7, 3, 0, 1, 1)

        self.lcdNumber_7 = QLCDNumber(self.video_filters)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")

        self.blur_grid.addWidget(self.lcdNumber_7, 3, 1, 1, 1)

        self.label_12 = QLabel(self.video_filters)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.blur_grid.addWidget(self.label_12, 2, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.blur_grid)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.thresh_grid = QGridLayout()
        self.thresh_grid.setObjectName(u"thresh_grid")
        self.horizontalSlider = QSlider(self.video_filters)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.thresh_grid.addWidget(self.horizontalSlider, 3, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.video_filters)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.thresh_grid.addWidget(self.horizontalSlider_2, 5, 0, 1, 1)

        self.lcdNumber = QLCDNumber(self.video_filters)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.thresh_grid.addWidget(self.lcdNumber, 3, 1, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.video_filters)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.thresh_grid.addWidget(self.lcdNumber_2, 5, 1, 1, 1)

        self.lcdNumber_3 = QLCDNumber(self.video_filters)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")

        self.thresh_grid.addWidget(self.lcdNumber_3, 7, 1, 1, 1)

        self.label_4 = QLabel(self.video_filters)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.thresh_grid.addWidget(self.label_4, 6, 0, 1, 2)

        self.label_3 = QLabel(self.video_filters)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.thresh_grid.addWidget(self.label_3, 4, 0, 1, 2)

        self.label_7 = QLabel(self.video_filters)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.thresh_grid.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_2 = QLabel(self.video_filters)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.thresh_grid.addWidget(self.label_2, 2, 0, 1, 2)

        self.line_6 = QFrame(self.video_filters)
        self.line_6.setObjectName(u"line_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy3)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.thresh_grid.addWidget(self.line_6, 1, 0, 1, 2)

        self.checkBox = QCheckBox(self.video_filters)
        self.checkBox.setObjectName(u"checkBox")

        self.thresh_grid.addWidget(self.checkBox, 0, 1, 1, 1)

        self.horizontalSlider_3 = QSlider(self.video_filters)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.thresh_grid.addWidget(self.horizontalSlider_3, 7, 0, 1, 1)

        self.thresh_grid.setColumnStretch(0, 1)

        self.verticalLayout_3.addLayout(self.thresh_grid)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)

        self.contour_grid = QGridLayout()
        self.contour_grid.setObjectName(u"contour_grid")
        self.horizontalSlider_5 = QSlider(self.video_filters)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.contour_grid.addWidget(self.horizontalSlider_5, 5, 0, 1, 1)

        self.label_6 = QLabel(self.video_filters)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.contour_grid.addWidget(self.label_6, 0, 0, 1, 1)

        self.line_5 = QFrame(self.video_filters)
        self.line_5.setObjectName(u"line_5")
        font4 = QFont()
        font4.setPointSize(26)
        self.line_5.setFont(font4)
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.contour_grid.addWidget(self.line_5, 1, 0, 1, 2)

        self.label_5 = QLabel(self.video_filters)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.contour_grid.addWidget(self.label_5, 2, 0, 1, 2)

        self.label_8 = QLabel(self.video_filters)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font2)

        self.contour_grid.addWidget(self.label_8, 4, 0, 1, 2)

        self.horizontalSlider_4 = QSlider(self.video_filters)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.contour_grid.addWidget(self.horizontalSlider_4, 3, 0, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.video_filters)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")

        self.contour_grid.addWidget(self.lcdNumber_4, 3, 1, 1, 1)

        self.lcdNumber_5 = QLCDNumber(self.video_filters)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")

        self.contour_grid.addWidget(self.lcdNumber_5, 5, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.video_filters)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.contour_grid.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.contour_grid.setColumnStretch(0, 1)

        self.verticalLayout_3.addLayout(self.contour_grid)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_3)

        self.tracking_grid = QGridLayout()
        self.tracking_grid.setObjectName(u"tracking_grid")
        self.checkBox_3 = QCheckBox(self.video_filters)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.tracking_grid.addWidget(self.checkBox_3, 0, 1, 1, 1)

        self.label_9 = QLabel(self.video_filters)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.tracking_grid.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.video_filters)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.tracking_grid.addWidget(self.label_10, 2, 0, 1, 2)

        self.line_7 = QFrame(self.video_filters)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.tracking_grid.addWidget(self.line_7, 1, 0, 1, 2)

        self.horizontalSlider_6 = QSlider(self.video_filters)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)

        self.tracking_grid.addWidget(self.horizontalSlider_6, 3, 0, 1, 1)

        self.lcdNumber_6 = QLCDNumber(self.video_filters)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")

        self.tracking_grid.addWidget(self.lcdNumber_6, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.tracking_grid)

        self.tabWidget.addTab(self.video_filters, "")
        self.drawing = QWidget()
        self.drawing.setObjectName(u"drawing")
        self.verticalLayout_2 = QVBoxLayout(self.drawing)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.drawing, "")

        self.tool_layout.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.tool_layout)

        self.horizontalLayout_2.setStretch(2, 4)

        self.verticalLayout.addWidget(self.horizontalFrame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.video_frame.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.replay.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect Camera", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect DLP", None))
        self.checkBox_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresh Constant", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresh Area", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresholding", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max Val", None))
        self.checkBox.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Contour Detection", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Min Area", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Circularity", None))
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bubble Tracking", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Min Position Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.video_filters), QCoreApplication.translate("MainWindow", u"Video Filters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drawing), QCoreApplication.translate("MainWindow", u"Drawing", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

