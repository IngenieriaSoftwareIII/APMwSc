# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *
from userHistory import *
from task        import *
from acceptanceCriteria import *

# Declaracion de constantes.
MIN_ID                 = 1
MIN_SPRINT_DESCRIPTION = 1
MAX_SPRINT_DESCRIPTION = 140
MIN_SPRINT_NUMBER = 1
MAX_SPRINT_NUMBER = 1000


class sprints(object):
	'''Clase que permite manejar los sprints de manera persistente'''

	def insertSprint(self, sprintNumber, sprintDescription, idBacklog): 
		'''Permite insertar una Sprint asociado a un producto'''   
		checkTypeDescription = type(sprintDescription) == str
		checkTypeId          = type(idBacklog) == int
		checkTypeNumber      = type(sprintNumber) == int

		if checkTypeDescription and checkTypeId and checkTypeNumber:
			checkSprintNumber          = MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
			checkLongSprintDescription = MIN_SPRINT_DESCRIPTION <= len(sprintDescription) <= MAX_SPRINT_DESCRIPTION
			checkLongId                = MIN_ID <= idBacklog

			if checkSprintNumber and checkLongSprintDescription and checkLongId:
				foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()                      
				
				if foundBacklog != []:
					foundSprints = clsSprint.query.filter_by(S_idBacklog = idBacklog).all()

					for num in foundSprints:
						if num.S_numero  == sprintNumber:
							return False
						 
					# Si S_numero no se repite
					newSprint = clsSprint(sprintNumber, sprintDescription, idBacklog)

					db.session.add(newSprint)
					db.session.commit()
					return True
		return False



	def updateSprint(self, idSprint, idBacklog, newSprintNumber,newDescription):
		'''Permite actualizar la descripcion de una sprint'''   
		checkTypeId              = type(idSprint) == int
		checkTypeNewSprintNumber = type(newSprintNumber) == int
		checkTypeNewdescription  = type(newDescription) == str
		
		if checkTypeId and checkTypeNewdescription and checkTypeNewSprintNumber:
			checkLongNewDescription = MIN_SPRINT_DESCRIPTION <= len(newDescription) <= MAX_SPRINT_DESCRIPTION
			foundSprint             = self.searchIdSprint(idSprint, idBacklog)
			if foundSprint != [] and checkLongNewDescription:
				if foundSprint[0].S_numero != newSprintNumber:
					for num in clsSprint.query.filter_by(S_idBacklog = idBacklog).all():
						if num.S_numero  == newSprintNumber:
							return False
				foundSprint[0].S_sprintDescription = newDescription
				foundSprint[0].S_numero = newSprintNumber
				db.session.commit()
				return True
		return False

	def searchIdSprint(self, sprintNumber, backlog):
		'''Permite buscar sprints por su id'''
		checkTypeIdSprint = type(sprintNumber) == int
		checkTypeBacklog  = type(backlog) == int
		foundSprint       = []

		if checkTypeIdSprint and checkTypeBacklog:
			foundSprint = clsSprint.query.filter_by(S_numero=sprintNumber,S_idBacklog =backlog).all()
		return foundSprint

	def deleteSprint(self,sprintNumber,idBacklog):
		'''Permite eliminar un Sprint segun su numero en el backlog'''
		checkTypeSprintNumber = type(sprintNumber) == int
		checkTypeidBacklog    = type(idBacklog) == int

		if checkTypeSprintNumber and checkTypeidBacklog:
			checkLenSprintNumber = MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
			checkLongIdBacklog   = MIN_ID <= idBacklog

			if checkLenSprintNumber and checkLongIdBacklog:
				foundSprint = clsSprint.query.filter_by(S_numero=sprintNumber,S_idBacklog=idBacklog).all()
				if foundSprint != []:
					for i in foundSprint:
						db.session.delete(i)
					db.session.commit()
					return True
		return False

	def asignSprintHistory(self, sprintNumber, idBacklog, idUserHistory):
		''' Permite asignar a un Sprint una historia de usuario asociado al producto '''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		checkidUserHistory = type(idUserHistory) == int and MIN_ID <= idUserHistory
		if checkSprintNumber and checkidBacklog and checkidUserHistory:
			oUserHistory = userHistory()
			history = oUserHistory.searchIdUserHistory(idUserHistory)
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			if history != [] and sprint != []:
				history[0].UH_idSprint = sprint[0].S_idSprint
				db.session.commit()
				return True
		return False

	def getAssignedSprintHistory(self, sprintNumber, idBacklog):
		'''Permite obtener las historias asociados a un determinado Sprint'''

		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog

		if checkSprintNumber and checkidBacklog:
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			found = clsUserHistory.query.filter_by(UH_idSprint = sprint[0].S_idSprint).all()
			return found
		return []

	def deleteAssignedSprintHistory(self, sprintNumber, idBacklog, idUserHistory):
		''' Permite eliminar la asignacion de una historia asociado a un Sprint dado su id'''

		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		checkidUserHistory = type(idUserHistory) == int and MIN_ID <= idUserHistory
		
		if checkSprintNumber and checkidBacklog and checkidUserHistory:
			oUserHistory = userHistory()
			history = oUserHistory.searchIdUserHistory(idUserHistory)
			if history != []:
				history[0].UH_idSprint = None
				history[0].UH_resume = None
				db.session.commit()
				return True
		return False

	def asignSprintTask(self, sprintNumber, idBacklog, idTask):
		''' Permite asignar a un Sprint una tarea asociado a sus historias'''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		checkidTask = type(idTask) == int and MIN_ID <= idTask
		if checkSprintNumber and checkidBacklog and checkidTask:
			oTask = task()
			tarea = oTask.getTaskById(idTask)
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			if tarea and sprint:
				tarea.HW_idSprint = sprint[0].S_idSprint
				db.session.commit()
				return True
		return False

	def getAssignedSprintTask(self, sprintNumber, idBacklog):
		'''Permite obtener las Tareas asociados a un determinado Sprint'''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		if checkSprintNumber and checkidBacklog:
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			found = clsTask.query.filter_by(HW_idSprint = sprint[0].S_idSprint).all()
			return found
		return []

		#Nuevo metodo Sprint 2
	def deleteAssignedSprintTask(self, sprintNumber, idBacklog, idTask):
		''' Permite la asignacion de una historia asociado a un Sprint dado su id'''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		checkidTask = type(idTask) == int and MIN_ID <= idTask
		if checkSprintNumber and checkidBacklog and checkidTask:
			oTask = task()
			tarea = oTask.getTaskById(idTask)
			if tarea:
				tarea.HW_idSprint = None
				db.session.commit()
				return True
		return False

	def assignSprintAcceptanceCriteria(self, sprintNumber, idBacklog, idAC):
		''' Permite asignar a un Sprint una criterio de aceptación asociado a sus historias'''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		checkidAC = type(idAC) == int and MIN_ID <= idAC
		if checkSprintNumber and checkidBacklog and checkidAC:
			oAcceptanceCriteria = acceptanceCriteria()
			criterio = oAcceptanceCriteria.getACById(idAC)
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			if criterio and sprint:
				criterio.HAC_idSprint = sprint[0].S_idSprint
				db.session.commit()
				return True
		return False

	def getAssignedSprintAC(self, sprintNumber, idBacklog):
		'''Permite obtener los criterios de aceptación asociados a un determinado Sprint'''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		if checkSprintNumber and checkidBacklog:
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			found = clsAcceptanceCriteria.query.filter_by(HAC_idSprint = sprint[0].S_idSprint).all()
			return found
		return []

# Fin Clase Sprint