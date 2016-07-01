# # -*- coding: utf-8 -*-. 
 
import sys
import unittest
 
# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')
 
from accions     import *
from objective   import *
from userHistory import *
from datetime    import *

TODAY = datetime.utcnow()
 
class TestHistory(unittest.TestCase):
    
    #############################################      
    #       Pruebas para insertUserHistory      #
    #############################################
           
    # Caso Inicial
       
    # Prueba 1
    def testInsertHistoryExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 2
    # Insertando una historia en un idBacklog que no existe
    def testInsertHistoryElementNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('OdL',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        result = searchHist = aHist.searchUserHistory('OdL',idBacklog)
        self.assertTrue(result)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
             
    # Prueba 3
    def testInsertHistoryRepeatedElement(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('OdL',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        result1 = aHist.insertUserHistory('OdL',0,1,idFound,99,1,True,TODAY,True,TODAY)
        self.assertFalse(result1)
        searchHist = aHist.searchUserHistory('OdL',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                        
    # Casos Fronteras
         
    # Prueba 4
    def testInsertHistoryShortDesc0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 5
    def testInsertHistoryShortDesc1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 6
    def testInsertHistoryShortDesc11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('H'*11,idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 7
    def testInsertHistoryElementType2(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('SdC',0,2,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
        searchHist = aHist.searchUserHistory('SdC',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('SdC')
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 8
    def testInsertHistoryElementBacklog2(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('SdC',0, 2,idFound,99,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 9
    def testInsertHistoryElementCodBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 2,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 10
    def testInsertHistoryElementTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 2*((2^31)-1),idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 11
    def testInsertHistoryElementBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 2,idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Casos Esquinas
          
    # Prueba 12
    def testInsertUserHistoryIdBacklogNoExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('jDw',0, 2,idFound, 99,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 13
    def testInsertUserHistoryLongDesc11AndIdBacklogNoExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2,idFound, 99,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 14
    def testInsertUserHistoryLongCod11AndIdBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2,idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 15
    def testInsertUserHistoryLongCod11AndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2*((2^31)-1),idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 16
    def testInsertUserHistory0Cod11AndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 17
    def testInsertUserHistoryLongCod11AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 2*((2^31)-1),idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 18
    def testInsertUserHistory0Cod11AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 2*((2^31)-1),idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 19
    def testInsertUserHistoryLongCod11AndType0AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 20
    def testInsertUserHistoryLongBacklog0AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 21
    def testInsertUserHistoryLongCod0AndType0AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 0,idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 22
    def testInsertUserHistoryLongCodBigAndType0AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 0,idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 23
    def testInsertUserHistoryLongCodBigAndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 24
    def testInsertUserHistoryLongCod1AndTypeBigAndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 25
    def testInsertUserHistoryLongCod1AndType1AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 26
    def testInsertUserHistoryLongCod0AndType1AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('',0, 1,idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 27
    def testInsertUserHistoryLongCod1AndType1AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1,idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
              
    # Prueba 28
    def testInsertUserHistoryLongCod1AndType0AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 29
    def testInsertUserHistoryLongCod1AndType1AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 1*((2^31)-1),idFound, 1,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 30
    def testInsertUserHistoryLongCod1AndType0AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H',0, 0,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 31
    def testInsertUserHistoryLongCod11AndType0AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
              
    # Prueba 32
    def testInsertUserHistoryLongCod11AndType0AndBacklog00(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound,0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')      
         
    # Prueba 33
    def testInsertUserHistoryLongCod11AndType1AndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Prueba 34
    def testInsertUserHistoryLongCod11AndType1AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
        
    # Prueba 35
    def testInsertUserHistoryLongCod11AndTypeBigAndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 36
    def testInsertUserHistoryLongCod11AndType1AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1,idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 37
    def testInsertUserHistoryLongCod11AndType0AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 0,idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 38
    def testInsertUserHistoryLongCod11AndTypeBigAndBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 0,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
         
    # Prueba 39
    def testInsertUserHistoryLongCod11AndTypeBigAndBacklog11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 11,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Prueba 40
    def testInsertUserHistoryLongCod11AndTypeBigAndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*11,0, 1*((2^31)-1),idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
         
    # Prueba 41
    def testInsertUserHistoryLongCodBigAndTypeBigAndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('H'*((2^31)-1),0, 1*((2^31)-1),idFound, 1*((2^31)-1),1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
                 
    # Casos Maliciosos
         
    # Prueba 42
    def testInsertUserHistoryCodNotString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(123,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 43
    def testInsertUserHistoryCodNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(None,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 44
    def testInsertUserHistoryTypeNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('OdL',0, None,idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
           
    # Prueba 45
    def testInsertUserHistoryBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('SdC',0, 1,idFound, None,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 46
    def testInsertUserHistoryTypeNoneBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('SdC',0, None,idFound, None,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
              
    # Prueba 47
    def testInsertUserHistoryCodeNoneTypeNoneBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory(None,0, None,idFound, None,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
           
    # Prueba 48
    def testInsertUserHistoryTypeNoneBacklogString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('SdC',0, None,idFound, '1',1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
           
    # Prueba 49
    def testInsertUserHistoryTypeStringBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('SdC',0, '1',idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
              
    # Prueba 50
    def testInsertUserHistoryTypeArrayBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        result = aHist.insertUserHistory('SdC',0, [],idFound,idBacklog,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')        
              
    #############################################      
    #       Pruebas para searchUserHistory      #
    #############################################
        
    #Casos Frontera
       
    # Prueba 51
    def testSearchHistoryExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        self.assertTrue(searchHist)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 52
    def testSearchHistoryNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        aHist = userHistory()
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        self.assertEqual([],searchHist)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
            
    # Prueba 53
    def testSearchHistoryLong11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertNotEqual([],searchHist)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 54
    def testSearchHistoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*((2^31)-1),idBacklog)
        self.assertEqual([],searchHist)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
    
    # Prueba 55
    def testSearchHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory(None,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*((2^31)-1),idBacklog)
        self.assertEqual([],searchHist)
                   
        # Eliminamos historia, accion y producto
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
    
    # Prueba 56
    def testSearchHistoryBackLogNoneExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11,637472)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
        
    # Prueba 57
    def testSearchHistoryBackLog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11,0)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 58
    def testSearchHistoryBackLogMax(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11,(2^31)-1)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
    
    # Prueba 59
    def testSearchHistoryBackLogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11,None)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
    
    # Casos Esquina
    
    # Prueba 60
    def testSearchHistoryAllMin(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('Q',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('Q',idBacklog)
        self.assertNotEqual([],searchHist)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 61
    def testSearchHistory1BackLog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H',0)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
    
    # Prueba 62
    def testSearchHistoryLen0Backlog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('',idBacklog)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 63
    def testSearchHistoryAll0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('',0)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 64
    def testSearchHistoryMaxBackLog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*12,0)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
    
    # Casos Malicia  
        
    # Prueba 65
    def testSearchHistoryMaxIntAll(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory(('H'*12),(2^31)-1)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')        
    
    # Prueba 66
    def testSearchHistoryAllNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory(None,None)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
    
    # Prueba 67
    def testSearchHistoryAllArray(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory([],[])
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
    
    # Prueba 68
    def testSearchHistorYLen0BacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('',None)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 69
    def testSearchHistoryNoneBacklog0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory(None,0)
        searchHist1 = aHist.searchUserHistory('H'*11,idBacklog)
        self.assertEqual([],searchHist)
        idFound1 = searchHist1[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
    
    ######################################################      
    #           Pruebas para deleteUserHistory           #
    ###################################################### 
          
    # Caso Inicial
       
    # Prueba 70
    def testDeleteUserHistoryExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(idFound1)
        self.assertTrue(result)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Prueba 71
    def testDeleteUserHistoryNotExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('kjefb')
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
            
    # Casos Fronteras
   
    # Prueba 72
    def testDeleteUserHistoryLong11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*11,0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('H'*11,idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(idFound1)
        self.assertTrue(result)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Prueba 73
    def testDeleteUserHistoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('H'*((2^31)-1),0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)

        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory((2^31)-1)
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
   
    # Casos Maliciosos
      
    # Prueba 74
    def testDeleteUserHistoryInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory('')
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 

    # Prueba 75
    def testDeleteUserHistoryNotString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(12345)
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
           
    # Prueba 76  
    def testDeleteUserHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
                   
        # Eliminamos historia, accion y producto
        result = aHist.deleteUserHistory(None)
        self.assertFalse(result)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
 
    ######################################################      
    #            Pruebas para updatePriority             #
    ######################################################
      
    # Casos Frontera 
     
    # Prueba 77
    def testUpdatePriorityExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        aHist.updatePriority(idFound,1)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
  
    # Prueba 78
    def testUpdatePriorityTrue(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,1)

        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 79
    def testUpdatePriorityNoIdFound(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(100,1)

        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 80
    def testUpdatePriority0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,0)

        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 81     
    def testUpdatePriority20(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,20)

        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 82
    def testUpdatePriority21(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,21)

        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 83   
    def testUpdatePriorityId0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(0,1)

        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
 
    # Casos Esquina
  
    # Prueba 84
    def testUpdatePriority11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,1)
        
        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    # Prueba 85        
    def testUpdatePriority020(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(0,20)
        
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
 
    # Prueba 86        
    def testUpdatePriority121(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,21)
        
        # Eliminamos historia, accion y producto
        self.assertTrue(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Casos Malicia
     
    # Prueba 87   
    def testUpdatePriorityNoneHistory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(None,20)
        
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 88    
    def testUpdatePriorityNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(idFound1,None)
        
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
     
    # Prueba 89    
    def testUpdatePriorityNoParam(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        result = aHist.updatePriority(None,None)
        
        # Eliminamos historia, accion y producto
        self.assertFalse(result)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
         
    # ###########################################     
    #           Pruebas para succesors          #
    ############################################# 
       
    # Prueba 90
    def testExistsSuccesors(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist  = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        aHist.succesors(idFound1)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
 
    # Prueba 91
    def testNoExistsSuccesors(self):         
        # Insertamos la historia
        aHist  = userHistory()        
        result = aHist.succesors(99)
        self.assertFalse(result)
                  
    # Casos Frontera        

    # Prueba 92    
    def testSuccesorsIdNegative(self):
       # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Dsjsdn',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
          
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia 1
        aHist  = userHistory()
        result = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        res    = aHist.searchUserHistory('jDw',idBacklog)
        idUH   = res[0].UH_idUserHistory
         
        # Insertamos la historia 2
        aHist     = userHistory()
        result    = aHist.insertUserHistory('OdL',idUH, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        histFound = aHist.searchUserHistory('OdL',idBacklog) 
        idFound1  = histFound[0].UH_idUserHistory 
        
        # Insertamos la historia 3
        aHist  = userHistory()
        result = aHist.insertUserHistory('SdC',1, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
         
        result = aHist.succesors(-1)
        self.assertEqual(result,[])
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
         
    ######################################################      
    #           Pruebas para getAllUserHistoryId         #
    ###################################################### 
        
    # Caso Inicial
     
    # Prueba 93
    def testGetAllUserHistoryIdNormal(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId(idBacklog)
        self.assertNotEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 94
    def testGetAllUserHistoryIdNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId(100)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Frontera
     
    # Prueba 95
    def testGetAllUserHistoryId0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId(0)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
         
    # Prueba 96
    def testGetAllUserHistoryIdMaxNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId((2^31)-1)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
     
    # Casos Malicia
     
    # Prueba 97
    def testGetAllUserHistoryIdNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId(None)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')      
         
    # Prueba 98
    def testGetAllUserHistoryIdNegativeNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId(-1)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Prueba 99
    def testGetAllUserHistoryIdString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId('1')
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')       
         
    # Prueba 100
    def testGetAllUserHistoryIdArray(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        aHist = userHistory()
        temp = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        foundHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = foundHist[0].UH_idUserHistory
        result = aHist.getAllUserHistoryId([])
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    ######################################################      
    #                Pruebas para isEpic                 #
    ###################################################### 
        
    # Caso Inicial
     
    # Prueba 101
    def testExistsIsEpic(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(idHist)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 102
    def testExistsIsEpicExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(idHist)
        self.assertTrue(idHist)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 103
    def testExistsIsEpicNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(2)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Frontera
     
    # Prueba 104
    def testExistsIsEpic0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(0)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 105
    def testExistsIsEpicMaxInt(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic((2^31)-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Casos Malicia
     
    # Prueba 106
    def testExistsIsEpicNegativeNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
     
    # Prueba 107
    def testExistsIsEpicNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic(None)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
     
    # Prueba 108
    def testExistsIsEpicString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.isEpic('1')
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    ######################################################      
    #            Pruebas para historySuccesors           #
    ###################################################### 
        
    # Caso Inicial
     
    # Prueba 109
    def testhistorySuccesors(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(1)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Normal
     
    # Prueba 110
    def testhistorySuccesorsExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(idHist)
        self.assertEqual(result,[])
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 111
    def testhistorySuccesorsNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(idHist)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Casos Frontera
     
    # Prueba 112
    def testhistorySuccesors0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(0)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 113
    def testhistorySuccesorsMaxInt(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors((2^31)-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
         
    # Casos Malicia
     
    # Prueba 114
    def testhistorySuccesorsNegativeNumber(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(-1)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
     
    # Prueba 115
    def testhistorySuccesorsNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors(None)
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
     
    # Prueba 116
    def testhistorySuccesorsString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search  = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist  = userHistory()
        temp   = aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        hist   = aHist.searchUserHistory('jDw',idBacklog)
        idHist = hist[0].UH_idUserHistory
        result = aHist.historySuccesors('1')
        self.assertFalse(result)
                 
        # Eliminamos producto
        aHist.deleteUserHistory(idHist)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    #########################################################      
    #         Pruebas para searchidUserHistoryIdAccion      #
    #########################################################     
      
    # Caso Inicial 
       
    # Prueba 117
    def testSearchidUserHistoryIdAccion(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
  
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
          
        # Buscamos id's de historias que contengan asociado una acción por su id
        aHist.searchidUserHistoryIdAccion(idFound) 
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Casos Frontera

    # Prueba 118
    def testSearchidUserHistoryIdAccionNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
  
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
                
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(0) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Prueba 119
    def testSearchidUserHistoryIdAccionOne(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(idFound) 
        self.assertNotEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
               
    # Prueba 120
    def testSearchidUserHistoryIdAccionBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory        
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(2**28) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Casos Malicia
     
    # Prueba 121
    def testSearchidUserHistoryIdAccionString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion('Patricia') 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Prueba 122
    def testSearchidUserHistoryIdAccionInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(-9898989898) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Prueba 123
    def testSearchidUserHistoryIdAccionNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
             
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchidUserHistoryIdAccion(None) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')     

    #########################################################      
    #        Pruebas para accionsAsociatedToUserHistory     #
    #########################################################
        
    # Caso Inicial
       
    # Prueba 124
    def testAccionsAsociatedToUserHistoryExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory(idFound1)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Caso Normal

    # Prueba 125
    def testAccionsAsociatedToUserHistoryExistTrue(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory(idFound1)
        self.assertNotEqual(result,[])
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 126
    def testAccionsAsociatedToUserHistoryExistFalse(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory(99)
        self.assertEqual(result,[])
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Caso Frontera

    # Prueba 127
    def testAccionsAsociatedToUserHistoryId1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory(idFound1)
        self.assertNotEqual(result,[])
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
        
    # Caso Malicia

    # Prueba 128
    def testAccionsAsociatedToUserHistoryExistId0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory(0)
        self.assertEqual(result,[])
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 129
    def testAccionsAsociatedToUserHistoryNegativeId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory(-6)
        self.assertEqual(result,[])
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 130
    def testAccionsAsociatedToUserHistoryNotId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory('jsjmms')
        self.assertEqual(result,[])
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 131
    def testAccionsAsociatedToUserHistoryIdNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Buscamos las acciones asociadas 
        result = aHist.accionsAsociatedToUserHistory(None)
        self.assertEqual(result,[])
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    ###############################################      
    #       Pruebas para transformUserHistory     #
    ###############################################
        
    # Caso Inicial
       
    # Prueba 132
    def testTransformUserHistoryExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory(idFound1)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Caso Normal

    # Prueba 133
    def testTransformUserHistoryExistTrue(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory(idFound1)
        self.assertNotEqual(result,{})
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 134
    def testTransformUserHistoryExistFalse(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory(99)
        self.assertEqual(result,{})
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Caso Frontera

    # Prueba 135
    def testTransformUserHistoryId1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory(idFound1)
        self.assertNotEqual(result,{})
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
        
    # Caso Malicia

    # Prueba 136
    def testTransformUserHistoryExistId0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory(0)
        self.assertEqual(result,{})
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 137
    def testTransformUserHistoryNegativeId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory(-6)
        self.assertEqual(result,{})
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 138
    def testTransformUserHistoryNotId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory('jsjmms')
        self.assertEqual(result,{})
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  

    # Prueba 139
    def testTransformUserHistoryIdNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0, 1,idFound,idBacklog,1,True,TODAY,True,TODAY)
           
        # Buscamos el codigo de la historia
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Obtenemos los elementos de la historia
        result = aHist.transformUserHistory(None)
        self.assertEqual(result,{})
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')

    #############################################      
    #        Pruebas para updateUserHistory     #
    #############################################
    
    # Caso Inicial
       
    # Prueba 140
    def testUpdateUserHistoryExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Dxfynyr',idBacklog)
        search = aAcc.searchAccion('Dxfynyr',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'jDw',0,1,idFound,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
                    
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Dxfynyr',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                        
    # Prueba 141
    def testUpdateUserHistoryRepeatedElement(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('OdL',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('OdL',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'OdL',0,1,idFound,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                        
    # Casos Fronteras
         
    # Prueba 142
    def testUpdateUserHistoryShortDesc0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'',0, 1,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
            
    # Prueba 143
    def testUpdateUserHistoryShortDesc1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H',0, 1,idFound,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H')
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
          
    # Prueba 144
    def testUpdateUserHistoryShortDesc11(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H'*11,0,1,idFound,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 145
    def testUpdateUserHistoryElementType2(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'SdC',0,2,idFound,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('SdC')
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                      
    # Prueba 146
    def testUpdateUserHistoryElementCodBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H'*((2^31)-1),0, 2,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
   
    # Prueba 147
    def testUpdateUserHistoryElementTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H',0, 2*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                   
    # Casos Esquinas                     
           
    # Prueba 148
    def testUpdateUserHistoryLongCod11AndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H'*11,0, 2*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 149
    def testUpdateUserHistory0Cod11AndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'',0, 2*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 150
    def testUpdateUserHistoryLongCod11AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(0,'H'*11,0, 2*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 151
    def testUpdateUserHistory0Cod11AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'',0, 2*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 152
    def testUpdateUserHistoryLongCod11AndType0AndIdUser0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(0,'H'*11,0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 153
    def testUpdateUserHistoryLongBacklog0AndType0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H',0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
         
    # Prueba 154
    def testUpdateUserHistoryLongCod0AndType0AndIdUser0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(0,'',0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 155
    def testUpdateUserHistoryLongCodBigAndType0AndIdUser0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(0,'H'*((2^31)-1),0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 156
    def testUpdateUserHistoryLongCodBigAndTypeBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(0,'H'*((2^31)-1),0, 1*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
        
    # Prueba 157
    def testUpdateUserHistoryLongCod1AndTypeBigAndIdUserBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(1*((2^31)-1),'H',0, 1*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
                      
    # Prueba 158
    def testUpdateUserHistoryLongCod0AndType1AndBacklogBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(1*((2^31)-1),'',0, 1,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 159
    def testUpdateUserHistoryLongCod1AndType0AndIdUserBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(1*((2^31)-1),'H',0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 160
    def testUpdateUserHistoryLongCod1AndType0AndIdUser1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H',0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
       
    # Prueba 161
    def testUpdateUserHistoryLongCod11AndType0AndBacklog1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H'*11,0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz') 
              
    # Prueba 162
    def testUpdateUserHistoryLongCod11AndType0AndIdUser00(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(0,'H'*11,0,0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')      
                  
    # Prueba 163
    def testUpdateUserHistoryLongCod11AndType1AndIdUser1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H'*11,0, 1,idFound,1,True,TODAY,True,TODAY)
        self.assertTrue(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory('H'*11)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
        
    # Prueba 164
    def testUpdateUserHistoryLongCod11AndTypeBigAndIdUser1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'H'*11,0, 1*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')             
           
    # Prueba 165
    def testUpdateUserHistoryLongCod11AndType0AndIdUserBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(1*((2^31)-1),'H'*11,0, 0,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 166
    def testUpdateUserHistoryLongCod11AndTypeBigAndIdUser0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(0,'H'*11,0, 1*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')           
         
    # Prueba 167
    def testUpdateUserHistoryLongCod11AndTypeBigAndIdUserBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(1*((2^31)-1),'H'*11,0, 1*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
         
    # Prueba 168
    def testUpdateUserHistoryLongCodBigAndTypeBigAndIdUserBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(1*((2^31)-1),'H'*((2^31)-1),0, 1*((2^31)-1),idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
                 
    # Casos Maliciosos
         
    # Prueba 169
    def testUpdateUserHistoryCodNotString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,123,0, 1,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')
           
    # Prueba 170
    def testUpdateUserHistoryCodNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,None,0,1,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 171
    def testUpdateUserHistoryTypeNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(idFound1,'OdL',0, None,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')   
           
    # Prueba 172
    def testUpdateUserHistoryIdUserNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(None,'SdC',0, 1,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
           
    # Prueba 173
    def testUpdateUserHistoryTypeNoneIdUserNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(None,'SdC',0, None,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')  
              
    # Prueba 174
    def testUpdateUserHistoryCodeNoneTypeNoneBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory(None,None,0, None,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')     
           
    # Prueba 175
    def testUpdateUserHistoryTypeNoneBacklogString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Actualizamos la historia
        result = aHist.updateUserHistory('1','SdC',0, None,idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')    
                         
    # Prueba 176
    def testUpdateUserHistoryTypeArrayBacklogNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog 
           
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('Xtry cxsy',idBacklog)
        search = aAcc.searchAccion('Xtry cxsy',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('jDw',0,1,idFound,idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('jDw',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Actualizamos una historia
        result = aHist.updateUserHistory(idFound1,'SdC',0,[],idFound,1,True,TODAY,True,TODAY)
        self.assertFalse(result)
                   
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('Xtry cxsy',idBacklog)
        aBacklog.deleteProduct('Bxtyllz')        

    #########################################################      
    #            Pruebas para searchIdUserHistory           #
    #########################################################     
      
    # Caso Inicial 
       
    # Prueba 177
    def testSearchIdUserHistoryExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
  
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
          
        # Buscamos id's de historias que contengan asociado una acción por su id
        aHist.searchIdUserHistory(idFound1) 
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Casos Frontera

    # Prueba 178
    def testSearchIdUserHistoryNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
  
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
                
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchIdUserHistory(0) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Prueba 179
    def testSearchIdUserHistoryValid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
          
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        histFound = aHist.searchUserHistory('lllzz',idBacklog) 
        idFound1 = histFound[0].UH_idUserHistory
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchIdUserHistory(idFound1) 
        self.assertNotEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
               
    # Prueba 180
    def testSearchIdUserHistoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        histFound = aHist.searchUserHistory('lllzz',idBacklog) 
        idFound1 = histFound[0].UH_idUserHistory
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchUserHistory(2**28,idBacklog) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Casos Malicia
     
    # Prueba 181
    def testSearchIdUserHistoryString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        histFound = aHist.searchUserHistory('lllzz',idBacklog) 
        idFound1 = histFound[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchIdUserHistory('Patricia') 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Prueba 182
    def testSearchIdUserHistoryInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        histFound = aHist.searchUserHistory('lllzz',idBacklog) 
        idFound1 = histFound[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchIdUserHistory(-9898989898) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
             
    # Prueba 183
    def testSearchidUserHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        histFound = aHist.searchUserHistory('lllzz',idBacklog) 
        idFound1 = histFound[0].UH_idUserHistory
        
        # Buscamos id's de historias que contengan asociado una acción por su id
        res = aHist.searchIdUserHistory(None) 
        self.assertEqual([],res)
                  
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  
        
#Fin Casos userHistory
