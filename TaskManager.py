import os

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic.properties import QtCore

import db_helper
import main_menu


class TaskManager(QMainWindow):
    got_name = QtCore.pyqtSignal(str)

    def __init__(self):
        super(TaskManager, self).__init__()
        self.ui = main_menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = db_helper.DB_helper()

        self.cu_menu = None
        self.details_menu = None

        self.uncompleted_tasks = []
        self.completed_tasks = []

        self.init_db()

        self.ui.actionUnselect_all_actual_tasks.triggered.connect(self.unselect_all_actual_tasks)
        self.ui.actionUnselect_All_complete_tasks.triggered.connect(self.unselect_all_complete_tasks)

    def init_db(self):
        files = os.listdir()
        if 'tasks.db' not in files:
            self.db.create_tables()

    def unselect_all_actual_tasks(self):
        self.ui.actual_tasks_list.clearSelection()

    def unselect_all_complete_tasks(self):
        self.ui.complete_tasks_list.clearSelection()
