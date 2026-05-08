# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EthioVet-EpiGIS: Veterinary Epidemiology Tool for Ethiopia
   A QGIS plugin tailored for Jinka Regional Veterinary Laboratory
   Outbreak Case Management Logic (Herd-Level)
                              -------------------
        updated              : 2026-05-08
        rebranded by         : Bayilla Geda
        original copyright   : (C) 2015 by Norbert Solymosi
 ***************************************************************************/
"""

import os
from qgis.PyQt.QtGui import QRegularExpressionValidator, QPalette, QFont
from qgis.PyQt.QtWidgets import QDialog, QTableWidgetItem, QDialogButtonBox, QMessageBox
from qgis.PyQt.QtCore import QRegularExpression, Qt
from qgis.PyQt.QtSql import QSqlQuery

from .caser_dialog import Ui_Dialog
from .xaffected import Dialog as xaffdial
from .xcoordtrafo import Dialog as xtrafodial
# Updated Class Name Reference
from .qvfuncs import EthioVetEpiGISFuncs as EthioVetEpiGISFuncs


class CaserDialog(QDialog, Ui_Dialog):
    def __init__(self, db_connection, iface):
        """
        Constructor for the EthioVet-EpiGIS Case Entry Dialog.
        :param db_connection: Open QSqlDatabase connection to EthioVet SpatiaLite
        :param iface: QGIS Interface handle
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.db = db_connection
        
        # Instantiate the newly named functions class
        self.funcs = EthioVetEpiGISFuncs()

        # Save button handling
        self.btnsave = self.buttonBox.button(QDialogButtonBox.Save)

        # 1. Setup Tool Buttons (Herd/Species Management)
        self.toolButton_species_add.setToolTip('Add species group to this outbreak')
        self.toolButton_species_add.clicked.connect(self.addNewSpecies)

        self.toolButton_2_species_remove.setToolTip('Remove selected species group')
        self.toolButton_2_species_remove.clicked.connect(self.removeRec)

        self.toolButton_5_species_dots.setToolTip('Edit species group counts')
        self.toolButton_5_species_dots.clicked.connect(self.editRec)

        self.toolButton_3_dms.setToolTip('Convert Degrees/Minutes/Seconds to Decimal')
        self.toolButton_3_dms.clicked.connect(self.coordinateTransformation)

        # 2. Populate Status (DOVAR Standard: Continuing vs Ended)
        self.comboBox_3_status.clear()
        self.comboBox_3_status.addItems(['', 'C - Continuing', 'E - Ended'])

        # 3. Populate Diagnosis Type (ADNIS Standard)
        self.comboBox_4_large_scale.clear()
        self.comboBox_4_large_scale.addItems(['', 'S - Suspected', 'P - Probable', 'C - Confirmed (Lab)'])

        # 4. Input Validation (MoA 2024 Standards)
        int_regex = QRegularExpression('[0-9]+')
        int_validator = QRegularExpressionValidator(int_regex)
        self.lineEdit_4_year.setValidator(int_validator)
        self.lineEdit_6_num_animals.setValidator(int_validator)

        coord_regex = QRegularExpression(r'^[0-9]{1,2}(\.[0-9]{1,8})?$')
        coord_validator = QRegularExpressionValidator(coord_regex)
        self.lineEdit_longitude.setValidator(coord_validator)
        self.lineEdit_2_latitude.setValidator(coord_validator)

        # 5. Populate Diseases from xdiseases Master Table
        self.loadDiseases()

        # 6. Date Handling Logic
        self.checkBox_dates_suspect.clicked.connect(self.toggleDate1)
        self.checkBox_2_dates_confirmation.clicked.connect(self.toggleDate2)
        self.checkBox_3_dates_expiration.clicked.connect(self.toggleDate3)

        # 7. Form Controls (Validation for Save)
        self.lineEdit_3_id.textChanged.connect(self.validateForm)
        self.lineEdit_4_year.textChanged.connect(self.validateForm)
        self.comboBox_2_disease.currentIndexChanged.connect(self.validateForm)
        self.comboBox_3_status.currentIndexChanged.connect(self.validateForm)
        
        self.lineEdit_6_num_animals.setText("1")
        self.validateForm()

    def loadDiseases(self):
        """Loads MoA 2024 Diseases into dropdown"""
        self.comboBox_2_disease.clear()
        self.comboBox_2_disease.addItem('', '')
        
        query = QSqlQuery("SELECT name_en, moa_code FROM xdiseases ORDER BY name_en", self.db)
        while query.next():
            self.comboBox_2_disease.addItem(query.value(0), query.value(1))

    def toggleDate1(self):
        self.dateEdit_dates_suspect.setEnabled(self.checkBox_dates_suspect.isChecked())

    def toggleDate2(self):
        self.dateEdit_2_dates_confirmation.setEnabled(self.checkBox_2_dates_confirmation.isChecked())

    def toggleDate3(self):
        self.dateEdit_3_dates_expiration.setEnabled(self.checkBox_3_dates_expiration.isChecked())

    def coordinateTransformation(self):
        """Opens DMS to Decimal converter for field staff using updated class reference"""
        dlg = xtrafodial()
        dlg.setWindowTitle('Jinka Lab: GPS Coordinate Conversion')

        lon_dec = self.lineEdit_longitude.text()
        lat_dec = self.lineEdit_2_latitude.text()
        
        if lon_dec and lat_dec:
            # Calling the updated class methods
            res_lon = self.funcs.dec2deg(lon_dec)
            res_lat = self.funcs.dec2deg(lat_dec)
        
        if dlg.exec_() == QDialog.Accepted:
            res_lon_dec = self.funcs.deg2dec(dlg.lineEdit.text(), dlg.lineEdit_2.text(), dlg.lineEdit_3.text())
            self.lineEdit_longitude.setText(str(res_lon_dec))
            res_lat_dec = self.funcs.deg2dec(dlg.lineEdit_4.text(), dlg.lineEdit_5.text(), dlg.lineEdit_6.text())
            self.lineEdit_2_latitude.setText(str(res_lat_dec))

    def addNewSpecies(self):
        """Opens sub-dialog to add a species-herd count to the outbreak"""
        dlg = xaffdial()
        dlg.setWindowTitle('Add Herd Species Group')
        
        query = QSqlQuery("SELECT name_en, moa_code FROM xspecies", self.db)
        while query.next():
            dlg.comboBox.addItem(query.value(0), query.value(1))

        if dlg.exec_() == QDialog.Accepted:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(dlg.comboBox.currentText()))
            count = dlg.lineEdit.text() if dlg.lineEdit.text() else '0'
            self.tableWidget.setItem(row, 1, QTableWidgetItem(count))
            self.validateForm()

    def removeRec(self):
        if self.tableWidget.currentRow() >= 0:
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            self.validateForm()

    def validateForm(self):
        """Enforces mandatory fields before allowing Save"""
        errors = 0
        if not self.lineEdit_3_id.text(): errors += 1
        if not self.lineEdit_4_year.text(): errors += 1
        if self.comboBox_2_disease.currentIndex() <= 0: errors += 1
        if self.comboBox_3_status.currentIndex() <= 0: errors += 1
        if self.tableWidget.rowCount() == 0: errors += 1

        if errors == 0:
            self.btnsave.setEnabled(True)
            self.label_12.setText('')
        else:
            self.btnsave.setEnabled(False)
            self.label_12.setStyleSheet("color: red;")
            self.label_12.setText('Bold fields and at least one species are required!')
