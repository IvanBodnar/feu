# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/gui_feu.ui'
#
# Created: Sun May 22 19:28:37 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(616, 749)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox_NumeroHecho = QtGui.QSpinBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_NumeroHecho.sizePolicy().hasHeightForWidth())
        self.spinBox_NumeroHecho.setSizePolicy(sizePolicy)
        self.spinBox_NumeroHecho.setMaximum(10000)
        self.spinBox_NumeroHecho.setObjectName(_fromUtf8("spinBox_NumeroHecho"))
        self.horizontalLayout_2.addWidget(self.spinBox_NumeroHecho)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.fecha_dateEdit = QtGui.QDateEdit(self.tab)
        self.fecha_dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.fecha_dateEdit.setObjectName(_fromUtf8("fecha_dateEdit"))
        self.horizontalLayout.addWidget(self.fecha_dateEdit)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.hora_timeEdit = QtGui.QTimeEdit(self.tab)
        self.hora_timeEdit.setObjectName(_fromUtf8("hora_timeEdit"))
        self.horizontalLayout.addWidget(self.hora_timeEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.calle1_comboBox = QtGui.QComboBox(self.tab)
        self.calle1_comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.calle1_comboBox.setEditable(True)
        self.calle1_comboBox.setObjectName(_fromUtf8("calle1_comboBox"))
        self.gridLayout.addWidget(self.calle1_comboBox, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.calle2_comboBox = QtGui.QComboBox(self.tab)
        self.calle2_comboBox.setEditable(True)
        self.calle2_comboBox.setObjectName(_fromUtf8("calle2_comboBox"))
        self.gridLayout.addWidget(self.calle2_comboBox, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.tipoArteria1_comboBox = QtGui.QComboBox(self.tab)
        self.tipoArteria1_comboBox.setObjectName(_fromUtf8("tipoArteria1_comboBox"))
        self.gridLayout.addWidget(self.tipoArteria1_comboBox, 0, 3, 1, 1)
        self.tipoArteria2_comboBox = QtGui.QComboBox(self.tab)
        self.tipoArteria2_comboBox.setObjectName(_fromUtf8("tipoArteria2_comboBox"))
        self.gridLayout.addWidget(self.tipoArteria2_comboBox, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.altura_spinBox = QtGui.QSpinBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.altura_spinBox.sizePolicy().hasHeightForWidth())
        self.altura_spinBox.setSizePolicy(sizePolicy)
        self.altura_spinBox.setObjectName(_fromUtf8("altura_spinBox"))
        self.horizontalLayout_3.addWidget(self.altura_spinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.tipoSiniestro_comboBox = QtGui.QComboBox(self.tab)
        self.tipoSiniestro_comboBox.setObjectName(_fromUtf8("tipoSiniestro_comboBox"))
        self.horizontalLayout_4.addWidget(self.tipoSiniestro_comboBox)
        self.label_10 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.tipoColision_comboBox = QtGui.QComboBox(self.tab)
        self.tipoColision_comboBox.setObjectName(_fromUtf8("tipoColision_comboBox"))
        self.horizontalLayout_4.addWidget(self.tipoColision_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.totalHeridos_spinBox = QtGui.QSpinBox(self.tab)
        self.totalHeridos_spinBox.setObjectName(_fromUtf8("totalHeridos_spinBox"))
        self.horizontalLayout_5.addWidget(self.totalHeridos_spinBox)
        self.label_12 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_5.addWidget(self.label_12)
        self.totalObitos_spinBox = QtGui.QSpinBox(self.tab)
        self.totalObitos_spinBox.setObjectName(_fromUtf8("totalObitos_spinBox"))
        self.horizontalLayout_5.addWidget(self.totalObitos_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_13 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_6.addWidget(self.label_13)
        self.entidadInstructora_comboBox = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entidadInstructora_comboBox.sizePolicy().hasHeightForWidth())
        self.entidadInstructora_comboBox.setSizePolicy(sizePolicy)
        self.entidadInstructora_comboBox.setObjectName(_fromUtf8("entidadInstructora_comboBox"))
        self.horizontalLayout_6.addWidget(self.entidadInstructora_comboBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.pushButton_AgregarDato = QtGui.QPushButton(self.tab)
        self.pushButton_AgregarDato.setObjectName(_fromUtf8("pushButton_AgregarDato"))
        self.verticalLayout_2.addWidget(self.pushButton_AgregarDato)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Numero de Hecho:", None))
        self.label.setText(_translate("Dialog", "Fecha:", None))
        self.label_2.setText(_translate("Dialog", "Hora:", None))
        self.label_6.setText(_translate("Dialog", "Tipo de arteria 1:", None))
        self.label_7.setText(_translate("Dialog", "Tipo de arteria 2:", None))
        self.label_5.setText(_translate("Dialog", "Calle 2:", None))
        self.label_4.setText(_translate("Dialog", "Calle 1:", None))
        self.label_8.setText(_translate("Dialog", "Altura:", None))
        self.label_11.setText(_translate("Dialog", "Tipo de Siniestro:", None))
        self.label_10.setText(_translate("Dialog", "Tipo de Colisión:", None))
        self.label_9.setText(_translate("Dialog", "Total Heridos:", None))
        self.label_12.setText(_translate("Dialog", "Total Óbitos:", None))
        self.label_13.setText(_translate("Dialog", "Entidad Instructora:", None))
        self.pushButton_AgregarDato.setText(_translate("Dialog", "Agregar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))

