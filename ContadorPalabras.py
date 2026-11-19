import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # CARGA DE NUESTRA VISTA
        uic.loadUi("ContadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.ContarPalabras)

    def ContarPalabras(self):
        # Recuperar texto (check)
        texto = self.edtCaracteres.text()

        # Separar palabras (check)
        textoSeparado = texto.split()
        print(textoSeparado)

        # Contar palabras
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Palabras: {cantidadPalabras}")

        # Contar caracteres (sin contar espacios)
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")

        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet('font: 11pt "MS Shell Dlg 2"; color: #ff756b')
        else:
            self.tvPalabras.setStyleSheet('font: 11pt "MS Shell Dlg 2"; color: #000000')

        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet('font: 11pt "MS Shell Dlg 2"; color: #ff756b')
        else:
            self.tvCaracteres.setStyleSheet('font: 11pt "MS Shell Dlg 2"; color: #000000')

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())