# -*- coding: utf-8 -*-.

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog import *
from accions import *
from userHistory import *
from model import *
from task import *
from category import *
from datetime import *

TODAY = datetime.utcnow()
TOMORROW = TODAY + timedelta(days=1)

class TestUserHistory(unittest.TestCase):
    #########################
    #   COMPLETE HISTORY    #
    #########################

    def testCompletarHistoriaUsuarioSinTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        self.assertEqual((aHist.completeHistory(idFound1)), True)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testCompletarHistoriaUsuarioConTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh', 1)

        # Insertamos la tarea 1
        aTarea = task()
        aTarea.insertTask('dwidjw', 1, 1, idFound1, True, TODAY,True, TOMORROW)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask

        # Insertamos la tarea 2
        bTarea = task()
        bTarea.insertTask('dfghj', 2, 2, idFound1, True, TODAY,True, TOMORROW)
        searchTask2 = bTarea.searchTask('dfghj')
        idsegunda = searchTask2[0].HW_idTask

        # Completamos historia
        self.assertEqual((aHist.completeHistory(idFound1)), True)

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        bTarea.deleteTask('dfghj')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testCompletarHistoriaUsuarioNoExistenteSinTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = 1324
        self.assertEqual((aHist.completeHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testCompletarHistoriaUsuarioNoExistenteConTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh', 1)

        # Insertamos la tarea 1
        aTarea = task()
        aTarea.insertTask('dwidjw', 1, 1, idFound1, True, TODAY,True, TOMORROW)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask

        # Insertamos la tarea 2
        bTarea = task()
        bTarea.insertTask('dfghj', 2, 2, idFound1, True, TODAY,True, TOMORROW)
        searchTask2 = bTarea.searchTask('dfghj')
        idsegunda = searchTask2[0].HW_idTask

        # Completamos historia
        badId = idFound1 + 1
        self.assertEqual((aHist.completeHistory(badId)), False)

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        bTarea.deleteTask('dfghj')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testCompletarHistoriaUsuarioIdNeg(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = -1
        self.assertEqual((aHist.completeHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testCompletarHistoriaUsuarioIdFloat(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = 1.2
        self.assertEqual((aHist.completeHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testCompletarHistoriaUsuarioIdString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = "mala idea"
        self.assertEqual((aHist.completeHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testCompletarHistoriaUsuarioIdBool(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = False
        self.assertEqual((aHist.completeHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    #########################
    #  INCOMPLETE HISTORY   #
    #########################

    def testIncompleteHistoriaUsuarioSinTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY, True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        self.assertEqual((aHist.incompleteHistory(idFound1)), True)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testIncompleteHistoriaUsuarioConTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh', 1)

        # Insertamos la tarea 1
        aTarea = task()
        aTarea.insertTask('dwidjw', 1, 1, idFound1, True, TODAY,True, TOMORROW)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask

        # Insertamos la tarea 2
        bTarea = task()
        bTarea.insertTask('dfghj', 2, 2, idFound1, True, TODAY,True, TOMORROW)
        searchTask2 = bTarea.searchTask('dfghj')
        idsegunda = searchTask2[0].HW_idTask

        # Completamos historia
        self.assertEqual((aHist.incompleteHistory(idFound1)), True)

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        bTarea.deleteTask('dfghj')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testIncompleteHistoriaUsuarioNoExistenteSinTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = idFound1 + 1
        self.assertEqual((aHist.incompleteHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testIncompleteHistoriaUsuarioNoExistenteConTareas(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh', 1)

        # Insertamos la tarea 1
        aTarea = task()
        aTarea.insertTask('dwidjw', 1, 1, idFound1, True, TODAY,True, TOMORROW)
        searchTask1 = aTarea.searchTask('dwidjw')
        idprimera = searchTask1[0].HW_idTask

        # Insertamos la tarea 2
        bTarea = task()
        bTarea.insertTask('dfghj', 2, 2, idFound1, True, TODAY,True, TOMORROW)
        searchTask2 = bTarea.searchTask('dfghj')
        idsegunda = searchTask2[0].HW_idTask

        # Completamos historia
        badId = idFound1 + 1
        self.assertEqual((aHist.incompleteHistory(badId)), False)

        # Eliminamos todo de la BD
        aTarea.deleteTask('dwidjw')
        bTarea.deleteTask('dfghj')
        aCategory.deleteCategory('wofhweoifh')
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testIncompleteHistoriaUsuarioIdNeg(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = -1
        self.assertEqual((aHist.incompleteHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testIncompleteHistoriaUsuarioIdFloat(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = 1.2
        self.assertEqual((aHist.incompleteHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testIncompleteHistoriaUsuarioIdString(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = "mala idea"
        self.assertEqual((aHist.incompleteHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')

    def testIncompleteHistoriaUsuarioIdBool(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.', 'ODJdbeidbww', 1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog

        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia', idFound0)
        search = aAcc.searchAccion('cinrohbwidia', idFound0)
        idFound = search[0].AC_idAccion

        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1', 0, 1, idFound, idFound0, 1, True, TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1', idFound0)
        idFound1 = searchHist[0].UH_idUserHistory

        # Completamos historia
        badId = False
        self.assertEqual((aHist.incompleteHistory(badId)), False)

        # Eliminamos todo de la BD
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia', idFound0)
        aBacklog.deleteProduct('Podn fjdd.')


if __name__ == '__main__':
    unittest.main()
