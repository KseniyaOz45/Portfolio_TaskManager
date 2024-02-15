import datetime

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from datetime import datetime

import cu_menu
import db_helper


class CU_Menu(QMainWindow):

    got_status = QtCore.pyqtSignal(str)

    def __init__(self):
        super(CU_Menu, self).__init__()
        self.ui = cu_menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = db_helper.DB_helper()

        self.ui.discard_changes_Btn.clicked.connect(self.back)
        self.ui.save_changes_Btn.clicked.connect(self.create_task)

    def back(self):
        self.close()

    def create_task(self):
        data = {
            'task_name': self.ui.task_name_field.text(),
            'task_desc': self.ui.task_description_field.toPlainText(),
            'start_date': datetime.now().date(),
            'exp_date': self.ui.expiration_date_spinner.date().toPyDate(),
            'status': 'Uncomplete'
        }
        status = self.db.create_new_task(data)
        self.got_status.emit(status)
        self.close()

