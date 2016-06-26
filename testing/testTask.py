# -*- coding: utf-8 -*-.

import sys
import unittest

#Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog                import *
from actorsUserHistory      import *
from userHistory            import *
from accions                import *
from model                  import *
from task                   import *
from category               import *
from datetime               import *

TODAY = datetime.utcnow()

class TestTask(unittest.TestCase):

     #############################################
     #           Pruebas para insertTask         #
     #############################################

     # Caso Inicial

     # Prueba 1
     def testInserTaskExists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',idFound0)
         search = aAcc.searchAccion('cinrohbwidia',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 2
     def testInsertTaskElementNotExist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         self.assertTrue(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 3
     def testInsertTaskRepeatedElement(self):
          # Insertamos Producto
          aBacklog = backlog()
          aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
          searchBacklog = aBacklog.findName('Podn fjdd.')
          idFound0 = searchBacklog[0].BL_idBacklog

          # Insertamos la accion
          aAcc = accions()
          aAcc.insertAccion('eirnbodn',idFound0)
          search = aAcc.searchAccion('eirnbodn',idFound0)
          idFound = search[0].AC_idAccion

          # Insertamos la historia
          aHist = userHistory()
          aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
          searchHist = aHist.searchUserHistory('hIDBW',idFound0)
          idFound1 = searchHist[0].UH_idUserHistory

          # Insertamos la categoria
          aCategory = category()
          aCategory.insertCategory('wofhweoifh',5)

          # Insertamos la tarea
          aTarea = task()
          aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
          result = aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
          self.assertFalse(result)

          # Eliminamos la tarea, categoria, historia, accion y producto
          aTarea.deleteTask('dwidjw')
          aCategory.deleteCategory('wofhweoifh')
          aHist.deleteUserHistory('hIDBW')
          aAcc.deleteAccion('eirnbodn', idFound0)
          aBacklog.deleteProduct('Podn fjdd.')


     # Casos Fronteras

     # Prueba 4
     def testInsertTaskShortDesc0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('', 1, 1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')


     # Prueba 5
     def testInsertTaskShortDesc1(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('T', 1, 1, idFound1,True,TODAY,False,None)
         self.assertTrue(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask('T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 6
     def testInsertTaskShortDesc140(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         self.assertTrue(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 7
     def testInsertHistoryLong141(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(141*'T',1,1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 8
     def testInsertTaskId0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,1,0,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 9
     def testInsertTaskNoHistory(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,1,100,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 10
     def testInsertTaskLongId(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,1,2**31,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 11
     def testInsertTaskIdCategory0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',0,1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 12
     def testInsertTaskNoCategory(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',100,1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 13
     def testInsertTaskLongIdCategory(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',2**31,1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 14
     def testInsertTaskWeight0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,0,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 15
     def testInsertTaskNegativeWeight(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,-1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 16
     def testInsertTaskLongWeight(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',5)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,2**31,idFound1,True,TODAY,False,None)
         self.assertTrue(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Esquinas

     # Prueba 17
     def testinsertTaskODJdbeidbww1Id1(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         self.assertTrue(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask('T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 18
     def testInsertTask140Id1(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(140*'A',1,1,idFound1,True,TODAY,False,None)
         self.assertTrue(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask(140*'A')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 19
     def testInsertTask141NoId(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result  = aTarea.insertTask(141*'A',1,1,100,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 20
     def testInsertTask140NoId(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(140*'H',1,1,100,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 21
     def testInserTask0Id1(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('',1,1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 22
     def testInserTaskDescription1Id0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('T',1,1,0,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 23
     def testInsertTaskDescription141Id0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(141*'H',1,1,0,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 24
     def testInsertTaskDescriptionE140Id1(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result  = aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         self.assertTrue(result)

         # Eliminamos la tarea, categoria, historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aTarea.deleteTask(140*'T')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 25
     def testinsertTaskDesc1IdCWeightIdHBig(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('T',2**31,2**31,2**31,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 26
     def testinsertTaskDesc140IdCWeightIdHBig(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(140*'T',2**31,2**31,2**31,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 27
     def testinsertTaskDesc1IdC0Weight0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('T',0,0,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 28
     def testinsertTaskDesc0IdCWeightIdH0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('',2**31,2**31,0,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 29
     def testinsertTaskDesc0IdCBigWeightNegativeIdHValid(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('T',2**31,-1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 30
     def testinsertTaskDesc140IdC1Weight0IdH0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(140*'T',1,0,0,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 31
     def testinsertTaskDesc0IdC1WeightBigIdHValid(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('',1,2**31,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')


     # Prueba 32
     def testinsertTaskDesc140IdCBigWeight1IdH0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(140*'T',2**31,1,0,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn', idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Malicia

     # Prueba 33
     def testInsertTaskDesc0IdC0W0IdH0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('',0,0,0,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 34
     def testInsertTaskDescNoneIdCNoneWNoneIdHNone(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result  = aTarea.insertTask(None,None,None,None,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 35
     def testInsertTaskNoneDescIdCValidWValidIdHValid(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask(None,1,1,idFound1,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 36
     def testInsertTaskDescValidIdCValidWValidIdHBone(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,1,None,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 37
     def testInsertTaskIdCString(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw','gjasdfio',1,None,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 38
     def testInsertTaskIdCInvalid(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',-98989562321,1,None,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

 # Prueba 39
     def testInsertTaskWeightString(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,'gjasdfio',None,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 40
     def testInsertTaskWeightInvalid(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',idFound0)
         search = aAcc.searchAccion('eirnbodn',idFound0)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         # Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         # Insertamos la tarea
         aTarea = task()
         result = aTarea.insertTask('dwidjw',1,-99559523232,None,True,TODAY,False,None)
         self.assertFalse(result)

         # Eliminamos la categoria, historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',idFound0)
         aBacklog.deleteProduct('Podn fjdd.')

     #############################################
     #           Pruebas para getAllTask         #
     #############################################

      #Casos Frontera

     # Prueba 41
     def testGetAllTaskExist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         aTarea.getAllTask(idFound1)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 42
     def testGetAllTaskValid(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.getAllTask(idFound1)
         self.assertNotEqual(result,[])

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aTarea.deleteTask('dwidjw')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 43
     def testGetAllTaskNoId(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.getAllTask(100)
         self.assertEqual(result,[])

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aTarea.deleteTask('dwidjw')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 44
     def testGetAllTaskNoTask(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         result = aTarea.getAllTask(idFound1)
         self.assertEqual(result,[])

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 45
     def testGetAllTaskMaxId(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.getAllTask(2**31)
         self.assertEqual(result,[])

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Malicia

     # Prueba 46
     def testGetAllTaskNone(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.getAllTask(None)
         self.assertEqual(result,[])

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 47
     def testGetAllTaskid0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.getAllTask(0)
         self.assertEqual(result,[])

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 48
     def testGetAllTaskString(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.getAllTask("uno")
         self.assertEqual(result,[])

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #############################################
     #          Pruebas para updateTask          #
     #############################################

     # Caso Inicial

     # Prueba 49
     def testUpdateTaskExists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         aTarea.updateTask('dwidjw','diifneo',1,1,1,True,TODAY,False,None,1)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('diifneo')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 50
     def testUpdateTaskTrue(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',1,1,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('diifneo')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')


     # Casos Fronteras

     # Prueba 51
     def testUpdateTaskShortDesc0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('','diifneo',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')
         aTarea = task()

         # Eliminamos accion y producto
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 52
     def testUpdateTaskShortDesc1(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','T',1,1,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 53
     def testUpdateTaskShortDesc140(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw',140*'T',1,1,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 54
     def testUpdateHistoryLong141(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(141*'T',idFound1,1,1,True,TODAY,False,None)
         result  = aTarea.updateTask(141*'T',140*'T',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 55
     def testUpdateTaskNew0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')


     # Prueba 56
     def testUpdateTaskNoDesc(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('OEdfeenfr','diifneo',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 57
     def testUpdateTaskLongNew(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw',140*'T',1,1,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 58
     def testUpdateTaskCategory0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',0,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 59
     def testUpdateTaskNoCategory(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',1000,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 60
     def testUpdateTaskNoneCategory(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',None,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 61
     def testUpdateTaskStringCategory(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo','',1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 62
     def testUpdateTaskWeight0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',1,0,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 63
     def testUpdateTaskWeightMax(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',1,2**32,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 64
     def testUpdateTaskNoneWeight(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',1,None,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 65
     def testUpdateTaskStringWeight(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw','diifneo',1,'',1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

      # Casos Esquinas

     # Prueba 66
     def testUpdateTaskNew1(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('T','A',1,1,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('A')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 67
     def testUpdateTaskNewDescLong0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'A',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'A','',0,0,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'A')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 68
     def testUpdateTask140long141(self):
                 # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'A',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'A',141*'T',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'A')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 69
     def testUpdateTask140None(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'H',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'H',None,1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'H')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 70
     def testUpdateTask0NewDesc1(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('','T',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 71
     def testUpdateTaskDesc1New0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('T','',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 72
     def testUpdateTaskDesc141New0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         result  = aTarea.updateTask(141*'T','',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 73
     def testUpdateTaskDescE140New1(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T','T',1,1,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Malicia

     # Prueba 74
     def testUpdateTaskDesc0New0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('OEdfeenfr',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('','',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('OEdfeenfr')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 75
     def testUpdateTaskDescNoneNewNone(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(None,None,1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 76
     def testUpdateTaskNoneDescNewValid(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(None,'diifneo',1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 77
     def testUpdateTaskDescIntNew(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('dwidjw',1234,1,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 78
     def testUpdateTaskMaxValues(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('T',140*'A',1,2**31,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'A')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 79
     def testUpdateTaskMaxWeightMaxString(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',1,2**31,1,True,TODAY,False,None,None)
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'A')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 80
     def testUpdateTaskMaxDescMaxWeight(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(141*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(141*'T','A',1,2**31,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 81
     def testUpdateTaskMaxNewMaxWeight(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('T',141*'A',1,2**31,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 82
     def testUpdateTaskMaxNoCategory(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',2**31,2**31,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 83
     def testUpdateTaskMaxNoWeight(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(141*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(141*'T',141*'A',2**31,1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 84
     def testUpdateTaskMaxNoDesc(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('T',141*'A',2**31,2**31,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 85
     def testUpdateTaskLong0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('T','',1,2**31,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 86
     def testUpdateTaskLong0All(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('','',1,2**31,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 87
     def testUpdateTaskNUm0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',0,2**31,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 88
     def testUpdateTaskNum0All(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',0,0,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 89
     def testUpdateTask1None(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',1,None,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 90
     def testUpdateTask2None(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',None,None,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 91
     def testUpdateTask3None(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',None,None,None,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 92
     def testUpdateTaskMinAllParams(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('','',0,0,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 93
     def testUpdateTask2String(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',140*'a',140*'a',1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 94
     def testUpdateTask1String(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',1,140*'A',1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 95
     def testUpdateTask1StringLeft(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',140*'A',1,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Malicia

     #Prueba 96
     def testUpdateTaskNoParams(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask('','','','',1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 97
     def testUpdateAllNone(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(None,None,None,None,1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 98
     def testUpdateAllString(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('eirnbodn',1)
         search = aAcc.searchAccion('eirnbodn',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('hIDBW',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('hIDBW',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(140*'T',1,1,idFound1,True,TODAY,False,None)
         result  = aTarea.updateTask(140*'T',140*'A',140*'S',140*'R',1,True,TODAY,False,None,None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask(140*'T')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory('hIDBW')
         aAcc.deleteAccion('eirnbodn',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #############################################
     #          Pruebas para searchTask          #
     #############################################

     # Caso Inicial

     # Prueba 99
     def testSearchTask(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         aTarea.searchTask('dwidjw')

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 100
     def testSearchTaskExists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('dwidjw')
         self.assertTrue(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 101
     def testSearchTaskNotExists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('diifneo')
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Frontera

     # Prueba 102
     def testSearchTask1Exists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('T')
         self.assertTrue(result)


         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 103
     def testSearchTask140Exists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T'*140,1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('T'*140)
         self.assertTrue(result)


         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 104
     def testSearchTask0Exists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('')
         self.assertFalse(result)


         # Eliminamos historia, accion y producto
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 105
     def testSearchTask1NotExists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('A')
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 106
     def testSearchTask140NotExists(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T'*140,1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('A'*140)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Malicia

     # Prueba 107
     def testSearchTaskNone(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask(None)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 108
     def testSearchTaskStringSpace(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask(' ')
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 109
     def testSearchTaskNotString(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask(88)
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 110
     def testSearchTaskArray(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask([])
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 111
     def testSearchTaskDisctionary(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask({})
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 112
     def testSearchTaskStringLong(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
         result = aTarea.searchTask('a'*((2^31)-1))
         self.assertFalse(result)

         # Eliminamos historia, accion y producto
         aTarea.deleteTask('dwidjw')
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')


     #############################################
     #          Pruebas para deleteTask          #
     #############################################

     # Caso Inicial

     # Prueba 113
     def testdeleteTaskExist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('dwidjw')
         self.assertTrue(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 114
     def testdeleteTaskNotExist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('diifneo')
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Frontera

     # Prueba 115
     def testdeleteTask1Exist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('T')
         self.assertTrue(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 116
     def testdeleteTask140Exist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T'*140,1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('T'*140)
         self.assertTrue(result)
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 117
     def testdeleteTask1NotExist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('A')
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 118
     def testdeleteTask140NotExist(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T'*140,1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('A'*140)
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 119
     def testdeleteTask0(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('')
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 120
     def testdeleteTask(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('')
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Malicia

     # Prueba 121
     def testdeleteTaskStringSpace(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask(' ',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask(' ')
         self.assertTrue(result)
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 122
     def testdeleteTaskNotString(self):
         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask(88)
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 123
     def testdeleteTaskNone(self):
         # Insertamos Producto
         aBacklog      = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0      = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc    = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search  = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask(None)
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 124
     def testdeleteTaskArray(self):
         # Insertamos Producto
         aBacklog      = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0      = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc     = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search  = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist      = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1   = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask([])
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 125
     def testdeleteTaskDictionary(self):
         # Insertamos Producto
         aBacklog      = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0      = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc    = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search  = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist      = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1   = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask({})
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Prueba 126
     def testdeleteTaskLong(self):
         # Insertamos Producto
         aBacklog      = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0      = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc    = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search  = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist      = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1   = searchHist[0].UH_idUserHistory

         #Insertamos la categoria
         aCategory = category()
         aCategory.insertCategory('wofhweoifh',1)

         aTarea    = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)

         # Eliminamos historia, accion y producto
         result = aTarea.deleteTask('T'*((2^31)-1))
         self.assertFalse(result)
         aCategory.deleteCategory('wofhweoifh')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

    #########################################################
    #         Suite de Pruebas para historyWeight           #
    #########################################################

    # Caso Inicial

    # Prueba 127
     def testHistoryWeightExists(self):
        # Insertamos Producto
        aBacklog      = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0      = searchBacklog[0].BL_idBacklog
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0      = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc    = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search  = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist      = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1   = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound1)
        self.assertEqual(1, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos Frontera

    # Prueba 128
     def testHistoryWeightNotExists(self):
        # Insertamos Producto
        aBacklog      = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0      = searchBacklog[0].BL_idBacklog
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0      = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc    = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search  = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist      = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1   = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(0)
        self.assertEqual(0, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 129
     def testHistoryWeightIdOneEpic(self):
        # Insertamos Producto
        aBacklog      = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0      = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc     = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search  = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist      = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1   = searchHist[0].UH_idUserHistory
        aHist.insertUserHistory('BIEEIEB12',idFound1, 1,idFound, idFound0,1,True,TODAY,False,None)

        searchHist2 = aHist.searchUserHistory('BIEEIEB12',idFound0)
        idFound2    = searchHist2[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound2,True,TODAY,False,None)
        aTarea.insertTask('dwasidjw',1,5,idFound2,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound1)
        self.assertEqual('', result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwasidjw')
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory('BIEEIEB12')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 130
     def testHistoryWeightIdOneNotEpic(self):
        # Insertamos Producto
        aBacklog      = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0      = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc    = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search  = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist      = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1   = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        aCategory.insertCategory('uweuwwqe',6)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        aTarea.insertTask('dwasidjw',1,5,idFound1,True,TODAY,False,None)
        aTarea.insertTask('uyrwuwry',2,9,idFound1,True,TODAY,False,None)
        aTarea.insertTask('iophkjmbnb',2,6,idFound1,True,TODAY,False,None)
        aTarea.insertTask('qazxc',1,8,idFound1,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound1)
        self.assertEqual(29, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('qazxc')
        aTarea.deleteTask('iophkjmbnb')
        aTarea.deleteTask('uyrwuwry')
        aTarea.deleteTask('dwasidjw')
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('uweuwwqe')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 131
     def testHistoryWeightNotEpic(self):
        # Insertamos Producto
        aBacklog      = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0      = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc    = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search  = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist       = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist  = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1    = searchHist[0].UH_idUserHistory
        aHist.insertUserHistory('BIEEIEB12',idFound1, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist2 = aHist.searchUserHistory('BIEEIEB12',idFound0)
        idFound2    = searchHist2[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
        aCategory.insertCategory('jiokl',6)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound2,True,TODAY,False,None)
        aTarea.insertTask('dwasidjw',2,6,idFound2,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(idFound2)
        self.assertEqual(7, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwasidjw')
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('jiokl')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound2)
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 132
     def testHistoryWeightIdBig(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(2**31)
        self.assertEqual(0, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos Malicia

    # Prueba 133
     def testHistoryWeightIdString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight('uasshj')
        self.assertEqual(0, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 134
     def testHistoryWeightIdInvalid(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(-215848774)
        self.assertEqual(0, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba 135
     def testHistoryWeightIdNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)

        # Insertamos las tareas
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)

        # Obtenemos el peso de la historia
        result = aTarea.historyWeight(None)
        self.assertEqual(0, result)

        # Eliminamos la tarea, categoria, historia, accion y producto
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

     #########################################
     #          Pruebas para lookup          #
     #########################################

     # Caso Inicial

     # Prueba 136
     def testLookupExist(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,1),(2,2)]
         r = aTarea.lookup(l,idFound1)

         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 137
     def testLookupTrue(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,1),(2,2),(idFound1,20)]
         result  = aTarea.lookup(l,idFound1)
         self.assertNotEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Frontera

     #Prueba 138
     def testLookuId0(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,1),(2,2)]
         result  = aTarea.lookup(l,0)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 139
     def testLookupNoId(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,1),(2,2)]
         result  = aTarea.lookup(l,100)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 140
     def testLookupMaxId(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,1),(2,2)]
         result  = aTarea.lookup(l,2**31)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 141
     def testLookupNoneId(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,1),(2,2)]
         result  = aTarea.lookup(l,None)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 142
     def testLookupEmpty(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = []
         result  = aTarea.lookup(l,1)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 143
     def testLookupLen1(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,1)]
         result  = aTarea.lookup(l,1)
         self.assertNotEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 144
     def testLookupNoTupleFound(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(2,1)]
         result  = aTarea.lookup(l,1)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 145
     def testLookupNoneTuple(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [None]
         result  = aTarea.lookup(l,1)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 146
     def testLookupNoneTupleList(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = None
         result  = aTarea.lookup(l,1)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Esquina

     #Prueba 147
     def testLookupLenwithNotuple(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,2),2]
         result  = aTarea.lookup(l,1)
         self.assertNotEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 148
     def testLookupNoneTupleWithString(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = ['a',(2,1)]
         result  = aTarea.lookup(l,2)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 149
     def testLookupNoneTupleLen3(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [(1,2),None,(2,1)]
         result  = aTarea.lookup(l,2)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 150
     def testLookupLen0NoneId(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = []
         result  = aTarea.lookup(l,None)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 151
     def testLookupLen0Id0(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = []
         result  = aTarea.lookup(l,0)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     # Casos Malicia

     #Prueba 152
     def testLookupAllNone(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = None
         result  = aTarea.lookup(l,None)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 153
     def testLookupNoneTupleListNoneid(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [None]
         result  = aTarea.lookup(l,None)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 154
     def testLookupNoneTupleIdstring(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = [None]
         result  = aTarea.lookup(l,"abc")
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

     #Prueba 155
     def testLookupLen0MaxId(self):

         # Insertamos Producto
         aBacklog = backlog()
         aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
         searchBacklog = aBacklog.findName('Podn fjdd.')
         idFound0 = searchBacklog[0].BL_idBacklog

         # Insertamos la accion
         aAcc = accions()
         aAcc.insertAccion('cinrohbwidia',1)
         search = aAcc.searchAccion('cinrohbwidia',1)
         idFound = search[0].AC_idAccion

         # Insertamos la historia
         aHist = userHistory()
         aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
         searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
         idFound1 = searchHist[0].UH_idUserHistory

         aTarea = task()
         aTarea.insertTask('T',1,1,idFound1,True,TODAY,False,None)
         l = []
         result  = aTarea.lookup(l,2**1)
         self.assertEqual('',result)

         #ELiminamos la historia, tarea, accion y backlog
         aTarea.deleteTask('T')
         aHist.deleteUserHistory(idFound1)
         aAcc.deleteAccion('cinrohbwidia',1)
         aBacklog.deleteProduct('Podn fjdd.')

    #########################
    #     COMPLETE TASK     #
    #########################


     def testCompletarTarea(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos Tarea
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask
        searchTask1 = searchTask1[0]

        # Completamos tarea
        self.assertTrue(aTarea.updateTask(searchTask1.HW_description,searchTask1.HW_description,searchTask1.HW_idCategory,searchTask1.HW_weight,searchTask1.HW_estimatedTime,searchTask1.HW_iniciado, searchTask1.HW_fechaInicio,True,TODAY,5))

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

     def testCompletarTareaNoExistente(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos tarea
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask
        searchTask1=searchTask1[0]

        # Completamos historia
        badId = idprimera + 1
        self.assertFalse(aTarea.updateTask("lol",searchTask1.HW_description,searchTask1.HW_idCategory,searchTask1.HW_weight,searchTask1.HW_estimatedTime, searchTask1.HW_iniciado, searchTask1.HW_fechaInicio,True,TODAY,5))

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    
    #########################
    #  INCOMPLETE HISTORY   #
    #########################

     def testCompletarTareaFechaInferiorInicio(self):
          # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos Tarea
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask
        searchTask1 = searchTask1[0]

        # Completamos tarea
        self.assertFalse(aTarea.updateTask(searchTask1.HW_description,searchTask1.HW_description,searchTask1.HW_idCategory,searchTask1.HW_weight,searchTask1.HW_estimatedTime,searchTask1.HW_iniciado, searchTask1.HW_fechaInicio,True,TODAY-timedelta(days=1),5))

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

     def testIncompleteTarea(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos Tarea
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        searchTask1 = aTarea.searchTask('dwidjw')
        searchTask1=searchTask1[0]
        

        # Completamos historia
        self.assertTrue(aTarea.updateTask(searchTask1.HW_description,searchTask1.HW_description,searchTask1.HW_idCategory,searchTask1.HW_weight,searchTask1.HW_estimatedTime, searchTask1.HW_iniciado, searchTask1.HW_fechaInicio,False,None,5))

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

     def testIncompleteTareaNoExistente(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos Tarea
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask
        searchTask1 = searchTask1[0]

        # Completamos historia
        badId = idprimera + 1
        self.assertFalse(aTarea.updateTask("lol",searchTask1.HW_description,searchTask1.HW_idCategory,searchTask1.HW_weight,searchTask1.HW_estimatedTime,False, TODAY,False,None,5))


        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
        
     def testNegativeEstimatedHours(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos Tarea
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask
        searchTask1 = searchTask1[0]
        
        # 
        badId = idprimera + 1
        self.assertFalse(aTarea.updateTask("dwidjw",searchTask1.HW_description,searchTask1.HW_idCategory,searchTask1.HW_weight,-1,False, TODAY,False,None,5))

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
        
     def testNegativeRealHours(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idFound0)
        search = aAcc.searchAccion('cinrohbwidia',idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1,True,TODAY,False,None)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos Tarea
        aTarea = task()
        aTarea.insertTask('dwidjw',1,1,idFound1,True,TODAY,False,None)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask
        searchTask1 = searchTask1[0]
        
        # 
        badId = idprimera + 1
        self.assertFalse(aTarea.updateTask("dwidjw",searchTask1.HW_description,searchTask1.HW_idCategory,searchTask1.HW_weight,5,False, TODAY,False,None,-5))

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')
        
        
