# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\gui_feu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(548, 760)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.hechos_tab = QtGui.QWidget()
        self.hechos_tab.setObjectName(_fromUtf8("hechos_tab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.hechos_tab)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.groupBox_8 = QtGui.QGroupBox(self.hechos_tab)
        self.groupBox_8.setTitle(_fromUtf8(""))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_8)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.fecha_dateEdit = QtGui.QDateEdit(self.groupBox_8)
        self.fecha_dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.fecha_dateEdit.setObjectName(_fromUtf8("fecha_dateEdit"))
        self.horizontalLayout.addWidget(self.fecha_dateEdit)
        self.label_2 = QtGui.QLabel(self.groupBox_8)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.hora_timeEdit = QtGui.QTimeEdit(self.groupBox_8)
        self.hora_timeEdit.setObjectName(_fromUtf8("hora_timeEdit"))
        self.horizontalLayout.addWidget(self.hora_timeEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addWidget(self.groupBox_8)
        self.groupBox_9 = QtGui.QGroupBox(self.hechos_tab)
        self.groupBox_9.setTitle(_fromUtf8(""))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.calle1_comboBox = QtGui.QComboBox(self.groupBox_9)
        self.calle1_comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.calle1_comboBox.setEditable(True)
        self.calle1_comboBox.setObjectName(_fromUtf8("calle1_comboBox"))
        self.gridLayout.addWidget(self.calle1_comboBox, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.calle2_comboBox = QtGui.QComboBox(self.groupBox_9)
        self.calle2_comboBox.setEditable(True)
        self.calle2_comboBox.setObjectName(_fromUtf8("calle2_comboBox"))
        self.gridLayout.addWidget(self.calle2_comboBox, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.tipoArteria1_comboBox = QtGui.QComboBox(self.groupBox_9)
        self.tipoArteria1_comboBox.setEditable(False)
        self.tipoArteria1_comboBox.setObjectName(_fromUtf8("tipoArteria1_comboBox"))
        self.gridLayout.addWidget(self.tipoArteria1_comboBox, 0, 3, 1, 1)
        self.tipoArteria2_comboBox = QtGui.QComboBox(self.groupBox_9)
        self.tipoArteria2_comboBox.setEditable(False)
        self.tipoArteria2_comboBox.setObjectName(_fromUtf8("tipoArteria2_comboBox"))
        self.gridLayout.addWidget(self.tipoArteria2_comboBox, 1, 3, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.altura_spinBox = QtGui.QSpinBox(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.altura_spinBox.sizePolicy().hasHeightForWidth())
        self.altura_spinBox.setSizePolicy(sizePolicy)
        self.altura_spinBox.setMaximum(15000)
        self.altura_spinBox.setObjectName(_fromUtf8("altura_spinBox"))
        self.horizontalLayout_3.addWidget(self.altura_spinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_11 = QtGui.QLabel(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.latitud_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_9)
        self.latitud_doubleSpinBox.setReadOnly(True)
        self.latitud_doubleSpinBox.setDecimals(8)
        self.latitud_doubleSpinBox.setMinimum(-99.99)
        self.latitud_doubleSpinBox.setObjectName(_fromUtf8("latitud_doubleSpinBox"))
        self.horizontalLayout_12.addWidget(self.latitud_doubleSpinBox)
        self.label_14 = QtGui.QLabel(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_12.addWidget(self.label_14)
        self.longitud_doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_9)
        self.longitud_doubleSpinBox.setReadOnly(True)
        self.longitud_doubleSpinBox.setDecimals(8)
        self.longitud_doubleSpinBox.setMinimum(-99.99)
        self.longitud_doubleSpinBox.setObjectName(_fromUtf8("longitud_doubleSpinBox"))
        self.horizontalLayout_12.addWidget(self.longitud_doubleSpinBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.geocodificar_pushButton = QtGui.QPushButton(self.groupBox_9)
        self.geocodificar_pushButton.setObjectName(_fromUtf8("geocodificar_pushButton"))
        self.horizontalLayout_13.addWidget(self.geocodificar_pushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.verticalLayout_10.addWidget(self.groupBox_9)
        self.groupBox_10 = QtGui.QGroupBox(self.hechos_tab)
        self.groupBox_10.setTitle(_fromUtf8(""))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_10 = QtGui.QLabel(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.tipoColision_comboBox = QtGui.QComboBox(self.groupBox_10)
        self.tipoColision_comboBox.setObjectName(_fromUtf8("tipoColision_comboBox"))
        self.horizontalLayout_4.addWidget(self.tipoColision_comboBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.totalHeridos_spinBox = QtGui.QSpinBox(self.groupBox_10)
        self.totalHeridos_spinBox.setObjectName(_fromUtf8("totalHeridos_spinBox"))
        self.horizontalLayout_5.addWidget(self.totalHeridos_spinBox)
        self.label_12 = QtGui.QLabel(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_5.addWidget(self.label_12)
        self.totalObitos_spinBox = QtGui.QSpinBox(self.groupBox_10)
        self.totalObitos_spinBox.setObjectName(_fromUtf8("totalObitos_spinBox"))
        self.horizontalLayout_5.addWidget(self.totalObitos_spinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_13 = QtGui.QLabel(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_6.addWidget(self.label_13)
        self.entidadInstructora_comboBox = QtGui.QComboBox(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entidadInstructora_comboBox.sizePolicy().hasHeightForWidth())
        self.entidadInstructora_comboBox.setSizePolicy(sizePolicy)
        self.entidadInstructora_comboBox.setObjectName(_fromUtf8("entidadInstructora_comboBox"))
        self.horizontalLayout_6.addWidget(self.entidadInstructora_comboBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_27 = QtGui.QLabel(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_18.addWidget(self.label_27)
        self.idDgc_spinBox = QtGui.QSpinBox(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idDgc_spinBox.sizePolicy().hasHeightForWidth())
        self.idDgc_spinBox.setSizePolicy(sizePolicy)
        self.idDgc_spinBox.setObjectName(_fromUtf8("idDgc_spinBox"))
        self.horizontalLayout_18.addWidget(self.idDgc_spinBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        self.verticalLayout_10.addWidget(self.groupBox_10)
        self.groupBox_11 = QtGui.QGroupBox(self.hechos_tab)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.observaciones_plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_11)
        self.observaciones_plainTextEdit.setObjectName(_fromUtf8("observaciones_plainTextEdit"))
        self.horizontalLayout_21.addWidget(self.observaciones_plainTextEdit)
        self.verticalLayout_10.addWidget(self.groupBox_11)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.clearHechos_pushButton = QtGui.QPushButton(self.hechos_tab)
        self.clearHechos_pushButton.setObjectName(_fromUtf8("clearHechos_pushButton"))
        self.horizontalLayout_14.addWidget(self.clearHechos_pushButton)
        self.addHecho_pushButton = QtGui.QPushButton(self.hechos_tab)
        self.addHecho_pushButton.setObjectName(_fromUtf8("addHecho_pushButton"))
        self.horizontalLayout_14.addWidget(self.addHecho_pushButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.tabWidget.addTab(self.hechos_tab, _fromUtf8(""))
        self.participantes_tab = QtGui.QWidget()
        self.participantes_tab.setObjectName(_fromUtf8("participantes_tab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.participantes_tab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox = QtGui.QGroupBox(self.participantes_tab)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.idHecho_spinBox = QtGui.QSpinBox(self.groupBox)
        self.idHecho_spinBox.setObjectName(_fromUtf8("idHecho_spinBox"))
        self.horizontalLayout_2.addWidget(self.idHecho_spinBox)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.participantes_tab)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_7.addWidget(self.label_15)
        self.tipoParticipante_comboBox = QtGui.QComboBox(self.groupBox_3)
        self.tipoParticipante_comboBox.setObjectName(_fromUtf8("tipoParticipante_comboBox"))
        self.horizontalLayout_7.addWidget(self.tipoParticipante_comboBox)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.participantes_tab)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_9.addWidget(self.label_16)
        self.marcaParticipante_comboBox = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marcaParticipante_comboBox.sizePolicy().hasHeightForWidth())
        self.marcaParticipante_comboBox.setSizePolicy(sizePolicy)
        self.marcaParticipante_comboBox.setEditable(True)
        self.marcaParticipante_comboBox.setObjectName(_fromUtf8("marcaParticipante_comboBox"))
        self.horizontalLayout_9.addWidget(self.marcaParticipante_comboBox)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_22 = QtGui.QLabel(self.groupBox_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_15.addWidget(self.label_22)
        self.modeloParticipante_comboBox = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeloParticipante_comboBox.sizePolicy().hasHeightForWidth())
        self.modeloParticipante_comboBox.setSizePolicy(sizePolicy)
        self.modeloParticipante_comboBox.setEditable(True)
        self.modeloParticipante_comboBox.setObjectName(_fromUtf8("modeloParticipante_comboBox"))
        self.horizontalLayout_15.addWidget(self.modeloParticipante_comboBox)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_23 = QtGui.QLabel(self.groupBox_2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_16.addWidget(self.label_23)
        self.dominioParticipante_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.dominioParticipante_lineEdit.setObjectName(_fromUtf8("dominioParticipante_lineEdit"))
        self.horizontalLayout_16.addWidget(self.dominioParticipante_lineEdit)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.clearParticipante_pushButton = QtGui.QPushButton(self.participantes_tab)
        self.clearParticipante_pushButton.setObjectName(_fromUtf8("clearParticipante_pushButton"))
        self.horizontalLayout_8.addWidget(self.clearParticipante_pushButton)
        self.addParticipante_pushButton = QtGui.QPushButton(self.participantes_tab)
        self.addParticipante_pushButton.setObjectName(_fromUtf8("addParticipante_pushButton"))
        self.horizontalLayout_8.addWidget(self.addParticipante_pushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem13)
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.tabWidget.addTab(self.participantes_tab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab)
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_17 = QtGui.QLabel(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_10.addWidget(self.label_17)
        self.idHecho_victimas_spinBox = QtGui.QSpinBox(self.groupBox_6)
        self.idHecho_victimas_spinBox.setObjectName(_fromUtf8("idHecho_victimas_spinBox"))
        self.horizontalLayout_10.addWidget(self.idHecho_victimas_spinBox)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addWidget(self.groupBox_6)
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)
        self.edad_spinBox = QtGui.QSpinBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edad_spinBox.sizePolicy().hasHeightForWidth())
        self.edad_spinBox.setSizePolicy(sizePolicy)
        self.edad_spinBox.setProperty("value", 0)
        self.edad_spinBox.setObjectName(_fromUtf8("edad_spinBox"))
        self.gridLayout_2.addWidget(self.edad_spinBox, 1, 1, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 1, 2, 1, 1)
        self.sexo_comboBox = QtGui.QComboBox(self.groupBox_4)
        self.sexo_comboBox.setObjectName(_fromUtf8("sexo_comboBox"))
        self.gridLayout_2.addWidget(self.sexo_comboBox, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_4)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 2, 0, 1, 1)
        self.rol_comboBox = QtGui.QComboBox(self.groupBox_4)
        self.rol_comboBox.setObjectName(_fromUtf8("rol_comboBox"))
        self.gridLayout_2.addWidget(self.rol_comboBox, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.tab)
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_25 = QtGui.QLabel(self.groupBox_5)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_3.addWidget(self.label_25, 0, 0, 1, 1)
        self.apellido_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.apellido_lineEdit.setObjectName(_fromUtf8("apellido_lineEdit"))
        self.gridLayout_3.addWidget(self.apellido_lineEdit, 0, 1, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem16, 0, 2, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_5)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_3.addWidget(self.label_26, 1, 0, 1, 1)
        self.nombre_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.nombre_lineEdit.setObjectName(_fromUtf8("nombre_lineEdit"))
        self.gridLayout_3.addWidget(self.nombre_lineEdit, 1, 1, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(185, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem17, 1, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.groupBox_7 = QtGui.QGroupBox(self.tab)
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_24 = QtGui.QLabel(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_20.addWidget(self.label_24)
        self.dni_spinBox = QtGui.QSpinBox(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dni_spinBox.sizePolicy().hasHeightForWidth())
        self.dni_spinBox.setSizePolicy(sizePolicy)
        self.dni_spinBox.setMinimum(1000000)
        self.dni_spinBox.setMaximum(500000000)
        self.dni_spinBox.setObjectName(_fromUtf8("dni_spinBox"))
        self.horizontalLayout_20.addWidget(self.dni_spinBox)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem18)
        self.verticalLayout_7.addWidget(self.groupBox_7)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem19)
        self.clearVictima_pushButton = QtGui.QPushButton(self.tab)
        self.clearVictima_pushButton.setObjectName(_fromUtf8("clearVictima_pushButton"))
        self.horizontalLayout_11.addWidget(self.clearVictima_pushButton)
        self.addVictima_pushButton = QtGui.QPushButton(self.tab)
        self.addVictima_pushButton.setObjectName(_fromUtf8("addVictima_pushButton"))
        self.horizontalLayout_11.addWidget(self.addVictima_pushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        spacerItem20 = QtGui.QSpacerItem(20, 506, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem20)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Fecha:", None))
        self.label_2.setText(_translate("Dialog", "Hora:", None))
        self.label_6.setText(_translate("Dialog", "Tipo de arteria 1:", None))
        self.label_7.setText(_translate("Dialog", "Tipo de arteria 2:", None))
        self.label_5.setText(_translate("Dialog", "Calle 2:", None))
        self.label_4.setText(_translate("Dialog", "Calle 1:", None))
        self.label_8.setText(_translate("Dialog", "Altura:", None))
        self.label_11.setText(_translate("Dialog", "Latitud:", None))
        self.label_14.setText(_translate("Dialog", "Longitud:", None))
        self.geocodificar_pushButton.setText(_translate("Dialog", "Geocodificar", None))
        self.label_10.setText(_translate("Dialog", "Tipo de Colisión:", None))
        self.label_9.setText(_translate("Dialog", "Total Heridos:", None))
        self.label_12.setText(_translate("Dialog", "Total Óbitos:", None))
        self.label_13.setText(_translate("Dialog", "Entidad Instructora:", None))
        self.label_27.setText(_translate("Dialog", "Id DGC:", None))
        self.groupBox_11.setTitle(_translate("Dialog", "Observaciones:", None))
        self.clearHechos_pushButton.setText(_translate("Dialog", "Limpiar", None))
        self.addHecho_pushButton.setText(_translate("Dialog", "Agregar Dato", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hechos_tab), _translate("Dialog", "Hechos", None))
        self.label_3.setText(_translate("Dialog", "Id del Hecho:", None))
        self.label_15.setText(_translate("Dialog", "Tipo de Participante:", None))
        self.label_16.setText(_translate("Dialog", "Marca:  ", None))
        self.label_22.setText(_translate("Dialog", "Modelo: ", None))
        self.label_23.setText(_translate("Dialog", "Dominio:", None))
        self.clearParticipante_pushButton.setText(_translate("Dialog", "Limpiar", None))
        self.addParticipante_pushButton.setText(_translate("Dialog", "Agregar Dato", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.participantes_tab), _translate("Dialog", "Participantes", None))
        self.label_17.setText(_translate("Dialog", "Id del Hecho:", None))
        self.label_18.setText(_translate("Dialog", "Sexo:", None))
        self.label_19.setText(_translate("Dialog", "Edad:", None))
        self.label_20.setText(_translate("Dialog", "Rol:", None))
        self.label_25.setText(_translate("Dialog", "Apellido:", None))
        self.label_26.setText(_translate("Dialog", "Nombre:", None))
        self.label_24.setText(_translate("Dialog", "Dni:    ", None))
        self.clearVictima_pushButton.setText(_translate("Dialog", "Limpiar", None))
        self.addVictima_pushButton.setText(_translate("Dialog", "Agregar Dato", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Víctimas", None))

