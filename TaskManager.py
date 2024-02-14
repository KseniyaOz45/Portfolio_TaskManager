from PyQt5.QtWidgets import QMainWindow

import main_menu


class TaskManager(QMainWindow):
    def __init__(self):
        super(TaskManager, self).__init__()
        self.ui = main_menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.cu_menu = None
        self.details_menu = None

        self.ui.actionUnselect_all_actual_tasks.triggered.connect(self.unselect_all_actual_tasks)
        self.ui.actionUnselect_All_complete_tasks.triggered.connect(self.unselect_all_complete_tasks)

    def unselect_all_actual_tasks(self):
        self.ui.actual_tasks_list.clearSelection()

    def unselect_all_complete_tasks(self):
        self.ui.complete_tasks_list.clearSelection()
