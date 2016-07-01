# -*- coding: utf-8 -*-. 

import sys
import unittest

sys.path.append('../app/scrum')
from backLog                import *
from actorsUserHistory      import *
from userHistory            import *
from accions                import *   
from model                  import *  
from datetime               import *

TODAY = datetime.utcnow()


class TestActorsUserHistory(unittest.TestCase):
    
    #############################################      
    #         Pruebas para insertAccion         #
    #############################################
         
    # Caso Inicial
 
    # Prueba 0
    def testinsertActorAsociatedInUserHistory(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Casos Normales
     
    # Prueba 1
     
    def testinsertActorAsociatedInUserHistory1(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        self.assertTrue(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
          
     # Casos Fronteras
      
     # Prueba 2
    def testinsertActorAsociatedInUserHistoryIdActorNoExist(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(0, idFound1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
 
     # Prueba 3
    def testinsertActorAsociatedInUserHistoryIdHistoryNoExist(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, 0) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
 
    # Prueba 4
    def testinsertActorAsociatedInUserHistoryIdActorBig(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory((2**31)-1, idFound1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
 
    # Prueba 5
    def testinsertActorAsociatedInUserHistoryIdUserHistoryBig(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, (2**31)-1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Caso Esquina
     
    # Prueba 6   
     
    def testinsertActorAsociatedInUserHistoryNotExist(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(0, 0) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
    
    # Prueba 7
    def testinsertActorAsociatedInUserHistoryIdActorAndIdHIstoryBig(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory((2**31)-1, (2**31)-1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
    # Prueba 8
    def testinsertActorAsociatedInUserHistoryIdActorNotExistIdHIstoryBig(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(0, (2**31)-1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
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
        aAcc.insertAccion('pppp',idBacklog)
        search = aAcc.searchAccion('pppp',idBacklog)
        idFound = search[0].AC_idAccion
         
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory((2**31)-1, 0) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
      
      
    # Casos Malicia 
      
     # Prueba 10   
    def testinsertActorAsociatedInUserHistoryNoExists(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(-1, -1) 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
                 
      # Prueba 11   
    def testinsertActorAsociatedInUserHistoryString(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
         
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory('1', '0') 
        self.assertFalse(result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
         
     # Prueba 12   
    def testinsertActorAsociatedInUserHistoryIdActorNone(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(None, idFound1) 
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
 
     # Prueba 13   
    def testinsertActorAsociatedInUserHistoryIduserHIstoryNone(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, None) 
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')    
  
      # Prueba 14   
    def testinsertActorAsociatedInUserHistoryNone(self):
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
              
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(None, None) 
        self.assertFalse(result)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
          
    #########################################################      
    #       Pruebas para idActorsAsociatedToUserHistory     #
    #########################################################     
        
    # Caso Inicial 
       
    # Prueba 15
      
    def testidActorsAsociatedToUserHistory(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(None, None) 
        self.assertFalse(result)
           
        #Inicio de caso de prueba 
        # Buscamos los ids de los actores asociados a una historia de usuario
        aAccAs.idActorsAsociatedToUserHistory(idFound1)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
          
    # Caso Frontera
      
    # Prueba 16    
    def testidActorsAsociatedToUserHistoryUH_idUserHistory1(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(None, None) 
          
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aAccAs.idActorsAsociatedToUserHistory(idFound1)
        self.assertEqual([],result)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
      
      # Prueba 17   
    def testidActorsAsociatedToUserHistoryUH_idUserHistory0(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(None, None) 
          
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aAccAs.idActorsAsociatedToUserHistory(0)
        self.assertEqual([],result)
          
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
         
      # Prueba 18   
    def testidActorsAsociatedToUserHistoryUH_idUserHistoryBig(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(None, None) 
         
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aAccAs.idActorsAsociatedToUserHistory((2**31)-1)
        self.assertEqual([],result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
 
    # Casos Malicia
 
      # Prueba 19   
    def testidActorsAsociatedToUserHistoryUH_idUserHistoryNoExist(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(None, None) 
         
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aAccAs.idActorsAsociatedToUserHistory(-1)
        self.assertEqual([],result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
 
      # Prueba 20   
    def testidActorsAsociatedToUserHistoryUH_idUserHistoryNoInt(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(None, None) 

         
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aAccAs.idActorsAsociatedToUserHistory('1')
        self.assertEqual([],result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
         
      # Prueba 21   
    def testidActorsAsociatedToUserHistoryUH_idUserHistoryNone(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(None, None) 
         
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aAccAs.idActorsAsociatedToUserHistory(None)
        self.assertEqual([],result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
         
      # Prueba 22   
    def testidActorsAsociatedToUserHistoryUH_idUserHistoryStringInvalid(self):
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

        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor
          
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        aAccAs.insertActorAsociatedInUserHistory(None, None) 
         
        #Inicio de caso de prueba
        # Buscamos los ids de los actores asociados a una historia de usuario
        result = aAccAs.idActorsAsociatedToUserHistory(' ')
        self.assertEqual([],result)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aAct.deleteActor('SSS',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
       
    #########################################################      
    #        Pruebas para searchidUserHistoryIdActors       #
    #########################################################     
        
    # Caso Inicial 
     
    # Prueba 23
    
    def testidUserHistoryIdActors(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Buscamos id's de historias que contengan asociado un actor
        aAccAs = actorsUserHistory()
        aAccAs.searchidUserHistoryIdActors(idFound2) 
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')
        
    # Casos Frontera
    
    # Prueba 24
    
    def testidUserHistoryIdActorsNotExist(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Buscamos id's de historias que contengan asociado un actor
        aAccAs = actorsUserHistory()
        res = aAccAs.searchidUserHistoryIdActors(0) 
        self.assertEqual(None, res)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')

    # Prueba 25
    
    def testidUserHistoryIdActorsOne(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Buscamos id's de historias que contengan asociado un actor
        aAccAs = actorsUserHistory()
        res = aAccAs.searchidUserHistoryIdActors(1) 
        self.assertNotEqual(None, res)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk') 
        
    # Prueba 26
    
    def testidUserHistoryIdActorsBig(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Buscamos id's de historias que contengan asociado un actor
        aAccAs = actorsUserHistory()
        res = aAccAs.searchidUserHistoryIdActors(2**28) 
        self.assertNotEqual(None, res)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
        
    # Casos Malicia
    
    # Prueba 27
    
    def testidUserHistoryIdActorsString(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Buscamos id's de historias que contengan asociado un actor
        aAccAs = actorsUserHistory()
        res = aAccAs.searchidUserHistoryIdActors('2') 
        self.assertEqual(None, res)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   

    # Prueba 28
    
    def testidUserHistoryIdActorsInvalid(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Buscamos id's de historias que contengan asociado un actor
        aAccAs = actorsUserHistory()
        res = aAccAs.searchidUserHistoryIdActors(-4) 
        self.assertEqual(None, res)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   

    # Prueba 29
    
    def testidUserHistoryIdActorsNone(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
        
        # Buscamos id's de historias que contengan asociado un actor
        aAccAs = actorsUserHistory()
        res = aAccAs.searchidUserHistoryIdActors(None) 
        self.assertEqual(None, res)
                
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
        
    ###############################################################      
    #        Pruebas para deleteActorAsociatedInUserHistory       #
    ###############################################################
    
    # Caso Inicial     
    
    # Prueba 30
     
    def testDeleteUserHistoryIdActors(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        aAccAs.deleteActorAsociatedInUserHistory(idFound2,idFound1) 
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
        
    # Casos Frontera
    
    # Prueba 31
    
    def testidUserHistoryIdActorsNotExistAndIdUserHistoryExists(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(0,idFound1) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
        
    # Caso 32
        
    def testidUserHistoryIdActoraExistAndIdUserHistoryNotExists(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(idFound2, 0) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
        
    # Prueba 33
    
    def testidUserHistoryIdActorsOneAndIdUserHistoryValid(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
        
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(idFound2, idFound1) 
        self.assertTrue(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
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
        aHist.insertUserHistory('lllzz',0, 1,idFound, idBacklog,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('lllzz',idBacklog)
        idFound1 = searchHist[0].UH_idUserHistory
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(idFound2, idFound1) 
        self.assertTrue(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
        
    # Prueba 35
    
    def testidUserHistoryIdActorsBigAndIdUserHistoryValid(self):
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
        
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(2**28, idFound1) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')   
        
    # Casos Esquinas
    
    # Caso 37
    
    def testidUserHistoryIdActorsNotExistAndIdUserHistoryNotExists(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(0,0) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  
        
    # Prueba 38
    
    def testidUserHistoryIdOneAndIdUserHistoryOne(self):

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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2,idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(1,1) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  
        
    # Prueba 39
    
    def testidUserHistoryIdActorsBigAndIdUserHistoryBig(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(2**28,2**28) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  

    # Casos Malicia
    
    # Prueba 40
    
    def testidUserHistoryIdActorsNotValidAndIdUserHistoryNotValid(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(-3,-2) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  
         
      # Prueba 41
    
    def testidUserHistoryIdActorStringAndIdUserHistoryNotValid(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory('3',-2) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  
        
    # Prueba 42
    
    def testidUserHistoryIdActorValidAndIdUserHistoryNone(self):
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
         
        # Insertamos Actor
        aAct = role()
        aAct.insertActor('SSS', 'Ddd', idBacklog)
        searchAct = aAct.findNameActor('SSS',idBacklog)
        idFound2 = searchAct[0].A_idActor 
                  
        # Insertamos Actor asociado
        aAccAs = actorsUserHistory()
        result = aAccAs.insertActorAsociatedInUserHistory(idFound2, idFound1) 
         
        # Inicio de caso de prueba
        # Buscamos id's de historias que contengan asociado un objetivo        
        aAccAs = actorsUserHistory()
        res    = aAccAs.deleteActorAsociatedInUserHistory(idFound2,None) 
        self.assertFalse(res)
         
        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('pppp',idBacklog)
        aBacklog.deleteProduct('hhJJkkk')  
        
# Fin de casos ActorsUserHistory
