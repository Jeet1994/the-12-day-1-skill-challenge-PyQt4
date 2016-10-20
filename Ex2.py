import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Hit : Button 1")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Hit : Button 2")
   b2.move(50,50)
   QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)

   win.setGeometry(200,100,200,100)
   win.setWindowTitle("My button method")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
   print ("You have hit the 1st Button")

def b2_clicked():
   print ("You have hit the 2nd Button")

if __name__ == '__main__':
   window()