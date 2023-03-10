from PyQt6 import QtCore, QtGui,QtWidgets

from Views.run_session import RunningGraphsUi


class ControlSessionBoardUi(object):
    def __init__(self, parent):
        self.parent = parent
        # self.create_session_ui = parent.parent.main_window
        self.vm = self.parent.vm
        self.gridLayout = None
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.stop_pushButton = None
        self.running_buttons_horizontalLayout = QtWidgets.QHBoxLayout()
        self.pause_pushButton = None
        self.resume_pushButton = None
        self.actions_during_horizontalLayout = QtWidgets.QHBoxLayout()
        self.repeat_trial_pushButton = None
        self.present_data_pushButton = None
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.reward_pushButton = None
        self.reward_comboBox = None
        self.finish_pushButton = None
        self.data_window = QtWidgets.QDialog()
        self.data_ui = None

    def setupUi(self, dialog):
        # open a session's data in the background
        self.data_ui = RunningGraphsUi(self)
        self.data_ui.setupUi(self.data_window)
        self.data_window.hide()
        self.parent.parent.main_window.close()  # close create session window
        self.parent.parent.parent.main_window.show()  # open main system window
        self.parent.parent.parent.control_session_board = dialog
        dialog.setObjectName("dialog")
        dialog.resize(321, 195)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.setObjectName("verticalLayout")
        # create buttons to control running a session
        self.stop_pushButton = QtWidgets.QPushButton(dialog)
        self.stop_pushButton.clicked.connect(self.on_stop_click)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.verticalLayout.addWidget(self.stop_pushButton)
        self.running_buttons_horizontalLayout.setObjectName("running_buttons_horizontalLayout")
        self.pause_pushButton = QtWidgets.QPushButton(dialog)
        self.pause_pushButton.clicked.connect(self.on_pause_click)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.running_buttons_horizontalLayout.addWidget(self.pause_pushButton)
        self.resume_pushButton = QtWidgets.QPushButton(dialog)
        self.resume_pushButton.clicked.connect(self.on_resume_click)
        self.resume_pushButton.setObjectName("resume_pushButton")
        self.running_buttons_horizontalLayout.addWidget(self.resume_pushButton)
        self.verticalLayout.addLayout(self.running_buttons_horizontalLayout)
        # actions during a running
        self.actions_during_horizontalLayout.setObjectName("actions_during_horizontalLayout")
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.actions_during_horizontalLayout.addItem(spacer_item)
        self.repeat_trial_pushButton = QtWidgets.QPushButton(dialog)
        self.repeat_trial_pushButton.clicked.connect(self.on_repeat_trial_click)
        self.repeat_trial_pushButton.setObjectName("repeat_trial_pushButton")
        self.actions_during_horizontalLayout.addWidget(self.repeat_trial_pushButton)
        self.present_data_pushButton = QtWidgets.QPushButton(dialog)
        self.present_data_pushButton.clicked.connect(self.on_present_data_click)
        self.present_data_pushButton.setObjectName("present_data_pushButton")
        self.actions_during_horizontalLayout.addWidget(self.present_data_pushButton)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.actions_during_horizontalLayout.addItem(spacer_item1)
        self.actions_during_horizontalLayout.setStretch(0, 1)
        self.actions_during_horizontalLayout.setStretch(1, 1)
        self.actions_during_horizontalLayout.setStretch(2, 1)
        self.actions_during_horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.actions_during_horizontalLayout)

        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item2)
        self.reward_pushButton = QtWidgets.QPushButton(dialog)
        self.reward_pushButton.setObjectName("reward_pushButton")
        self.reward_pushButton.clicked.connect(self.on_give_reward_click)
        self.horizontalLayout_2.addWidget(self.reward_pushButton)
        self.reward_comboBox = QtWidgets.QComboBox(dialog)
        self.reward_comboBox.setObjectName("reward_comboBox")
        self.reward_comboBox.addItems(self.vm.get_reward_name_list_for_session())
        self.horizontalLayout_2.addWidget(self.reward_comboBox)
        spacer_item3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item3)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacer_item4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item4)
        self.finish_pushButton = QtWidgets.QPushButton(dialog)
        self.finish_pushButton.clicked.connect(self.on_finish_click)
        self.finish_pushButton.setObjectName("finish_pushButton")
        self.verticalLayout.addWidget(self.finish_pushButton)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def on_give_reward_click(self):
        curr_text = self.reward_comboBox.currentText()
        if curr_text != "":
            self.vm.give_reward(curr_text)
        pass

    def on_stop_click(self):
        self.parent.parent.vm.end_Session()
        # show data, enable finish button, go back to main window?
        pass

    def on_pause_click(self):
        self.parent.parent.vm.pause_sess()
        pass

    def on_resume_click(self):
        self.parent.parent.vm.resume_sess()
        pass

    def on_repeat_trial_click(self):
        self.parent.parent.vm.repeat_trial()
        pass

    def on_present_data_click(self):
        # open a session's data
        # self.data_ui = RunningGraphsUi(self)
        # self.data_ui.setupUi(self.data_window)
        self.data_window.show()

    def on_finish_click(self):
        pass

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Control session board"))
        self.stop_pushButton.setText(_translate("dialog", "Stop"))
        self.pause_pushButton.setText(_translate("dialog", "Pause"))
        self.resume_pushButton.setText(_translate("dialog", "Resume"))
        self.repeat_trial_pushButton.setText(_translate("dialog", "Repeat trial"))
        self.present_data_pushButton.setText(_translate("dialog", "Present data"))
        self.reward_pushButton.setText(_translate("dialog", "Give reward"))
        self.finish_pushButton.setText(_translate("dialog", "Finish"))

