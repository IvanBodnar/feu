import sys
from designer.gui_feu import *
from database.db_main import *
from database.db_add_data import *


class FormularioFeu(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButton_AgregarDato,
                               QtCore.SIGNAL('clicked()'),
                               self.add_data)
        QtCore.QObject.connect(self.ui.connectDatabase_pushButton,
                               QtCore.SIGNAL('clicked()'),
                               self.set_db_connection)

    def set_db_connection(self):
        db = ConnectToDatabase(user=self.ui.user_lineEdit.text(),
                               password=self.ui.password_lineEdit.text(),
                               host=self.ui.host_lineEdit.text(),
                               port=self.ui.port_lineEdit.text(),
                               database=self.ui.database_lineEdit.text())

        if db.engine.connect():
            print('Conexion exitosa')
            return db.engine

    def add_data(self):
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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    formulario = FormularioFeu()
    formulario.show()
    sys.exit(app.exec_())
