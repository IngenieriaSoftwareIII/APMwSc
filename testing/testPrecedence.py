# -*- coding: utf-8 -*-. 
 
import sys
import unittest

#Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog				import *
from actorsUserHistory		import *
from userHistory			import *
from accions				import *   
from model				  	import *  
from task				   	import *
from category				import *
from precedence				import *

class TestPrecedence (unittest.TestCase):

	#########################
	#   INSERT PRECEDENCE   #
	#########################

	#Prueba 1: insercion correcta de precedencia
	def testInsertCorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 2: Segunda tarea no valida
	def testInsertPrimeraTareaNoValida(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.insertPrecedence(idprimera,None,idFound0)), None)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aTarea.deleteTask('dwidjw')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	# Prueba 3: Primera tarea no valida
	def testInsertSegundaTareaNoValida(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.insertPrecedence(None,idsegunda,idFound0)), None)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	# Prueba 4: No permitir prelarse a si mismo
	def testAntecedenteIgualConsecuente(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.insertPrecedence(idprimera,idprimera,idFound0)), None)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aTarea.deleteTask('dwidjw')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	# Prueba 5: Ciclo
	def testCiclo(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask
		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera, idsegunda, idFound0)
		self.assertEqual ((aPrecedence.insertPrecedence(idsegunda,idprimera,idFound0)), None)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	# Prueba 6: Ciclo indirecto
	def testCicloIndirecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		# Insertamos la tarea 3
		cTarea = task()
		cTarea.insertTask('dfghj2',3,3,idFound1)
		searchTask3 = cTarea.searchTask('dfghj2')
		idtercera = searchTask3[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera, idsegunda, idFound0)
		aPrecedence.insertPrecedence(idsegunda, idtercera, idFound0)
		self.assertEqual ((aPrecedence.insertPrecedence(idtercera,idprimera,idFound0)), None)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aPrecedence.deletePrecedence(idsegunda,idtercera)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		bTarea.deleteTask('dfghj2')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 7: Repeticion de precedencias
	def testPrecedenciaRepetida(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)), None)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 8: Eliminacion de precedencias en tope de lista de precedencias (Caso borde, lista de un elemento)
	def testDeleteCorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		self.assertEqual ((aPrecedence.deletePrecedence(idprimera,idsegunda)), True)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 9: Eliminacion de precedencia no existente
	def testDeleteIncorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.deletePrecedence(idprimera,idsegunda)), None)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 10: Verificar existencia de precedencias
	def testExistsCorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.existPrecedence(idprimera,idsegunda)), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 11: Verificar existencia de precedencia que no existe
	def testExistsIncorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.existPrecedence(idprimera,idsegunda)), False)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 12: Buscar precedencias del antecedente = 1 (Caso borde)
	def testSearchAntecedenteCorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.searchTaskByPrec(idprimera) != []), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 13: Buscar precedencias del antecedente es []
	def testSearchAntecedenteVacio(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.searchTaskByPrec(idprimera) == []), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 14: Buscar precedencias del antecedente > 1 
	def testSearchAntecedenteMuchosCorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		# Insertamos la tarea 3
		cTarea = task()
		cTarea.insertTask('dfghj2',3,3,idFound1)
		searchTask3 = cTarea.searchTask('dfghj2')
		idtercera = searchTask3[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idprimera,idtercera,idFound0)
		self.assertEqual ((aPrecedence.searchTaskByPrec(idprimera) != []), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aPrecedence.deletePrecedence(idprimera,idtercera)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		bTarea.deleteTask('dfghj2')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 15: Buscar precedencias del consecuente es []
	def testSearchConsecuenteVacio(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		self.assertEqual ((aPrecedence.searchTaskByCons(idsegunda) == []), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 12: Buscar precedencias del consecuente = 1 (Caso borde)
	def testSearchConsecuenteCorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.searchTaskByCons(idsegunda) != []), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 17: Buscar precedencias del consecuente > 1 
	def testSearchConsecuenteMuchosCorrecto(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		# Insertamos la tarea 3
		cTarea = task()
		cTarea.insertTask('dfghj2',3,3,idFound1)
		searchTask3 = cTarea.searchTask('dfghj2')
		idtercera = searchTask3[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idtercera,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.searchTaskByCons(idsegunda) != []), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aPrecedence.deletePrecedence(idtercera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		bTarea.deleteTask('dfghj2')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')

	#Prueba 18: Eliminar precedencia que no esta en tope de lista de precedencias
	def testEliminarCentroPrecedencia(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		# Insertamos la tarea 3
		cTarea = task()
		cTarea.insertTask('dfghj2',3,3,idFound1)
		searchTask3 = cTarea.searchTask('dfghj2')
		idtercera = searchTask3[0].HW_idTask

		# Insertamos la tarea 4
		cTarea = task()
		cTarea.insertTask('dfghj3',4,4,idFound1)
		searchTask4 = cTarea.searchTask('dfghj3')
		idcuarta = searchTask4[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idtercera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idcuarta,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.deletePrecedence(idtercera,idsegunda)), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aPrecedence.deletePrecedence(idcuarta,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		bTarea.deleteTask('dfghj2')
		bTarea.deleteTask('dfghj3')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')
	
	#Prueba 19: Eliminar precedencia que esta en fondo de lista de precedencias
	def testEliminarUltima(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		# Insertamos la tarea 3
		cTarea = task()
		cTarea.insertTask('dfghj2',3,3,idFound1)
		searchTask3 = cTarea.searchTask('dfghj2')
		idtercera = searchTask3[0].HW_idTask

		# Insertamos la tarea 4
		cTarea = task()
		cTarea.insertTask('dfghj3',4,4,idFound1)
		searchTask4 = cTarea.searchTask('dfghj3')
		idcuarta = searchTask4[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idtercera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idcuarta,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.deletePrecedence(idprimera,idsegunda)), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idtercera,idsegunda)
		aPrecedence.deletePrecedence(idcuarta,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		bTarea.deleteTask('dfghj2')
		bTarea.deleteTask('dfghj3')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')
	
	#Prueba 20: Eliminar precedencia que esta en final de lista de precedencias
	def testEliminarPrimera(self):
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
		aHist.insertUserHistory('BIEEIEB1',0, 1,idFound, idFound0,1)
		searchHist = aHist.searchUserHistory('BIEEIEB1',idFound0)
		idFound1 = searchHist[0].UH_idUserHistory 
		 
		# Insertamos la categoria
		aCategory = category()
		aCategory.insertCategory('wofhweoifh',1)
		 
		# Insertamos la tarea 1  
		aTarea = task()
		aTarea.insertTask('dwidjw',1,1,idFound1)
		searchTask1 = aTarea.searchTask('dwidjw')
		idprimera = searchTask1[0].HW_idTask

		# Insertamos la tarea 2
		bTarea = task()
		bTarea.insertTask('dfghj',2,2,idFound1)
		searchTask2 = bTarea.searchTask('dfghj')
		idsegunda = searchTask2[0].HW_idTask

		# Insertamos la tarea 3
		cTarea = task()
		cTarea.insertTask('dfghj2',3,3,idFound1)
		searchTask3 = cTarea.searchTask('dfghj2')
		idtercera = searchTask3[0].HW_idTask

		# Insertamos la tarea 4
		cTarea = task()
		cTarea.insertTask('dfghj3',4,4,idFound1)
		searchTask4 = cTarea.searchTask('dfghj3')
		idcuarta = searchTask4[0].HW_idTask

		#Insertamos la precedencia
		aPrecedence = precedence()
		aPrecedence.insertPrecedence(idprimera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idtercera,idsegunda,idFound0)
		aPrecedence.insertPrecedence(idcuarta,idsegunda,idFound0)
		self.assertEqual ((aPrecedence.deletePrecedence(idcuarta,idsegunda)), True)

		# Eliminamos la precedencia, tarea, categoria, historia, accion y producto
		aPrecedence.deletePrecedence(idprimera,idsegunda)
		aPrecedence.deletePrecedence(idtercera,idsegunda)
		aTarea.deleteTask('dwidjw')
		bTarea.deleteTask('dfghj')
		bTarea.deleteTask('dfghj2')
		bTarea.deleteTask('dfghj3')
		aCategory.deleteCategory('wofhweoifh')
		aHist.deleteUserHistory(idFound1)
		aAcc.deleteAccion('cinrohbwidia', idFound0)
		aBacklog.deleteProduct('Podn fjdd.')
	

if __name__ == '__main__':
    unittest.main()