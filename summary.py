# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from app import Ui_MainWindow


class Ui_SUMMARY(object):

    # def openWindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()


    def setupUi(self, SUMMARY):
        SUMMARY.setObjectName("SUMMARY")
        SUMMARY.resize(643, 474)
        SUMMARY.setWindowTitle("SUMMARY DISPLAY")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/about_dis.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SUMMARY.setWindowIcon(icon)
        SUMMARY.setStyleSheet("")
        self.formLayout = QtWidgets.QFormLayout(SUMMARY)
        self.formLayout.setObjectName("formLayout")
        self.summary_head = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.summary_head.setFont(font)
        self.summary_head.setStyleSheet("color: rgb(0, 0, 0);")
        self.summary_head.setObjectName("summary_head")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.summary_head)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Span_length_for_inline_flow_viv = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Span_length_for_inline_flow_viv.setFont(font)
        self.Span_length_for_inline_flow_viv.setObjectName("Span_length_for_inline_flow_viv")
        self.horizontalLayout.addWidget(self.Span_length_for_inline_flow_viv)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Span_length_for_inline_flow_viv_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Span_length_for_inline_flow_viv_value.setFont(font)
        self.Span_length_for_inline_flow_viv_value.setObjectName("Span_length_for_inline_flow_viv_value")
        self.horizontalLayout.addWidget(self.Span_length_for_inline_flow_viv_value)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spanlength_for_crossflow_viv = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spanlength_for_crossflow_viv.setFont(font)
        self.spanlength_for_crossflow_viv.setObjectName("spanlength_for_crossflow_viv")
        self.horizontalLayout_2.addWidget(self.spanlength_for_crossflow_viv)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.spanlength_for_crossflow_viv_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spanlength_for_crossflow_viv_value.setFont(font)
        self.spanlength_for_crossflow_viv_value.setObjectName("spanlength_for_crossflow_viv_value")
        self.horizontalLayout_2.addWidget(self.spanlength_for_crossflow_viv_value)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spanlength_for_crossflow_uls = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spanlength_for_crossflow_uls.setFont(font)
        self.spanlength_for_crossflow_uls.setObjectName("spanlength_for_crossflow_uls")
        self.horizontalLayout_3.addWidget(self.spanlength_for_crossflow_uls)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.spanlength_for_crossflow_uls_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spanlength_for_crossflow_uls_value.setFont(font)
        self.spanlength_for_crossflow_uls_value.setObjectName("spanlength_for_crossflow_uls_value")
        self.horizontalLayout_3.addWidget(self.spanlength_for_crossflow_uls_value)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spanlength_for_inlineflow_uls = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spanlength_for_inlineflow_uls.setFont(font)
        self.spanlength_for_inlineflow_uls.setObjectName("spanlength_for_inlineflow_uls")
        self.horizontalLayout_4.addWidget(self.spanlength_for_inlineflow_uls)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.spanlength_for_inlineflow_uls_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spanlength_for_inlineflow_uls_value.setFont(font)
        self.spanlength_for_inlineflow_uls_value.setObjectName("spanlength_for_inlineflow_uls_value")
        self.horizontalLayout_4.addWidget(self.spanlength_for_inlineflow_uls_value)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.maximum_deflection = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maximum_deflection.setFont(font)
        self.maximum_deflection.setObjectName("maximum_deflection")
        self.horizontalLayout_5.addWidget(self.maximum_deflection)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.maximum_deflection_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maximum_deflection_value.setFont(font)
        self.maximum_deflection_value.setObjectName("maximum_deflection_value")
        self.horizontalLayout_5.addWidget(self.maximum_deflection_value)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bar_buckling_criteria = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bar_buckling_criteria.setFont(font)
        self.bar_buckling_criteria.setObjectName("bar_buckling_criteria")
        self.horizontalLayout_6.addWidget(self.bar_buckling_criteria)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.bar_buckling_criteria_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bar_buckling_criteria_value.setFont(font)
        self.bar_buckling_criteria_value.setObjectName("bar_buckling_criteria_value")
        self.horizontalLayout_6.addWidget(self.bar_buckling_criteria_value)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.model_length_validity = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.model_length_validity.setFont(font)
        self.model_length_validity.setObjectName("model_length_validity")
        self.horizontalLayout_7.addWidget(self.model_length_validity)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.model_length_validity_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.model_length_validity_value.setFont(font)
        self.model_length_validity_value.setObjectName("model_length_validity_value")
        self.horizontalLayout_7.addWidget(self.model_length_validity_value)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.overall_max_allowable_spanlength = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.overall_max_allowable_spanlength.setFont(font)
        self.overall_max_allowable_spanlength.setObjectName("overall_max_allowable_spanlength")
        self.horizontalLayout_8.addWidget(self.overall_max_allowable_spanlength)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.overall_max_allowable_spanlength_value = QtWidgets.QLabel(SUMMARY)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.overall_max_allowable_spanlength_value.setFont(font)
        self.overall_max_allowable_spanlength_value.setObjectName("overall_max_allowable_spanlength_value")
        self.horizontalLayout_8.addWidget(self.overall_max_allowable_spanlength_value)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 395, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(593, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem9)

        self.retranslateUi(SUMMARY)
        QtCore.QMetaObject.connectSlotsByName(SUMMARY)

    def retranslateUi(self, SUMMARY):
        _translate = QtCore.QCoreApplication.translate
        SUMMARY.setToolTip(_translate("SUMMARY", "Summary"))
        SUMMARY.setStatusTip(_translate("SUMMARY", "Summary Display"))
        self.summary_head.setText(_translate("SUMMARY", "SUMMARY"))
        self.Span_length_for_inline_flow_viv.setText(_translate("SUMMARY", "Span Length for Inline Flow VIV [LVIV in]"))
        self.Span_length_for_inline_flow_viv_value.setText(_translate("SUMMARY", "TextLabel"))
        self.spanlength_for_crossflow_viv.setText(_translate("SUMMARY", "Span Length for Cross Flow VIV [LVIV cr]"))
        self.spanlength_for_crossflow_viv_value.setText(_translate("SUMMARY", "TextLabel"))
        self.spanlength_for_crossflow_uls.setText(_translate("SUMMARY", "Span Length for Cross Flow ULS [LULS cr]"))
        self.spanlength_for_crossflow_uls_value.setText(_translate("SUMMARY", "TextLabel"))
        self.spanlength_for_inlineflow_uls.setText(_translate("SUMMARY", "Span Length for Inline Flow ULS [LULS in]"))
        self.spanlength_for_inlineflow_uls_value.setText(_translate("SUMMARY", "TextLabel"))
        self.maximum_deflection.setText(_translate("SUMMARY", "Maximum Deflection"))
        self.maximum_deflection_value.setText(_translate("SUMMARY", "TextLabel"))
        self.bar_buckling_criteria.setText(_translate("SUMMARY", "Bar Buckling Criteria"))
        self.bar_buckling_criteria_value.setText(_translate("SUMMARY", "TextLabel"))
        self.model_length_validity.setText(_translate("SUMMARY", "Model Length Validity"))
        self.model_length_validity_value.setText(_translate("SUMMARY", "TextLabel"))
        self.overall_max_allowable_spanlength.setText(_translate("SUMMARY", "Overall Maximum Allowable Span Length"))
        self.overall_max_allowable_spanlength_value.setText(_translate("SUMMARY", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SUMMARY = QtWidgets.QDialog()
    ui = Ui_SUMMARY()
    ui.setupUi(SUMMARY)
    SUMMARY.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("\n\tApplication is closing..!!")