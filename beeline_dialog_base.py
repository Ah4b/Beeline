# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beeline_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BeelineDialogBase(object):
    def setupUi(self, BeelineDialogBase):
        BeelineDialogBase.setObjectName("BeelineDialogBase")
        BeelineDialogBase.resize(506, 308)
        self.verticalLayout = QtWidgets.QVBoxLayout(BeelineDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_1 = QtWidgets.QGroupBox(BeelineDialogBase)
        self.groupBox_1.setObjectName("groupBox_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmbInputLayer = QtWidgets.QComboBox(self.groupBox_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbInputLayer.sizePolicy().hasHeightForWidth())
        self.cmbInputLayer.setSizePolicy(sizePolicy)
        self.cmbInputLayer.setObjectName("cmbInputLayer")
        self.horizontalLayout.addWidget(self.cmbInputLayer)
        self.verticalLayout.addWidget(self.groupBox_1)
        self.groupBox_2 = QtWidgets.QGroupBox(BeelineDialogBase)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.memoryLayerOutput = QtWidgets.QRadioButton(self.groupBox_2)
        self.memoryLayerOutput.setChecked(True)
        self.memoryLayerOutput.setObjectName("memoryLayerOutput")
        self.horizontalLayout_9.addWidget(self.memoryLayerOutput)
        self.shapefileOutput = QtWidgets.QRadioButton(self.groupBox_2)
        self.shapefileOutput.setChecked(False)
        self.shapefileOutput.setObjectName("shapefileOutput")
        self.horizontalLayout_9.addWidget(self.shapefileOutput)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.outputFilename = QtWidgets.QLineEdit(self.groupBox_2)
        self.outputFilename.setEnabled(False)
        self.outputFilename.setReadOnly(True)
        self.outputFilename.setObjectName("outputFilename")
        self.horizontalLayout_3.addWidget(self.outputFilename)
        self.selectFilename = QtWidgets.QToolButton(self.groupBox_2)
        self.selectFilename.setEnabled(False)
        self.selectFilename.setObjectName("selectFilename")
        self.horizontalLayout_3.addWidget(self.selectFilename)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.addToCanvas = QtWidgets.QCheckBox(self.groupBox_2)
        self.addToCanvas.setEnabled(False)
        self.addToCanvas.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addToCanvas.setChecked(True)
        self.addToCanvas.setObjectName("addToCanvas")
        self.verticalLayout_2.addWidget(self.addToCanvas)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(BeelineDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BeelineDialogBase)
        QtCore.QMetaObject.connectSlotsByName(BeelineDialogBase)

    def retranslateUi(self, BeelineDialogBase):
        _translate = QtCore.QCoreApplication.translate
        BeelineDialogBase.setWindowTitle(_translate("BeelineDialogBase", "Beeline"))
        self.groupBox_1.setTitle(_translate("BeelineDialogBase", "Input"))
        self.label.setText(_translate("BeelineDialogBase", "Point Layer"))
        self.groupBox_2.setTitle(_translate("BeelineDialogBase", "Output"))
        self.memoryLayerOutput.setText(_translate("BeelineDialogBase", "Memory"))
        self.shapefileOutput.setText(_translate("BeelineDialogBase", "Shapefile"))
        self.label_4.setText(_translate("BeelineDialogBase", "File name"))
        self.selectFilename.setText(_translate("BeelineDialogBase", "..."))
        self.addToCanvas.setText(_translate("BeelineDialogBase", "add to canvas"))

