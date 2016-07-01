# -*- coding: utf-8 -*-.

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog                import *
from userHistory            import *
from accions                import *   
from model                  import *  
from acceptanceTest         import *
from datetime               import *

TODAY = datetime.utcnow()
TOMORROW = TODAY + timedelta(days=1)


class testPrueba(unittest.TestCase):


    ####################################################
    #         Pruebas para insertAcceptanceTest        #
    ####################################################

    # Caso inicial
    #Verificar que el prueba se pueda cargar con el nombre correspondiente
    # Prueba 1
    def testInsertTestExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        oTest.insertAcceptanceTest(idStory, 'VtXcyr', '/foo/bar/baz')

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos Normales
    #Verificar que la prueba se pueda cargar con el nombre correspondiente
    # Prueba 2
    def testInsertTestElement(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest(idStory, 'VtXcyr', '/foo/bar/baz')
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos fronteras
    # Prueba posee Mayuscula
    # Prueba 3
    def testInsertTestElementMay(self):

        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest(idStory, 'SDFSDF', '/foo/bar/baz')
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba posee Minusculas
    # Prueba 4
    def testInsertTestElementMin(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest(idStory, 'pokemonisdabest', '/foo/bar/baz')
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba posee numeros
    # Prueba 5
    def testInsertTestElementDigits(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest(idStory, '1532', '/foo/bar/baz')
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba posee una combinacion de minusculas, mayusculas y numeros
    # Prueba 6
    def testInsertTestElementMixed(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest(idStory, 'PokemonDaBest1532', '/foo/bar/baz')
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Prueba con descripcion de 200 caracteres
    # Prueba 7
    def testInsertTestElement200Long(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest(idStory, 200*'S', '/foo/bar/baz')
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos esquina
    # Sin Backlog
    # Prueba 8
    def testInsertTestElementSinHistoria(self):
        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest([], 'PokemonDaBest1532', '/foo/bar/baz')
        self.assertFalse(result)

    # nombre de mas de 200 sin backlog
    # Prueba 9
    def testInsertElement250Description(self):
        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest([], 250*'S', '/foo/bar/baz')
        self.assertFalse(result)

    # Casos Maliciosos
    # Prueba 10
    def testInsertElementPathSys(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.insertAcceptanceTest(idStory, '../..', '/foo/bar/baz')
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    ####################################################
    #         Pruebas para findIdAcceptanceTest        #
    ####################################################

    # Caso inicial
    # Busqueda exitosa
    # Prueba 11
    def testIdAcceptanceTest(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        oTest.insertAcceptanceTest(idStory, 'VtXcyr', '/foo/bar/baz')
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        result = oTest.findIdAcceptanceTest(test.AT_idAT)

        self.assertTrue(result)

        # Eliminamos los datos insertados.
        
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Si el archivo existe
    # Prueba 12
    def testIdAcceptanceTestExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        oTest.insertAcceptanceTest(idStory, 'VtXcyr', '/foo/bar/baz')
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        result = oTest.findIdAcceptanceTest(test.AT_idAT)

        self.assertTrue(result)

        # Eliminamos los datos insertados.
        
        oTest.deleteAcceptanceTest(test.AT_idAT)
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Si el archivo no existe
    # Prueba 13
    def testIdAcceptanceTestDoesNotExists(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.findIdAcceptanceTest(1532)

        self.assertFalse(result)

        # Eliminamos los datos insertados.
        
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos Maliciosos
    # Id invalido
    # Prueba 14
    def testIdAcceptanceTestInvalid(self):
        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.findIdAcceptanceTest("a")
        self.assertFalse(result)

    # Id negativo
    # Prueba 15
    def testIdAcceptanceTestNegative(self):
        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.findIdAcceptanceTest(-1)
        self.assertFalse(result)

    ####################################################
    #         Pruebas para deleteAcceptanceTest        #
    ####################################################

    # Caso inicial
    # Prueba 16
    def testdeleteAcceptanceTest(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        oTest.insertAcceptanceTest(idStory, 'VtXcyr', '/foo/bar/baz')
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        result = oTest.deleteAcceptanceTest(test.AT_idAT)
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos normales
    # La prueba existe y se borra exitosamente
    # Prueba 17
    def testdeleteAcceptanceTestNormal(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',1)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idBacklog = searchBacklog[0].BL_idBacklog
    
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',idBacklog)
        search = aAcc.searchAccion('cinrohbwidia',idBacklog)
        idAccion = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idAccion, idBacklog,1,True,TODAY,True, TOMORROW)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idBacklog)
        idStory = searchHist[0].UH_idUserHistory 

        # Inicio de la prueba.
        oTest = acceptanceTest()
        oTest.insertAcceptanceTest(idStory, 'VtXcyr', '/foo/bar/baz')
        test = aHist.testsAsociatedToUserHistory(idStory)[0]
        result = oTest.deleteAcceptanceTest(test.AT_idAT)
        self.assertTrue(result)

        # Eliminamos los datos insertados.
        aHist.deleteUserHistory(idStory)
        aAcc.deleteAccion('cinrohbwidia', idBacklog)
        aBacklog.deleteProduct('Podn fjdd.')

    # Casos maliciosos
    # Id invalido
    # Prueba 18
    def testdeleteAcceptanceTestInvalidId(self):
        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.deleteAcceptanceTest("a")
        self.assertFalse(result)

    # Id negativo
    # Prueba 19
    def testdeleteAcceptanceTestNegativeId(self):
        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.deleteAcceptanceTest(-1)
        self.assertFalse(result)

    # Id nulo
    # Prueba 20
    def testdeleteAcceptanceTestNullId(self):
        # Inicio de la prueba.
        oTest = acceptanceTest()
        result = oTest.deleteAcceptanceTest(None)
        self.assertFalse(result)
