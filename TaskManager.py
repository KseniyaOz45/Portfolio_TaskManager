import os

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

import CU_menu_window
import db_helper
import main_menu


class TaskManager(QMainWindow):
    got_id = QtCore.pyqtSignal(int)

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
        self.load_uncompleted_tasks()
        self.load_completed_tasks()

        self.ui.actionUnselect_all_actual_tasks.triggered.connect(self.unselect_all_actual_tasks)
        self.ui.actionUnselect_All_complete_tasks.triggered.connect(self.unselect_all_complete_tasks)
        self.ui.actionAdd_new.triggered.connect(self.start_task_creation)

    def init_db(self):
        files = os.listdir()
        if 'tasks.db' not in files:
            self.db.create_tables()

    def load_uncompleted_tasks(self):
        self.uncompleted_tasks.clear()
        self.ui.actual_tasks_list.clear()

        self.uncompleted_tasks = self.db.get_completed_uncompleted_tasks('Uncomplete')

        for task in self.uncompleted_tasks:
            self.ui.actual_tasks_list.addItem(task.name)

    def load_completed_tasks(self):
        self.completed_tasks.clear()
        self.ui.complete_tasks_list.clear()

        self.completed_tasks = self.db.get_completed_uncompleted_tasks('Complete')

        for task in self.completed_tasks:
            self.ui.complete_tasks_list.addItem(task.name)

    def start_task_creation(self):
        self.cu_menu = CU_menu_window.CU_Menu()
        self.cu_menu.got_status.connect(self.create_task)
        self.cu_menu.show()

    def create_task(self, status):
        self.ui.statusbar.setStatusTip(status)
        self.load_uncompleted_tasks()

    def unselect_all_actual_tasks(self):
        self.ui.actual_tasks_list.clearSelection()

    def unselect_all_complete_tasks(self):
        self.ui.complete_tasks_list.clearSelection()
