import sys
from PyQt4 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello PyQt")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle('My first PyQt')
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()