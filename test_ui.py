from PyQt6.QtCore import Qt, QRect, QLocale, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QWidget, QTabWidget, QGridLayout, QPushButton, QLCDNumber, QFrame, QLabel, QLineEdit, \
    QCheckBox, QHBoxLayout, QScrollBar, QProgressBar, QMenuBar, QMenu, QStatusBar



class Ui_AstrOkay(object):
    def setupUi(self, AstrOkay):
        AstrOkay.setObjectName("AstrOkay")
        AstrOkay.setWindowModality(Qt.WindowModality.ApplicationModal)
        AstrOkay.setEnabled(True)
        AstrOkay.resize(1440, 799)
        AstrOkay.setAutoFillBackground(False)
        AstrOkay.setDocumentMode(False)
        self.centralwidget = QWidget(AstrOkay)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(20, 80, 431, 741))
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setLocale(QLocale(QLocale.Language.English, QLocale.Country.UnitedStates))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 310, 371, 177))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 3, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 0, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMouseTracking(True)

        self.gridLayout.addWidget(self.pushButton_11, 1, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 3, 0, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.gridLayout.addWidget(self.lcdNumber_2, 0, 3, 1, 1)

        self.lcdNumber_3 = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")

        self.gridLayout.addWidget(self.lcdNumber_3, 1, 3, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")

        self.gridLayout.addWidget(self.lcdNumber_4, 2, 3, 1, 1)

        self.lcdNumber_5 = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")

        self.gridLayout.addWidget(self.lcdNumber_5, 3, 3, 1, 1)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(20, 490, 371, 20))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 290, 371, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 150, 371, 131))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_30 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_3.addWidget(self.pushButton_30, 7, 2, 1, 1)

        self.pushButton_29 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout_3.addWidget(self.pushButton_29, 7, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 5, 0, 1, 1)

        self.lcdNumber_11 = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_11.setObjectName(u"lcdNumber_11")

        self.gridLayout_3.addWidget(self.lcdNumber_11, 7, 3, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 5, 1, 1, 3)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 7, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 2)

        self.pushButton_34 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.gridLayout_3.addWidget(self.pushButton_34, 6, 0, 1, 4)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 130, 371, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.checkBox_3 = QCheckBox(self.tab)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 110, 371, 20))
        self.checkBox_2 = QCheckBox(self.tab)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 90, 371, 20))
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 70, 371, 20))
        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 60, 371, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayoutWidget_2 = QWidget(self.tab)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 10, 371, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_2.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_2.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_2.addWidget(self.pushButton_18)

        self.lcdNumber_6 = QLCDNumber(self.horizontalLayoutWidget_2)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setMouseTracking(False)

        self.horizontalLayout_2.addWidget(self.lcdNumber_6)

        self.verticalScrollBar = QScrollBar(self.tab)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(400, 10, 16, 691))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 510, 371, 177))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_20 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_2.addWidget(self.pushButton_20, 2, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_2.addWidget(self.pushButton_21, 1, 0, 1, 1)

        self.pushButton_22 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout_2.addWidget(self.pushButton_22, 3, 2, 1, 1)

        self.pushButton_23 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_2.addWidget(self.pushButton_23, 3, 1, 1, 1)

        self.pushButton_24 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_2.addWidget(self.pushButton_24, 0, 1, 1, 1)

        self.pushButton_25 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_2.addWidget(self.pushButton_25, 1, 1, 1, 1)

        self.pushButton_26 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout_2.addWidget(self.pushButton_26, 0, 2, 1, 1)

        self.pushButton_27 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.gridLayout_2.addWidget(self.pushButton_27, 2, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout_2.addWidget(self.pushButton_28, 1, 2, 1, 1)

        self.pushButton_31 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.gridLayout_2.addWidget(self.pushButton_31, 2, 2, 1, 1)

        self.pushButton_32 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.gridLayout_2.addWidget(self.pushButton_32, 0, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.gridLayout_2.addWidget(self.pushButton_33, 3, 0, 1, 1)

        self.lcdNumber_7 = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")

        self.gridLayout_2.addWidget(self.lcdNumber_7, 0, 3, 1, 1)

        self.lcdNumber_8 = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_8.setObjectName(u"lcdNumber_8")

        self.gridLayout_2.addWidget(self.lcdNumber_8, 1, 3, 1, 1)

        self.lcdNumber_9 = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")

        self.gridLayout_2.addWidget(self.lcdNumber_9, 2, 3, 1, 1)

        self.lcdNumber_10 = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_10.setObjectName(u"lcdNumber_10")

        self.gridLayout_2.addWidget(self.lcdNumber_10, 3, 3, 1, 1)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(20, 690, 371, 20))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 0, 81, 31))
        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(220, 0, 100, 32))
        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(20, 0, 100, 32))
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(120, 0, 100, 32))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 30, 51, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 30, 81, 21))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(160, 30, 161, 23))
        self.progressBar.setValue(24)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 81, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 50, 81, 21))
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(460, 10, 16, 811))
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        AstrOkay.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AstrOkay)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 24))
        self.menuWelcome_to_AstrOkay = QMenu(self.menubar)
        self.menuWelcome_to_AstrOkay.setObjectName(u"menuWelcome_to_AstrOkay")
        AstrOkay.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AstrOkay)
        self.statusbar.setObjectName(u"statusbar")
        AstrOkay.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuWelcome_to_AstrOkay.menuAction())

        self.retranslateUi(AstrOkay)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(AstrOkay)
        # setupUi

    def retranslateUi(self, AstrOkay):
        AstrOkay.setWindowTitle(QCoreApplication.translate("AstrOkay", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("AstrOkay", u"DarkFlat Frame ", None))
        self.pushButton_3.setText(QCoreApplication.translate("AstrOkay", u"Dark Frame", None))
        self.pushButton_13.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_9.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_6.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_7.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_10.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_8.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_11.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_12.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_2.setText(QCoreApplication.translate("AstrOkay", u"Flat Frame ", None))
        self.pushButton_5.setText(QCoreApplication.translate("AstrOkay", u"Bias Frame", None))
        self.pushButton_30.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_29.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.label_7.setText(QCoreApplication.translate("AstrOkay", u"Write Here:", None))
        self.pushButton.setText(QCoreApplication.translate("AstrOkay", u"   Ligth Frame   ", None))
        self.label_6.setText(QCoreApplication.translate("AstrOkay", u"What's You Project Name?", None))
        self.pushButton_34.setText(QCoreApplication.translate("AstrOkay", u"Start Project", None))
        self.checkBox_3.setText(QCoreApplication.translate("AstrOkay", u"Auto-Detect Master & Integrations", None))
        self.checkBox_2.setText(QCoreApplication.translate("AstrOkay", u"Multi-Session Processing", None))
        self.checkBox.setText(QCoreApplication.translate("AstrOkay", u"Multi-Channel/Filter Processing", None))
        self.pushButton_16.setText(QCoreApplication.translate("AstrOkay", u"Your Frames", None))
        self.pushButton_17.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_18.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_20.setText(QCoreApplication.translate("AstrOkay", u"Master DarkFlat", None))
        self.pushButton_21.setText(QCoreApplication.translate("AstrOkay", u"Master Dark", None))
        self.pushButton_22.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_23.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_24.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_25.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_26.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_27.setText(QCoreApplication.translate("AstrOkay", u"All", None))
        self.pushButton_28.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_31.setText(QCoreApplication.translate("AstrOkay", u"Clean", None))
        self.pushButton_32.setText(QCoreApplication.translate("AstrOkay", u"Master Flat", None))
        self.pushButton_33.setText(QCoreApplication.translate("AstrOkay", u"Master Bias", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("AstrOkay", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("AstrOkay", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("AstrOkay", u"HDD .... GB", None))
        self.pushButton_19.setText(QCoreApplication.translate("AstrOkay", u"Lisance", None))
        self.pushButton_15.setText(QCoreApplication.translate("AstrOkay", u"Config", None))
        self.pushButton_14.setText(QCoreApplication.translate("AstrOkay", u"Gpu/Cpu", None))
        self.label_4.setText(QCoreApplication.translate("AstrOkay", u"CPU %.", None))
        self.label_5.setText(QCoreApplication.translate("AstrOkay", u"STATUS", None))
        self.label_2.setText(QCoreApplication.translate("AstrOkay", u"APP %.", None))
        self.label_3.setText(QCoreApplication.translate("AstrOkay", u"OS %", None))
        self.menuWelcome_to_AstrOkay.setTitle(QCoreApplication.translate("AstrOkay", u"Welcome to AstrOkay", None))
    # retranslateUi

