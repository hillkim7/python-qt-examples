#!/usr/bin/env python
#-*- coding:utf-8 -*-
###
# Simple QAbstractListModel/ QlistView 
# reference from:
# https://www.saltycrane.com/blog/2008/01/pyqt-43-simple-qabstractlistmodel/
###
import sys
from PyQt5 import QtCore, QtWidgets

#################################################################### 
def main(): 
    app = QtWidgets.QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 

#################################################################### 
class MyWindow(QtWidgets.QWidget): 
    def __init__(self, *args): 
        super(MyWindow, self).__init__(*args)

        # create table
        list_data = [1,2,3,4]
        lm = MyListModel(list_data, self)
        lv = QtWidgets.QListView()
        lv.setModel(lm)

        # layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lv) 
        self.setLayout(layout)

#################################################################### 
class MyListModel(QtCore.QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.listdata[index.row()])
        else: 
            return QtCore.QVariant()

####################################################################
if __name__ == "__main__": 
    main()