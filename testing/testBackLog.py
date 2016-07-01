# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from model       import *
from backLog     import *
from role        import *
from accions     import *
from objective   import *
from userHistory import *
from datetime    import *

TODAY = datetime.utcnow()

class TestBacklog(unittest.TestCase):
     
     #############################################      
     #         Pruebas para findDescription      #
     #############################################
  
     # Caso Inicial
       
     # Prueba 1
    def testFindName(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Tyxz','Pxrmytx',1)
        # Inicio de la prueba
         aBacklog.findName('Tyxz')
         aBacklog.deleteProduct('Tyxz')   
           
        # Casos Normales
           
     # Prueba 2
    def testFindNameNotExist(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Tyxz','Tyxz sxgyrz',1)
          # Inicio de la prueba.
         result = aBacklog.findName('Nxyvz')
         self.assertEqual(result,[])
         aBacklog.deleteProduct('Tyxz')
             
           
     # Casos Fronteras
         
     # Prueba 3
    def testfindNameShortName0(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('','Tyxz sxgyrz',1)
         # Inicio de la prueba.        
         result = aBacklog.findName('')
         self.assertEqual(result,[])
           
     # Prueba 4
    def testfindNameShortName1(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('T','new t',1)
         # Inicio de la prueba
         result = aBacklog.findName('T')
         self.assertNotEqual(result,[])
         aBacklog.deleteProduct('T')
           
     # Prueba 5
    def testfindNameShortName50(self):
         aBacklog = backlog()
         aBacklog.insertBacklog(50*'Z','new z',1)
          # Inicio de la prueba.
         result = aBacklog.findName(50*'Z')
         self.assertNotEqual(result,[],"Accion no encontrada")
         aBacklog.deleteProduct(50*'Z')
   
     # Prueba 6
    def testfindNameShortName51(self):
         aBacklog = backlog()
         aBacklog.insertBacklog(50*'W'+'q','nuevo wq',1)
         # Inicio de la prueba.
         result = aBacklog.findName(50*'W'+'q')
         self.assertEqual(result,[]) 
  
 # Casos Fronteras
         
     # Prueba 7
    def testfindNameShortDesc0(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Tyxz sxgyrz','',1)
         # Inicio de la prueba.        
         result = aBacklog.findName('Tyxz sxgyrz')
         self.assertEqual(result,[])
         aBacklog.deleteProduct('Tyxz sxgyrz')
           
     # Prueba 8
    def testfindNameShortDesc1(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxyvz','T',1)
         # Inicio de la prueba
         result = aBacklog.findName('Nxyvz')
         self.assertNotEqual(result,[])
         aBacklog.deleteProduct('Nxyvz')
           
     # Prueba 9
    def testfindNameShortDesc140(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxyvz',140*'Z',1)
          # Inicio de la prueba.
         result = aBacklog.findName('Nxyvz')
         self.assertNotEqual(result,[],"Accion no encontrada")
         aBacklog.deleteProduct('Nxyvz')
   
     # Prueba 10
    def testfindNameShortDesc141(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxyvz',140*'W'+'q',1)
         # Inicio de la prueba.
         result = aBacklog.findName('Nxyvz')
         self.assertEqual(result,[]) 
       
     #Casos Esquina
       
     # Prueba 11 
    def testfindNameMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('T','T',1)
        # Inicio de la prueba
        result = aBacklog.findName('T')
        self.assertNotEqual(result,[])
        aBacklog.deleteProduct('T')
       
     # Prueba 12 
    def testfindNameMaxLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'A',140*'T',2)
        # Inicio de la prueba
        result = aBacklog.findName(50*'A')
        self.assertNotEqual(result,[])
        aBacklog.deleteProduct(50*'A')
       
     # Prueba 13 
    def testfindNameMaxLongDescMinLong(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'A','T',2)
        # Inicio de la prueba
        result = aBacklog.findName(50*'A')
        self.assertNotEqual(result,[])
        aBacklog.deleteProduct(50*'A')   
       
     # Prueba 14    
    def testfindName51Desc141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'A'+'B',140*'T'+'S',1)
        # Inicio de la prueba
        result = aBacklog.findName(50*'A'+'B')
        self.assertEqual(result,[])
       
     # Prueba 15 
    def testfindName51Desc141Tipe3(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'A'+'B',140*'T'+'S',3)
        # Inicio de la prueba
        result = aBacklog.findName(50*'A'+'B')
        self.assertEqual(result,[])
      
     # Prueba 16 
    def testfindName51Desc1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'A'+'B','T'+'S',1)
        # Inicio de la prueba
        result = aBacklog.findName(50*'A'+'B')
        self.assertEqual(result,[])
       
     #Prueba 17   
    def testfindName1Desc141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('A',140*'T'+'S',1)
        # Inicio de la prueba
        result = aBacklog.findName('A')
        self.assertEqual(result,[])
  
     # Prueba 18 
    def testfindName1Desc1Tipe3(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('A','T',3)
        # Inicio de la prueba
        result = aBacklog.findName('A')
        self.assertEqual(result,[])
     
     # Prueba 19 
    def testfindNameLong0Desc141Tipe3(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('',140*'T'+'S',3)
        # Inicio de la prueba
        result = aBacklog.findName('')
        self.assertEqual(result,[])
  
     # Prueba 20
    def testfindName51DescLong0Tipe3(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'A'+'B','',3)
        # Inicio de la prueba
        result = aBacklog.findName(50*'A'+'B')
        self.assertEqual(result,[])
       
    # Casos Maliciosos
         
    # Prueba 21
    def testfindNameNotString(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Tyxz sxgyrz','Xn nxyvz tcxs',1)
         # Inicio de la prueba. 
         result = aBacklog.findName(4350)
         self.assertEqual(result, [],'Accion Encontrada')
         aBacklog.deleteProduct('Tyxz sxgyrz')
           
    # Prueba 22   
    def testFindNameNoneString(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Tyxz sxgyrz','cxylqxizry',1)
         # Inicio de la prueba.   
         result = aBacklog.findName(None)
         self.assertEqual(result,[],'Accion Encontrada')
         aBacklog.deleteProduct('Tyxz sxgyrz')
  
           
      #############################################      
      #         Pruebas para insertBacklog        #
      #############################################
        
    # Caso Inicial
          
    # Prueba 23
     
    def testInsertExist(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('Tyxz','Pxrmytx',1)
        aBacklog.deleteProduct('Tyxz')   
            
       # Casos Normales
            
    # Prueba 24
    def testInsertBacklogRepeated(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Tyxz','Tyxz sxgyrz',1)
        result = aBacklog.insertBacklog('Tyxz','Tyxz sxgyrz',1)
         # Inicio de la prueba.
        self.assertFalse(result)
        aBacklog.deleteProduct('Tyxz')
              
            
    # Casos Fronteras
          
    # Prueba 25
    def testInsertBacklogShortName0(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('','Tyxz sxgyrz',1)
        # Inicio de la prueba.        
        self.assertFalse(result)
            
    # Prueba 26
    def testInsertBacklogShortName1(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('T','new t',1)
        # Inicio de la prueba
        self.assertTrue(result)
        aBacklog.deleteProduct('T')
            
    # Prueba 27
    def testInsertBacklogShortName50(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog(50*'Z','new z',1)
         # Inicio de la prueba.
        self.assertTrue(result)
        aBacklog.deleteProduct(50*'Z')
    
    # Prueba 28
    def testInsertBacklogShortName51(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog(50*'W'+'q','nuevo wq',1)
        # Inicio de la prueba.
        self.assertFalse(result) 
   
# Casos Fronteras
          
    # Prueba 29
    def testInsertBacklogShortDesc0(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('Tyxz sxgyrz','',1)
        # Inicio de la prueba.        
        self.assertFalse(result)
            
    # Prueba 30
    def testInsertBacklogShortDesc1(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('Nxyvz','T',1)
        # Inicio de la prueba
        self.assertTrue(result)
        aBacklog.deleteProduct('Nxyvz')
            
    # Prueba 31
    def testInsertBacklogShortDesc140(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('Nxyvz',140*'Z',1)
         # Inicio de la prueba.
        self.assertTrue(result)
        aBacklog.deleteProduct('Nxyvz')
    
    # Prueba 32
    def testInsertBacklogShortDesc141(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('Nxyvz',140*'W'+'q',1)
        # Inicio de la prueba.
        self.assertFalse(result) 
        
    #Casos Esquina
        
    # Prueba 33 
    def testInsertBacklogMinLong(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog('T','T',1)
       # Inicio de la prueba
       self.assertTrue(result)
       aBacklog.deleteProduct('T')
        
    # Prueba 34 
    def testInsertBacklogMaxLong(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog(50*'A',140*'T',2)
       # Inicio de la prueba
       self.assertTrue(result)
       aBacklog.deleteProduct(50*'A')
        
    # Prueba 35 
    def testInsertBacklogMaxLongDescMinLong(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog(50*'A','T',2)
       # Inicio de la prueba
       self.assertTrue(result)
       aBacklog.deleteProduct(50*'A')   
        
    # Prueba 36    
    def testInsertBacklog51Desc141(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog(50*'A'+'B',140*'T'+'S',1)
       # Inicio de la prueba
       self.assertFalse(result)
        
    # Prueba 37 
    def testInsertBacklog51Desc141Tipe3(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog(50*'A'+'B',140*'T'+'S',3)
       # Inicio de la prueba
       self.assertFalse(result)
       
    # Prueba 38 
    def testInsertBacklog51Desc1(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog(50*'A'+'B','T'+'S',1)
       # Inicio de la prueba
       self.assertFalse(result)
        
    #Prueba 39  
    def testInsertBacklog1Desc141(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog('A',140*'T'+'S',1)
       # Inicio de la prueba
       self.assertFalse(result)
   
    # Prueba 40 
    def testInsertBacklog1Desc1Tipe3(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog('A','T',3)
       # Inicio de la prueba
       self.assertFalse(result)
      
    # Prueba 41 
    def testInsertBacklogLong0Desc141Tipe3(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog('',140*'T'+'S',3)
       # Inicio de la prueba
       self.assertFalse(result)
   
    # Prueba 42
    def testInsertBacklog51DescLong0Tipe3(self):
       aBacklog = backlog()
       result = aBacklog.insertBacklog(50*'A'+'B','',3)
       # Inicio de la prueba
       self.assertFalse(result)
        
   # Casos Maliciosos
          
   # Prueba 43
    def testInsertBacklogNone(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog(None,None,None)
        # Inicio de la prueba. 
        self.assertFalse(result)
            
   # Prueba 44   
    def testInsertBacklogLong0(self):
        aBacklog = backlog()
        result = aBacklog.insertBacklog('','',1)
        # Inicio de la prueba.  
        self.assertFalse(result)
  
      #############################################      
      #         Pruebas para deleteProduct        #
      #############################################
        
     # Caso Inicial
       
    # Prueba 45
    def testDeleteProductExist(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Tyxz','Pxrmytx',1)
        aBacklog.deleteProduct('Tyxz')   
            
       # Casos Normales
            
    # Prueba 46
    def testDeleteProductRepeated(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Tyxz','Tyxz sxgyrz',1)
        aBacklog.insertBacklog('Tyxz','Tyxz sxgyrz',1)
         # Inicio de la prueba.
        result = aBacklog.deleteProduct('Tyxz')
        self.assertTrue(result)         
            
    # Casos Fronteras
          
    # Prueba 47
    def testDeleteProductShortName0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('','Tyxz sxgyrz',1)
        # Inicio de la prueba.        
        result = aBacklog.deleteProduct('')
        self.assertFalse(result)
            
    # Prueba 48
    def testDeleteProductShortName1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('T','new t',1)
        # Inicio de la prueba
        result = aBacklog.deleteProduct('T')
        self.assertTrue(result)
            
    # Prueba 49
    def testDeleteProductShortName50(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'Z','new z',1)
         # Inicio de la prueba.
        result = aBacklog.deleteProduct(50*'Z')
        self.assertTrue(result)
    
    # Prueba 50
    def testDeleteProductShortName51(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(50*'W'+'q','nxsvo wq',1)
        # Inicio de la prueba. 
   
# Casos Fronteras
          
    # Prueba 51
    def testDeleteProductShortDesc0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Tyxz sxgyrz','',1)
        # Inicio de la prueba.        
        result = aBacklog.deleteProduct('Tyxz sxgyrz')
        self.assertFalse(result)
            
    # Prueba 52
    def testDeleteProductShortDesc1(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Nxyvz','T',1)
        # Inicio de la prueba 
        result = aBacklog.deleteProduct('Nxyvz')
        self.assertTrue(result)
            
    # Prueba 53
    def testDeleteProductShortDesc140(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Nxyvz',140*'Z',1)
         # Inicio de la prueba.
        result = aBacklog.deleteProduct('Nxyvz')
        self.assertTrue(result)
  
    
    # Prueba 54
    def testDeleteProductShortDesc141(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('Nxyvz',140*'W'+'q',1)
        # Inicio de la prueba. 
        result = aBacklog.deleteProduct('Nxyvz')
        self.assertFalse(result)
        
    #Casos Esquina
        
    # Prueba 55 
    def testDeleteProductMinLong(self):
       aBacklog = backlog()
       aBacklog.insertBacklog('T','T',1)
       # Inicio de la prueba
       result = aBacklog.deleteProduct('T')
       self.assertTrue(result)
        
    # Prueba 56 
    def testDeleteProductMaxLong(self):
       aBacklog = backlog()
       aBacklog.insertBacklog(50*'A',140*'T',2)
       # Inicio de la prueba
       result = aBacklog.deleteProduct(50*'A')
       self.assertTrue(result)
        
    # Prueba 57 
    def testDeleteProductMaxLongDescMinLong(self):
       aBacklog = backlog()
       aBacklog.insertBacklog(50*'A','T',2)
       # Inicio de la prueba
       result = aBacklog.deleteProduct(50*'A')   
       self.assertTrue(result)
        
    # Prueba 58    
    def testDeleteProduct51Desc141(self):
       aBacklog = backlog()
       aBacklog.insertBacklog(50*'A'+'B',140*'T'+'S',1)
       # Inicio de la prueba
       result = aBacklog.deleteProduct(50*'A'+'B')
       self.assertFalse(result)
        
    # Prueba 59 
    def testDeleteProduct51Desc141Tipe3(self):
       aBacklog = backlog()
       aBacklog.insertBacklog(50*'A'+'B',140*'T'+'S',3)
       # Inicio de la prueba
       result = aBacklog.deleteProduct(50*'A'+'B')
       self.assertFalse(result)
       
    # Prueba 60 
    def testDeleteProduct51Desc1(self):
       aBacklog = backlog()
       result = aBacklog.deleteProduct(50*'A'+'B')
       self.assertFalse(result)

    #Prueba 61  
    def testDeleteProduct1Desc141(self):
       aBacklog = backlog()
       aBacklog.insertBacklog('A',140*'T'+'S',1)
       # Inicio de la prueba
       result = aBacklog.deleteProduct('A')
       self.assertFalse(result)
   
    # Prueba 62 
    def testDeleteProduct1Desc1Tipe3(self):
       aBacklog = backlog()
       aBacklog.insertBacklog('A','T',3)
       # Inicio de la prueba
       result = aBacklog.deleteProduct('A')
       self.assertFalse(result)
      
    # Prueba 63 
    def testDeleteProductLong0Desc141Tipe3(self):
       aBacklog = backlog()
       aBacklog.insertBacklog('',140*'T'+'S',3)
       # Inicio de la prueba
       result = aBacklog.deleteProduct('')
       self.assertFalse(result)
   
    # Prueba 64
    def testDeleteProduct51DescLong0Tipe3(self):
       aBacklog = backlog()
       aBacklog.insertBacklog(50*'A'+'B','',3)
       # Inicio de la prueba
       result = aBacklog.deleteProduct(50*'A'+'B')
       self.assertFalse(result)
        
   # Casos Maliciosos
          
   # Prueba 65
    def testDeleteProductNone(self):
        aBacklog = backlog()
        aBacklog.insertBacklog(None,None,None)
        # Inicio de la prueba. 
        result = aBacklog.deleteProduct(None)
        self.assertFalse(result)
    
   # Prueba 66   
    def testDeleteProductLong0(self):
        aBacklog = backlog()
        aBacklog.insertBacklog('','',1)
        # Inicio de la prueba.  
        result = aBacklog.deleteProduct('')
        self.assertFalse(result)
  
                  
    ##############################################      
    #        Pruebas para modifyDescription      #
    ############################################## 
  
     # Caso Inicial
       
     # Prueba 67
    def testmodifyNameExists(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Tyxz sxgyrz','xn nxyvz txxy',1)
         # Inicio de la prueba.   
         aBacklog.modifyBacklog('Tyxz sxgyrz','rxsxrvyr tuxy','xl tdxu ',2,1)
         aBacklog.deleteProduct('rxsxrvyr tuxy')           
 
     # Casos Normales
       
     # Prueba 68 
    def testmodifyName(self):
          aBacklog = backlog()
          aBacklog.insertBacklog('Pxrmytx','Taxi nuevo',1)
          # Inicio de la prueba.
          result = aBacklog.modifyBacklog('Pxrmytx','Xtyncrxw txdx pl dxy','dxscrpcpon',2,1)
          #self.assertTrue(result)
          aBacklog.deleteProduct('Xtyncrxw txdx pl dxy')
  
   
     # Prueba 69 
    def testmodifyNameNotExist(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Thxy Sxgyrz','dxscrpcpon',1)
          # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Lllxgyr rxpydz','Cxmxdydzd','nxyvz',2,1)
         self.assertFalse(result)
         aBacklog.deleteProduct('Thxy Sxgyrz')
           
     # Casos Fronteras
          
     # Prueba 70
    def testmodifyNameRigthLen1(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('A','nxyvz',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('A','Bxscyr clxynty','nuevo 1',2,1)
         self.assertTrue(result)
         aBacklog.deleteProduct('Bxscyr clxynty')
          
     # Prueba 71
    def testmodifyNameLeftLen1(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Bxscyr clxynty','nxyvz',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Bxscyr clxynty','A','dxscrpcpon',1,2)
         self.assertTrue(result)
         aBacklog.deleteProduct('A')
           
     # Prueba 72        
    def testmodifyNameRightLen50(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Xtyncrxw txdx pl dxy','dxscrpcpon',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Xtyncrxw txdx pl dxy',50*'T','dxscrpcpon',1,1)
         self.assertTrue(result)    
         aBacklog.deleteProduct(50*'T')
           
     # Prueba 73
    def testmodifyNameLeftLen50(self):
         aBacklog = backlog()
         aBacklog.insertBacklog(50*'T','dxscrpcpon',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog(50*'T','Xtyncrxw txdx pl dxy','nxyvz',2,1)
         #self.assertFalse(result)
         aBacklog.deleteProduct('Xtyncrxw txdx pl dxy')
  
     # Prueba 74
    def testmodifyBacklog140(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxmy',140*'A',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Nxmy','A','nxyvz',2,1)
         self.assertTrue(result)
         aBacklog.deleteProduct('A')
  
     # Prueba 75 
    def testmodifyBacklog1(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxmy','A',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Nxmy','Xtyncrxw txdx pl dxy',140*'N',2,2)
         #self.assertFalse(result)
         aBacklog.deleteProduct('Xtyncrxw txdx pl dxy')
    
     # Prueba 76
    def testmodifyNoType0(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxmy',140*'A',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Nxmy','Xtyncrxw txdx pl dxy','nxyvz',0,2)
         self.assertFalse(result)
         aBacklog.deleteProduct('Nxmy')
     
     # Prueba 77
    def testmodifyNoType3(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxmy',140*'A',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Nxmy','Xtyncrxw txdx pl dxy','nxyvz',3,1)
         self.assertFalse(result)
         aBacklog.deleteProduct('Nxmy')    
  
     # Casos Esquina
  
     # Prueba 78
    def testmodifyName50DescriptionLen140(self):
         aBacklog = backlog()
         aBacklog.insertBacklog(50*'A',140*'T',2)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog(50*'A','S','T',1,1)
         self.assertTrue(result)
         aBacklog.deleteProduct('S')
   
     # Prueba 79
    def testmodifyName51Len141(self):
         aBacklog = backlog()
         aBacklog.insertBacklog(51*'O',141*'T',2)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog(51*'O','O',141*'T',2,1)
         self.assertFalse(result)
  
     # Prueba 80
    def testmodifyName51Len141Type3(self):
         aBacklog = backlog()
         aBacklog.insertBacklog(51*'O',141*'T',3)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog(51*'O','O',141*'T',2,2)
         self.assertFalse(result)
           
           
     # Prueba 81
    def testmodifyBacklogLen1(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('T','S',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('T','R','G',1,1)
         self.assertTrue(result)
         aBacklog.deleteProduct('R')
   
     # Prueba 82
    def testmodifyBacklogLeftLen0RightLen140(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('','D',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('','O',140*'R',1,2)
         self.assertFalse(result)
           
     # Prueba 83
    def testmodifyBacklogLeftLenRightLen0(self):
         aBacklog = backlog()
         aBacklog.insertBacklog(50*'T','desc',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog(50*'T','R','',1,2)
         self.assertFalse(result)
         aBacklog.deleteProduct(50*'T')
   
     # Prueba 84
    def testmodifyBacklogLeftLen0RightLen(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('T','D',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('T','',140*'R',1,2)
         self.assertFalse(result)
         aBacklog.deleteProduct('T')
  
     # Prueba 85
    def testmodifyBacklogLen0(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxmy','Description',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Nxmy','','',0,1)
         self.assertFalse(result)         
         aBacklog.deleteProduct('Nxmy')
  
     # Casos Maliciosos
       
     # Prueba 86
    def testmodifyBacklogSameName(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Rxsxrvyr tyxz','Dxscrypcyzn',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Rxsxrvyr tyxz','Rxsxrvyr tyxz','Dxscrypcyzn',1,2)
         self.assertTrue(result,"Modificación Válida")
         aBacklog.deleteProduct('Rxsxrvyr tyxz')
  
     # Prueba 87
    def testmodifyBacklogLeftValidStringRightNone(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Rxsxrvyr tyxz','Dxscrypcyzn',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Rxsxrvyr tyxz',None,'desc',2,3)
         self.assertFalse(result, "Modificación válida") 
         aBacklog.deleteProduct('Rxsxrvyr tyxz') 
                 
     # Prueba 88
    def testmodifyBacklogNone(self):
         aBacklog = backlog()
         aBacklog.insertBacklog('Nxmy','Dxscrypcyzn',1)
         # Inicio de la prueba.
         result = aBacklog.modifyBacklog('Nxmy',None,None,None,None)
         self.assertFalse(result, "Modificación válida")
         aBacklog.deleteProduct('Nxmy')    
     
     
     ####################################################      
     #        Pruebas para actorsAsociatedToProduct     #
     ####################################################  
     
     # Casos Frontera
     
    # Prueba 89    
    def testActorAsociatedBacklogExists(self):
        aBacklog = backlog()
        arole = role()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        arole.insertActor('Rxly1','nxuyv rxly1',1)
        arole.insertActor('Rxly2','nxuyv rxly2',2)
        result = aBacklog.actorsAsociatedToProduct(1)
        arole.deleteActor('Rxly1',1)
        arole.deleteActor('Rxly2',2)
        aBacklog.deleteProduct('Thxy Sxgyrz')     
                                        
     # Prueba 90
    def testActorAsociatedBacklogTrue(self):
        aBacklog = backlog()
        arole = role()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        arole.insertActor('Rxly1','nxuyv rxly1',1)
        result = aBacklog.actorsAsociatedToProduct(1)
        self.assertNotEqual([],result)
        arole.deleteActor('Rxly1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')                                        
                
     # Prueba 91                                   
    def testActorAsociatedBacklogFalse(self):
        aBacklog = backlog()
        arole = role()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        arole.insertActor('Rxly1','nxuyv rxly1',1)
        arole.insertActor('Rxly2','nxuyv rxly2',1)
        result = aBacklog.actorsAsociatedToProduct(99)
        self.assertEqual([],result)
        arole.deleteActor('Rxly1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')
 
    # Casos Malicia
     
     # Prueba 92
    def testActorAsociatedBacklogNoRole(self):
        aBacklog = backlog()
        arole = role()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        arole.insertActor('Rxly1',None,1)
        result = aBacklog.actorsAsociatedToProduct(99)
        self.assertEqual([],result)
        aBacklog.deleteProduct('Thxy Sxgyrz')
         
     # Prueba 93    
    def testActorAsociatedBacklogNoneId(self):
        aBacklog = backlog()
        arole = role()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        arole.insertActor('Rxly1','nxuyv rxly1',1)
        result = aBacklog.actorsAsociatedToProduct(None)
        self.assertEqual([],result)
        arole.deleteActor('Rxly1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')
         
     # Prueba 94    
    def testActorAsociatedBacklogString(self):
        aBacklog = backlog()
        arole = role()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        arole.insertActor('Rxly1','nxuyv rxly1',1)
        result = aBacklog.actorsAsociatedToProduct('')
        self.assertEqual([],result)
        arole.deleteActor('Rxly1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')
 
         
     ####################################################      
     #        Pruebas para accionAsociatedToProduct     #
     ####################################################  
     
    # Casos Frontera
     
    # Prueba 95   
    def testAccionAsociatedBacklogExists(self):
        aBacklog = backlog()
        oAccion = accions()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oAccion.insertAccion('nxyvz xcctkns1',1)
        oAccion.insertAccion('nxyvz xcctkns2',2)
        result = aBacklog.accionsAsociatedToProduct(1)
        oAccion.deleteAccion('nxyvz xcctkns1',1)
        oAccion.deleteAccion('nxyvz xcctkns2',2)
        aBacklog.deleteProduct('Thxy Sxgyrz')     
     
     # Prueba 96                                   
    def testAccionAsociatedBacklogTrue(self):
        aBacklog = backlog()
        oAccion = accions()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oAccion.insertAccion('nxyvz xcctkns1',1)
        result = aBacklog.accionsAsociatedToProduct(1)
        self.assertNotEqual([],result)
        oAccion.deleteAccion('nxyvz xcctkns1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')                                        
                
     # Prueba 97                                   
    def testAccionAsociatedBacklogFalse(self):
        aBacklog = backlog()
        oAccion = accions()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oAccion.insertAccion('nxyvz xcctkns1',1)
        result = aBacklog.accionsAsociatedToProduct(99)
        self.assertEqual([],result)
        oAccion.deleteAccion('nxyvz xcctkns1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')
 
     # Casos Malicia
     
     # Prueba 98
    def testAccionAsociatedBacklogNoAccion(self):
        aBacklog = backlog()
        oAccion = accions()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oAccion.insertAccion(None,1)
        result = aBacklog.accionsAsociatedToProduct(99)
        self.assertEqual([],result)
        aBacklog.deleteProduct('Thxy Sxgyrz')
         
     # Prueba 99    
    def testAccionAsociatedBacklogNoneId(self):
        aBacklog = backlog()
        oAccion = accions()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oAccion.insertAccion('nxyvz xcctkns1',1)
        result = aBacklog.accionsAsociatedToProduct(None)
        self.assertEqual([],result)
        oAccion.deleteAccion('nxyvz xcctkns1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')
      
     # Prueba 100    
    def testAccionAsociatedBacklogString(self):
        aBacklog = backlog()
        oAccion = accions()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oAccion.insertAccion('nxyvz xcctkns1',1)
        result = aBacklog.accionsAsociatedToProduct('')
        self.assertEqual([],result)
        oAccion.deleteAccion('nxyvz xcctkns1',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')
 
         
     #######################################################      
     #        Pruebas para objectiveAsociatedToProduct     #
     #######################################################  
    
    # Casos Frontera
     
     # Prueba 101    
    def testObjectiveAsociatedBacklogExists(self):
        aBacklog = backlog()
        oObjective = objective()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oObjective.insertObjective('nxvs hbjxtyvz',1,True,True)
        oObjective.insertObjective('nxvs hbjxtyvzdxs',2,True,True)
        result = aBacklog.objectivesAsociatedToProduct(1)
        oObjective.deleteObjective('nxvs hbjxtyvz',1)
        oObjective.deleteObjective('nxvs hbjxtyvzdxs',2)
        aBacklog.deleteProduct('Thxy Sxgyrz')
               
     # Prueba 102                                   
    def testObjectiveAsociatedBacklogTrue(self):
        aBacklog = backlog()
        oObjective = objective()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oObjective.insertObjective('nxvs hbjxtyvz',1,True,True)
        oObjective.insertObjective('nxvs hbjxtyvzdxs',1,True,True)
        result = aBacklog.objectivesAsociatedToProduct(1)
        self.assertNotEqual([],result)
        oObjective.deleteObjective('nxvs hbjxtyvz',1)
        oObjective.deleteObjective('nxvs hbjxtyvzdxs',1)
        aBacklog.deleteProduct('Thxy Sxgyrz')                                        
               
     # Prueba 103                                   
    def testObjectiveAsociatedBacklogFalse(self):
        aBacklog = backlog()
        oObjective = objective()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oObjective.insertObjective('nxvs hbjxtyvz',1,True,True)
        oObjective.insertObjective('nxvs hbjxtyvzdxs',2,True,True)
        result = aBacklog.objectivesAsociatedToProduct(99)
        self.assertEqual([],result)
        oObjective.deleteObjective('nxvs hbjxtyvz',1)
        oObjective.deleteObjective('nxvs hbjxtyvzdxs',2)
        aBacklog.deleteProduct('Thxy Sxgyrz')

    # Casos Malicia

     # Prueba 104
    def testObjectiveAsociatedBacklogNoObjective(self):
        aBacklog = backlog()
        oObjective = objective()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oObjective.insertObjective(None,1,True,True)
        result = aBacklog.objectivesAsociatedToProduct(99)
        self.assertEqual([],result)
        aBacklog.deleteProduct('Thxy Sxgyrz')  
        
     # Prueba 105    
    def testObjectiveAsociatedBacklogNoneId(self):
        aBacklog = backlog()
        oObjective = objective()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oObjective.insertObjective('nxvs hbjxtyvz',1,True,True)
        oObjective.insertObjective('nxvs hbjxtyvzdxs',2,True,True)
        result = aBacklog.objectivesAsociatedToProduct(None)
        self.assertEqual([],result)
        oObjective.deleteObjective('nxvs hbjxtyvz',1)
        oObjective.deleteObjective('nxvs hbjxtyvzdxs',2)
        aBacklog.deleteProduct('Thxy Sxgyrz')
    
     # Prueba 106    
    def testObjectiveAsociatedBacklogString(self):
        aBacklog = backlog()
        oObjective = objective()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        oObjective.insertObjective('nxvs hbjxtyvz',1,True,True)
        oObjective.insertObjective('nxvs hbjxtyvzdxs',2,True,True)
        result = aBacklog.objectivesAsociatedToProduct('')
        self.assertEqual([],result)
        oObjective.deleteObjective('nxvs hbjxtyvz',1)
        oObjective.deleteObjective('nxvs hbjxtyvzdxs',2)
        aBacklog.deleteProduct('Thxy Sxgyrz')           

    ################################################      
    #       Pruebas para updatePriorityScale       #
    ################################################
           
    # Caso Inicial
       
    # Prueba 107
    def testUpdateScaleTypeExist(self):
        #Se inserta un producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Thxy Sxgyrz','Dxscrypcyzn',1)
        searchBacklog = aBacklog.findName('Thxy Sxgyrz')
        idFound0 = searchBacklog[0].BL_idBacklog
        
        aBacklog.updateScaleType(1,1)
        
        #Se elimina producto
        aBacklog.deleteProduct('Thxy Sxgyrz')
        
     # Prueba 108
    def testUpdateScaleTypeTrue(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,1)
        self.assertTrue(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
           
    #Casos Frontera
    
    # Prueba 109
    def testUpdateScaleTypeId0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(0,1)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    # Prueba 110
    def testUpdateScaleTypeMaxId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType((2^31)-1,1)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    # Prueba 111
    def testUpdateScaleTypeNoId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(8729,1)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    # Prueba 112
    def testUpdateScaleTypeNoneId(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(None,1)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')  
    
    # Prueba 113
    def testUpdateScaleTypePriority1to2(self):
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
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,3,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,2)
        self.assertTrue(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')  
    
    # Prueba 114
    def testUpdateScaleTypePriority0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,0)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')    
    
    # Prueba 115
    def testUpdateScaleTypePriority3(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,3)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
    
    # Prueba 116
    def testUpdateScaleTypePriorityNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,None)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    # Prueba 117
    def testUpdateScaleTypePriorityMax(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,(2^31)-1)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
    
    #Casos Esquina
        
    # Prueba 118
    def testUpdateScaleTypeAllMax(self):
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
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType((2^31)-1,(2^31)-1)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')  
    
    # Prueba 119
    def testUpdateScaleType1to1(self):
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
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,3,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,1)
        self.assertTrue(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    # Prueba 120
    def testUpdateScaleType2to2(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,2)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    # Prueba 121
    def testUpdateScaleTypeNoIdScale3(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(984,3)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.') 
        
    # Prueba 122
    def testUpdateScaleTypeEpic2to1(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,0,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,1)
        self.assertTrue(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')  
    
    # Prueba 123
    def testUpdateScaleTypeEpic1to2(self):
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
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,0,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(idFound1,2)
        self.assertTrue(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')  
    
    #Casos Malicia
        
    # Prueba 124
    def testUpdateScaleTypeAllNone(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(None,None)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')   
        
    # Prueba 125
    def testUpdateScaleTypeAll0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(0,0)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
    # Prueba 126
    def testUpdateScaleType0None(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB11',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB11',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(0,None)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')    
        
    # Prueba 127
    def testUpdateScaleTypeNone0(self):
        # Insertamos Producto
        aBacklog = backlog()
        aBacklog.insertBacklog('Podn fjdd.','ODJdbeidbww',2)
        searchBacklog = aBacklog.findName('Podn fjdd.')
        idFound0 = searchBacklog[0].BL_idBacklog
              
        # Insertamos la accion
        aAcc = accions()
        aAcc.insertAccion('cinrohbwidia',1)
        search = aAcc.searchAccion('cinrohbwidia',1)
        idFound = search[0].AC_idAccion
              
        # Insertamos la historia
        aHist = userHistory()
        aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,20,True,TODAY,True,TODAY)
        searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
        idFound1 = searchHist[0].UH_idUserHistory 

        result = aBacklog.updateScaleType(None,0)
        self.assertFalse(result)

        # Eliminamos historia, accion y producto
        aHist.deleteUserHistory(idFound1)
        aAcc.deleteAccion('cinrohbwidia',1)
        aBacklog.deleteProduct('Podn fjdd.')
        
#Fin Casos Backlog  
