# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlpctlpVzuiJ.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from widgets import ClickableLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(976, 845)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(999999, 999999))
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
        self.horizontalFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.video_layout = QVBoxLayout()
        self.video_layout.setObjectName(u"video_layout")
        self.video_frame = ClickableLabel(self.horizontalFrame_2)
        self.video_frame.setObjectName(u"video_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video_frame.sizePolicy().hasHeightForWidth())
        self.video_frame.setSizePolicy(sizePolicy1)
        self.video_frame.setMinimumSize(QSize(0, 0))
        self.video_frame.setMouseTracking(False)
        self.video_frame.setScaledContents(False)
        self.video_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.video_layout.addWidget(self.video_frame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.label_13 = QLabel(self.horizontalFrame_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.exposure_slider = QSlider(self.horizontalFrame_2)
        self.exposure_slider.setObjectName(u"exposure_slider")
        self.exposure_slider.setMinimum(100)
        self.exposure_slider.setMaximum(100000)
        self.exposure_slider.setSingleStep(0)
        self.exposure_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.exposure_slider)

        self.exposure_spinbox = QSpinBox(self.horizontalFrame_2)
        self.exposure_spinbox.setObjectName(u"exposure_spinbox")
        self.exposure_spinbox.setMinimum(100)
        self.exposure_spinbox.setMaximum(100000)
        self.exposure_spinbox.setSingleStep(50)
        self.exposure_spinbox.setValue(1000)

        self.horizontalLayout_3.addWidget(self.exposure_spinbox)


        self.video_layout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play = QPushButton(self.horizontalFrame_2)
        self.play.setObjectName(u"play")
        icon = QIcon(QIcon.fromTheme(u"media-playback-start"))
        self.play.setIcon(icon)

        self.horizontalLayout.addWidget(self.play)

        self.pause = QPushButton(self.horizontalFrame_2)
        self.pause.setObjectName(u"pause")
        icon1 = QIcon(QIcon.fromTheme(u"media-playback-pause"))
        self.pause.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pause)

        self.replay = QPushButton(self.horizontalFrame_2)
        self.replay.setObjectName(u"replay")
        icon2 = QIcon(QIcon.fromTheme(u"media-playlist-repeat"))
        self.replay.setIcon(icon2)

        self.horizontalLayout.addWidget(self.replay)

        self.capture = QPushButton(self.horizontalFrame_2)
        self.capture.setObjectName(u"capture")
        icon3 = QIcon(QIcon.fromTheme(u"media-record"))
        self.capture.setIcon(icon3)

        self.horizontalLayout.addWidget(self.capture)

        self.load_bitmask = QPushButton(self.horizontalFrame_2)
        self.load_bitmask.setObjectName(u"load_bitmask")
        icon4 = QIcon(QIcon.fromTheme(u"document-open"))
        self.load_bitmask.setIcon(icon4)

        self.horizontalLayout.addWidget(self.load_bitmask)


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
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.video_filters_tab = QWidget()
        self.video_filters_tab.setObjectName(u"video_filters_tab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.video_filters_tab.sizePolicy().hasHeightForWidth())
        self.video_filters_tab.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.video_filters_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.video_filters_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -13, 269, 703))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.analysis_button = QPushButton(self.scrollAreaWidgetContents)
        self.analysis_button.setObjectName(u"analysis_button")
        self.analysis_button.setCheckable(True)

        self.verticalLayout_4.addWidget(self.analysis_button)

        self.show_filters = QPushButton(self.scrollAreaWidgetContents)
        self.show_filters.setObjectName(u"show_filters")
        self.show_filters.setCheckable(True)
        self.show_filters.setChecked(True)

        self.verticalLayout_4.addWidget(self.show_filters)

        self.blur_grid = QGridLayout()
        self.blur_grid.setObjectName(u"blur_grid")
        self.blur_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.blur_checkbox.setObjectName(u"blur_checkbox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.blur_checkbox.sizePolicy().hasHeightForWidth())
        self.blur_checkbox.setSizePolicy(sizePolicy3)

        self.blur_grid.addWidget(self.blur_checkbox, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.label_12.setFont(font1)

        self.blur_grid.addWidget(self.label_12, 2, 0, 1, 2)

        self.blur_slider = QSlider(self.scrollAreaWidgetContents)
        self.blur_slider.setObjectName(u"blur_slider")
        sizePolicy4.setHeightForWidth(self.blur_slider.sizePolicy().hasHeightForWidth())
        self.blur_slider.setSizePolicy(sizePolicy4)
        self.blur_slider.setMinimum(1)
        self.blur_slider.setSingleStep(2)
        self.blur_slider.setOrientation(Qt.Orientation.Horizontal)

        self.blur_grid.addWidget(self.blur_slider, 3, 0, 1, 1)

        self.blur_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.blur_spinbox.setObjectName(u"blur_spinbox")
        sizePolicy3.setHeightForWidth(self.blur_spinbox.sizePolicy().hasHeightForWidth())
        self.blur_spinbox.setSizePolicy(sizePolicy3)
        self.blur_spinbox.setFont(font1)
        self.blur_spinbox.setMaximum(100)

        self.blur_grid.addWidget(self.blur_spinbox, 3, 1, 1, 1)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.blur_grid.addWidget(self.line_8, 1, 0, 1, 2)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.label_11.setFont(font2)

        self.blur_grid.addWidget(self.label_11, 0, 0, 1, 1)

        self.blur_grid.setColumnStretch(0, 2)
        self.blur_grid.setColumnStretch(1, 1)

        self.verticalLayout_4.addLayout(self.blur_grid)

        self.thresh_grid = QGridLayout()
        self.thresh_grid.setObjectName(u"thresh_grid")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font1)

        self.thresh_grid.addWidget(self.label_3, 3, 0, 1, 2)

        self.thresh_area_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.thresh_area_spinbox.setObjectName(u"thresh_area_spinbox")
        sizePolicy3.setHeightForWidth(self.thresh_area_spinbox.sizePolicy().hasHeightForWidth())
        self.thresh_area_spinbox.setSizePolicy(sizePolicy3)
        self.thresh_area_spinbox.setFont(font1)
        self.thresh_area_spinbox.setMinimum(1)

        self.thresh_grid.addWidget(self.thresh_area_spinbox, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.thresh_grid.addItem(self.horizontalSpacer_2, 7, 0, 1, 1)

        self.thresh_const_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.thresh_const_spinbox.setObjectName(u"thresh_const_spinbox")
        sizePolicy3.setHeightForWidth(self.thresh_const_spinbox.sizePolicy().hasHeightForWidth())
        self.thresh_const_spinbox.setSizePolicy(sizePolicy3)
        self.thresh_const_spinbox.setFont(font1)

        self.thresh_grid.addWidget(self.thresh_const_spinbox, 6, 1, 1, 1)

        self.thresh_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.thresh_checkbox.setObjectName(u"thresh_checkbox")
        sizePolicy3.setHeightForWidth(self.thresh_checkbox.sizePolicy().hasHeightForWidth())
        self.thresh_checkbox.setSizePolicy(sizePolicy3)

        self.thresh_grid.addWidget(self.thresh_checkbox, 1, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.contour_grid = QGridLayout()
        self.contour_grid.setObjectName(u"contour_grid")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setFont(font1)

        self.contour_grid.addWidget(self.label_8, 4, 0, 1, 2)

        self.circularity_spinbox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.circularity_spinbox.setObjectName(u"circularity_spinbox")
        sizePolicy4.setHeightForWidth(self.circularity_spinbox.sizePolicy().hasHeightForWidth())
        self.circularity_spinbox.setSizePolicy(sizePolicy4)
        self.circularity_spinbox.setFont(font1)
        self.circularity_spinbox.setMinimum(0.010000000000000)
        self.circularity_spinbox.setMaximum(1.000000000000000)
        self.circularity_spinbox.setSingleStep(0.010000000000000)

        self.contour_grid.addWidget(self.circularity_spinbox, 5, 0, 1, 2)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        self.line_5.setFont(font3)
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.contour_grid.addWidget(self.line_5, 1, 0, 1, 2)

        self.contour_slider = QSlider(self.scrollAreaWidgetContents)
        self.contour_slider.setObjectName(u"contour_slider")
        sizePolicy4.setHeightForWidth(self.contour_slider.sizePolicy().hasHeightForWidth())
        self.contour_slider.setSizePolicy(sizePolicy4)
        self.contour_slider.setOrientation(Qt.Orientation.Horizontal)

        self.contour_grid.addWidget(self.contour_slider, 3, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.contour_grid.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setFont(font1)

        self.contour_grid.addWidget(self.label_5, 2, 0, 1, 2)

        self.contour_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.contour_spinbox.setObjectName(u"contour_spinbox")
        sizePolicy3.setHeightForWidth(self.contour_spinbox.sizePolicy().hasHeightForWidth())
        self.contour_spinbox.setSizePolicy(sizePolicy3)
        self.contour_spinbox.setFont(font1)

        self.contour_grid.addWidget(self.contour_spinbox, 3, 1, 1, 1)

        self.contour_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.contour_checkbox.setObjectName(u"contour_checkbox")
        sizePolicy3.setHeightForWidth(self.contour_checkbox.sizePolicy().hasHeightForWidth())
        self.contour_checkbox.setSizePolicy(sizePolicy3)

        self.contour_grid.addWidget(self.contour_checkbox, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.contour_grid.setColumnStretch(0, 2)

        self.thresh_grid.addLayout(self.contour_grid, 8, 0, 1, 1)

        self.thresh_area_slider = QSlider(self.scrollAreaWidgetContents)
        self.thresh_area_slider.setObjectName(u"thresh_area_slider")
        sizePolicy4.setHeightForWidth(self.thresh_area_slider.sizePolicy().hasHeightForWidth())
        self.thresh_area_slider.setSizePolicy(sizePolicy4)
        self.thresh_area_slider.setMinimum(1)
        self.thresh_area_slider.setOrientation(Qt.Orientation.Horizontal)

        self.thresh_grid.addWidget(self.thresh_area_slider, 4, 0, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        sizePolicy5.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy5)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.thresh_grid.addWidget(self.line_6, 2, 0, 1, 2)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font1)

        self.thresh_grid.addWidget(self.label_4, 5, 0, 1, 2)

        self.thresh_const_slider = QSlider(self.scrollAreaWidgetContents)
        self.thresh_const_slider.setObjectName(u"thresh_const_slider")
        sizePolicy4.setHeightForWidth(self.thresh_const_slider.sizePolicy().hasHeightForWidth())
        self.thresh_const_slider.setSizePolicy(sizePolicy4)
        self.thresh_const_slider.setOrientation(Qt.Orientation.Horizontal)

        self.thresh_grid.addWidget(self.thresh_const_slider, 6, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.thresh_grid.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.thresh_grid.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.thresh_grid.setColumnStretch(0, 2)

        self.verticalLayout_4.addLayout(self.thresh_grid)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_3)

        self.tracking_grid = QGridLayout()
        self.tracking_grid.setObjectName(u"tracking_grid")
        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.tracking_grid.addWidget(self.line_7, 1, 0, 1, 2)

        self.tracking_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.tracking_checkbox.setObjectName(u"tracking_checkbox")
        sizePolicy5.setHeightForWidth(self.tracking_checkbox.sizePolicy().hasHeightForWidth())
        self.tracking_checkbox.setSizePolicy(sizePolicy5)

        self.tracking_grid.addWidget(self.tracking_checkbox, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.tracking_min_error_spinbox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.tracking_min_error_spinbox.setObjectName(u"tracking_min_error_spinbox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tracking_min_error_spinbox.sizePolicy().hasHeightForWidth())
        self.tracking_min_error_spinbox.setSizePolicy(sizePolicy6)
        self.tracking_min_error_spinbox.setFont(font1)
        self.tracking_min_error_spinbox.setMinimum(0.500000000000000)
        self.tracking_min_error_spinbox.setMaximum(99.000000000000000)
        self.tracking_min_error_spinbox.setSingleStep(0.500000000000000)

        self.tracking_grid.addWidget(self.tracking_min_error_spinbox, 3, 0, 1, 2)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setFont(font2)

        self.tracking_grid.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setFont(font1)

        self.tracking_grid.addWidget(self.label_10, 2, 0, 1, 2)

        self.tracking_grid.setColumnStretch(0, 2)

        self.verticalLayout_4.addLayout(self.tracking_grid)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_4)

        self.selection_grid = QGridLayout()
        self.selection_grid.setObjectName(u"selection_grid")
        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.selection_grid.addWidget(self.line_4, 1, 0, 1, 2)

        self.selection_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.selection_checkbox.setObjectName(u"selection_checkbox")
        sizePolicy5.setHeightForWidth(self.selection_checkbox.sizePolicy().hasHeightForWidth())
        self.selection_checkbox.setSizePolicy(sizePolicy5)

        self.selection_grid.addWidget(self.selection_checkbox, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.clear_all = QPushButton(self.scrollAreaWidgetContents)
        self.clear_all.setObjectName(u"clear_all")
        self.clear_all.setFont(font2)

        self.selection_grid.addWidget(self.clear_all, 2, 0, 1, 2)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.selection_grid.addWidget(self.label, 0, 0, 1, 1)

        self.selection_grid.setColumnStretch(0, 2)

        self.verticalLayout_4.addLayout(self.selection_grid)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_5)

        self.pid_grid = QGridLayout()
        self.pid_grid.setObjectName(u"pid_grid")
        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.pid_grid.addWidget(self.line_2, 1, 0, 1, 2)

        self.pid_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.pid_checkbox.setObjectName(u"pid_checkbox")
        sizePolicy5.setHeightForWidth(self.pid_checkbox.sizePolicy().hasHeightForWidth())
        self.pid_checkbox.setSizePolicy(sizePolicy5)
        self.pid_checkbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.pid_grid.addWidget(self.pid_checkbox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.pid_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.pid_grid.setColumnStretch(0, 2)

        self.verticalLayout_4.addLayout(self.pid_grid)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.mouse_pos = QLabel(self.video_filters_tab)
        self.mouse_pos.setObjectName(u"mouse_pos")
        sizePolicy4.setHeightForWidth(self.mouse_pos.sizePolicy().hasHeightForWidth())
        self.mouse_pos.setSizePolicy(sizePolicy4)
        self.mouse_pos.setFont(font2)
        self.mouse_pos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.mouse_pos)

        self.tabWidget.addTab(self.video_filters_tab, "")
        self.devices_tab = QWidget()
        self.devices_tab.setObjectName(u"devices_tab")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.devices_tab.sizePolicy().hasHeightForWidth())
        self.devices_tab.setSizePolicy(sizePolicy7)
        self.verticalLayout_2 = QVBoxLayout(self.devices_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.devices_tab)
        self.pushButton.setObjectName(u"pushButton")
        icon5 = QIcon(QIcon.fromTheme(u"camera-photo"))
        self.pushButton.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.devices_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon6 = QIcon(QIcon.fromTheme(u"camera-video"))
        self.pushButton_2.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.device_list = QListWidget(self.devices_tab)
        self.device_list.setObjectName(u"device_list")

        self.verticalLayout_2.addWidget(self.device_list)

        self.refresh_devices = QPushButton(self.devices_tab)
        self.refresh_devices.setObjectName(u"refresh_devices")
        icon7 = QIcon(QIcon.fromTheme(u"system-reboot"))
        self.refresh_devices.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.refresh_devices)

        self.tabWidget.addTab(self.devices_tab, "")
        self.afg_tab = QWidget()
        self.afg_tab.setObjectName(u"afg_tab")
        self.verticalLayout_4 = QVBoxLayout(self.afg_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_3 = QPushButton(self.afg_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        self.pushButton_3.setIcon(icon8)

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.scrollArea = QScrollArea(self.afg_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy8)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 237, 225))
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.waveform_grid = QGridLayout()
        self.waveform_grid.setObjectName(u"waveform_grid")
        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.waveform_grid.addWidget(self.line_3, 1, 0, 1, 1)

        self.waveform_combobox = QComboBox(self.scrollAreaWidgetContents)
        self.waveform_combobox.addItem("")
        self.waveform_combobox.addItem("")
        self.waveform_combobox.addItem("")
        self.waveform_combobox.addItem("")
        self.waveform_combobox.addItem("")
        self.waveform_combobox.addItem("")
        self.waveform_combobox.setObjectName(u"waveform_combobox")
        self.waveform_combobox.setFont(font2)

        self.waveform_grid.addWidget(self.waveform_combobox, 3, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.waveform_grid.addWidget(self.label_14, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)

        self.waveform_grid.addWidget(self.pushButton_4, 4, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.waveform_grid)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_6)

        self.freq_grid = QGridLayout()
        self.freq_grid.setObjectName(u"freq_grid")
        self.freq_spinbox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.freq_spinbox.setObjectName(u"freq_spinbox")
        sizePolicy4.setHeightForWidth(self.freq_spinbox.sizePolicy().hasHeightForWidth())
        self.freq_spinbox.setSizePolicy(sizePolicy4)
        self.freq_spinbox.setFont(font2)
        self.freq_spinbox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.freq_spinbox.setMinimum(1.000000000000000)
        self.freq_spinbox.setMaximum(999.000000000000000)

        self.freq_grid.addWidget(self.freq_spinbox, 2, 0, 1, 2)

        self.freq_combo_box = QComboBox(self.scrollAreaWidgetContents)
        self.freq_combo_box.addItem("")
        self.freq_combo_box.addItem("")
        self.freq_combo_box.addItem("")
        self.freq_combo_box.addItem("")
        self.freq_combo_box.addItem("")
        self.freq_combo_box.addItem("")
        self.freq_combo_box.setObjectName(u"freq_combo_box")
        sizePolicy4.setHeightForWidth(self.freq_combo_box.sizePolicy().hasHeightForWidth())
        self.freq_combo_box.setSizePolicy(sizePolicy4)
        self.freq_combo_box.setFont(font2)

        self.freq_grid.addWidget(self.freq_combo_box, 2, 2, 1, 1)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.freq_grid.addWidget(self.line_9, 1, 0, 1, 3)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.freq_grid.addWidget(self.label_15, 0, 0, 1, 3)

        self.freq_slider = QSlider(self.scrollAreaWidgetContents)
        self.freq_slider.setObjectName(u"freq_slider")
        self.freq_slider.setOrientation(Qt.Orientation.Horizontal)

        self.freq_grid.addWidget(self.freq_slider, 3, 0, 1, 3)


        self.verticalLayout_6.addLayout(self.freq_grid)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.afg_tab, "")

        self.tool_layout.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.tool_layout)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout.addWidget(self.horizontalFrame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1130, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"dlpctl", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.video_frame.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
#if QT_CONFIG(tooltip)
        self.exposure_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Exposure", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.exposure_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Exposure", None))
#endif // QT_CONFIG(tooltip)
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.replay.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.load_bitmask.setText(QCoreApplication.translate("MainWindow", u"Load Bitmask", None))
        self.analysis_button.setText(QCoreApplication.translate("MainWindow", u"Analysis Off", None))
        self.show_filters.setText(QCoreApplication.translate("MainWindow", u"Show Filters", None))
        self.blur_checkbox.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Activate Gaussian Blur", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresh Area", None))
        self.thresh_checkbox.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Circularity", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Activate Contour Detection", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Min Area", None))
        self.contour_checkbox.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adaptive Thresh Constant", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activate Adaptive Thresh", None))
        self.tracking_checkbox.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Activate Bubble Tracking", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Min Position Error", None))
        self.selection_checkbox.setText("")
        self.clear_all.setText(QCoreApplication.translate("MainWindow", u"Clear All Bubbles", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Activate Bubble Selection", None))
        self.pid_checkbox.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Activate PID Control", None))
        self.mouse_pos.setText(QCoreApplication.translate("MainWindow", u"Frame Position (X, Y): ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.video_filters_tab), QCoreApplication.translate("MainWindow", u"Video Tools", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect Camera", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect DLP", None))
        self.refresh_devices.setText(QCoreApplication.translate("MainWindow", u"Refresh Device List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devices_tab), QCoreApplication.translate("MainWindow", u"Devices", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Connect Function Generator", None))
        self.waveform_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sine", None))
        self.waveform_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Square", None))
        self.waveform_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Ramp", None))
        self.waveform_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.waveform_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.waveform_combobox.setItemText(5, QCoreApplication.translate("MainWindow", u"Noise", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Waveform", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Reset Waveform", None))
        self.freq_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.freq_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"kHz", None))
        self.freq_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"dHz", None))
        self.freq_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"cHz", None))
        self.freq_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"mHz", None))
        self.freq_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"uHz", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.afg_tab), QCoreApplication.translate("MainWindow", u"Function Generator", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

