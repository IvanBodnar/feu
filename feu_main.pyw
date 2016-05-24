import sys
from designer.gui_feu import *
from database.db_main import *
from database.db_add_data import *

# Prueba clone

class FormularioFeu(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButton_AgregarDato,
                               QtCore.SIGNAL('clicked()'),
                               self.add_data)

    def add_data(self):
        numero_hecho = self.ui.spinBox_NumeroHecho.value()
        fecha = self.ui.fecha_dateEdit.date().toPyDate()
        hora = self.ui.hora_timeEdit.time().toString()
        calle1 = self.ui.calle1_comboBox.currentText()
        calle2 = self.ui.calle2_comboBox.currentText()
        tipo_calle1 = self.ui.tipoArteria1_comboBox.currentText()
        tipo_calle2 = self.ui.tipoArteria2_comboBox.currentText()
        altura = self.ui.altura_spinBox.value()
        tipo_siniestro = self.ui.tipoSiniestro_comboBox.currentText()
        tipo_colision = self.ui.tipoColision_comboBox.currentText()
        total_heridos = self.ui.totalHeridos_spinBox.value()
        total_obitos = self.ui.totalObitos_spinBox.value()
        entidad_instructora=self.ui.entidadInstructora_comboBox.currentText()

        hecho = Hechos(id_hecho=numero_hecho,
                       fecha=fecha,
                       hora=hora,
                       calle1=calle1,
                       calle2=calle2,
                       tipo_calle1=tipo_calle1,
                       tipo_calle2=tipo_calle2,
                       altura_calle=altura,
                       tipo_siniestro=tipo_siniestro,
                       tipo_colision=tipo_colision,
                       total_heridos=total_heridos,
                       total_obitos=total_obitos,
                       entidad_instructora=entidad_instructora)
        session.add(hecho)
        session.commit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    formulario = FormularioFeu()
    formulario.show()
    sys.exit(app.exec_())
