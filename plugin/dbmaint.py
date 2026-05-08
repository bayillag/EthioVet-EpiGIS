# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EthioVet-EpiGIS: Veterinary Epidemiology Tool for Ethiopia
   A QGIS plugin tailored for Jinka Regional Veterinary Laboratory
   Database Maintenance & Dictionary Management
                              -------------------
        updated              : 2026-05-08
        rebranded by         : Bayilla Geda
        original copyright   : (C) 2015 by Norbert Solymosi
 ***************************************************************************/
"""

import os
from qgis.PyQt.QtGui import QRegularExpressionValidator
from qgis.PyQt.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from qgis.PyQt.QtCore import QRegularExpression, Qt
from qgis.PyQt.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from qgis.core import QgsProject, QgsVectorLayer

from .dbmaint_dialog import Ui_Dialog
from .xitem import Dialog as insdlg


class DBMaintDialog(QDialog, Ui_Dialog):
    def __init__(self, db_connection):
        """
        Constructor for the database maintenance dialog.
        :param db_connection: Open QSqlDatabase connection to EthioVet SpatiaLite
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.db = db_connection

        # Modern validation for translation entries (QGIS 4 / Qt6 ready)
        # Avoids characters that break SQL strings
        regex = QRegularExpression("[^|'\"]+")
        validator = QRegularExpressionValidator(regex)
        self.lineEdit_translation.setValidator(validator)

        self.toolButton_translation.setToolTip('Update localized name (e.g. Amharic)')
        self.toolButton_lang.setToolTip('Add new entry to Master Dictionary')

        # Connect UI Signals
        self.comboBox_lists.currentIndexChanged.connect(self.tabUpdate)
        self.tableView_lists.clicked.connect(self.itemSel)
        self.toolButton_translation.clicked.connect(self.saveTrans)
        self.lineEdit_translation.returnPressed.connect(self.saveTrans)
        self.toolButton_lang.clicked.connect(self.saveEn)

        # Close button logic
        self.bb = self.buttonBox.button(QDialogButtonBox.Close)
        self.bb.clicked.connect(self.accept)

        self.comboBox_translation.currentIndexChanged.connect(self.itemSel)

        self.toolButton_delete.clicked.connect(self.deLayer)
        self.toolButton_delete.setToolTip('Permanently delete selected spatial layer')
        self.toolButton_rename.clicked.connect(self.renameLayer)
        self.toolButton_rename.setToolTip('Rename spatial layer and update metadata')

        # Initialize Data
        self.loadLayers()
        self.tabUpdate()

    def loadLayers(self):
        """Refreshes the list of spatial tables from SpatiaLite metadata"""
        sql = 'SELECT f_table_name AS "Spatial Layers" FROM geometry_columns ORDER BY f_table_name'
        self.model2 = QSqlQueryModel()
        self.model2.setQuery(sql, self.db)
        self.tableView_layers.setModel(self.model2)
        self.tableView_layers.horizontalHeader().setStretchLastSection(True)

    def renameLayer(self):
        """Renames a table and updates all SpatiaLite geometry metadata"""
        idx_list = self.tableView_layers.selectionModel().selectedIndexes()
        if not idx_list:
            return

        oname = str(self.model2.data(idx_list[0]))
        dlg = insdlg()
        dlg.setWindowTitle('Jinka Lab: Rename Spatial Layer')
        dlg.label.setText('New table name:')
        dlg.lineEdit.setText(oname)

        if dlg.exec_() == QDialog.Accepted:
            nname = dlg.lineEdit.text().strip().lower().replace(" ", "_")
            
            # Remove from QGIS Legend if loaded to prevent file locking
            layers = QgsProject.instance().mapLayersByName(oname)
            for layer in layers:
                QgsProject.instance().removeMapLayer(layer.id())

            # Update SpatiaLite System Tables
            # We must update geometry_columns to keep the layer "spatial"
            queries = [
                f"ALTER TABLE {oname} RENAME TO {nname}",
                f"UPDATE geometry_columns SET f_table_name='{nname}' WHERE f_table_name='{oname}'",
                f"UPDATE geometry_columns_auth SET f_table_name='{nname}' WHERE f_table_name='{oname}'",
                f"UPDATE geometry_columns_field_infos SET f_table_name='{nname}' WHERE f_table_name='{oname}'",
                f"UPDATE geometry_columns_statistics SET f_table_name='{nname}' WHERE f_table_name='{oname}'"
            ]

            for sql in queries:
                self.db.exec_(sql)
            
            self.db.commit()
            self.loadLayers()

    def deLayer(self):
        """Drops a table and cleans up spatial metadata"""
        idx_list = self.tableView_layers.selectionModel().selectedIndexes()
        if not idx_list:
            return

        tname = str(self.model2.data(idx_list[0]))
        
        reply = QMessageBox.question(self, 'Confirmation', 
                                    f"Permanently delete layer '{tname}' and all its data?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Remove from QGIS Legend
            layers = QgsProject.instance().mapLayersByName(tname)
            for layer in layers:
                QgsProject.instance().removeMapLayer(layer.id())

            # Cleanup SpatiaLite metadata
            self.db.exec_(f"SELECT DiscardGeometryColumn('{tname}', 'geom')") # Adjust 'geom' if column name varies
            self.db.exec_(f"DROP TABLE {tname}")
            self.db.exec_(f"DELETE FROM geometry_columns WHERE f_table_name='{tname}'")
            self.db.commit()
            self.loadLayers()

    def tabUpdate(self):
        """Updates the list view for species, diseases, or vaccines based on selection"""
        table_map = {
            'Species': "SELECT name_en, moa_code FROM xspecies ORDER BY name_en",
            'Diseases': "SELECT name_en, moa_code FROM xdiseases ORDER BY name_en",
            'Vaccines': "SELECT vac_name, vac_code FROM xvaccines ORDER BY vac_name"
        }
        
        list_type = self.comboBox_lists.currentText()
        sql = table_map.get(list_type, "")
        
        if sql:
            self.model = QSqlQueryModel()
            self.model.setQuery(sql, self.db)
            self.tableView_lists.setModel(self.model)
            self.tableView_lists.horizontalHeader().setStretchLastSection(True)

    def itemSel(self):
        """Handles selecting an item for local naming (e.g. Amharic labels)"""
        idx_list = self.tableView_lists.selectionModel().selectedIndexes()
        if not idx_list:
            return

        # Note: In the EthioVet structure, we use columns name_en, moa_code, etc.
        # This logic fetches the localized variant if supported
        idx = idx_list[0]
        val = str(self.model.data(idx))
        self.lineEdit_translation.setText(val)
        self.lineEdit_translation.setFocus()

    def saveEn(self):
        """Adds a new item to the MoA Dictionary"""
        list_type = self.comboBox_lists.currentText()
        dlg = insdlg()
        dlg.setWindowTitle(f"Add New {list_type}")
        
        if dlg.exec_() == QDialog.Accepted:
            new_val = dlg.lineEdit.text()
            if list_type == 'Species':
                sql = f"INSERT INTO xspecies (name_en, moa_code) VALUES ('{new_val}', 99)" # Default 99 for unknown
            elif list_type == 'Diseases':
                sql = f"INSERT INTO xdiseases (name_en, moa_code, alpha_code, category) VALUES ('{new_val}', '00', 'UNK', 'Other')"
            
            self.db.exec_(sql)
            self.db.commit()
            self.tabUpdate()

    def saveTrans(self):
        """Updates a dictionary item name"""
        new_text = self.lineEdit_translation.text()
        if not new_text:
            return

        idx_list = self.tableView_lists.selectionModel().selectedIndexes()
        if len(idx_list) < 2: return
        
        # Identifier is in the second column (moa_code or vac_code)
        id_val = str(self.model.data(idx_list[1]))
        list_type = self.comboBox_lists.currentText()
        
        if list_type == 'Species':
            sql = f"UPDATE xspecies SET name_en='{new_text}' WHERE moa_code='{id_val}'"
        elif list_type == 'Diseases':
            sql = f"UPDATE xdiseases SET name_en='{new_text}' WHERE moa_code='{id_val}'"
        elif list_type == 'Vaccines':
            sql = f"UPDATE xvaccines SET vac_name='{new_text}' WHERE vac_code='{id_val}'"
        else:
            return

        self.db.exec_(sql)
        self.db.commit()
        self.tabUpdate()
        self.lineEdit_translation.clear()
