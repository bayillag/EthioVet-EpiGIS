# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EthioVet-EpiGIS: Veterinary Epidemiology Tool for Ethiopia
   A QGIS plugin tailored for Jinka Regional Veterinary Laboratory
   Outbreak Buffer & Surveillance Zone Generator
                              -------------------
        updated              : 2026-05-08
        rebranded by         : Bayilla Geda
        original copyright   : (C) 2015 by Norbert Solymosi
 ***************************************************************************/
"""

from qgis.PyQt.QtGui import QRegularExpressionValidator
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QRegularExpression
from qgis.PyQt.QtSql import QSqlQueryModel
from .buffer_dialog import Ui_Dialog


class BufferDialog(QDialog, Ui_Dialog):         
    def __init__(self, existing_tables=None):
        """
        Constructor for the EthioVet-EpiGIS Buffer Dialog.
        
        :param existing_tables: List of table names already in the SpatiaLite DB 
                                to prevent overwriting.
        """
        QDialog.__init__(self)                               
        self.setupUi(self)

        # List of existing tables in the database to prevent duplicates
        self.tablst = existing_tables if existing_tables else []
        
        # Validation: SpatiaLite table names should be lowercase, alphanumeric, and underscores
        # Updated to QRegularExpression for QGIS 3.2+ and QGIS 4 compatibility
        regex = QRegularExpression('^[a-z][a-z0-9_]*$')
        validator = QRegularExpressionValidator(regex)
        self.lineEdit.setValidator(validator)

        # Signals
        self.lineEdit.textChanged.connect(self.validate_buffer_name)
        self.spinBox.valueChanged.connect(self.auto_generate_name)
        
        # Set default spinbox to 10 (Standard OIE Surveillance Zone in KM)
        self.spinBox.setValue(10)
        self.auto_generate_name()

    def auto_generate_name(self):
        """
        Automatically generates a suggested table name based on the distance.
        E.g., 3km Protection Zone -> sz_3km, 10km Surveillance Zone -> sz_10km
        """
        distance = self.spinBox.value()
        # Using 'sz' prefix (Surveillance Zone) for shorter, cleaner database names
        suggested_name = 'sz_%skm' % distance
        self.lineEdit.setText(suggested_name)

    def validate_buffer_name(self):
        """
        Check if the typed name already exists in the database.
        Disables the 'OK' button if the name is taken or invalid.
        """
        name = self.lineEdit.text().strip()
        
        # 1. Check for empty string
        if not name:
            self.buttonBox.setEnabled(False)
            return

        # 2. Check against existing tables in the Jinka Lab Database
        if name in self.tablst:
            self.lineEdit.setStyleSheet("color: red; border: 1px solid red;")
            self.buttonBox.setEnabled(False)
            # You could add a tooltip here: "Table already exists in SpatiaLite"
        else:
            self.lineEdit.setStyleSheet("")
            self.buttonBox.setEnabled(True)

    def get_buffer_parameters(self):
        """Returns the user inputs for processing."""
        return {
            "name": self.lineEdit.text(),
            "distance": self.spinBox.value()
        }
