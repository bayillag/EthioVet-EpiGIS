# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caser_dialog_base.ui'
#
# Created by: PyQt6 UI code generator
# Rebranded for: EthioVet-EpiGIS (Ethiopian MoA / Jinka Lab Standards)
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 400) # Slightly increased for descriptive labels
        self.gridLayout_14 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_14.setObjectName("gridLayout_14")
        
        self.tabWidget_species = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_species.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_species.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_species.setObjectName("tabWidget")
        
        # --- TAB 1: LOCATION (Site & Geography) ---
        self.tab_location = QtWidgets.QWidget()
        self.tab_location.setObjectName("tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_location)
        self.gridLayout_11.setObjectName("gridLayout_11")
        
        # ADNIS Reference ID
        self.label_3_id = QtWidgets.QLabel(self.tab_location)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3_id.setFont(font)
        self.label_3_id.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3_id, 0, 0, 1, 1)
        self.lineEdit_3_id = QtWidgets.QLineEdit(self.tab_location)
        self.lineEdit_3_id.setMinimumSize(QtCore.QSize(311, 0))
        self.lineEdit_3_id.setPlaceholderText("Format: DDD/YYYY/RRZZWW/NNN")
        self.lineEdit_3_id.setObjectName("lineEdit_3")
        self.gridLayout_11.addWidget(self.lineEdit_3_id, 0, 1, 1, 3)
        
        # MoA Numeric Code
        self.label_6_code = QtWidgets.QLabel(self.tab_location)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6_code.setFont(font)
        self.label_6_code.setObjectName("label_6")
        self.gridLayout_11.addWidget(self.label_6_code, 1, 0, 1, 1)
        self.lineEdit_5_code = QtWidgets.QLineEdit(self.tab_location)
        self.lineEdit_5_code.setMinimumSize(QtCore.QSize(311, 0))
        self.lineEdit_5_code.setObjectName("lineEdit_5")
        self.gridLayout_11.addWidget(self.lineEdit_5_code, 1, 1, 1, 3)
        
        # Diagnosis Type (ADNIS Standard)
        self.label_9_large_scale = QtWidgets.QLabel(self.tab_location)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9_large_scale.setFont(font)
        self.label_9_large_scale.setObjectName("label_9")
        self.gridLayout_11.addWidget(self.label_9_large_scale, 2, 0, 1, 2)
        self.comboBox_4_large_scale = QtWidgets.QComboBox(self.tab_location)
        self.comboBox_4_large_scale.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_4_large_scale.setObjectName("comboBox_4")
        self.gridLayout_11.addWidget(self.comboBox_4_large_scale, 2, 2, 1, 2)
        
        # Coordinates Layout
        self.gridLayout_2_coords = QtWidgets.QGridLayout()
        self.gridLayout_2_coords.setObjectName("gridLayout_2")
        self.label_longitude = QtWidgets.QLabel(self.tab_location)
        self.label_longitude.setObjectName("label")
        self.gridLayout_2_coords.addWidget(self.label_longitude, 0, 0, 1, 1)
        self.lineEdit_longitude = QtWidgets.QLineEdit(self.tab_location)
        self.lineEdit_longitude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_longitude.setObjectName("lineEdit")
        self.gridLayout_2_coords.addWidget(self.lineEdit_longitude, 0, 1, 1, 1)
        self.toolButton_3_dms = QtWidgets.QToolButton(self.tab_location)
        self.toolButton_3_dms.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_3_dms.setObjectName("toolButton_3")
        self.gridLayout_2_coords.addWidget(self.toolButton_3_dms, 0, 2, 2, 1)
        self.label_2_latitude = QtWidgets.QLabel(self.tab_location)
        self.label_2_latitude.setObjectName("label_2")
        self.gridLayout_2_coords.addWidget(self.label_2_latitude, 1, 0, 1, 1)
        self.lineEdit_2_latitude = QtWidgets.QLineEdit(self.tab_location)
        self.lineEdit_2_latitude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2_latitude.setObjectName("lineEdit_2")
        self.gridLayout_2_coords.addWidget(self.lineEdit_2_latitude, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_2_coords, 3, 0, 1, 4)
        
        # Admin Reference
        self.gridLayout_6_reference = QtWidgets.QGridLayout()
        self.gridLayout_6_reference.setObjectName("gridLayout_6")
        self.label_4_reference = QtWidgets.QLabel(self.tab_location)
        self.label_4_reference.setObjectName("label_4")
        self.gridLayout_6_reference.addWidget(self.label_4_reference, 0, 0, 1, 1)
        self.comboBox_reference = QtWidgets.QComboBox(self.tab_location)
        self.comboBox_reference.setMinimumSize(QtCore.QSize(241, 0))
        self.comboBox_reference.setObjectName("comboBox")
        self.gridLayout_6_reference.addWidget(self.comboBox_reference, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_6_reference, 5, 0, 1, 4)
        
        self.tabWidget_species.addTab(self.tab_location, "")
        
        # --- TAB 2: DISEASE (Etiology & Counts) ---
        self.tab_2_disease = QtWidgets.QWidget()
        self.tab_2_disease.setObjectName("tab_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_2_disease)
        self.gridLayout_12.setObjectName("gridLayout_12")
        
        # Target Disease Selection
        self.gridLayout_5_disease = QtWidgets.QGridLayout()
        self.gridLayout_5_disease.setObjectName("gridLayout_5")
        self.label_5_disease = QtWidgets.QLabel(self.tab_2_disease)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5_disease.setFont(font)
        self.label_5_disease.setObjectName("label_5")
        self.gridLayout_5_disease.addWidget(self.label_5_disease, 0, 0, 1, 1)
        self.comboBox_2_disease = QtWidgets.QComboBox(self.tab_2_disease)
        self.comboBox_2_disease.setMinimumSize(QtCore.QSize(280, 0))
        self.comboBox_2_disease.setObjectName("comboBox_2")
        self.gridLayout_5_disease.addWidget(self.comboBox_2_disease, 0, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_5_disease, 0, 0, 1, 2)
        
        # Aggregate PAR (Population at Risk)
        self.gridLayout_4_num_animals = QtWidgets.QGridLayout()
        self.gridLayout_4_num_animals.setObjectName("gridLayout_4")
        self.label_11_num_animals = QtWidgets.QLabel(self.tab_2_disease)
        self.label_11_num_animals.setObjectName("label_11")
        self.gridLayout_4_num_animals.addWidget(self.label_11_num_animals, 0, 0, 1, 1)
        self.lineEdit_6_num_animals = QtWidgets.QLineEdit(self.tab_2_disease)
        self.lineEdit_6_num_animals.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit_6_num_animals.setObjectName("lineEdit_6")
        self.gridLayout_4_num_animals.addWidget(self.lineEdit_6_num_animals, 0, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_4_num_animals, 1, 0, 1, 2)
        
        # Herd/Species Table
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2_disease)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_12.addWidget(self.tableWidget, 2, 0, 1, 1)
        
        # Toolbuttons for Species
        self.gridLayout_10_species_add_remove = QtWidgets.QVBoxLayout()
        self.toolButton_species_add = QtWidgets.QToolButton(self.tab_2_disease)
        self.toolButton_species_add.setText("+")
        self.gridLayout_10_species_add_remove.addWidget(self.toolButton_species_add)
        self.toolButton_5_species_dots = QtWidgets.QToolButton(self.tab_2_disease)
        self.toolButton_5_species_dots.setText("...")
        self.gridLayout_10_species_add_remove.addWidget(self.toolButton_5_species_dots)
        self.toolButton_2_species_remove = QtWidgets.QToolButton(self.tab_2_disease)
        self.toolButton_2_species_remove.setText("-")
        self.gridLayout_10_species_add_remove.addWidget(self.toolButton_2_species_remove)
        self.gridLayout_12.addLayout(self.gridLayout_10_species_add_remove, 2, 1, 1, 1)
        
        self.tabWidget_species.addTab(self.tab_2_disease, "")
        
        # --- TAB 3: STATUS (Temporal Data) ---
        self.tab_3_status = QtWidgets.QWidget()
        self.tab_3_status.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3_status)
        self.gridLayout_9.setObjectName("gridLayout_9")
        
        # Year of Outbreak
        self.label_8_year = QtWidgets.QLabel(self.tab_3_status)
        font.setBold(True)
        self.label_8_year.setFont(font)
        self.gridLayout_9.addWidget(self.label_8_year, 0, 0, 1, 1)
        self.lineEdit_4_year = QtWidgets.QLineEdit(self.tab_3_status)
        self.lineEdit_4_year.setAlignment(QtCore.Qt.AlignRight)
        self.gridLayout_9.addWidget(self.lineEdit_4_year, 0, 1, 1, 1)
        
        # Outbreak Status (C or E)
        self.label_7_status = QtWidgets.QLabel(self.tab_3_status)
        self.label_7_status.setFont(font)
        self.gridLayout_9.addWidget(self.label_7_status, 1, 0, 1, 1)
        self.comboBox_3_status = QtWidgets.QComboBox(self.tab_3_status)
        self.gridLayout_9.addWidget(self.comboBox_3_status, 1, 1, 1, 2)
        
        # Dates Group
        self.groupBox_dates = QtWidgets.QGroupBox(self.tab_3_status)
        self.groupBox_dates.setObjectName("groupBox")
        self.gridLayout_d = QtWidgets.QGridLayout(self.groupBox_dates)
        self.checkBox_dates_suspect = QtWidgets.QCheckBox("First Case Noted:")
        self.dateEdit_dates_suspect = QtWidgets.QDateEdit(calendarPopup=True)
        self.gridLayout_d.addWidget(self.checkBox_dates_suspect, 0, 0)
        self.gridLayout_d.addWidget(self.dateEdit_dates_suspect, 0, 1)
        self.checkBox_2_dates_confirmation = QtWidgets.QCheckBox("Lab Confirmation:")
        self.dateEdit_2_dates_confirmation = QtWidgets.QDateEdit(calendarPopup=True)
        self.gridLayout_d.addWidget(self.checkBox_2_dates_confirmation, 1, 0)
        self.gridLayout_d.addWidget(self.dateEdit_2_dates_confirmation, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_dates, 2, 0, 1, 3)
        
        self.tabWidget_species.addTab(self.tab_3_status, "")
        
        # --- TAB 4: NOTES ---
        self.tab_4_notes = QtWidgets.QWidget()
        self.textEdit_notes = QtWidgets.QTextEdit(self.tab_4_notes)
        self.tabWidget_species.addTab(self.tab_4_notes, "")
        
        # Bottom Buttons
        self.label_12_err = QtWidgets.QLabel("")
        self.gridLayout_14.addWidget(self.label_12_err, 1, 0)
        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.gridLayout_14.addWidget(self.buttonBox, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget_species.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EthioVet-EpiGIS | Jinka Lab Outbreak Manager"))
        
        # Location Tab
        self.label_3_id.setText(_translate("Dialog", "ADNIS ID:"))
        self.label_6_code.setText(_translate("Dialog", "MoA Code:"))
        self.label_9_large_scale.setText(_translate("Dialog", "Diag. Type:"))
        self.label_longitude.setText(_translate("Dialog", "Longitude (E):"))
        self.label_2_latitude.setText(_translate("Dialog", "Latitude (N):"))
        self.toolButton_3_dms.setText(_translate("Dialog", "DMS"))
        self.label_4_reference.setText(_translate("Dialog", "Woreda/Admin Boundary:"))
        self.tabWidget_species.setTabText(0, _translate("Dialog", "1. Site & geography"))
        
        # Disease Tab
        self.label_5_disease.setText(_translate("Dialog", "Suspected Disease:"))
        self.label_11_num_animals.setText(_translate("Dialog", "Population at Risk (PAR):"))
        self.tableWidget.horizontalHeaderItem(0).setText(_translate("Dialog", "Species (MoA Code)"))
        self.tableWidget.horizontalHeaderItem(1).setText(_translate("Dialog", "Production System"))
        self.tabWidget_species.setTabText(1, _translate("Dialog", "2. Etiology & Counts"))
        
        # Status Tab
        self.label_8_year.setText(_translate("Dialog", "Reporting Year:"))
        self.label_7_status.setText(_translate("Dialog", "Outbreak Status:"))
        self.groupBox_dates.setTitle(_translate("Dialog", "Epidemiological Timeline"))
        self.tabWidget_species.setTabText(2, _translate("Dialog", "3. Temporal Data"))
        
        # Notes
        self.tabWidget_species.setTabText(3, _translate("Dialog", "4. Clinical Notes"))
