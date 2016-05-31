from database.db_main import engine, Hechos
from sqlalchemy.orm import sessionmaker
from PyQt4.QtGui import QMessageBox
from sqlalchemy import exc

Session = sessionmaker(bind=engine)
session = Session()


# Maneja la inserción de datos en la db. Instanciar un objeto de tabla
# con los datos a agregar y pasarlos a __init__. Incluye pop-ups para
# cada operación
class AddData:
    def __init__(self, table):
        self.table = table

    def add(self):
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

                table = self.table

                session.add(table)
                session.commit()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('Dato Agregado')
                result = msg.exec_()
                if result == QMessageBox.Ok:
                    print('ok')
                return True

            else:
                msg_no_agregado.exec_()
                print('no agregado')
                return False

        except exc.SQLAlchemyError as e:
            session.rollback()
            msg_no_agregado.setDetailedText(e.args[0])
            msg_no_agregado.exec_()
            print('no agregado')
            return False


