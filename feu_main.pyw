import sys
import os
#sys.path.insert(0, os.path.abspath('..'))
from designer.gui_feu import *
from database.db_main import *
from database.db_add_data import *
from externo.datos import *
from externo.geo import *
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QTime
from sqlalchemy import exc
import requests
from helpers import check_boxes


class FormularioFeu(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        try:
            engine.connect()
            self.ui.calle1_comboBox.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
            self.ui.calle2_comboBox.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
            self.ui.marcaParticipante_comboBox.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
            self.ui.modeloParticipante_comboBox.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
            self.ui.fecha_dateEdit.setDate(QtCore.QDate.currentDate())

            QtCore.QObject.connect(self.ui.addHecho_pushButton,
                                   QtCore.SIGNAL('clicked()'),
                                   self.add_data_hechos)
            QtCore.QObject.connect(self.ui.addParticipante_pushButton,
                                   QtCore.SIGNAL('clicked()'),
                                   self.add_data_participantes)
            QtCore.QObject.connect(self.ui.addVictima_pushButton,
                                   QtCore.SIGNAL('clicked()'),
                                   self.add_data_victimas)
            QtCore.QObject.connect(self.ui.geocodificar_pushButton,
                                   QtCore.SIGNAL('clicked()'),
                                   self.geocodificar_campos)
            QtCore.QObject.connect(self.ui.clearHechos_pushButton,
                                   QtCore.SIGNAL('clicked()'),
                                   self.clear_form_hechos)
            QtCore.QObject.connect(self.ui.clearParticipante_pushButton,
                                   QtCore.SIGNAL('clicked()'),
                                   self.clear_form_participantes)
            QtCore.QObject.connect(self.ui.clearVictima_pushButton,
                                   QtCore.SIGNAL('clicked()'),
                                   self.clear_form_victimas)


            self.populate_combobox()
            if maxima_id():
                self.ui.idHecho_spinBox.setValue(maxima_id())
                self.ui.idHecho_victimas_spinBox.setValue(maxima_id())
            self.clear_form_hechos()
            self.clear_form_participantes()
            self.clear_form_victimas()

        except exc.OperationalError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Sin conexión a la Base de Datos')
            msg.setDetailedText(e.args[0])
            msg.exec_()

    def populate_combobox(self):
        lista_combobox = ListasCombobox()
        self.ui.calle1_comboBox.addItems(lista_combobox.get_list('calles'))
        self.ui.calle2_comboBox.addItems(lista_combobox.get_list('calles'))
        self.ui.tipoArteria1_comboBox.addItems(lista_combobox.get_list('tipo_calle'))
        self.ui.tipoArteria2_comboBox.addItems(lista_combobox.get_list('tipo_calle'))
        self.ui.entidadInstructora_comboBox.addItems(lista_combobox.get_list('entidad_instructora'))
        self.ui.tipoParticipante_comboBox.addItems(lista_combobox.get_list('tipo_participante'))
        self.ui.marcaParticipante_comboBox.addItems(lista_combobox.get_list('marca_participante'))
        self.ui.sexo_comboBox.addItems(lista_combobox.get_list('sexo'))
        self.ui.rol_comboBox.addItems(lista_combobox.get_list('rol'))
        self.ui.modeloParticipante_comboBox.addItems(lista_combobox.get_list('modelo_participante'))
        self.ui.causa_comboBox.addItems(lista_combobox.get_list('causa'))
        self.ui.lugarVia_comboBox.addItems(lista_combobox.get_list('lugar_via'))
        self.ui.tiempo_comboBox.addItems(lista_combobox.get_list('tiempo'))

    def clear_form_hechos(self):
        self.ui.calle1_comboBox.clearEditText()
        self.ui.calle2_comboBox.clearEditText()
        self.ui.hora_timeEdit.setTime(QTime(0, 0, 0))
        self.ui.tipoArteria1_comboBox.setCurrentIndex(0)
        self.ui.tipoArteria2_comboBox.setCurrentIndex(0)
        self.ui.entidadInstructora_comboBox.setCurrentIndex(0)
        self.ui.totalHeridos_spinBox.setValue(0)
        self.ui.totalObitos_spinBox.setValue(0)
        self.ui.sumario_spinBox.setValue(0)
        self.ui.latitud_doubleSpinBox.setValue(0.00000000)
        self.ui.longitud_doubleSpinBox.setValue(0.00000000)
        self.ui.observaciones_plainTextEdit.clear()
        self.ui.lugarVia_comboBox.setCurrentIndex(0)
        self.ui.tiempo_comboBox.setCurrentIndex(0)
        self.ui.altura_spinBox.setValue(0)
        self.ui.idDgc_spinBox.setValue(0)

    def clear_form_participantes(self):
        self.ui.tipoParticipante_comboBox.setCurrentIndex(0)
        self.ui.marcaParticipante_comboBox.setCurrentIndex(0)
        self.ui.modeloParticipante_comboBox.setCurrentIndex(0)
        self.ui.numeroParticipantePar_spinBox.setValue(0)
        self.ui.dominioParticipante_lineEdit.clear()
        self.ui.observacionesPart_plainTextEdit.clear()

    def clear_form_victimas(self):
        self.ui.sexo_comboBox.setCurrentIndex(0)
        self.ui.edad_spinBox.setValue(0)
        self.ui.rol_comboBox.setCurrentIndex(0)
        self.ui.numeroParticipanteVic_spinBox.setValue(0)
        self.ui.causa_comboBox.setCurrentIndex(0)
        self.ui.apellido_lineEdit.clear()
        self.ui.nombre_lineEdit.clear()
        self.ui.dni_spinBox.setValue(0)
        self.ui.observacionesVic_plainTextEdit.clear()

    def geocodificar_campos(self):
        try:
            if self.ui.altura_spinBox.value():
                coordenadas = geocodificar(self.ui.calle1_comboBox.currentText(),
                                           self.ui.calle2_comboBox.currentText(),
                                           self.ui.altura_spinBox.value())
            else:
                coordenadas = geocodificar(self.ui.calle1_comboBox.currentText(),
                                           self.ui.calle2_comboBox.currentText())

            self.ui.latitud_doubleSpinBox.setValue(coordenadas['lat'])
            self.ui.longitud_doubleSpinBox.setValue(coordenadas['lng'])
        except requests.exceptions.ConnectionError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText(str(e))
            msg.setText('Fallo')
            msg.exec_()

    def add_data_hechos(self):

        if self.ui.longitud_doubleSpinBox.value():
            long = self.ui.longitud_doubleSpinBox.value()
        else:
            long = None
        if self.ui.latitud_doubleSpinBox.value():
            lat = self.ui.latitud_doubleSpinBox.value()
        else:
            lat = None

        via_dividida_list = check_boxes(self.ui.viaDivididaPor_groupBox.children())
        prioridad_regulada_list = check_boxes(self.ui.prioridadReguladaPor_groupBox.children())

        table = Hechos(  # id_hecho='cosa', #PARA TESTEAR
            fecha=self.ui.fecha_dateEdit.date().toPyDate(),
            hora=self.ui.hora_timeEdit.time().toString(),
            calle1=self.ui.calle1_comboBox.currentText().lower(),
            calle2=self.ui.calle2_comboBox.currentText().lower(),
            tipo_calle1=self.ui.tipoArteria1_comboBox.currentText(),
            tipo_calle2=self.ui.tipoArteria2_comboBox.currentText(),
            altura_calle=self.ui.altura_spinBox.value(),
            lugar_via_publica=self.ui.lugarVia_comboBox.currentText(),
            tiempo=self.ui.tiempo_comboBox.currentText(),
            via_dividida_por=via_dividida_list,
            prioridad_regulada_por=prioridad_regulada_list,
            total_heridos=self.ui.totalHeridos_spinBox.value(),
            total_obitos=self.ui.totalObitos_spinBox.value(),
            entidad_instructora=self.ui.entidadInstructora_comboBox.currentText(),
            longitud=long,
            latitud=lat,
            observaciones=self.ui.observaciones_plainTextEdit.toPlainText(),
            id_dgc=self.ui.idDgc_spinBox.value(),
            sumario=self.ui.sumario_spinBox.value()
        )

        agregar = AddData(table=table)
        agregar.add()

        if agregar:
            self.ui.idHecho_spinBox.setValue(maxima_id())
            self.ui.idHecho_victimas_spinBox.setValue(maxima_id())
            self.clear_form_hechos()

    def add_data_participantes(self):

        table = Participantes(
            id_hecho=self.ui.idHecho_spinBox.value(),
            tipo=self.ui.tipoParticipante_comboBox.currentText(),
            marca=self.ui.marcaParticipante_comboBox.currentText(),
            modelo=self.ui.modeloParticipante_comboBox.currentText(),
            dominio=self.ui.dominioParticipante_lineEdit.text(),
            numero_participante=self.ui.numeroParticipantePar_spinBox.value(),
            observaciones=self.ui.observacionesPart_plainTextEdit.toPlainText()
        )

        agregar = AddData(table=table)
        agregar.add()

        if agregar:
            self.clear_form_participantes()

    def add_data_victimas(self):

        table = Victimas(
            id_hecho=self.ui.idHecho_victimas_spinBox.value(),
            causa=self.ui.causa_comboBox.currentText(),
            sexo=self.ui.sexo_comboBox.currentText(),
            edad=self.ui.edad_spinBox.value(),
            rol=self.ui.rol_comboBox.currentText(),
            dni=self.ui.dni_spinBox.value(),
            apellido=self.ui.apellido_lineEdit.text(),
            nombre=self.ui.nombre_lineEdit.text(),
            numero_participante=self.ui.numeroParticipanteVic_spinBox.value(),
            observaciones=self.ui.observacionesVic_plainTextEdit.toPlainText()
        )

        agregar = AddData(table=table)
        agregar.add()

        if agregar:
            self.clear_form_victimas()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    formulario = FormularioFeu()
    formulario.show()
    sys.exit(app.exec_())
