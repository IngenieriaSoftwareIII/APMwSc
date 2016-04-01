# -*- coding: utf-8 -*-.

import sys
import unittest

# Ruta que permite utilizar el módulo acceptanceCriteria.py
sys.path.append('../app/scrum')

from acceptanceCriteria import *
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
        self.idHistory = oHistory.searchUserHistory('jDw',self.idBacklog)[0].UH_idUserHistory #Obtenemos el id de la historia


    def tearDown(self):
        # Eliminamos los datos insertados.
        self.aBacklog.deleteProduct('Bxtyllz')


    ###################################################
    #       Pruebas para insertAcceptanceCriteria     #
    ###################################################
        # Caso InicialaSprint

    # Prueba 1
    def testAcceptanceCriteria(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Casos Normales

    # Prueba 2
    def testInsertAcceptanceCriteria(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        self.assertTrue(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba 3
    def testInsertRepeatedCriteria(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        self.assertFalse(result)
        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Casos Fronteras

    # Prueba 4
    def testInsertRepeatedCriteriaDiferentHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Accion2', self.idBacklog)
        search  = oAccion.searchAccion('Accion2', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        oHistory.insertUserHistory('Historia2',0,1,idFound,self.idBacklog,1)
        idHistoria2 = oHistory.searchUserHistory('Historia2',self.idBacklog)[0].UH_idUserHistory #Obtenemos el id de la historia

        result = aCriteria.insertAcceptanceCriteria(idHistoria2, 'Descripcion Criterio1')

        self.assertTrue(result)
        #Eliminamos los datos insertados
        idCriterio1 = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        idCriterio2 = aCriteria.getAceptanceCriteriaID(idHistoria2, 'Descripcion Criterio1')
        aCriteria.deleteAcceptanceCriteria(idCriterio1)
        aCriteria.deleteAcceptanceCriteria(idCriterio2)

    # Prueba 5
    def testInsertCriteriaShortDesc0(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, 'D')

        self.assertTrue(result)
        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'D')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba 6
    def testInsertCriteriaLongDesc1(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, '@')

        self.assertTrue(result)
        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, '@')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba 7
    def testInsertCriteriaLongDesc140(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, 20*'LlWmcrl')

        self.assertTrue(result)
        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 20*'LlWmcrl')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba 8
    def testInsertCriteriaLongDesc141(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, 20*'LlWmcrl'+'x')
        self.assertFalse(result)

    # Prueba 9
    def testInsertCriteriaIdBackLogInvalid(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(0, 'Descripcion Criterio')
        self.assertFalse(result)

    # Casos Esquinas
    # Prueba 10
    def testInsertCriteriaIdBacklogNoExists(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(80, 'Descripcion Criterio')
        self.assertFalse(result)

    # Prueba 11
    def testInsertSprintLongDesc140AndIdBackLogNoExists(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(80, 100*'LlWmcrl')
        self.assertFalse(result)

    # Casos Maliciosos
    # Prueba 12
    def testInsertNotString(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(80, 1548785)
        self.assertFalse(result)

    # Prueba 13
    def testInsertNoneAsString(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(80, None)
        self.assertFalse(result)

    # Prueba 14
    def testInsertIdNegative(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(-1, 'Descripcion Criterio')
        self.assertFalse(result)

    # Prueba 15
    def testInsertIdAsString(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(str(self.idHistory), 'Descripcion Criterio')
        self.assertFalse(result)

    #Prueba 16
    def testInsertNegativeDescription(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, -1)
        self.assertFalse(result)

    ##############################################
    #   Pruebas para deleteAcceptanceCriteria    #
    ##############################################
    