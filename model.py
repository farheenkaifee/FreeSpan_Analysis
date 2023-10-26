import numpy as np
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys


class TableModel(QtCore.QAbstractTableModel):
   
    columns_name_map = {
        "values1": " ",
        "values2" : " ",
        "values3" : " ",
        "values4" : " ",

        "units1" : " ",
    #     "b1" : " ",
    #     "c1" : " ",
    #     "d1" : " ",

    #     "w"  : " ",
    #     "x"  :  " ",
    #     "y"  : " ",
    #     "z"   : " ",

    #     "w1"  : " ",
    #     "x1"  :  " ",
    #     "y1"  : " ",
    #     "z1"   : " ",

    #     "w2"  : " ",
    #     "x2"  :  " ",
    #     "y2"  : " ",
    #     "z2"   : " ",
        
    #     "values": " INPUT",
    #     "values1": "SYMBOL ",
    #     "values2": "UNIT ",
    #     "values3": "DATA ",

    #     "values8": " INPUT",
    #     "values9": "SYMBOL ",
    #     "values10": "UNIT ",
    #     "values1011": "DATA ",

        "values" : " ",


        # "values11": " INPUT",
        # "values12": "SYMBOL ",
        # "values14": "DATA ",

        "values31": " INPUT",
        "values32": "SYMBOL ",
        "values33": "UNIT ",
        "values34": "DATA ",

    #     "values81": " INPUT",
    #     "values91": "SYMBOL ",
    #     "values101": "UNIT ",
    #     "values1044": "DATA ",

    #     "values11a": " INPUT",
    #     "values12a": "SYMBOL ",
    #     "values13a": "UNIT ",
    #     "values14a": "DATA ",

        "values098" : "Information",
        "values0100": " "

        
    }
    def __init__(self, data):
        super(TableModel, self).__init__()
         
        self._data = data
        """self._header = header
        self._editable_status = editable_status
        self._columns_name_map = columns_name_map"""

    def data(self, index, role):
        # if role == QtCore.Qt.BackgroundRole:
        #     if index.row() == 0:
        #         return QBrush(QColor(183,182,193))
        
        # if role == QtCore.Qt.ForegroundRole:
        #     if index.row() == 0:
        #         return QBrush(QtCore.Qt.black)
                
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter
        if index.isValid():
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                value = self._data.iloc[index.row(), index.column()]
                if isinstance(value, np.generic):
                    return str('{:.3f}'.format(round(value.item(), 3))) 
                else:
                    return value
        return QtCore.QVariant()
        

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]


    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            return self.columns_name_map[self._data.columns[section]]


    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        elif not self._data.columns[index.column()]: 
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsEnabled
    
    def setData(self, index, val, role=QtCore.Qt.EditRole):
        if (role == QtCore.Qt.EditRole):
            self._data.iloc[index.row(), index.column()] = val
            self.__calculate(index)
            return True
        else:
            return True

    # def __calculate(self, index):
    #     if (self._data.columns[index.column()] in ['l2','l3','l4','l5','l6','l7']):

    #         self._data.loc[index.row(),'l3'] = (self._data.loc[index.row(), 'l2'] /100 )* self._data.loc[index.row(), 'l3']
    #         self._data.loc[index.row(),'l4'] = self._data.loc[index.row(), 'l2'] * 100
    #         self._data.loc[index.row(),'l5'] = self._data.loc[index.row(), 'l2'] + 100
    #         self._data.loc[index.row(),'l6'] = self._data.loc[index.row(), 'l3'] + 200
        

     
    def get_data(self):
        return self._data

       