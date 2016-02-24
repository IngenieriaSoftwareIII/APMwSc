# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *

# Declaracion de constantes.
MIN_ID                 = 1
MIN_SPRINT_DESCRIPTION = 1
MAX_SPRINT_DESCRIPTION = 140


class sprints(object):
	'''Clase que permite manejar los sprints de manera persistente'''

	def insertSprint(self, sprintNumber, sprintDescription, idBacklog):

		'''Permite insertar una Sprint asociado a un producto'''   
		
		checkTypeDescription = type(sprintDescription) == str
		checkTypeId          = type(idBacklog) == int
		checkTypeNumber      = type(sprintNumber) == int

		if checkTypeDescription and checkTypeId and checkTypeNumber:
			checkLongSprintDescription = MIN_SPRINT_DESCRIPTION <= len(sprintDescription) <= MAX_SPRINT_DESCRIPTION
			checkLongId                = MIN_ID <= idBacklog
		
			if checkLongSprintDescription and checkLongId:
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
		
		checkTypeId    = type(idSprint) == int
		checkTypeNewSprintNumber = type(newSprintNumber) == int
		checkTypeNewdescription = type(newDescription) == str
		
		if checkTypeId and checkTypeNewdescription and checkTypeNewSprintNumber:
			checkLongNewDescription    = MIN_SPRINT_DESCRIPTION <= len(newDescription) <= MAX_SPRINT_DESCRIPTION
			foundSprint = self.searchIdSprint(idSprint, idBacklog)
			if foundSprint != [] and checkLongNewDescription:
				for num in clsSprint.query.filter_by(S_idBacklog = idBacklog).all():
					if num.S_numero  == newSprintNumber:
						return False
				foundSprint[0].S_sprintDescription = newDescription
				foundSprint[0].S_numero = newSprintNumber
				foundSprint[0].S_idSprint = idSprint
				db.session.commit()
				return True
		return False

	def searchIdSprint(self, sprintNumber, backlog):
		'''Permite buscar sprints por su id'''
		
		checkTypeIdSprint = type(sprintNumber) == int
		checkTypeBacklog = type(backlog) == int
		foundSprint       = []

		if checkTypeIdSprint and checkTypeBacklog:
			foundSprint = clsSprint.query.filter_by(S_numero  = sprintNumber).filter_by(S_idBacklog = backlog).all()
		return foundSprint





# Fin Clase Sprint