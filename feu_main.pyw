import sys
from designer.gui_feu import *
from database.db_main import *
from database.db_add_data import *
from externo.datos import *


class FormularioFeu(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.calle1_comboBox.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.calle2_comboBox.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)

        QtCore.QObject.connect(self.ui.addHecho_pushButton,
                               QtCore.SIGNAL('clicked()'),
                               self.add_data_hechos)
        QtCore.QObject.connect(self.ui.addParticipante_pushButton,
                               QtCore.SIGNAL('clicked()'),
                               self.add_data_participantes)
        QtCore.QObject.connect(self.ui.addVictima_pushButton,
                               QtCore.SIGNAL('clicked()'),
                               self.add_data_victimas)

        if maxima_id():
            self.ui.idHecho_spinBox.setValue(maxima_id())
            self.ui.idHecho_victimas_spinBox.setValue(maxima_id())
        self.populate_combobox()
        self.clear_form_hechos()

    def populate_combobox(self):
        lista_combobox = ListasCombobox()
        self.ui.calle1_comboBox.addItems(lista_combobox.get_list('calles'))
        self.ui.calle2_comboBox.addItems(lista_combobox.get_list('calles'))
        self.ui.tipoArteria1_comboBox.addItems(lista_combobox.get_list('tipo_calle'))
        self.ui.tipoArteria2_comboBox.addItems(lista_combobox.get_list('tipo_calle'))
        self.ui.tipoColision_comboBox.addItems(lista_combobox.get_list('tipo_colision'))
        self.ui.entidadInstructora_comboBox.addItems(lista_combobox.get_list('entidad_instructora'))
        self.ui.tipoParticipante_comboBox.addItems(lista_combobox.get_list('tipo_participante'))
        self.ui.marcaParticipante_comboBox.addItems(lista_combobox.get_list('marca_participante'))
        self.ui.sexo_comboBox.addItems(lista_combobox.get_list('sexo'))
        self.ui.rol_comboBox.addItems(lista_combobox.get_list('rol'))

    def clear_form_hechos(self):
        self.ui.calle1_comboBox.clearEditText()
        self.ui.calle2_comboBox.clearEditText()
        self.ui.tipoArteria1_comboBox.setCurrentIndex(0)
        self.ui.tipoArteria2_comboBox.setCurrentIndex(0)
        self.ui.tipoColision_comboBox.setCurrentIndex(0)
        self.ui.entidadInstructora_comboBox.setCurrentIndex(0)

    def add_data_hechos(self):

        table = Hechos(  # id_hecho='cosa', #PARA TESTEAR
            fecha=self.ui.fecha_dateEdit.date().toPyDate(),
            hora=self.ui.hora_timeEdit.time().toString(),
            calle1=self.ui.calle1_comboBox.currentText().lower(),
            calle2=self.ui.calle2_comboBox.currentText().lower(),
            tipo_calle1=self.ui.tipoArteria1_comboBox.currentText(),
            tipo_calle2=self.ui.tipoArteria2_comboBox.currentText(),
            altura_calle=self.ui.altura_spinBox.value(),
            tipo_colision=self.ui.tipoColision_comboBox.currentText(),
            total_heridos=self.ui.totalHeridos_spinBox.value(),
            total_obitos=self.ui.totalObitos_spinBox.value(),
            entidad_instructora=self.ui.entidadInstructora_comboBox.currentText()
        )

        agregar = AddData(table=table)
        agregar = agregar.add()

        if agregar:
            self.ui.idHecho_spinBox.setValue(maxima_id())
            self.ui.idHecho_victimas_spinBox.setValue(maxima_id())

    def add_data_participantes(self):

        table = Participantes(
            id_hecho=self.ui.idHecho_spinBox.value(),
            tipo_participante=self.ui.tipoParticipante_comboBox.currentText(),
            marca_participante=self.ui.marcaParticipante_comboBox.currentText()
        )

        agregar = AddData(table=table)
        agregar.add()

    def add_data_victimas(self):

        table = Victimas(
            id_hecho=self.ui.idHecho_victimas_spinBox.value(),
            sexo=self.ui.sexo_comboBox.currentText(),
            edad=self.ui.edad_spinBox.value(),
            rol=self.ui.rol_comboBox.currentText()
        )

        agregar = AddData(table=table)
        agregar.add()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    formulario = FormularioFeu()
    formulario.show()
    sys.exit(app.exec_())
