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

        QtCore.QObject.connect(self.ui.pushButton_AgregarDato,
                               QtCore.SIGNAL('clicked()'),
                               self.add_data)
        self.populate_combobox()
        self.clear_form_hechos()

    def populate_combobox(self):
        self.ui.calle1_comboBox.addItems(CALLES_LIST)
        self.ui.calle2_comboBox.addItems(CALLES_LIST)
        self.ui.tipoArteria1_comboBox.addItems(TIPO_ARTERIA_LIST)
        self.ui.tipoArteria2_comboBox.addItems(TIPO_ARTERIA_LIST)

    def clear_form_hechos(self):
        self.ui.calle1_comboBox.clearEditText()
        self.ui.calle2_comboBox.clearEditText()
        self.ui.tipoArteria1_comboBox.clearEditText()
        self.ui.tipoArteria2_comboBox.clearEditText()

    def add_data(self):
        try:
            hecho = Hechos(id_hecho=self.ui.spinBox_NumeroHecho.value(),
                           fecha=self.ui.fecha_dateEdit.date().toPyDate(),
                           hora=self.ui.hora_timeEdit.time().toString(),
                           calle1=self.ui.calle1_comboBox.currentText(),
                           calle2=self.ui.calle2_comboBox.currentText(),
                           tipo_calle1=self.ui.tipoArteria1_comboBox.currentText(),
                           tipo_calle2=self.ui.tipoArteria2_comboBox.currentText(),
                           altura_calle=self.ui.altura_spinBox.value(),
                           tipo_siniestro=self.ui.tipoSiniestro_comboBox.currentText(),
                           tipo_colision=self.ui.tipoColision_comboBox.currentText(),
                           total_heridos=self.ui.totalHeridos_spinBox.value(),
                           total_obitos=self.ui.totalObitos_spinBox.value(),
                           entidad_instructora=self.ui.entidadInstructora_comboBox.currentText())
            session.add(hecho)
            session.commit()
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText('Dato Agregado')
            result = msg.exec_()
            if result == QtGui.QMessageBox.Ok:
                print('ok')
        except:
            session.rollback()
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText('Dato no Agregado')
            msg.exec_()
            print('no agregado')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    formulario = FormularioFeu()
    formulario.show()
    sys.exit(app.exec_())
