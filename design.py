# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_v4-7.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1344, 1315)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(_fromUtf8("QWidget { \n"
"\n"
"    background-color: rgb(222,222,222);\n"
"\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 8px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    color: black;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    /*image: url(:/UI/Arrow10x10px.png);*/\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QFrame {\n"
"\n"
"    background: #cccccc;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    border-top-color: white;\n"
"    border-left-color: white;\n"
"    border-right-color: black;\n"
"    border-bottom-color: black;\n"
"\n"
"}\n"
"\n"
"QFrame#frame {\n"
"    background: #808080;\n"
"    border: 2px solid gray;\n"
"    border-style: inset;\n"
"    border top color: black;\n"
"    border left color: black;\n"
"    border right color: white;\n"
"    border bottom color: white;\n"
"}QFrame#frame_2 {\n"
"    background: #808080;\n"
"    border: 2px solid gray;\n"
"    border-style: inset;\n"
"    border top color: black;\n"
"    border left color: black;\n"
"    border right color: white;\n"
"    border bottom color: white;\n"
"}QFrame#frame_3 {\n"
"    background: #808080;\n"
"    border: 2px solid gray;\n"
"    border-style: inset;\n"
"    border top color: black;\n"
"    border left color: black;\n"
"    border right color: white;\n"
"    border bottom color: white;\n"
"}QFrame#frame_4 {\n"
"    background: #808080;\n"
"    border: 2px solid gray;\n"
"    border-style: inset;\n"
"    border top color: black;\n"
"    border left color: black;\n"
"    border right color: white;\n"
"    border bottom color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"\n"
"    background-color: rgba(0,0,0,0);\n"
"    font: 36px;\n"
"    font: bold;\n"
"    color: rgb(0,0,0);\n"
"    border-style: none;\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QLabel#Hint_PlaneFIlter {\n"
"\n"
"    background-color: rgba(0,0,0,0);\n"
"    font: 18px;\n"
"    font: italic;\n"
"    color: rgb(0,0,0);\n"
"    border-style: none;\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid gray;\n"
"    border-top-color: #4D4D4D;\n"
"    border-bottom-color: #4D4D4D;\n"
"    border-left-color: #4D4D4D;\n"
"    border-right-color: #4D4D4D;\n"
"    border-radius: 5px;\n"
"    /*text-align: center;\n"
"    font: 24px;\n"
"    font: bold;*/\n"
"    color: rgba(0,0,0,0);\n"
"    \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #F7931E;\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QRadioButton{ \n"
"    font: 24px;\n"
"    font: bold;\n"
"    color: #000000;\n"
"    background: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QRadioButton::indicator:hovered:!pressed {\n"
"    /*background-color: #F7931E;*/\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"    left: 10px;\n"
"    top: 0px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    background-color: #F7931E;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       #FFFFFF;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QSlider:horizontal {\n"
"    background: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background: white;\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #f7d366, stop: 0.6 #F7931E);\n"
"    background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #f7d366, stop: 0.6 #F7931E);\n"
"    border: 1px solid #777;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #EEE, stop:1 #CCC);\n"
"    border: 1px solid #777;\n"
"    width: 10px;\n"
"    margin-top: -3px;\n"
"    margin-bottom: -3px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFF, stop:1 #DDD);\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #bbb;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background: #eee;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QFormLayout {\n"
"    background: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QVBoxLayout {\n"
"    \n"
"    background: rgba(0,0,0,0);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.F01_Method = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F01_Method.sizePolicy().hasHeightForWidth())
        self.F01_Method.setSizePolicy(sizePolicy)
        self.F01_Method.setFrameShape(QtGui.QFrame.Panel)
        self.F01_Method.setFrameShadow(QtGui.QFrame.Raised)
        self.F01_Method.setObjectName(_fromUtf8("F01_Method"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.F01_Method)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.Label_Step_ChooseMethod = QtGui.QLabel(self.F01_Method)
        self.Label_Step_ChooseMethod.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Label_Step_ChooseMethod.setObjectName(_fromUtf8("Label_Step_ChooseMethod"))
        self.verticalLayout_4.addWidget(self.Label_Step_ChooseMethod)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.frame = QtGui.QFrame(self.F01_Method)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_9.addWidget(self.label_2)
        self.List_Method = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.List_Method.sizePolicy().hasHeightForWidth())
        self.List_Method.setSizePolicy(sizePolicy)
        self.List_Method.setObjectName(_fromUtf8("List_Method"))
        self.List_Method.addItem(_fromUtf8(""))
        self.List_Method.addItem(_fromUtf8(""))
        self.verticalLayout_9.addWidget(self.List_Method)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addWidget(self.F01_Method)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.F02_Setup = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F02_Setup.sizePolicy().hasHeightForWidth())
        self.F02_Setup.setSizePolicy(sizePolicy)
        self.F02_Setup.setFrameShape(QtGui.QFrame.Panel)
        self.F02_Setup.setFrameShadow(QtGui.QFrame.Raised)
        self.F02_Setup.setObjectName(_fromUtf8("F02_Setup"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.F02_Setup)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.Label2_SetupParameters = QtGui.QLabel(self.F02_Setup)
        self.Label2_SetupParameters.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Label2_SetupParameters.setObjectName(_fromUtf8("Label2_SetupParameters"))
        self.verticalLayout_13.addWidget(self.Label2_SetupParameters)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem2)
        self.frame_2 = QtGui.QFrame(self.F02_Setup)
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.Label_QualitySettings = QtGui.QLabel(self.frame_2)
        self.Label_QualitySettings.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Label_QualitySettings.setObjectName(_fromUtf8("Label_QualitySettings"))
        self.verticalLayout_22.addWidget(self.Label_QualitySettings)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem3)
        self.Label_NumberOfPictures = QtGui.QLabel(self.frame_2)
        self.Label_NumberOfPictures.setWhatsThis(_fromUtf8(""))
        self.Label_NumberOfPictures.setObjectName(_fromUtf8("Label_NumberOfPictures"))
        self.verticalLayout_22.addWidget(self.Label_NumberOfPictures)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Slider_NumberOfPictures = QtGui.QSlider(self.frame_2)
        self.Slider_NumberOfPictures.setMinimum(1)
        self.Slider_NumberOfPictures.setMaximum(80)
        self.Slider_NumberOfPictures.setProperty("value", 50)
        self.Slider_NumberOfPictures.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_NumberOfPictures.setObjectName(_fromUtf8("Slider_NumberOfPictures"))
        self.horizontalLayout_2.addWidget(self.Slider_NumberOfPictures)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.Value_NumberOfPictures_2 = QtGui.QLabel(self.frame_2)
        self.Value_NumberOfPictures_2.setObjectName(_fromUtf8("Value_NumberOfPictures_2"))
        self.horizontalLayout_2.addWidget(self.Value_NumberOfPictures_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_22.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem6)
        self.label_14 = QtGui.QLabel(self.frame_2)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_22.addWidget(self.label_14)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.RBTN_640x480 = QtGui.QRadioButton(self.frame_2)
        self.RBTN_640x480.setMaximumSize(QtCore.QSize(16777215, 100))
        self.RBTN_640x480.setObjectName(_fromUtf8("RBTN_640x480"))
        self.horizontalLayout_9.addWidget(self.RBTN_640x480)
        self.RBTN_1920x1080 = QtGui.QRadioButton(self.frame_2)
        self.RBTN_1920x1080.setMaximumSize(QtCore.QSize(16777215, 100))
        self.RBTN_1920x1080.setObjectName(_fromUtf8("RBTN_1920x1080"))
        self.horizontalLayout_9.addWidget(self.RBTN_1920x1080)
        self.verticalLayout_22.addLayout(self.horizontalLayout_9)
        spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem7)
        self.Label_BlurThreshold = QtGui.QLabel(self.frame_2)
        self.Label_BlurThreshold.setObjectName(_fromUtf8("Label_BlurThreshold"))
        self.verticalLayout_22.addWidget(self.Label_BlurThreshold)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.Slider_BlurReductionValue = QtGui.QSlider(self.frame_2)
        self.Slider_BlurReductionValue.setMinimum(1)
        self.Slider_BlurReductionValue.setMaximum(10)
        self.Slider_BlurReductionValue.setProperty("value", 5)
        self.Slider_BlurReductionValue.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_BlurReductionValue.setObjectName(_fromUtf8("Slider_BlurReductionValue"))
        self.horizontalLayout_10.addWidget(self.Slider_BlurReductionValue)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.Value_BlurReductionValue = QtGui.QLabel(self.frame_2)
        self.Value_BlurReductionValue.setObjectName(_fromUtf8("Value_BlurReductionValue"))
        self.horizontalLayout_10.addWidget(self.Value_BlurReductionValue)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.verticalLayout_22.addLayout(self.horizontalLayout_10)
        self.verticalLayout_15.addLayout(self.verticalLayout_22)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.BTN_TakePictures = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.BTN_TakePictures.sizePolicy().hasHeightForWidth())
        self.BTN_TakePictures.setSizePolicy(sizePolicy)
        self.BTN_TakePictures.setObjectName(_fromUtf8("BTN_TakePictures"))
	self.horizontalLayout_17.addWidget(self.BTN_TakePictures)


	self.Mask_images = QtGui.QPushButton(self.frame_2)
        sizePolicy.setHeightForWidth(self.Mask_images.sizePolicy().hasHeightForWidth())
        self.Mask_images.setSizePolicy(sizePolicy)
        self.Mask_images.setObjectName(_fromUtf8("BTN_Maskimages"))
        self.horizontalLayout_17.addWidget(self.Mask_images)

        self.verticalLayout_15.addLayout(self.horizontalLayout_17)
        self.verticalLayout_13.addWidget(self.frame_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.verticalLayout_2.addWidget(self.F02_Setup)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label = QtGui.QLabel(self.frame_5)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_15.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.frame_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_15.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.frame_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_15.addWidget(self.label_4)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_11.addWidget(self.frame_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem10 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.F03_GeneratePC = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F03_GeneratePC.sizePolicy().hasHeightForWidth())
        self.F03_GeneratePC.setSizePolicy(sizePolicy)
        self.F03_GeneratePC.setFrameShape(QtGui.QFrame.Panel)
        self.F03_GeneratePC.setFrameShadow(QtGui.QFrame.Raised)
        self.F03_GeneratePC.setObjectName(_fromUtf8("F03_GeneratePC"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.F03_GeneratePC)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.Label_Step3GeneratePointCloud = QtGui.QLabel(self.F03_GeneratePC)
        self.Label_Step3GeneratePointCloud.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Label_Step3GeneratePointCloud.setObjectName(_fromUtf8("Label_Step3GeneratePointCloud"))
        self.verticalLayout_16.addWidget(self.Label_Step3GeneratePointCloud)
        spacerItem11 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_16.addItem(spacerItem11)
        self.frame_3 = QtGui.QFrame(self.F03_GeneratePC)
        self.frame_3.setFrameShape(QtGui.QFrame.Panel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.BTN_GeneratePointCloud = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_GeneratePointCloud.sizePolicy().hasHeightForWidth())
        self.BTN_GeneratePointCloud.setSizePolicy(sizePolicy)
        self.BTN_GeneratePointCloud.setObjectName(_fromUtf8("BTN_GeneratePointCloud"))
        self.horizontalLayout_13.addWidget(self.BTN_GeneratePointCloud)
        self.verticalLayout_18.addLayout(self.horizontalLayout_13)
        spacerItem12 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem12)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.BTN_PreviewPointCloud = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PreviewPointCloud.sizePolicy().hasHeightForWidth())
        self.BTN_PreviewPointCloud.setSizePolicy(sizePolicy)
        self.BTN_PreviewPointCloud.setObjectName(_fromUtf8("BTN_PreviewPointCloud"))
        self.horizontalLayout_21.addWidget(self.BTN_PreviewPointCloud)
        self.verticalLayout_18.addLayout(self.horizontalLayout_21)
        spacerItem13 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem13)
        self.Progress_PointCloud = QtGui.QProgressBar(self.frame_3)
        self.Progress_PointCloud.setProperty("value", 24)
        self.Progress_PointCloud.setObjectName(_fromUtf8("Progress_PointCloud"))
        self.verticalLayout_18.addWidget(self.Progress_PointCloud)
        spacerItem14 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem14)


        self.Label_PlaneFilter = QtGui.QLabel(self.frame_3)
        self.Label_PlaneFilter.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Label_PlaneFilter.setObjectName(_fromUtf8("Label_PlaneFilter"))
        self.verticalLayout_18.addWidget(self.Label_PlaneFilter)

        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
	"""
        self.Slider_PlaneFilter = QtGui.QSlider(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_PlaneFilter.sizePolicy().hasHeightForWidth())
        self.Slider_PlaneFilter.setSizePolicy(sizePolicy)
        self.Slider_PlaneFilter.setMaximumSize(QtCore.QSize(800, 400))
        self.Slider_PlaneFilter.setBaseSize(QtCore.QSize(0, 0))
        self.Slider_PlaneFilter.setMinimum(0)
        self.Slider_PlaneFilter.setMaximum(10)
        self.Slider_PlaneFilter.setProperty("value", 3)
        self.Slider_PlaneFilter.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_PlaneFilter.setObjectName(_fromUtf8("Slider_PlaneFilter"))
       	self.horizontalLayout_5.addWidget(self.Slider_PlaneFilter)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.Value_PlaneFilter = QtGui.QLabel(self.frame_3)
        self.Value_PlaneFilter.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Value_PlaneFilter.setObjectName(_fromUtf8("Value_PlaneFilter"))
        self.horizontalLayout_5.addWidget(self.Value_PlaneFilter)
	"""

        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.verticalLayout_18.addLayout(self.horizontalLayout_5)
        spacerItem17 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem17)
        self.Label_OutlierFilter = QtGui.QLabel(self.frame_3)
        self.Label_OutlierFilter.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Label_OutlierFilter.setObjectName(_fromUtf8("Label_OutlierFilter"))
        self.verticalLayout_18.addWidget(self.Label_OutlierFilter)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.Slider_OutlierFilter = QtGui.QSlider(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_OutlierFilter.sizePolicy().hasHeightForWidth())
        self.Slider_OutlierFilter.setSizePolicy(sizePolicy)
        self.Slider_OutlierFilter.setMaximumSize(QtCore.QSize(800, 400))
        self.Slider_OutlierFilter.setBaseSize(QtCore.QSize(0, 0))
        self.Slider_OutlierFilter.setMinimum(1)
        self.Slider_OutlierFilter.setMaximum(100)
        self.Slider_OutlierFilter.setProperty("value", 30)
        self.Slider_OutlierFilter.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_OutlierFilter.setObjectName(_fromUtf8("Slider_OutlierFilter"))
        self.horizontalLayout_6.addWidget(self.Slider_OutlierFilter)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.Value_OutlierFilter = QtGui.QLabel(self.frame_3)
        self.Value_OutlierFilter.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Value_OutlierFilter.setObjectName(_fromUtf8("Value_OutlierFilter"))
        self.horizontalLayout_6.addWidget(self.Value_OutlierFilter)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.verticalLayout_18.addLayout(self.horizontalLayout_6)
        spacerItem20 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem20)
        self.Label_Parameter3 = QtGui.QLabel(self.frame_3)
        self.Label_Parameter3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Label_Parameter3.setObjectName(_fromUtf8("Label_Parameter3"))
        self.verticalLayout_18.addWidget(self.Label_Parameter3)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.Slider_Threshold = QtGui.QSlider(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_Threshold.sizePolicy().hasHeightForWidth())
        self.Slider_Threshold.setSizePolicy(sizePolicy)
        self.Slider_Threshold.setMaximumSize(QtCore.QSize(800, 400))
        self.Slider_Threshold.setBaseSize(QtCore.QSize(0, 0))
        self.Slider_Threshold.setMinimum(1)
        self.Slider_Threshold.setMaximum(10)
        self.Slider_Threshold.setProperty("value", 1)
        self.Slider_Threshold.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Threshold.setObjectName(_fromUtf8("Slider_Threshold"))
        self.horizontalLayout_20.addWidget(self.Slider_Threshold)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem21)
        self.ValueParameter3 = QtGui.QLabel(self.frame_3)
        self.ValueParameter3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.ValueParameter3.setObjectName(_fromUtf8("ValueParameter3"))
        self.horizontalLayout_20.addWidget(self.ValueParameter3)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem22)
        self.verticalLayout_18.addLayout(self.horizontalLayout_20)
        spacerItem23 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem23)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.BTN_FilterPointCloud = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_FilterPointCloud.sizePolicy().hasHeightForWidth())
        self.BTN_FilterPointCloud.setSizePolicy(sizePolicy)
        self.BTN_FilterPointCloud.setObjectName(_fromUtf8("BTN_FilterPointCloud"))
        self.horizontalLayout_14.addWidget(self.BTN_FilterPointCloud)
        self.verticalLayout_18.addLayout(self.horizontalLayout_14)
        spacerItem24 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem24)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.BTN_PreviewFilteredPointCloud = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PreviewFilteredPointCloud.sizePolicy().hasHeightForWidth())
        self.BTN_PreviewFilteredPointCloud.setSizePolicy(sizePolicy)
        self.BTN_PreviewFilteredPointCloud.setObjectName(_fromUtf8("BTN_PreviewFilteredPointCloud"))
        self.horizontalLayout_16.addWidget(self.BTN_PreviewFilteredPointCloud)
        self.verticalLayout_18.addLayout(self.horizontalLayout_16)
        self.verticalLayout_17.addLayout(self.verticalLayout_18)
        self.verticalLayout_16.addWidget(self.frame_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_16)
        self.verticalLayout.addWidget(self.F03_GeneratePC)
        spacerItem25 = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem25)
        self.F04_GenerateMesh = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F04_GenerateMesh.sizePolicy().hasHeightForWidth())
        self.F04_GenerateMesh.setSizePolicy(sizePolicy)
        self.F04_GenerateMesh.setFrameShape(QtGui.QFrame.Panel)
        self.F04_GenerateMesh.setFrameShadow(QtGui.QFrame.Raised)
        self.F04_GenerateMesh.setObjectName(_fromUtf8("F04_GenerateMesh"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.F04_GenerateMesh)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.Label_Step4Generate3DMesh = QtGui.QLabel(self.F04_GenerateMesh)
        self.Label_Step4Generate3DMesh.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Label_Step4Generate3DMesh.setObjectName(_fromUtf8("Label_Step4Generate3DMesh"))
        self.verticalLayout_19.addWidget(self.Label_Step4Generate3DMesh)
        spacerItem26 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_19.addItem(spacerItem26)
        self.frame_4 = QtGui.QFrame(self.F04_GenerateMesh)
        self.frame_4.setFrameShape(QtGui.QFrame.Panel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.Param_LabelC = QtGui.QLabel(self.frame_4)
        self.Param_LabelC.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Param_LabelC.setObjectName(_fromUtf8("Param_LabelC"))
        self.verticalLayout_21.addWidget(self.Param_LabelC)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.Slider_CleanMesh = QtGui.QSlider(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_CleanMesh.sizePolicy().hasHeightForWidth())
        self.Slider_CleanMesh.setSizePolicy(sizePolicy)
        self.Slider_CleanMesh.setMaximumSize(QtCore.QSize(800, 400))
        self.Slider_CleanMesh.setBaseSize(QtCore.QSize(0, 0))
        self.Slider_CleanMesh.setMinimum(5)
        self.Slider_CleanMesh.setMaximum(10)
        self.Slider_CleanMesh.setProperty("value", 8)
        self.Slider_CleanMesh.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_CleanMesh.setObjectName(_fromUtf8("Slider_CleanMesh"))
        self.horizontalLayout_7.addWidget(self.Slider_CleanMesh)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem27)
        self.Value_CleanMesh = QtGui.QLabel(self.frame_4)
        self.Value_CleanMesh.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Value_CleanMesh.setObjectName(_fromUtf8("Value_CleanMesh"))
        self.horizontalLayout_7.addWidget(self.Value_CleanMesh)
        spacerItem28 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem28)
        self.verticalLayout_21.addLayout(self.horizontalLayout_7)
        spacerItem29 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_21.addItem(spacerItem29)
        self.Param_LabelC_2 = QtGui.QLabel(self.frame_4)
        self.Param_LabelC_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Param_LabelC_2.setObjectName(_fromUtf8("Param_LabelC_2"))
        self.verticalLayout_21.addWidget(self.Param_LabelC_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.Slider_MeshDecimation = QtGui.QSlider(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_MeshDecimation.sizePolicy().hasHeightForWidth())
        self.Slider_MeshDecimation.setSizePolicy(sizePolicy)
        self.Slider_MeshDecimation.setMaximumSize(QtCore.QSize(800, 400))
        self.Slider_MeshDecimation.setBaseSize(QtCore.QSize(0, 0))
        self.Slider_MeshDecimation.setToolTip(_fromUtf8(""))
        self.Slider_MeshDecimation.setMinimum(5)
        self.Slider_MeshDecimation.setMaximum(10)
        self.Slider_MeshDecimation.setProperty("value", 8)
        self.Slider_MeshDecimation.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_MeshDecimation.setObjectName(_fromUtf8("Slider_MeshDecimation"))
        self.horizontalLayout_8.addWidget(self.Slider_MeshDecimation)
        spacerItem30 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem30)
        self.Value_MeshDecimation = QtGui.QLabel(self.frame_4)
        self.Value_MeshDecimation.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Value_MeshDecimation.setObjectName(_fromUtf8("Value_MeshDecimation"))
        self.horizontalLayout_8.addWidget(self.Value_MeshDecimation)
        spacerItem31 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem31)
        self.verticalLayout_21.addLayout(self.horizontalLayout_8)
        spacerItem32 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_21.addItem(spacerItem32)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.BTN_GenerateMeshFile = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_GenerateMeshFile.sizePolicy().hasHeightForWidth())
        self.BTN_GenerateMeshFile.setSizePolicy(sizePolicy)
        self.BTN_GenerateMeshFile.setObjectName(_fromUtf8("BTN_GenerateMeshFile"))
        self.horizontalLayout_12.addWidget(self.BTN_GenerateMeshFile)
        spacerItem33 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem33)
        self.BTN_PreviewMesh = QtGui.QPushButton(self.frame_4)
        self.BTN_PreviewMesh.setObjectName(_fromUtf8("BTN_PreviewMesh"))
        self.horizontalLayout_12.addWidget(self.BTN_PreviewMesh)
        self.verticalLayout_21.addLayout(self.horizontalLayout_12)
        spacerItem34 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_21.addItem(spacerItem34)
        self.Progress_MeshFile = QtGui.QProgressBar(self.frame_4)
        self.Progress_MeshFile.setProperty("value", 24)
        self.Progress_MeshFile.setObjectName(_fromUtf8("Progress_MeshFile"))
        self.verticalLayout_21.addWidget(self.Progress_MeshFile)
        spacerItem35 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_21.addItem(spacerItem35)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.BTN_ViewTexturedMesh = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_ViewTexturedMesh.sizePolicy().hasHeightForWidth())
        self.BTN_ViewTexturedMesh.setSizePolicy(sizePolicy)
        self.BTN_ViewTexturedMesh.setObjectName(_fromUtf8("BTN_ViewTexturedMesh"))
        self.horizontalLayout_18.addWidget(self.BTN_ViewTexturedMesh)
        self.verticalLayout_21.addLayout(self.horizontalLayout_18)
        self.verticalLayout_20.addLayout(self.verticalLayout_21)
        self.verticalLayout_19.addWidget(self.frame_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_19)
        self.verticalLayout.addWidget(self.F04_GenerateMesh)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.Slider_NumberOfPictures, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Value_NumberOfPictures_2.setNum)
        QtCore.QObject.connect(self.Slider_OutlierFilter, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Value_OutlierFilter.setNum)
        QtCore.QObject.connect(self.Slider_CleanMesh, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Value_CleanMesh.setNum)
        QtCore.QObject.connect(self.Slider_MeshDecimation, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Value_MeshDecimation.setNum)
        QtCore.QObject.connect(self.Slider_BlurReductionValue, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Value_BlurReductionValue.setNum)
        QtCore.QObject.connect(self.Slider_Threshold, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.ValueParameter3.setNum)
        #QtCore.QObject.connect(self.Slider_PlaneFilter, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Value_PlaneFilter.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Label_Step_ChooseMethod.setText(_translate("MainWindow", "Step 1: Choose Method", None))
        self.label_2.setText(_translate("MainWindow", "Method of 3D reconstruction", None))
        self.List_Method.setItemText(0, _translate("MainWindow", "SfM (Structure from Motion)", None))
        self.List_Method.setItemText(1, _translate("MainWindow", "Fringe Laser", None))
        self.Label2_SetupParameters.setText(_translate("MainWindow", "Step 2: Setup Parameters", None))
        self.Label_QualitySettings.setText(_translate("MainWindow", "Quality Settings", None))
        self.Label_NumberOfPictures.setText(_translate("MainWindow", "Number of Pictures", None))
        self.Value_NumberOfPictures_2.setText(_translate("MainWindow", "50", None))
        self.label_14.setText(_translate("MainWindow", "Aspect Ratio", None))
        self.RBTN_640x480.setText(_translate("MainWindow", "640 x 480", None))
        self.RBTN_1920x1080.setText(_translate("MainWindow", "1920 x 1080", None))
        self.Label_BlurThreshold.setText(_translate("MainWindow", "Blur Reduction Value", None))
        self.Value_BlurReductionValue.setText(_translate("MainWindow", "5", None))
        self.BTN_TakePictures.setText(_translate("MainWindow", "Take Pictures", None))
	self.Mask_images.setText(_translate("MainWindow", "Mask image", None))

        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Logos/LJMU.png\"/></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Logos/DigiArt Logo.png\"/></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Logos/EURC.png\"/></p></body></html>", None))
        self.Label_Step3GeneratePointCloud.setText(_translate("MainWindow", "Step 3: Generate Point Cloud", None))
        self.BTN_GeneratePointCloud.setText(_translate("MainWindow", "Generate Point Cloud", None))
        self.BTN_PreviewPointCloud.setText(_translate("MainWindow", "Preview Point Cloud", None))
        #self.Label_PlaneFilter.setText(_translate("MainWindow", "Plane Filter ", None))
        #self.Value_PlaneFilter.setText(_translate("MainWindow", "3", None))
        self.Label_OutlierFilter.setText(_translate("MainWindow", "Outlier Filter", None))
        self.Value_OutlierFilter.setText(_translate("MainWindow", "30", None))
        self.Label_Parameter3.setText(_translate("MainWindow", "Threshold", None))
        self.ValueParameter3.setText(_translate("MainWindow", "1", None))
        self.BTN_FilterPointCloud.setText(_translate("MainWindow", "Filter Point Cloud", None))
        self.BTN_PreviewFilteredPointCloud.setText(_translate("MainWindow", "Preview Filtered Point Cloud", None))
        self.Label_Step4Generate3DMesh.setText(_translate("MainWindow", "Step 4: Generate 3D Mesh", None))
        self.Param_LabelC.setText(_translate("MainWindow", "Clean Mesh", None))
        self.Value_CleanMesh.setText(_translate("MainWindow", "8", None))
        self.Param_LabelC_2.setText(_translate("MainWindow", "Mesh Decimation", None))
        self.Value_MeshDecimation.setText(_translate("MainWindow", "8", None))
        self.BTN_GenerateMeshFile.setText(_translate("MainWindow", "Generate Mesh", None))
        self.BTN_PreviewMesh.setText(_translate("MainWindow", "Preview Mesh", None))
        self.BTN_ViewTexturedMesh.setText(_translate("MainWindow", "View Textured Mesh", None))

import Images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

