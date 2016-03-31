# -*- coding: utf-8 -*-. 

import sys
import unittest

sys.path.append('../app/scrum')
from backLog                import *
from userHistory            import *
from accions                import *   
from objective              import *
from model                  import *  
from objectivesUserHistory  import *
from datetime               import *

TODAY = datetime.utcnow()


class TestObjectivesUserHistory(unittest.TestCase):
    
    #############################################      
    #        Pruebas para insertAccion          #
    #############################################

    # Caso Inicial
  
    # Prueba 0
    def testinsertObjectiveAsociatedInUserHistory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
         
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1) 
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
 
         
    # Casos Normales
      
    # Prueba 1
      
    def testinsertObjectiveAsociatedInUserHistory1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
        self.assertTrue(result)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
#      # Casos Fronteras
#      
#      # Prueba 2
#     def testinsertObjectiveAsociatedInUserHistoryIdObjectiveNoExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(0, idFound1) 
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
     # Prueba 3
    def testinsertObjectiveAsociatedInUserHistoryIdHistoryNoExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, 0) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Prueba 4
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
           
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory((2**31)-1,idFound1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Prueba 5
    def testinsertObjectiveAsociatedInUserHistoryIdUserHistoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, (2**31)-1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
  
     # Caso Esquina
      
    # Prueba 6   
    def testinsertObjectiveAsociatedInUserHistoryNotExist(self):
        #Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(0, 0) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Prueba 7
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveAndIdHIstoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory((2**31)-1, (2**31)-1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Prueba 8
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveNotExistIdHIstoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(0, (2**31)-1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Prueba 9
    def testinsertActorAsociatedInUserHistoryIdActorBigIdHIstoryNotExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory((2**31)-1, 0) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Casos Malicia 
       
     # Prueba 10   
    def testinsertObjectiveAsociatedInUserHistoryNoExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(-1, -1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Prueba 11   
    def testinsertObjectiveAsociatedInUserHistoryString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory('1', '0') 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
     # Prueba 12   
    def testinsertObjectiveAsociatedInUserHistoryIdObjectiveNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(None, idFound1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
     # Prueba 13   
    def testinsertObjectiveAsociatedInUserHistoryIduserHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, None) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Prueba 14   
    def testinsertObjectiveAsociatedInUserHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
         
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        #Inicio de caso de prueba
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(None, None) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    #########################################################      
    #       Pruebas para idActorsAsociatedToUserHistory     #
    #########################################################     
        
    # Caso Inicial 
       
    # Prueba 15
      
    def testidObjectivesAsociatedToUserHistory(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(idFound1)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Caso Frontera
      
    # Prueba 16    
    def testidObjectivesAsociatedToUserHistoryid_userHistory1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        asoc = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(idFound1)
        self.assertTrue(result) 
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
      # Prueba 18   
    def testidObjectivosAsociatedToUserHistoryid_userHistory0(self):
        #Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        asoc = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(0)
        self.assertEqual([],result)     
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
      # Prueba 18   
    def testidObjectivesAsociatedToUserHistoryid_userHistoryBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory((2**31)-1)
        self.assertEqual([],result)     
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
    # Casos Malicia
  
      # Prueba 19   
    def testidActorsAsociatedToUserHistoryid_userHistoryNoExist(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(-1)
        self.assertEqual([],result)     
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  
          
      # Prueba 20   
    def testidObjectivesAsociatedToUserHistoryid_userHistoryNoInt(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory('1')
        self.assertEqual([],result)     
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
      # Prueba 21   
    def testidObjectiveAsociatedToUserHistoryid_userHistoryNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(None)
        self.assertEqual([],result)     
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
      # Prueba 22   
    def testidActorsAsociatedToUserHistoryid_userHistoryStringInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('hhJJkkk','oooLLLLaa',1)
        findId = aBacklog.findName('hhJJkkk')
        idBacklog = findId[0].BL_idBacklog
 
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('llop', idBacklog)
        search = aAcc.searchAccion('llop',idBacklog)
        idFound = search[0].AC_idAccion
           
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
 
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aObjAsocUsrHist.idObjectivesAsociatedToUserHistory(' ')
        self.assertEqual([],result)     
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('llop',idBacklog)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')    
 
    #########################################################      
    #       Pruebas para searchidUserHistoryIdObjective     #
    #########################################################     
     
    # Caso Inicial 
      
    # Prueba 23
     
    def testidUserHistoryIdObjectives(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Buscamos id's de historias que contengan asociado un objetivo
        aObjAs = objectivesUserHistory()
        aObjAs.searchidUserHistoryIdObjective(idFound2) 
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Casos Frontera
    
    # Prueba 24
    
    def testidUserHistoryIdObjectivesNotExist(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Buscamos id's de historias que contengan asociado un objetivo
        aObjAs = objectivesUserHistory()
        res = aObjAs.searchidUserHistoryIdObjective(0) 
        self.assertEqual([],res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Prueba 25
    
    def testidUserHistoryIdObjectivesOne(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Buscamos id's de historias que contengan asociado un objetivo
        aObjAs = objectivesUserHistory()
        res = aObjAs.searchidUserHistoryIdObjective(1) 
        self.assertNotEqual(None,res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Prueba 26
    
    def testidUserHistoryIdObjectiveBig(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Buscamos id's de historias que contengan asociado un objetivo
        aObjAs = objectivesUserHistory()
        res = aObjAs.searchidUserHistoryIdObjective(2**28) 
        self.assertEqual([],res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Casos Malicia
    
    # Prueba 27
    
    def testidUserHistoryIdObjectivesString(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Buscamos id's de historias que contengan asociado un objetivo
        aObjAs = objectivesUserHistory()
        res    = aObjAs.searchidUserHistoryIdObjective('3') 
        self.assertEqual([],res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Prueba 28
    
    def testidUserHistoryIdObjectivesInvalid(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Buscamos id's de historias que contengan asociado un objetivo
        aObjAs = objectivesUserHistory()
        res = aObjAs.searchidUserHistoryIdObjective(-3) 
        self.assertEqual([],res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Prueba 29
    
    def testidUserHistoryIdObjectiveNone(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Buscamos id's de historias que contengan asociado un objetivo
        aObjAs = objectivesUserHistory()
        res = aObjAs.searchidUserHistoryIdObjective(None) 
        self.assertEqual([],res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    ###############################################################      
    #       Pruebas para deleteObjectiveAsociatedInUserHistory    #
    ###############################################################
    
    # Caso Inicial     
    
    # Prueba 30
     
    def testDeleteUserHistoryIdObjectives(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
          
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        aObjAs.deleteObjectiveAsociatedInUserHistory(idFound2,idFound1) 
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Casos Frontera
    
    # Prueba 31
    
    def testidUserHistoryIdObjectivesNotExistAndIdUserHistoryExists(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(0,idFound1) 
        self.assertFalse(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Caso 32
        
    def testidUserHistoryIdObjectivesExistAndIdUserHistoryNotExists(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(idFound2,0) 
        self.assertFalse(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Prueba 33
    
    def testidUserHistoryIdObjectivesOneAndIdUserHistoryValid(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(idFound2, idFound1) 
        self.assertTrue(res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Prueba 34
    
    def testidUserHistoryIdObjectivesValidAndIdUserHistoryOne(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(idFound2, idFound1) 
        self.assertTrue(res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Prueba 35
    
    def testidUserHistoryIdObjectiveBigAndIdUserHistoryValid(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(2**28, idFound1) 
        self.assertFalse(res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Prueba 36
    
    def testidUserHistoryIdObjectiveValidAndIdUserHistoryBig(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
            
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(idFound2, 2**28) 
        self.assertFalse(res)
        
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Casos Esquinas
    
    # Caso 37
    
    def testidUserHistoryIdObjectivesNotExistAndIdUserHistoryNotExists(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(0,0) 
        self.assertFalse(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Prueba 38
    
    def testidUserHistoryIdObjectivesOneAndIdUserHistoryOne(self):

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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(idFound2,idFound1) 
        self.assertTrue(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Prueba 39
    
    def testidUserHistoryIdObjectiveBigAndIdUserHistoryBig(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(2**28,2**28) 
        self.assertFalse(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Casos Malicia
    
    # Prueba 40
    
    def testidUserHistoryIdObjectiveNotValidAndIdUserHistoryNotValid(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(-3,-2) 
        self.assertFalse(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Prueba 41
    
    def testidUserHistoryIdObjectiveStringAndIdUserHistoryNotValid(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory('1',-2) 
        self.assertFalse(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Prueba 42
    
    def testidUserHistoryIdObjectiveValidAndIdUserHistoryNone(self):
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
         
      # Insertamos la objetivo
        aObj = objective()
        aObj.insertObjective('Ccc',idBacklog,0)
        search = aObj.searchObjective('Ccc',idBacklog)
        idFound2 = search[0].O_idObjective
        
        # Insertamos Objetivo asociado
        aObjAsocUsrHist = objectivesUserHistory()
        result          = aObjAsocUsrHist.insertObjectiveAsociatedInUserHistory(idFound2, idFound1)
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aObjAs = objectivesUserHistory()
        res    = aObjAs.deleteObjectiveAsociatedInUserHistory(idFound2,None) 
        self.assertFalse(res)
                 
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aObj.deleteObjective('Ccc',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 

# Fin de casos ObjectivesUserHistory
