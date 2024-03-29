# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 930)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(555, 930))
        MainWindow.setMaximumSize(QtCore.QSize(555, 930))
        MainWindow.setStyleSheet("background-color: #111933;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #087cc0;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.actual_tasks_list = QtWidgets.QListWidget(self.centralwidget)
        self.actual_tasks_list.setMinimumSize(QtCore.QSize(535, 305))
        self.actual_tasks_list.setMaximumSize(QtCore.QSize(535, 305))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.actual_tasks_list.setFont(font)
        self.actual_tasks_list.setStyleSheet("QListWidget{\n"
"    background-color: #087cc0;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 10px;\n"
"    border: 1px solid #087cc0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QListWidget::item:hover{\n"
"    background-color: #0d4273;\n"
"}\n"
"\n"
"QListWidget::item:selected{\n"
"    background-color: #0d4273;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background:#087cc0;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: #0d5377;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:#03d3f2;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #03d3f2;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.actual_tasks_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.actual_tasks_list.setWordWrap(True)
        self.actual_tasks_list.setObjectName("actual_tasks_list")
        self.verticalLayout.addWidget(self.actual_tasks_list)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_new_task_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_new_task_Btn.sizePolicy().hasHeightForWidth())
        self.create_new_task_Btn.setSizePolicy(sizePolicy)
        self.create_new_task_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.create_new_task_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.create_new_task_Btn.setObjectName("create_new_task_Btn")
        self.horizontalLayout.addWidget(self.create_new_task_Btn)
        self.update_selected_task_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_selected_task_Btn.sizePolicy().hasHeightForWidth())
        self.update_selected_task_Btn.setSizePolicy(sizePolicy)
        self.update_selected_task_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.update_selected_task_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.update_selected_task_Btn.setObjectName("update_selected_task_Btn")
        self.horizontalLayout.addWidget(self.update_selected_task_Btn)
        self.delete_selected_task_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_selected_task_Btn.sizePolicy().hasHeightForWidth())
        self.delete_selected_task_Btn.setSizePolicy(sizePolicy)
        self.delete_selected_task_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.delete_selected_task_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.delete_selected_task_Btn.setObjectName("delete_selected_task_Btn")
        self.horizontalLayout.addWidget(self.delete_selected_task_Btn)
        self.delete_all_tasks_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_all_tasks_Btn.sizePolicy().hasHeightForWidth())
        self.delete_all_tasks_Btn.setSizePolicy(sizePolicy)
        self.delete_all_tasks_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.delete_all_tasks_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.delete_all_tasks_Btn.setObjectName("delete_all_tasks_Btn")
        self.horizontalLayout.addWidget(self.delete_all_tasks_Btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.show_task_details_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_task_details_Btn.sizePolicy().hasHeightForWidth())
        self.show_task_details_Btn.setSizePolicy(sizePolicy)
        self.show_task_details_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.show_task_details_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.show_task_details_Btn.setObjectName("show_task_details_Btn")
        self.horizontalLayout.addWidget(self.show_task_details_Btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: #087cc0;\n"
"margin: 20px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #087cc0;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.complete_tasks_list = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.complete_tasks_list.setFont(font)
        self.complete_tasks_list.setStyleSheet("QListWidget{\n"
"    background-color: #087cc0;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 10px;\n"
"    border: 1px solid #087cc0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QListWidget::item:hover{\n"
"    background-color: #0d4273;\n"
"}\n"
"\n"
"QListWidget::item:selected{\n"
"    background-color: #0d4273;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background:#087cc0;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: #0d5377;\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:#03d3f2;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #03d3f2;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.complete_tasks_list.setObjectName("complete_tasks_list")
        self.verticalLayout_2.addWidget(self.complete_tasks_list)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete_selected_complete_task_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_selected_complete_task_Btn.sizePolicy().hasHeightForWidth())
        self.delete_selected_complete_task_Btn.setSizePolicy(sizePolicy)
        self.delete_selected_complete_task_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.delete_selected_complete_task_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.delete_selected_complete_task_Btn.setObjectName("delete_selected_complete_task_Btn")
        self.horizontalLayout_2.addWidget(self.delete_selected_complete_task_Btn)
        self.delete_all_completed_tasks_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_all_completed_tasks_Btn.sizePolicy().hasHeightForWidth())
        self.delete_all_completed_tasks_Btn.setSizePolicy(sizePolicy)
        self.delete_all_completed_tasks_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.delete_all_completed_tasks_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.delete_all_completed_tasks_Btn.setObjectName("delete_all_completed_tasks_Btn")
        self.horizontalLayout_2.addWidget(self.delete_all_completed_tasks_Btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.show_completed_task_details_Btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_completed_task_details_Btn.sizePolicy().hasHeightForWidth())
        self.show_completed_task_details_Btn.setSizePolicy(sizePolicy)
        self.show_completed_task_details_Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.show_completed_task_details_Btn.setStyleSheet("QPushButton{\n"
"\n"
"    border: 2px solid #087cc0;\n"
"    color: #087cc0;\n"
"    font: 75 14pt \"Book Antiqua\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(25, 38, 76);\n"
"}\n"
"\n"
"")
        self.show_completed_task_details_Btn.setObjectName("show_completed_task_details_Btn")
        self.horizontalLayout_2.addWidget(self.show_completed_task_details_Btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 73))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("QMenuBar{\n"
"    padding: 10px;\n"
"    margin: 10px;\n"
"    background-color: #087cc0;\n"
"    border:2px solid #087cc0;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"    background-color:#0d4273;\n"
"}\n"
"\n"
"QMenu{\n"
"    background-color: #0d4273;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item{\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"    background-color: #087cc0;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuTASKS = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menuTASKS.setFont(font)
        self.menuTASKS.setObjectName("menuTASKS")
        self.menuSELECTION = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menuSELECTION.setFont(font)
        self.menuSELECTION.setObjectName("menuSELECTION")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("QStatusBar{\n"
"    color: #087cc0;\n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_new = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.actionAdd_new.setFont(font)
        self.actionAdd_new.setObjectName("actionAdd_new")
        self.actionUpdate_selected = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.actionUpdate_selected.setFont(font)
        self.actionUpdate_selected.setObjectName("actionUpdate_selected")
        self.actionDelete_selected = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.actionDelete_selected.setFont(font)
        self.actionDelete_selected.setObjectName("actionDelete_selected")
        self.actionClear_all = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.actionClear_all.setFont(font)
        self.actionClear_all.setObjectName("actionClear_all")
        self.actionUnselect_all_actual_tasks = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.actionUnselect_all_actual_tasks.setFont(font)
        self.actionUnselect_all_actual_tasks.setObjectName("actionUnselect_all_actual_tasks")
        self.actionShow_details_of_selected = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.actionShow_details_of_selected.setFont(font)
        self.actionShow_details_of_selected.setObjectName("actionShow_details_of_selected")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionUnselect_All_complete_tasks = QtWidgets.QAction(MainWindow)
        self.actionUnselect_All_complete_tasks.setObjectName("actionUnselect_All_complete_tasks")
        self.menuTASKS.addAction(self.actionAdd_new)
        self.menuTASKS.addAction(self.actionUpdate_selected)
        self.menuTASKS.addAction(self.actionDelete_selected)
        self.menuTASKS.addAction(self.actionClear_all)
        self.menuTASKS.addSeparator()
        self.menuTASKS.addAction(self.actionShow_details_of_selected)
        self.menuSELECTION.addAction(self.actionUnselect_all_actual_tasks)
        self.menuSELECTION.addAction(self.actionUnselect_All_complete_tasks)
        self.menubar.addAction(self.menuTASKS.menuAction())
        self.menubar.addAction(self.menuSELECTION.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Actual tasks:"))
        self.create_new_task_Btn.setText(_translate("MainWindow", "ADD"))
        self.update_selected_task_Btn.setText(_translate("MainWindow", "UPD"))
        self.delete_selected_task_Btn.setText(_translate("MainWindow", "DEL"))
        self.delete_all_tasks_Btn.setText(_translate("MainWindow", "CLEAR"))
        self.show_task_details_Btn.setText(_translate("MainWindow", "INFO"))
        self.label_2.setText(_translate("MainWindow", "Completed tasks:"))
        self.delete_selected_complete_task_Btn.setText(_translate("MainWindow", "DEL"))
        self.delete_all_completed_tasks_Btn.setText(_translate("MainWindow", "CLEAR"))
        self.show_completed_task_details_Btn.setText(_translate("MainWindow", "INFO"))
        self.menuTASKS.setTitle(_translate("MainWindow", "TASKS"))
        self.menuSELECTION.setTitle(_translate("MainWindow", "SELECTION"))
        self.actionAdd_new.setText(_translate("MainWindow", "Add new"))
        self.actionUpdate_selected.setText(_translate("MainWindow", "Update selected"))
        self.actionDelete_selected.setText(_translate("MainWindow", "Delete selected"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))
        self.actionUnselect_all_actual_tasks.setText(_translate("MainWindow", "Unselect All Actual Tasks"))
        self.actionShow_details_of_selected.setText(_translate("MainWindow", "Show details of selected"))
        self.action_2.setText(_translate("MainWindow", "ТЕСТ"))
        self.actionUnselect_All_complete_tasks.setText(_translate("MainWindow", "Unselect All Complete Tasks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
