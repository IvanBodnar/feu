import sys
from designer.gui_feu import *
from database.db_main import *
from database.db_add_data import *
from externo.datos import *
from PyQt4.QtGui import QMessageBox
from sqlalchemy import exc


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
        self.populate_combobox()
        self.clear_form_hechos()

    def populate_combobox(self):
        lista_combobox = ListasCombobox()
        self.ui.calle1_comboBox.addItems(lista_combobox.get_list('calles'))
        self.ui.calle2_comboBox.addItems(lista_combobox.get_list('calles'))
        self.ui.tipoArteria1_comboBox.addItems(lista_combobox.get_list('tipo_calle'))
        self.ui.tipoArteria2_comboBox.addItems(lista_combobox.get_list('tipo_calle'))
        self.ui.tipoSiniestro_comboBox.addItems(lista_combobox.get_list('tipo_siniestro'))
        self.ui.tipoColision_comboBox.addItems(lista_combobox.get_list('tipo_siniestro'))
        self.ui.entidadInstructora_comboBox.addItems(lista_combobox.get_list('entidad_instructora'))
        self.ui.tipoParticipante_comboBox.addItems(lista_combobox.get_list('tipo_participante'))
        self.ui.marcaParticipante_comboBox.addItems(lista_combobox.get_list('marca_participante'))

    def clear_form_hechos(self):
        self.ui.calle1_comboBox.clearEditText()
        self.ui.calle2_comboBox.clearEditText()
        self.ui.tipoArteria1_comboBox.setCurrentIndex(0)
        self.ui.tipoArteria2_comboBox.setCurrentIndex(0)
        self.ui.tipoSiniestro_comboBox.setCurrentIndex(0)
        self.ui.tipoColision_comboBox.setCurrentIndex(0)
        self.ui.entidadInstructora_comboBox.setCurrentIndex(0)

    def add_data_hechos(self):

        msg_no_agregado = QMessageBox()
        msg_no_agregado.setIcon(QMessageBox.Critical)
        msg_no_agregado.setText('Dato no Agregado')

        try:
            confirm_msg = QMessageBox()
            confirm_msg.setIcon(QMessageBox.Question)
            confirm_msg.setText('Agregar Dato?')
            confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_msg_result = confirm_msg.exec_()

            if confirm_msg_result == QMessageBox.Yes:
                hecho = Hechos(#id_hecho='cosa', #PARA TESTEAR
                               fecha=self.ui.fecha_dateEdit.date().toPyDate(),
                               hora=self.ui.hora_timeEdit.time().toString(),
                               calle1=self.ui.calle1_comboBox.currentText().lower(),
                               calle2=self.ui.calle2_comboBox.currentText().lower(),
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

                self.clear_form_hechos()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('Dato Agregado')
                result = msg.exec_()
                if result == QMessageBox.Ok:
                    print('ok')

            else:
                msg_no_agregado.exec_()
                print('no agregado')

        except exc.SQLAlchemyError as e:
            session.rollback()
            msg_no_agregado.setDetailedText(e.args[0])
            msg_no_agregado.exec_()
            print('no agregado')

        # else:
        #     msg_no_agregado.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    formulario = FormularioFeu()
    formulario.show()
    sys.exit(app.exec_())
