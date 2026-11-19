import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #CARGA DE NUESTRA VISTA
        uic.loadUi("ContadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)
        
    def ContarPalabras(self):
        
        #Recuperar texto (check)
        texto = self.edtCaracteres.text()
        
        #Separar palabras (check)
        textoSeparado = texto.split()
        print(textoSeparado)
        
        #Contar palabras
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Palabras: {cantidadPalabras}")
        
        #Contar caracteres
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")
        
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())