import sys
from PyQt4 import QtCore, QtGui
from interface import Ui_Dialog

class UN(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		
		# here we connect signals with our slots
		
		#self.ui.pushButton = QtGui.QPushButton('Login', self)
		self.ui.pushButton.clicked.connect(self.Login)
		
		
		
	def Login(self):
		if (self.ui.lineEdit.text() == 'Mani' and self.ui.lineEdit_2.text() == 'Maran'):
			self.ui.accept()
	
		else:
				QtGui.QMessageBox.warning(self, 'error','please type correct user or password')
				
				
	#def accept(self):
					
				
				

if __name__ == "__main__":
	
	app = QtGui.QApplication(sys.argv)
	myapp = UN()
	myapp.show()
	sys.exit(app.exec_())
