# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buffer_dialog_base.ui'
#
# Created by: PyQt6 UI code generator
# Rebranded for: EthioVet-EpiGIS (Jinka Regional Veterinary Laboratory)
# Logic: Aligned with OIE Surveillance Zone standards

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 150)
        Dialog.setWindowIcon(QtGui.QIcon(':/plugins/EthioVet-EpiGIS/icon.png'))
        
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        # Radius Label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # Radius Spinbox
        # Changed defaults: OIE standards usually require 1km (protection) or 10km (surveillance)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setMinimumSize(QtCore.QSize(120, 0))
        self.spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox.setMinimum(1000)      # Min: 1km
        self.spinBox.setMaximum(100000)    # Max: 100km
        self.spinBox.setSingleStep(1000)   # Step by 1km
        self.spinBox.setProperty("value", 10000) # Default: 10km (OIE Surveillance Standard)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        
        # Unit Label
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        # Database Checkbox
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 1)
        
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        # Layer Name Label
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        
        # LineEdit for Table Name
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(251, 0))
        self.lineEdit.setPlaceholderText("e.g., sz_10km_ppr")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        
        # Button Box
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Branded Title
        Dialog.setWindowTitle(_translate("Dialog", "EthioVet-EpiGIS: Generate Surveillance Zone"))
        self.label.setText(_translate("Dialog", "Buffer Radius:"))
        self.label_2.setText(_translate("Dialog", "meters"))
        self.checkBox.setText(_translate("Dialog", "Commit to EthioVet SpatiaLite Database"))
        self.label_3.setText(_translate("Dialog", "Table/Layer Name:"))
