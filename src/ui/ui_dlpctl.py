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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(902, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QSize(30, 30))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
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
        self.video_frame = QLabel(self.horizontalFrame_2)
        self.video_frame.setObjectName(u"video_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video_frame.sizePolicy().hasHeightForWidth())
        self.video_frame.setSizePolicy(sizePolicy1)

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


        self.video_layout.addLayout(self.horizontalLayout)


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
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.video_filters = QWidget()
        self.video_filters.setObjectName(u"video_filters")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.video_filters.sizePolicy().hasHeightForWidth())
        self.video_filters.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.video_filters)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.blur_grid = QGridLayout()
        self.blur_grid.setObjectName(u"blur_grid")
        self.checkBox = QCheckBox(self.video_filters)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy3)

        self.blur_grid.addWidget(self.checkBox, 0, 1, 1, 1)

        self.line_8 = QFrame(self.video_filters)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.blur_grid.addWidget(self.line_8, 1, 0, 1, 2)

        self.label_11 = QLabel(self.video_filters)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(8)
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.blur_grid.addWidget(self.label_11, 0, 0, 1, 1)

        self.horizontalSlider_7 = QSlider(self.video_filters)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.horizontalSlider_7.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_7.setSizePolicy(sizePolicy4)
        self.horizontalSlider_7.setMinimum(1)
        self.horizontalSlider_7.setSingleStep(2)
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.blur_grid.addWidget(self.horizontalSlider_7, 3, 0, 1, 1)

        self.label_12 = QLabel(self.video_filters)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.blur_grid.addWidget(self.label_12, 2, 0, 1, 2)

        self.spinBox = QSpinBox(self.video_filters)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy4.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy4)
        self.spinBox.setFont(font2)
        self.spinBox.setMaximum(100)

        self.blur_grid.addWidget(self.spinBox, 3, 1, 1, 1)

        self.blur_grid.setColumnStretch(0, 3)
        self.blur_grid.setColumnStretch(1, 1)

        self.verticalLayout_3.addLayout(self.blur_grid)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.thresh_grid = QGridLayout()
        self.thresh_grid.setObjectName(u"thresh_grid")
        self.horizontalSlider_2 = QSlider(self.video_filters)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        sizePolicy4.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy4)
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.thresh_grid.addWidget(self.horizontalSlider_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self.video_filters)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.thresh_grid.addWidget(self.label_3, 2, 0, 1, 2)

        self.horizontalSlider_3 = QSlider(self.video_filters)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        sizePolicy4.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy4)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.thresh_grid.addWidget(self.horizontalSlider_3, 5, 0, 1, 1)

        self.line_6 = QFrame(self.video_filters)
        self.line_6.setObjectName(u"line_6")
        sizePolicy5.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy5)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.thresh_grid.addWidget(self.line_6, 1, 0, 1, 2)

        self.label_7 = QLabel(self.video_filters)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.thresh_grid.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_4 = QLabel(self.video_filters)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.thresh_grid.addWidget(self.label_4, 4, 0, 1, 2)

        self.checkBox_2 = QCheckBox(self.video_filters)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.thresh_grid.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.video_filters)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy4.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy4)
        self.spinBox_2.setFont(font2)
        self.spinBox_2.setMinimum(1)

        self.thresh_grid.addWidget(self.spinBox_2, 3, 1, 1, 1)

        self.spinBox_3 = QSpinBox(self.video_filters)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy4.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy4)
        self.spinBox_3.setFont(font2)

        self.thresh_grid.addWidget(self.spinBox_3, 5, 1, 1, 1)

        self.thresh_grid.setColumnStretch(0, 3)
        self.thresh_grid.setColumnStretch(1, 1)

        self.verticalLayout_3.addLayout(self.thresh_grid)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)

        self.contour_grid = QGridLayout()
        self.contour_grid.setObjectName(u"contour_grid")
        self.label_6 = QLabel(self.video_filters)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

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
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.contour_grid.addWidget(self.label_5, 2, 0, 1, 2)

        self.label_8 = QLabel(self.video_filters)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.contour_grid.addWidget(self.label_8, 4, 0, 1, 2)

        self.horizontalSlider_4 = QSlider(self.video_filters)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        sizePolicy4.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy4)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.contour_grid.addWidget(self.horizontalSlider_4, 3, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.video_filters)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.contour_grid.addWidget(self.checkBox_3, 0, 1, 1, 1)

        self.spinBox_4 = QSpinBox(self.video_filters)
        self.spinBox_4.setObjectName(u"spinBox_4")
        sizePolicy4.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy4)
        self.spinBox_4.setFont(font2)

        self.contour_grid.addWidget(self.spinBox_4, 3, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.video_filters)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy4.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy4)
        self.doubleSpinBox.setFont(font2)
        self.doubleSpinBox.setMinimum(0.010000000000000)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.010000000000000)

        self.contour_grid.addWidget(self.doubleSpinBox, 5, 0, 1, 2)

        self.contour_grid.setColumnStretch(0, 3)
        self.contour_grid.setColumnStretch(1, 1)

        self.verticalLayout_3.addLayout(self.contour_grid)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_3)

        self.tracking_grid = QGridLayout()
        self.tracking_grid.setObjectName(u"tracking_grid")
        self.checkBox_4 = QCheckBox(self.video_filters)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.tracking_grid.addWidget(self.checkBox_4, 0, 1, 1, 1)

        self.label_9 = QLabel(self.video_filters)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.tracking_grid.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.video_filters)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.tracking_grid.addWidget(self.label_10, 2, 0, 1, 2)

        self.line_7 = QFrame(self.video_filters)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.tracking_grid.addWidget(self.line_7, 1, 0, 1, 2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.video_filters)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        sizePolicy5.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy5)
        self.doubleSpinBox_2.setFont(font2)
        self.doubleSpinBox_2.setMinimum(0.500000000000000)
        self.doubleSpinBox_2.setMaximum(99.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.500000000000000)

        self.tracking_grid.addWidget(self.doubleSpinBox_2, 3, 0, 1, 2)

        self.tracking_grid.setColumnStretch(0, 3)
        self.tracking_grid.setColumnStretch(1, 1)

        self.verticalLayout_3.addLayout(self.tracking_grid)

        self.tabWidget.addTab(self.video_filters, "")

        self.tool_layout.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.tool_layout)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.horizontalFrame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 902, 21))
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
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.video_frame.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.replay.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect Camera", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect DLP", None))
        self.checkBox.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresh Area", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresh", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresh Constant", None))
        self.checkBox_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Contour Detection", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Min Area", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Circularity", None))
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bubble Tracking", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Min Position Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.video_filters), QCoreApplication.translate("MainWindow", u"Video Filters", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

