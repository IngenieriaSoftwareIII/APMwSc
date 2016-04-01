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
        # Caso InicialaCriteria

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
    def testInsertCriteriaIdHistoryInvalid(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(0, 'Descripcion Criterio')
        self.assertFalse(result)

    # Casos Esquinas
    # Prueba 10
    def testInsertCriteriaIdHistoryNoExists(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(80, 'Descripcion Criterio')
        self.assertFalse(result)

    # Prueba 11
    def testInsertCriteriaLongDesc140AndIdHistoryNoExists(self):
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
    # Caso Inicial

    # Prueba
    def testDeletCriteriaExists(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)


    # Casos Normales
    # Prueba
    def testDeleteValidCriteria(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        result = aCriteria.deleteAcceptanceCriteria(idCriterio)
        self.assertTrue(result)


    # Casos Fronteras internas

    # Prueba
    def testDeleteCriteriaNum1ValidIdHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    #Prueba
    def testDeleteCriteriaNum1000ValidIdHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(1000, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(1000, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    #Prueba
    def testDeleteCriteriaNum1ValidIdHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(1, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(1, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    #Prueba
    def testDeleteCriteriaNum1001ValidIdHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(1001, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(1001, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    #Prueba
    def testDeleteSprintNegativeNumValidIdHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(-1, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(-1, 'Descripcion Criterio')
        result = aCriteria.deleteAcceptanceCriteria(idCriterio)
        self.assertFalse(result)

    #Prueba
    def testDeleteCriteriaStringNumValidIdHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria('1', 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID('1', 'Descripcion Criterio')
        result = aCriteria.deleteAcceptanceCriteria(idCriterio)
        self.assertFalse(result)

    #Prueba
    def testDeleteCriteriaNoneNumValidIdHistory(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(None, 'Descripcion Criterio')

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(None, 'Descripcion Criterio')
        result = aCriteria.deleteAcceptanceCriteria(idCriterio)
        self.assertFalse(result)

    #Prueba
    def testDeleteSprintNotNumValidIdHistory(self):
        aCriteria = acceptanceCriteria()

        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        result = aCriteria.deleteAcceptanceCriteria(idCriterio)
        self.assertFalse(result)

    ##############################################
    #   Pruebas para modifyAcceptanceCriteria    #
    ##############################################

    # Prueba
    def testModifyCriteria(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        aCriteria.modifyAcceptanceCriteria(idCriterio, 'Descripcion Nueva')
        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Nueva')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Casos Normales

    # Prueba
    def testModifyAcceptanceCriteria(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(idCriterio, 'Descripcion Nueva')
        self.assertTrue(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Nueva')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyRepeatedCriteria(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(idCriterio, 'Descripcion Criterio') # mismo que el anterior
        self.assertTrue(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Casos Fronteras

    # Prueba
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

        aCriteria.insertAcceptanceCriteria(idHistoria2, 'Descripcion Criterio1')
        idCriterio2 = aCriteria.getAceptanceCriteriaID(idHistoria2, 'Descripcion Criterio1')
        result = aCriteria.modifyAcceptanceCriteria(idCriterio2, 'Descripcion Criterio1 Modificada')

        self.assertTrue(result)
        #Eliminamos los datos insertados
        idCriterio1 = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        idCriterio2 = aCriteria.getAceptanceCriteriaID(idHistoria2, 'Descripcion Criterio1 Modificada')
        aCriteria.deleteAcceptanceCriteria(idCriterio1)
        aCriteria.deleteAcceptanceCriteria(idCriterio2)

    # Prueba
    def testModifyCriteriaShortDesc0(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(idCriterio, 'D')
        self.assertTrue(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'D')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyCriteriaLongDesc1(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(idCriterio, '@')
        self.assertTrue(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, '@')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyCriteriaLongDesc140(self):
        aCriteria = acceptanceCriteria()
        result = aCriteria.insertAcceptanceCriteria(self.idHistory, 20*'LlWmcrl')

        self.assertTrue(result)
        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 20*'LlWmcrl')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyCriteriaLongDesc141(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(idCriterio, 20*'LlWmcrl'+'x')
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyCriteriaIdHistoryInvalid(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(0, 'Descripcion Criterio')
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Casos Esquinas
    # Prueba
    def testModifyCriteriaIdHistoryNoExists(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(80, 'Descripcion Criterio')
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyCriteriaLongDesc140AndIdHistoryNoExists(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(80, 100*'LlWmcrl')
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Casos Maliciosos
    # Prueba
    def testModifyNotString(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(80, 1548785)
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyNoneAsString(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(80, None)
        self.assertTrue(result)
        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyIdNegative(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(-1, 'Descripcion Criterio')
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    # Prueba
    def testModifyIdAsString(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(str(self.idHistory), 'Descripcion Criterio')
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)

    #Prueba 16
    def testModifyNegativeDescription(self):
        aCriteria = acceptanceCriteria()
        aCriteria.insertAcceptanceCriteria(self.idHistory, 'Descripcion Criterio')

        #Inicio Prueba
        result = aCriteria.modifyAcceptanceCriteria(self.idHistory, -1)
        self.assertFalse(result)

        #Eliminamos los datos insertados
        idCriterio = aCriteria.getAceptanceCriteriaID(self.idHistory, 'Descripcion Criterio')
        aCriteria.deleteAcceptanceCriteria(idCriterio)