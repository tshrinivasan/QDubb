import sys
from PyQt4 import QtCore, QtGui
from QDubb import Ui_QDubb
from os.path import isfile
import codecs
import csv

class StartQT4(QtGui.QMainWindow):

    line = 0
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_QDubb()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonLoad,QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.buttonNext,QtCore.SIGNAL("clicked()"), self.show_next)
        QtCore.QObject.connect(self.ui.buttonPrevious,QtCore.SIGNAL("clicked()"), self.show_previous)

    
    def file_dialog(self):

	    fd = QtGui.QFileDialog(self)
	    self.filename = fd.getOpenFileName()

	    if isfile(self.filename):
	    	text = codecs.open( self.filename, "r", "utf-8" ).read()
	    	self.ui.textFile.setText(text)
	
	    	filename = csv.reader(open(self.filename),quoting=csv.QUOTE_NONE)
	    	file_list = []
	    	file_list.extend(filename)
	    	self.times = []
	    	self.texts = []
	    	for data in file_list:
	    		self.times.append(data[0])
	    		self.texts.append(data[1].decode('utf-8'))
		
		
	    self.ui.textLine.setText(self.texts[0])
	    count_text = str(self.line+1) + "/" + str(len(self.texts))
	    self.ui.labelCounter.setText(count_text)
				
		


    def show_next(self):
	    if self.line >= len(self.texts):
	        reply = QtGui.QMessageBox.information(self,"Message","You reached the last line of the file",QtGui.QMessageBox.Ok)
	        return reply
	        
	    self.line = self.line + 1
	    
        if isfile(self.filename):
            self.ui.textLine.setText(self.texts[self.line])		    
		    count_text = str(self.line+1) + "/" + str(len(self.texts))
		    self.ui.labelCounter.setText(count_text)
		    

                
           
    def show_previous(self):
	    if self.line <= 0:
	        reply = QtGui.QMessageBox.information(self,"Message","You reached the start line of the file",QtGui.QMessageBox.Ok)
	        return reply


        self.line = self.line - 1
        if isfile(self.filename):
		    self.ui.textLine.setText(self.texts[self.line])
		    
		    count_text = str(self.line+1) + "/" + str(len(self.texts))
		    self.ui.labelCounter.setText(count_text)
		    

	
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
