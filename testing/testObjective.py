# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo objective.py
sys.path.append('../app/scrum')

from objective import *

class TestObjectives(unittest.TestCase):
    
    #############################################      
    #        Pruebas para insertObjective       #
    #############################################
          
    # Caso Inicial
  
    # Prueba 1
    def testInsertObjectiveExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True,False)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')        

    # Casos Normales
    
    # Prueba 2          
    def testInsertObjectiveElement(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj   = objective()
        result = oObj.insertObjective('Xstzdyzr',idBacklog,False,False)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Xstzdyzr',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
                         
    # Prueba 3
    def testInsertObjectiveRepeatedElement(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxñxn yl pynszm',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective('Xstzdyzr',idBacklog,True,False)
        result1   = oObj.insertObjective('Xstzdyzr',idBacklog,True,False)
        self.assertFalse(result1)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Xstzdyzr',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
              
    # Casos Fronteras
 
    # Prueba 4
    def testInsertObjectiveShortDesc0(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xmpysxblz cxncz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective('',idBacklog,True,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
                             
    # Prueba 5
    def testInsertObjectiveLongDesc1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxrsyr qxtry',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective('@',idBacklog,False,False)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('@',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
                   
    # Prueba 6
    def testInsertObjectiveLongDesc140(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Czmpytxcxzn',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective(20*'Llxmxry',idBacklog,False,False)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 7
    def testInsertObjectiveLongDesc141(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dx qytrx crxdytts',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective(20*'Llxmxry' + 's',idBacklog,True,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
                 
    # Prueba 8
    def testInsertObjectiveIdBacklogInvalid(self):
        # Insertamos los datos necesarios.
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Hxrys dz szxñy',1)
        # Inicio de la prueba.
        oObj     = objective()
        result   = oObj.insertObjective('Xstsdpxr',0,False,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 9
    def testInsertObjectiveObjTypeInvalid(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Hxrys dz szxñy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective('Xstzdyfr',idBacklog,'Falseee',False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Casos Esquinas
        
    # Prueba 10
    def testInsertObjectiveIdBacklogNoExists(self):
        # Insertamos los datos necesarios.
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxmplyczdz',1)
        # Inicio de la prueba.
        oObj     = objective()
        result   = oObj.insertObjective('Dxs pyrczylcs',99,True,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 11
    def testInsertObjectiveLongDesc140AndIdBacklogNoExists(self):
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        # Inicio de la prueba.
        oObj     = objective()
        result   = oObj.insertObjective(20*'Llxmxry',99,True,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 12
    def testInsertObjectiveLongDesc140AndIdBacklogExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective(20*'Llxmxry',idBacklog,False,False)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 13
    def testInsertObjectiveLongDesc1AndIdBacklogExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxcxs prxfysxrys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective('L',idBacklog,True,False)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('L',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 14
    def testInsertObjectiveLongDesc1AndIdBacklogNotExistsObjTypeExists(self):
        # Insertamos los datos necesarios.
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxcxs prxfysxrys',1)
        # Inicio de la prueba.
        oObj     = objective()
        result   = oObj.insertObjective('L',7,False,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 15
    def testInsertObjectiveLongDesc0AndIdBacklogExistsObjTypeExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective('',idBacklog,True,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
        
    # Casos Maliciosos
       
    # Prueba 16
    def testInsertNotString(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Pxsydy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective(4350,idBacklog,True,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
            
    # Prueba 17
    def testInsertNoneString(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx yxtxnsy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective(None,idBacklog,False,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 18
    def testInsertWrongObjType(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx yxtxnsy',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.insertObjective('Estudiar bastante',idBacklog,'Falseeeee',False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 19
    def testInsertWrongAllParameters(self):
        # Insertamos los datos necesarios.
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        # Inicio de la prueba.
        oObj     = objective()
        result   = oObj.insertObjective(13500,0,'True or False',False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 20
    def testInsertNoneAllParameters(self):
        # Insertamos los datos necesarios.
        oBacklog = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx',1)
        # Inicio de la prueba.
        oObj     = objective()
        result   = oObj.insertObjective(None,0,None,False)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    #############################################      
    #       Pruebas para searchObjective        #
    #############################################
        
    # Caso Inicial
        
    # Prueba 21 
    def testsearchObjectiveExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xstzdyfr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True,False)
        oObj.searchObjective('Szbxr xndxcy',idBacklog)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Casos Fronteras
        
    # Prueba 22
    def testsearchObjectiveShortDesc0(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Trxbxjxr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.        
        oObj      = objective()
        result    = oObj.searchObjective('',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
       
    # Prueba 23
    def testsearchObjectiveShortDesc1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Txrmynzr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba
        oObj      = objective()
        oObj.insertObjective('A',idBacklog,True,False)
        result    = oObj.searchObjective('A',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('A',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
            
    # Prueba 24
    def testsearchObjectiveShortDesc140(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Trxbxjxr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,True,False)
        result    = oObj.searchObjective(20*'Llxmxry',idBacklog)
        self.assertNotEqual(result,[],"Objectivo no encontrado")
        # Eliminamos los datos insertados.
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 25
    def testsearchObjectiveShortDesc141(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xstryctyrz dx ly mytxrgx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective(20*'Llxmxry'+'s',idBacklog,False,False)
        result    = oObj.searchObjective(20*'Llxmxry'+'s',idBacklog)
        self.assertFalse(result, "Objective no encontrado")
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
   
    # Caso Normal
       
    # Prueba 26
    def testsearchObjectiveDescNotExist(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxlyczvn',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.searchObjective('Cxmznycxrsd vyx cxrrzy',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
   
    # Casos Maliciosos
        
     # Prueba 27
    def testsearchObjectiveNotString(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Vxcxcyznvs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
 
        # Inicio de la prueba. 
        oObj      = objective()
        oObj.insertObjective(4350,1,True,False)
        result    = oObj.searchObjective(4350,idBacklog)
        self.assertEqual(result, [],'Objectivo encontrado')
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
  
    # Prueba 28 
    def testSearchNameNoneString(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxpydzz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.   
        oObj      = objective()
        result    = oObj.searchObjective(None,idBacklog)
        self.assertEqual(result, [],'objective encontrado')
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
           
    #############################################      
    #     Pruebas para searchIdObjective        #
    ############################################# 
     
    # Caso Inicial
           
    # Prueba 29  
    def testsearchIdObjectiveExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True,False)
        result    = oObj.searchObjective('Szbxr xndxcy',idBacklog)
        idObj     = result[0].O_idObjective
        oObj.searchIdObjective(idObj)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Caso Normal
           
    # Prueba 30 
    def testsearchValidIdObjective(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,False,False)
        result    = oObj.searchObjective('Szbxr xndxcy',idBacklog)
        idObj     = result[0].O_idObjective
        result    = oObj.searchIdObjective(idObj)
        self.assertNotEqual([],result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
               
    # Caso Frontera
           
    # Prueba 31 
    def testsearchIdObjective(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True,False)
        result    = oObj.searchObjective('Szbxr xndxcy',idBacklog)
        idObj     = result[0].O_idObjective
        result    = oObj.searchIdObjective(idObj)
        self.assertNotEqual([],result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
           
    # Prueba 32
    def testsearchInValidIdObjective(self):
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.searchIdObjective(2**28)
        self.assertEqual([],result)
 
    # Prueba 33
    def testSearchIdZero(self):
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.searchIdObjective(0)
        self.assertEqual(result,[],"Elemento no encontrado")
                     
    # Casos Maliciosos
      
    # Prueba 34
    def testSearchIdString(self):
        # Inicio de la prueba.
        oObj       = objective()
        result     = oObj.searchIdObjective('')
        self.assertEqual(result,[],"Elemento Insertado")      
 
    # Prueba 35
    def testSearchIdNoneString(self):
        # Inicio de la prueba.        
        oObjective= objective()
        result    = oObjective.searchIdObjective(None)
        self.assertEqual(result,[],"Válido")           
          
    #############################################      
    #       Pruebas para updateObjective        #
    #############################################  
    # Caso Inicial
       
    # Prueba 36
    def testupdateObjectiveExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxscrypcyzn',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.   
        oObj      = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True,False)
        oObj.updateObjective('Pxsxr cyn ctncy','Pxsxr cyn czncy',False,False,idBacklog)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Pxsxr cyn czncy',idBacklog)
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')  
 
    # Casos Normales
       
    # Prueba 37
    def testupdateObjectiveDesc(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Xnyvzrsydvd',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Xstzdyzr',idBacklog,True,False)
        result    = oObj.updateObjective('Xstzdyzr','Cxnsyltzas',False,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Xstzdyzr',idBacklog)
        oObj.deleteObjective('Cxnsyltzas',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')                                  
            
    # Prueba 38     
    def testupdateObjectiveDescNotExist(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.updateObjective('LLxgyr sxgzrj','Yr pxr lx szgvrx',True,False,idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Casos Fronteras
         
    # Prueba 39
    def testupdateObjectiveLeftLen1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Bxsqxydz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('A',idBacklog,False,False)
        result    = oObj.updateObjective('A','Bxscyr yl przft',True,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('A',idBacklog)
        oObj.deleteObjective('Bxscyr yl przft',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 40
    def testupdateObjectiveRightLong1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Bxsqxydz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Bxscyr yl przft',idBacklog, False,False)
        result    = oObj.updateObjective('Bxscyr yl przft','A',True,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Bxscyr yl przft',idBacklog)
        oObj.deleteObjective('A',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 41         
    def testupdateObjectiveRightLen140(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxchys mytzrvys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Cxrsyr fn pyrylflx',idBacklog,True,False)
        result    = oObj.updateObjective('Cxrsyr fn pyrylflx',140*'T',False,False,idBacklog)
        self.assertTrue(result)    
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Cxrsyr fn pyrylflx',idBacklog)
        oObj.deleteObjective(140*'T',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
                                   
    # Prueba 42
    def testupdateObjectiveLeftLen140(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzxs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective(140*'T',idBacklog, False,False)
        result    = oObj.updateObjective(140*'T','Mxtyrzxs x cfrsxr',True,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective(140*'T',idBacklog)
        oObj.deleteObjective('Mxtyrzxs x cfrsxr',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Casos Esquinas
        
    # Prueba 43
    def testupdateObjectiveLeftLen1RightLen140(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Vxrly',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('A',idBacklog,False,False)
        result    = oObj.updateObjective('A',70*'Us',True,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('A',idBacklog)
        oObj.deleteObjective(70*'Us',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs') 
 
    # Prueba 44
    def testupdateObjectiveLeftLen140RightLen140(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzxs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog         
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective(140*'U',idBacklog,True,False)
        result    = oObj.updateObjective(140*'U', 140*'M',False,False,idBacklog)
        self.assertTrue(result) 
        # Eliminamos los datos insertados.
        oObj.deleteObjective(140*'M',idBacklog)
        oObj.deleteObjective(140*'U',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 45
    def testupdateObjectiveLeftLen140RightLen1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Qxtry crzdytfs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,True,False)
        result    = oObj.updateObjective(20*'Llxmxry','M',False,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oObj.deleteObjective('M',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
            
    # Prueba 46
    def testupdateObjectiveLeftLen1RightLen1(self):
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Prxfysxrys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('X',idBacklog,True,False)
        result    = oObj.updateObjective('X','U',False,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('X',idBacklog)
        oObj.deleteObjective('U',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs') 
            
    # Casos Maliciosos
        
    # Prueba 47
    def testupdateSameName(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Txmys',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True,False)
        result    = oObj.updateObjective('Pxsxr cyn ctncy','Pxsxr cyn ctncy',False,False,idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
            
    # Prueba 48
    def testupdateObjectiveLeftLen1RightLen141(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('A',1,False,False)
        result    = oObj.updateObjective('',20*'Llxmxry'+'s',True,False,idBacklog)
        self.assertFalse(result, "Modificación válida") 
        # Eliminamos los datos insertados.
        oObj.deleteObjective('A',1)
        oBacklog.deleteProduct('Xstryctyrzs')
  
    # Prueba 49
    def testupdateObjectiveLeftLen140RightLen141(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxddxs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,False,False)
        result    = oObj.updateObjective(20*'Llxmxry',70*'Ma' + 's',False,False,idBacklog)
        self.assertFalse(result, "Modificación Válida") 
        # Eliminamos los datos insertados.
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
            
    # Prueba 50
    def testupdateObjectiveLeftLen140RightLen0(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx vxlzdx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective(20*'Llxmxry',idBacklog,True,False)
        result    = oObj.updateObjective(20*'Llxmxry','',False,False,idBacklog)
        self.assertFalse(result, "Modificación válida") 
        # Eliminamos los datos insertados.
        oObj.deleteObjective(20*'Llxmxry',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')  
         
    # Prueba 51
    def testupdateObjectiveLeftNoneRightValidString(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxcorrxr dyxgrxmx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.updateObjective(None,'Cxmznycxrsd vyx cxrrzy',True,False,idBacklog)
        self.assertFalse(result,"Modificación válida") 
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')  
 
    # Prueba 52
    def testupdateObjectiveLeftValidStringRightNone(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Rxcorrxr dyxgrxmx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,False,False)
        result    = oObj.updateObjective('Pxsxr cyn ctncy',None,True,False,idBacklog)
        self.assertFalse(result, "Modificación válida") 
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')    
 
    #############################################      
    #       Pruebas para deleteObjective        #
    ############################################# 
        
    # Caso Inicial
        
    # Prueba 53
    def testDeleteObjectiveExists(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzx Dyscrxtz',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        oObj      = objective()
        oObj.insertObjective('Rxsxrvyr czpk',idBacklog,True,False)
        # Inicio de la prueba.
        oObj.deleteObjective('Rxsxrvyr czpk',idBacklog)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
            
        # Casos Normales
 
    # Prueba 54
    def testDeleteObjective(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxrsyr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        oObj      = objective()
        oObj.insertObjective('U',idBacklog,False,False)
        # Inicio de la prueba.
        result    = oObj.deleteObjective('U',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Casos Fronteras
 
    # Prueba 55
    def testDeleteObjective1(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Fxltxn dzs',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        oObj      = objective()
        oObj.insertObjective('A',idBacklog,True,False)
        # Inicio de la prueba.
        result    = oObj.deleteObjective('A',idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')          
   
    # Prueba 56      
    def testDeleteObjectiveNoObjective(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxtyrzfs dy cxdynx',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        oObj      = objective()
        oObj.insertObjective('yyy',idBacklog,True,False)
        # Inicio de la prueba.
        result    = oObj.deleteObjective('xxx',idBacklog)
        self.assertFalse(result)
        oObj.deleteObjective('yyy',idBacklog)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
      
    # Casos Maliciosos
   
    # Prueba 57
    def testDeleteObjectiveInvalid(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.deleteObjective('',idBacklog)
        self.assertFalse(result,"Id no válido")
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
            
    # Prueba 58
    def testDeleteObjectiveNotString(self):
        # Insertamos los datos necesarios.
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Determinacion',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        oObj      = objective()
        oObj.insertObjective(12345,idBacklog,False,False)
        # Inicio de la prueba.
        result    = oObj.deleteObjective(12345,idBacklog)
        self.assertFalse(result,"Id no válido")
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Prueba 59    
    def testDeleteObjectiveNotExist(self):
        oBacklog  = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId    = oBacklog.findName('Xstryctyrzs')
        idBacklog = findId[0].BL_idBacklog 
        # Inicio de la prueba.
        oObj      = objective()
        result    = oObj.deleteObjective('Txrmynzr dx pzszr',idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        oBacklog.deleteProduct('Xstryctyrzs')
          
    ###################################################      
    #      Pruebas para VerifyObjectiveTransverse     #
    ###################################################
 
   # Caso Inicial
   
    # Prueba 60
    def testVerifyObjectiveExists(self):
        # Insertamos los datos necesarios.
        oBacklog   = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Mxyvy przmedxz',1)
        findId     = oBacklog.findName('Xstryctyrzs')
        idBacklog  = findId[0].BL_idBacklog 
        oObj       = objective()
        oObj.insertObjective('Pxsxr cyn ctncy',idBacklog,True,False)
        result     = oObj.searchObjective('Pxsxr cyn ctncy',idBacklog)
        idObj      = result[0].O_idObjective
        # Inicio de la prueba.
        transverse = oObj.verifyObjectiveTransverse(idObj)
        self.assertTrue(transverse)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Pxsxr cyn ctncy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Caso Normal
           
    # Prueba 61 
    def testVerifyValidIdObjectiveTransverse(self):
        # Insertamos los datos necesarios.
        oBacklog   = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId     = oBacklog.findName('Xstryctyrzs')
        idBacklog  = findId[0].BL_idBacklog 
        oObj       = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,False,False)
        result     = oObj.searchObjective('Szbxr xndxcy',idBacklog)
        idObj      = result[0].O_idObjective
        # Inicio de la prueba.
        transverse = oObj.verifyObjectiveTransverse(idObj)
        self.assertTrue(transverse)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
    # Caso Frontera
           
    # Prueba 62 
    def testVerifyIdObjectiveTransverse(self):
        # Insertamos los datos necesarios.
        oBacklog   = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Dxfxcxl dy zlvxdpr',1)
        findId     = oBacklog.findName('Xstryctyrzs')
        idBacklog  = findId[0].BL_idBacklog 
        oObj       = objective()
        oObj.insertObjective('Szbxr xndxcy',idBacklog,True,False) 
        result     = oObj.searchObjective('Szbxr xndxcy',idBacklog)
        idObj      = result[0].O_idObjective
        # Inicio de la prueba.
        transverse = oObj.verifyObjectiveTransverse(idObj)
        self.assertTrue(transverse)
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Szbxr xndxcy',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
              
    # Casos Maliciosos
      
    # Prueba 63
    def testVerifyIdStringObjectiveTransverse(self):
        # Insertamos los datos necesarios.
        oBacklog   = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxnjzntxs',1)
        findId     = oBacklog.findName('Xstryctyrzs')
        idBacklog  = findId[0].BL_idBacklog 
        oObj       = objective()
        oObj.insertObjective('Xsygzrxr trsmxstrx',idBacklog,False,False)
        # Inicio de la prueba.
        transverse = oObj.verifyObjectiveTransverse('')
        self.assertFalse([],transverse) 
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Xsygzrxr trsmxstrx',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')       
 
    # Prueba 64
    def testVerifyIdNoneStringObjectiveTransverse(self):
        # Insertamos los datos necesarios.
        oBacklog   = backlog()
        oBacklog.insertBacklog('Xstryctyrzs','Cxnxcymyzntx',1)
        findId     = oBacklog.findName('Xstryctyrzs')
        idBacklog  = findId[0].BL_idBacklog 
        # Inicio de la prueba.        
        oObj       = objective()
        oObj.insertObjective('Dvsxrryllzr conjzntys',idBacklog,False,False)
        transverse = oObj.searchIdObjective(None)
        self.assertEqual([],transverse)    
        # Eliminamos los datos insertados.
        oObj.deleteObjective('Dvsxrryllzr conjzntys',idBacklog)
        oBacklog.deleteProduct('Xstryctyrzs')
 
# Fin de casos Objective