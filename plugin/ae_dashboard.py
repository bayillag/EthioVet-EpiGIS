from qgis.PyQt.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel, QComboBox, QFrame, QGridLayout, QPushButton
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtSql import QSqlQuery

class EthioVetDBAEDashboard(QDockWidget):
    def __init__(self, iface, db_conn):
        super().__init__("EthioVetDB: Vaccine Safety Dashboard")
        self.iface = iface
        self.db = db_conn
        
        self.root = QWidget()
        self.layout = QVBoxLayout(self.root)
        
        # 1. Selection Header
        header = QLabel("<b>VACCINE ADVERSE EVENTS (VAE)</b>")
        header.setStyleSheet("font-size: 14px; color: #8e44ad;")
        self.layout.addWidget(header)
        
        self.cmb_mon = QComboBox()
        self.cmb_mon.addItems([f"{i:02d}" for i in range(1, 13)])
        self.layout.addWidget(self.cmb_mon)

        # 2. KPI Cards
        self.grid = QGridLayout()
        self.kpi_total_ae = self.add_kpi("Total Events", "0", "#9b59b6") # Amethyst
        self.kpi_reacted = self.add_kpi("Animals Reacted", "0", "#8e44ad") # Purple
        self.kpi_deaths = self.add_kpi("VAE Deaths", "0", "#2c3e50") # Midnight Blue
        
        self.grid.addWidget(self.kpi_total_ae, 0, 0)
        self.grid.addWidget(self.kpi_reacted, 0, 1)
        self.grid.addWidget(self.kpi_deaths, 1, 0)
        
        self.layout.addLayout(self.grid)

        # 3. Batch Watchlist
        self.layout.addWidget(QLabel("<b>High-Risk Batch Watchlist:</b>"))
        self.lbl_batch_warning = QLabel("No high-risk batches detected.")
        self.lbl_batch_warning.setWordWrap(True)
        self.lbl_batch_warning.setStyleSheet("padding: 10px; background-color: #ecf0f1; border-radius: 5px;")
        self.layout.addWidget(self.lbl_batch_warning)

        # 4. Action Buttons
        self.btn_refresh = QPushButton("🔄 Update Safety Stats")
        self.btn_refresh.clicked.connect(self.update_ae_stats)
        self.layout.addWidget(self.btn_refresh)
        
        self.btn_vdfaca = QPushButton("📄 Generate VDFACA Report")
        self.btn_vdfaca.setStyleSheet("background-color: #8e44ad; color: white; font-weight: bold;")
        self.layout.addWidget(self.btn_vdfaca)

        self.layout.addStretch()
        self.setWidget(self.root)

    def add_kpi(self, title, val, color):
        frame = QFrame()
        frame.setStyleSheet(f"background-color: {color}; border-radius: 5px; padding: 10px;")
        l = QVBoxLayout(frame)
        t = QLabel(title.upper())
        t.setStyleSheet("color: white; font-size: 9px; font-weight: bold;")
        v = QLabel(val)
        v.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        l.addWidget(t)
        l.addWidget(v)
        frame.val_label = v
        return frame

    def update_ae_stats(self):
        month = self.cmb_mon.currentText()
        query = QSqlQuery(self.db)
        
        # Aggregate Monthly Totals
        sql = f"SELECT COUNT(*), SUM(num_animals_reacted), SUM(num_deaths) FROM xvaccines_adverse_events WHERE strftime('%m', date_report_filed) = '{month}'"
        if query.exec_(sql) and query.next():
            self.kpi_total_ae.val_label.setText(str(query.value(0) or 0))
            self.kpi_reacted.val_label.setText(str(query.value(1) or 0))
            self.kpi_deaths.val_label.setText(str(query.value(2) or 0))

        # Check for Critical Batches (3 or more events for one batch)
        warning_sql = f"""
            SELECT batch_number, vac_name, total_events 
            FROM v_dashboard_adverse_events 
            WHERE month = '{month}' AND total_events >= 3
        """
        warnings = []
        if query.exec_(warning_sql):
            while query.next():
                warnings.append(f"⚠️ {query.value(1)} (Batch: {query.value(0)}) - {query.value(2)} events")
        
        if warnings:
            self.lbl_batch_warning.setText("\n".join(warnings))
            self.lbl_batch_warning.setStyleSheet("padding: 10px; background-color: #f1c40f; color: black; font-weight: bold;")
        else:
            self.lbl_batch_warning.setText("All batches within safety thresholds.")
            self.lbl_batch_warning.setStyleSheet("padding: 10px; background-color: #ecf0f1;")
