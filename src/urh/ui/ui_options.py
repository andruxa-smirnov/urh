# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogOptions(object):
    def setupUi(self, DialogOptions):
        DialogOptions.setObjectName("DialogOptions")
        DialogOptions.resize(696, 653)
        icon = QtGui.QIcon.fromTheme("configure")
        DialogOptions.setWindowIcon(icon)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(DialogOptions)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(DialogOptions)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGeneration = QtWidgets.QWidget()
        self.tabGeneration.setObjectName("tabGeneration")
        self.layoutWidget = QtWidgets.QWidget(self.tabGeneration)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 314, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBoxDefaultFuzzingPause = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxDefaultFuzzingPause.setObjectName("checkBoxDefaultFuzzingPause")
        self.gridLayout_4.addWidget(self.checkBoxDefaultFuzzingPause, 0, 0, 1, 2)
        self.doubleSpinBoxFuzzingPause = KillerDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxFuzzingPause.setDecimals(3)
        self.doubleSpinBoxFuzzingPause.setMaximum(999999999.0)
        self.doubleSpinBoxFuzzingPause.setObjectName("doubleSpinBoxFuzzingPause")
        self.gridLayout_4.addWidget(self.doubleSpinBoxFuzzingPause, 1, 0, 1, 1)
        self.labelFuzzingSamples = QtWidgets.QLabel(self.layoutWidget)
        self.labelFuzzingSamples.setObjectName("labelFuzzingSamples")
        self.gridLayout_4.addWidget(self.labelFuzzingSamples, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabGeneration, "")
        self.tabView = QtWidgets.QWidget()
        self.tabView.setObjectName("tabView")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tabView)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.comboBoxDefaultView = QtWidgets.QComboBox(self.tabView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDefaultView.sizePolicy().hasHeightForWidth())
        self.comboBoxDefaultView.setSizePolicy(sizePolicy)
        self.comboBoxDefaultView.setObjectName("comboBoxDefaultView")
        self.comboBoxDefaultView.addItem("")
        self.comboBoxDefaultView.addItem("")
        self.comboBoxDefaultView.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxDefaultView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.checkBoxShowConfirmCloseDialog = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxShowConfirmCloseDialog.setObjectName("checkBoxShowConfirmCloseDialog")
        self.verticalLayout.addWidget(self.checkBoxShowConfirmCloseDialog)
        self.checkBoxHoldShiftToDrag = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxHoldShiftToDrag.setObjectName("checkBoxHoldShiftToDrag")
        self.verticalLayout.addWidget(self.checkBoxHoldShiftToDrag)
        self.checkBoxPauseTime = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxPauseTime.setObjectName("checkBoxPauseTime")
        self.verticalLayout.addWidget(self.checkBoxPauseTime)
        self.checkBoxAlignLabels = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxAlignLabels.setObjectName("checkBoxAlignLabels")
        self.verticalLayout.addWidget(self.checkBoxAlignLabels)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.tabView)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.comboBoxTheme = QtWidgets.QComboBox(self.tabView)
        self.comboBoxTheme.setObjectName("comboBoxTheme")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxTheme)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelIconTheme = QtWidgets.QLabel(self.tabView)
        self.labelIconTheme.setObjectName("labelIconTheme")
        self.horizontalLayout_5.addWidget(self.labelIconTheme)
        self.comboBoxIconTheme = QtWidgets.QComboBox(self.tabView)
        self.comboBoxIconTheme.setObjectName("comboBoxIconTheme")
        self.comboBoxIconTheme.addItem("")
        self.comboBoxIconTheme.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxIconTheme)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.groupBoxSpectrogramColormap = QtWidgets.QGroupBox(self.tabView)
        self.groupBoxSpectrogramColormap.setObjectName("groupBoxSpectrogramColormap")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxSpectrogramColormap)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollAreaSpectrogramColormap = QtWidgets.QScrollArea(self.groupBoxSpectrogramColormap)
        self.scrollAreaSpectrogramColormap.setWidgetResizable(True)
        self.scrollAreaSpectrogramColormap.setObjectName("scrollAreaSpectrogramColormap")
        self.scrollAreaWidgetSpectrogramColormapContents = QtWidgets.QWidget()
        self.scrollAreaWidgetSpectrogramColormapContents.setGeometry(QtCore.QRect(0, 0, 616, 316))
        self.scrollAreaWidgetSpectrogramColormapContents.setObjectName("scrollAreaWidgetSpectrogramColormapContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetSpectrogramColormapContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollAreaSpectrogramColormap.setWidget(self.scrollAreaWidgetSpectrogramColormapContents)
        self.verticalLayout_2.addWidget(self.scrollAreaSpectrogramColormap)
        self.verticalLayout.addWidget(self.groupBoxSpectrogramColormap)
        self.tabWidget.addTab(self.tabView, "")
        self.tabFieldtypes = QtWidgets.QWidget()
        self.tabFieldtypes.setObjectName("tabFieldtypes")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabFieldtypes)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tblLabeltypes = QtWidgets.QTableView(self.tabFieldtypes)
        self.tblLabeltypes.setAlternatingRowColors(True)
        self.tblLabeltypes.setObjectName("tblLabeltypes")
        self.horizontalLayout_3.addWidget(self.tblLabeltypes)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnAddLabelType = QtWidgets.QToolButton(self.tabFieldtypes)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddLabelType.setIcon(icon)
        self.btnAddLabelType.setObjectName("btnAddLabelType")
        self.verticalLayout_3.addWidget(self.btnAddLabelType)
        self.btnRemoveLabeltype = QtWidgets.QToolButton(self.tabFieldtypes)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnRemoveLabeltype.setIcon(icon)
        self.btnRemoveLabeltype.setObjectName("btnRemoveLabeltype")
        self.verticalLayout_3.addWidget(self.btnRemoveLabeltype)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 203, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabFieldtypes, "")
        self.tab_plugins = QtWidgets.QWidget()
        self.tab_plugins.setObjectName("tab_plugins")
        self.tabWidget.addTab(self.tab_plugins, "")
        self.tabDevices = QtWidgets.QWidget()
        self.tabDevices.setObjectName("tabDevices")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabDevices)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidgetDevices = QtWidgets.QListWidget(self.tabDevices)
        self.listWidgetDevices.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidgetDevices.setAlternatingRowColors(True)
        self.listWidgetDevices.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidgetDevices.setObjectName("listWidgetDevices")
        self.horizontalLayout.addWidget(self.listWidgetDevices)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chkBoxDeviceEnabled = QtWidgets.QCheckBox(self.tabDevices)
        self.chkBoxDeviceEnabled.setObjectName("chkBoxDeviceEnabled")
        self.verticalLayout_7.addWidget(self.chkBoxDeviceEnabled)
        self.rbNativeBackend = QtWidgets.QRadioButton(self.tabDevices)
        self.rbNativeBackend.setObjectName("rbNativeBackend")
        self.verticalLayout_7.addWidget(self.rbNativeBackend)
        self.rbGnuradioBackend = QtWidgets.QRadioButton(self.tabDevices)
        self.rbGnuradioBackend.setObjectName("rbGnuradioBackend")
        self.verticalLayout_7.addWidget(self.rbGnuradioBackend)
        self.btnHealthCheck = QtWidgets.QPushButton(self.tabDevices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHealthCheck.sizePolicy().hasHeightForWidth())
        self.btnHealthCheck.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("heart")
        self.btnHealthCheck.setIcon(icon)
        self.btnHealthCheck.setObjectName("btnHealthCheck")
        self.verticalLayout_7.addWidget(self.btnHealthCheck)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.lSupport = QtWidgets.QLabel(self.tabDevices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSupport.sizePolicy().hasHeightForWidth())
        self.lSupport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lSupport.setFont(font)
        self.lSupport.setStyleSheet("color: green")
        self.lSupport.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lSupport.setObjectName("lSupport")
        self.verticalLayout_8.addWidget(self.lSupport)
        self.labelWindowsError = QtWidgets.QLabel(self.tabDevices)
        self.labelWindowsError.setWordWrap(True)
        self.labelWindowsError.setObjectName("labelWindowsError")
        self.verticalLayout_8.addWidget(self.labelWindowsError)
        self.line = QtWidgets.QFrame(self.tabDevices)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tabDevices)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.spinBoxNumSendingRepeats = QtWidgets.QSpinBox(self.tabDevices)
        self.spinBoxNumSendingRepeats.setProperty("showGroupSeparator", False)
        self.spinBoxNumSendingRepeats.setMaximum(999999999)
        self.spinBoxNumSendingRepeats.setDisplayIntegerBase(10)
        self.spinBoxNumSendingRepeats.setObjectName("spinBoxNumSendingRepeats")
        self.gridLayout_3.addWidget(self.spinBoxNumSendingRepeats, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tabDevices)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.doubleSpinBoxRAMThreshold = QtWidgets.QDoubleSpinBox(self.tabDevices)
        self.doubleSpinBoxRAMThreshold.setMinimum(1.0)
        self.doubleSpinBoxRAMThreshold.setMaximum(100.0)
        self.doubleSpinBoxRAMThreshold.setObjectName("doubleSpinBoxRAMThreshold")
        self.gridLayout_3.addWidget(self.doubleSpinBoxRAMThreshold, 1, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_3)
        self.line_2 = QtWidgets.QFrame(self.tabDevices)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabDevices)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 2)
        self.lineEditPython2Interpreter = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditPython2Interpreter.setObjectName("lineEditPython2Interpreter")
        self.gridLayout_2.addWidget(self.lineEditPython2Interpreter, 1, 1, 1, 1)
        self.lGnuradioInstalled = QtWidgets.QLabel(self.groupBox_3)
        self.lGnuradioInstalled.setStyleSheet("")
        self.lGnuradioInstalled.setObjectName("lGnuradioInstalled")
        self.gridLayout_2.addWidget(self.lGnuradioInstalled, 3, 0, 1, 2)
        self.lineEditGnuradioDirectory = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditGnuradioDirectory.setEnabled(True)
        self.lineEditGnuradioDirectory.setObjectName("lineEditGnuradioDirectory")
        self.gridLayout_2.addWidget(self.lineEditGnuradioDirectory, 2, 1, 1, 1)
        self.radioButtonPython2Interpreter = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonPython2Interpreter.setObjectName("radioButtonPython2Interpreter")
        self.gridLayout_2.addWidget(self.radioButtonPython2Interpreter, 1, 0, 1, 1)
        self.radioButtonGnuradioDirectory = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonGnuradioDirectory.setObjectName("radioButtonGnuradioDirectory")
        self.gridLayout_2.addWidget(self.radioButtonGnuradioDirectory, 2, 0, 1, 1)
        self.btnChoosePython2Interpreter = QtWidgets.QToolButton(self.groupBox_3)
        self.btnChoosePython2Interpreter.setObjectName("btnChoosePython2Interpreter")
        self.gridLayout_2.addWidget(self.btnChoosePython2Interpreter, 1, 2, 1, 1)
        self.btnChooseGnuRadioDirectory = QtWidgets.QToolButton(self.groupBox_3)
        self.btnChooseGnuRadioDirectory.setObjectName("btnChooseGnuRadioDirectory")
        self.gridLayout_2.addWidget(self.btnChooseGnuRadioDirectory, 2, 2, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.groupBoxNativeOptions = QtWidgets.QGroupBox(self.tabDevices)
        self.groupBoxNativeOptions.setObjectName("groupBoxNativeOptions")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxNativeOptions)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelLibDirs = QtWidgets.QLabel(self.groupBoxNativeOptions)
        self.labelLibDirs.setObjectName("labelLibDirs")
        self.gridLayout_5.addWidget(self.labelLibDirs, 2, 0, 1, 1)
        self.btnRebuildNative = QtWidgets.QPushButton(self.groupBoxNativeOptions)
        self.btnRebuildNative.setEnabled(True)
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnRebuildNative.setIcon(icon)
        self.btnRebuildNative.setObjectName("btnRebuildNative")
        self.gridLayout_5.addWidget(self.btnRebuildNative, 3, 0, 1, 1)
        self.labelNativeRebuildInfo = QtWidgets.QLabel(self.groupBoxNativeOptions)
        self.labelNativeRebuildInfo.setWordWrap(True)
        self.labelNativeRebuildInfo.setObjectName("labelNativeRebuildInfo")
        self.gridLayout_5.addWidget(self.labelNativeRebuildInfo, 1, 0, 1, 3)
        self.lineEditLibDirs = QtWidgets.QLineEdit(self.groupBoxNativeOptions)
        self.lineEditLibDirs.setObjectName("lineEditLibDirs")
        self.gridLayout_5.addWidget(self.lineEditLibDirs, 2, 2, 1, 1)
        self.labelRebuildNativeStatus = QtWidgets.QLabel(self.groupBoxNativeOptions)
        self.labelRebuildNativeStatus.setObjectName("labelRebuildNativeStatus")
        self.gridLayout_5.addWidget(self.labelRebuildNativeStatus, 3, 2, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBoxNativeOptions)
        self.tabWidget.addTab(self.tabDevices, "")
        self.verticalLayout_6.addWidget(self.tabWidget)

        self.retranslateUi(DialogOptions)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(DialogOptions)

    def retranslateUi(self, DialogOptions):
        _translate = QtCore.QCoreApplication.translate
        DialogOptions.setWindowTitle(_translate("DialogOptions", "Options"))
        self.checkBoxDefaultFuzzingPause.setToolTip(_translate("DialogOptions", "<html><head/><body><p>If you disable the default pause, the pause of the fuzzed message will be used.</p></body></html>"))
        self.checkBoxDefaultFuzzingPause.setText(_translate("DialogOptions", "Use a default pause for fuzzed messages"))
        self.labelFuzzingSamples.setText(_translate("DialogOptions", "Samples"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneration), _translate("DialogOptions", "Generation"))
        self.label_7.setText(_translate("DialogOptions", "Default View:"))
        self.comboBoxDefaultView.setItemText(0, _translate("DialogOptions", "Bit"))
        self.comboBoxDefaultView.setItemText(1, _translate("DialogOptions", "Hex"))
        self.comboBoxDefaultView.setItemText(2, _translate("DialogOptions", "ASCII"))
        self.checkBoxShowConfirmCloseDialog.setText(_translate("DialogOptions", "Show \"confirm close\" dialog"))
        self.checkBoxHoldShiftToDrag.setToolTip(_translate("DialogOptions", "<html><head/><body><p>If checked, you need to <span style=\" font-weight:600;\">hold the Shift key to drag</span> with the mouse inside graphic views like the drawn signal in Interpreation tab, while making a selection with the mouse does not require holding any buttons.</p><p>If unchecked, this is inverted: Hold shift to make a selection, and drag by default.</p></body></html>"))
        self.checkBoxHoldShiftToDrag.setText(_translate("DialogOptions", "Hold shift to drag"))
        self.checkBoxPauseTime.setText(_translate("DialogOptions", "Show pauses as time"))
        self.checkBoxAlignLabels.setText(_translate("DialogOptions", "Align on labels"))
        self.label_9.setText(_translate("DialogOptions", "Choose application theme (requires restart):"))
        self.comboBoxTheme.setItemText(0, _translate("DialogOptions", "native look (default)"))
        self.comboBoxTheme.setItemText(1, _translate("DialogOptions", "fallback theme"))
        self.comboBoxTheme.setItemText(2, _translate("DialogOptions", "fallback theme (dark)"))
        self.labelIconTheme.setText(_translate("DialogOptions", "Choose icon theme (requires restart):"))
        self.comboBoxIconTheme.setItemText(0, _translate("DialogOptions", "bundled icons (default)"))
        self.comboBoxIconTheme.setItemText(1, _translate("DialogOptions", "native icon theme"))
        self.groupBoxSpectrogramColormap.setTitle(_translate("DialogOptions", "Spectrogram Colormap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabView), _translate("DialogOptions", "View"))
        self.btnAddLabelType.setText(_translate("DialogOptions", "..."))
        self.btnRemoveLabeltype.setText(_translate("DialogOptions", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFieldtypes), _translate("DialogOptions", "Fieldtypes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plugins), _translate("DialogOptions", "Plugins"))
        self.chkBoxDeviceEnabled.setText(_translate("DialogOptions", "Enabled"))
        self.rbNativeBackend.setText(_translate("DialogOptions", "Native backend (recommended)"))
        self.rbGnuradioBackend.setText(_translate("DialogOptions", "Gnuradio backend"))
        self.btnHealthCheck.setToolTip(_translate("DialogOptions", "Perform a health check for native device extensions."))
        self.btnHealthCheck.setText(_translate("DialogOptions", "Health Check"))
        self.lSupport.setText(_translate("DialogOptions", "device supports sending and receiving"))
        self.labelWindowsError.setText(_translate("DialogOptions", "<html><head/><body><p><span style=\" color:#ff0000;\">Detected a 32 bit installation of python 3.</span> Install <span style=\" font-weight:600;\">64 bit version</span> to use native backends.</p></body></html>"))
        self.label_8.setText(_translate("DialogOptions", "Default sending repititions:"))
        self.spinBoxNumSendingRepeats.setSpecialValueText(_translate("DialogOptions", "Infinite"))
        self.label_5.setText(_translate("DialogOptions", "Use this percentage of available RAM for buffer allocation:"))
        self.doubleSpinBoxRAMThreshold.setSuffix(_translate("DialogOptions", "%"))
        self.groupBox_3.setTitle(_translate("DialogOptions", "Gnuradio options"))
        self.label_11.setText(_translate("DialogOptions", "Needed for Gnuradio backend only"))
        self.lineEditPython2Interpreter.setToolTip(_translate("DialogOptions", "<html><head/><body><p>Use this option if you installed Gnuradio with your package manager e.g. on Linux and Mac OS X.</p></body></html>"))
        self.lineEditPython2Interpreter.setPlaceholderText(_translate("DialogOptions", "/usr/bin/python2"))
        self.lGnuradioInstalled.setText(_translate("DialogOptions", "Gnuradio installation found"))
        self.lineEditGnuradioDirectory.setToolTip(_translate("DialogOptions", "<html><head/><body><p>If you installed Gnuradio with a bundled python interpreter, you need to enter the site-packages path of the installation here. The path should be something like <span style=\" font-style:italic;\">C:\\Program Files\\GNURadio-3.7</span>.</p></body></html>"))
        self.lineEditGnuradioDirectory.setPlaceholderText(_translate("DialogOptions", "C:\\...\\Gnuradio"))
        self.radioButtonPython2Interpreter.setToolTip(_translate("DialogOptions", "<html><head/><body><p>Use this option if you installed Gnuradio with your package manager e.g. on Linux and Mac OS X.</p></body></html>"))
        self.radioButtonPython2Interpreter.setText(_translate("DialogOptions", "Python2 interpreter"))
        self.radioButtonGnuradioDirectory.setToolTip(_translate("DialogOptions", "<html><head/><body><p>If you installed Gnuradio with a bundled python interpreter, you need to enter the site-packages path of the installation here. The path should be something like <span style=\" font-style:italic;\">C:\\Program Files\\GNURadio-3.7</span>.</p></body></html>"))
        self.radioButtonGnuradioDirectory.setText(_translate("DialogOptions", "Gnuradio Directory"))
        self.btnChoosePython2Interpreter.setText(_translate("DialogOptions", "..."))
        self.btnChooseGnuRadioDirectory.setText(_translate("DialogOptions", "..."))
        self.groupBoxNativeOptions.setTitle(_translate("DialogOptions", "Native options"))
        self.labelLibDirs.setText(_translate("DialogOptions", "Library directories:"))
        self.btnRebuildNative.setToolTip(_translate("DialogOptions", "<html><head/><body><p>Rebuild the native device extensions. You need to restart URH after this, to use new extensions.</p></body></html>"))
        self.btnRebuildNative.setText(_translate("DialogOptions", "Rebuild"))
        self.labelNativeRebuildInfo.setText(_translate("DialogOptions", "You can rebuild the native device extensions here. This is useful, when you installed a device driver afterwards or your drivers are stored in an unusual location."))
        self.lineEditLibDirs.setPlaceholderText(_translate("DialogOptions", "Comma separated list of additional library directories"))
        self.labelRebuildNativeStatus.setText(_translate("DialogOptions", "Rebuild <x> new device extensions. Please restart URH to use them."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDevices), _translate("DialogOptions", "Device"))

from urh.ui.KillerDoubleSpinBox import KillerDoubleSpinBox
