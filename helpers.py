
# Devuelve una lista con los textos de cada checkbox si el checkbox fue clickeado.
# Acepta la lista dada por gruopBox.children() (grupo de checkboxes).
def check_boxes(lista):
    result = []

    for check in lista:
        try:
            if check.isChecked():
                result.append(check.text().lower())
        except:
            pass
    return result
