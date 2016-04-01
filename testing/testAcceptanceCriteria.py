# -*- coding: utf-8 -*-.

import sys
import unittest

# Ruta que permite utilizar el módulo sprintClass.py
sys.path.append('../app/scrum')

from sprintClass import *
from accions     import *
from category    import *
from task        import *

class TestAcceptanceCriteriaClass(unittest.TestCase):
    def setUp(self):
        # Insertamos el backlog de prueba.
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog

        # Insertamos el sprint de prueba.
        oSprint  = sprints()

        #Creamos un nuevo sprint
        oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)


    def tearDown(self):
        # Eliminamos los datos insertados.
        self.aBacklog.deleteProduct('Bxtyllz')


    ###################################################
    #       Pruebas para insertAcceptanceCriteria     #
    ###################################################
        # Caso Inicial
    # Prueba 1
    def testAcceptanceCriteria(self):
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Casos Normales

    # Prueba 2
    def testInsertSprintElement(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 3
    def testInsertSprintRepeatedNumber(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        result1   = aSprint.insertSprint(1,'Haskndwkd akdmkwdmdwa',self.idBacklog)
        self.assertFalse(result1)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Casos Fronteras

    # Prueba 4
    def testInsertSprintShortDesc0(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'',self.idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 5
    def testInsertSprintLongDesc1(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,'@',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 6
    def testInsertSprintLongDesc140(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,20*'LlWmcrl',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 7
    def testInsertSprintLongDesc141(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,20*'LlWmcrl' + 'x',self.idBacklog)
        self.assertFalse(result)
        aSprint.deleteSprint(1,self.idBacklog)

    # Prueba 8
    def testInsertSprintIdBackLogInvalid(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'Wtqczr ul mds dfbyl',0)
        self.assertFalse(result)

    # Casos Esquinas

    # Prueba 9
    def testInsertSprintIdBacklogNoExists(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'DwfEndqr cun fw3rzv',80)
        self.assertFalse(result)

    # Prueba 10
    def testInsertSprintLongDesc140AndIdBackLogNoExists(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,20*'LlWmcrl',99)
        self.assertFalse(result)

    def testInsertMaxSprintNumber(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(MAX_SPRINT_NUMBER,'MAX_SPRINT_TEST',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(MAX_SPRINT_NUMBER,self.idBacklog)