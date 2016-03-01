# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from sprintClass import *

# Declaracion de constantes.
MIN_ID_SPRINT= 1

MIN_MEETING_ACTIVITIES = 1
MAX_MEETING_ACTIVITIES = 300

MIN_MEETING_SUGGESTIONS = 1
MAX_MEETING_SUGGESTIONS = 300

MIN_MEETING_CHALLENGES = 1
MAX_MEETING_CHALLENGES = 300

class meeting(object):
	'''Clase que permite manejar las Reuniones Diarias de un Sprin'''

	def emptyTable(self):
        '''Permite saber si la tabla meeting esta vacia'''
        aMeeting = clsSprintMeeting.query.all()
        return (aMeeting == [])

    def getMeetings(self,idSprint):
        '''Entrega la lista de reuniones diarias de un sprint'''
        aMeeting = clsSprintMeeting.query.filter_by(SM_idSprint = idSprint).all()
        return (aMeeting)

	def searchMeeting(self, date, idSprint):
		'''Retorna la lista de reuniones con un fecha y sprint determinado'''
		#checkTypeDate = type(date) == DateTime
		checkTypeIdSprint = type(idSprint) == int
		foundMeeting       = []

		if checkTypeIdSprint:
			foundMeeting = clsSprintMeeting.query.filter_by(SM_meetingDate = date, SM_idSprint = idSprint).all()
		return foundMeeting

	def insertMeeting(self, date, activities, suggestions, challenges, idSprint): 
		'''Permite insertar una reunión diaria a un sprint'''   
		#checkTypeDate 			= type(date) == DateTime
		checkTypeActivities     = type(activities) == str
		checkTypeSuggestions    = type(suggestions) == str
		checkTypeChallenges     = type(challenges) == str
		checkTypeIdSprint      	= type(idSprint) == int

		# Verifica que la longitud de los campos sea correcta
		if checkTypeActivities and checkTypeSuggestions and checkTypeChallenges and checkTypeIdSprint:
			checkActivityLong = MIN_MEETING_ACTIVITIES <= len(activities) <= MAX_MEETING_ACTIVITIES
			checkSusggestionLong = MIN_MEETING_SUGGESTIONS <= len(suggestions) <= MAX_MEETING_SUGGESTIONS
			checkChallengeLong = MIN_MEETING_CHALLENGES <= len(challenges) <= MAX_MEETING_CHALLENGES
			checkSprintId = MIN_ID_SPRINT <= idSprint

			# Si todas las longitudes son correctas
			if checkActivityLong and checkSusggestionLong and checkChallengeLong and checkSprintId:
				
				# Verifico que el sprint exista
				foundSprint = clsSprint.query.filter_by(S_idSprint = idSprint)
				
				# Si el sprint existe. Verifico que la fecha no se repita
				if foundSprint != []:

					foundMeeting = self.searchMeeting(date,idSprint)

					if foundMeeting == []
						# Si la fecha no se repite
						newMeeting = clsSprintMeeting(date,activities,suggestions,challenges,idSprint)
						db.session.add(newMeeting)
						db.session.commit()
						return True

		return False

	def updateMeeting(self, date, newDate, newActivities, newSuggestions, newChallenges, idSprint):
		'''Permite actualizar los datos de una reunión diaria'''   
		#checkTypeDate 			   = type(date) == DateTime
		#checkTypeNewDate 		   = type(NewDate) == DateTime
		checkTypeNewActivities     = type(newActivities) == str
		checkTypeNewSuggestions    = type(newSuggestions) == str
		checkTypeNewChallenges     = type(newChallenges) == str
		checkTypeIdSprint      	   = type(idSprint) == int
		
		# Verifica la longitud de los campos
		if checkTypeNewActivities and checkTypeNewSuggestions and checkTypeNewChallenges and checkTypeIdSprint:
			checkNewActivityLong    = MIN_MEETING_ACTIVITIES <= len(newActivities) <= MAX_MEETING_ACTIVITIES
			checkNewSusggestionLong = MIN_MEETING_SUGGESTIONS <= len(newSuggestions) <= MAX_MEETING_SUGGESTIONS
			checkNewChallengeLong   = MIN_MEETING_CHALLENGES <= len(newChallenges) <= MAX_MEETING_CHALLENGES
			checkSprintId 			= MIN_ID_SPRINT <= idSprint

			#Si las longitudes son correctas
			if checkNewActivityLong and checkNewSusggestionLong and checkNewChallengeLong and checkSprintId:
				
				# Busca las reuniones que tengan la nueva fecha
				foundMeeting = self.searchMeeting(newDate,idSprint)

				# Si hay reuniones con la nueva fecha, el mismo sprint y date != de newDate (cambió la fecha)
				if  foundMeeting != [] and foundMeeting[0].SM_idSprint != idSprint and date != newDate:
					return False
					
				foundMeeting[0].SM_meetingDate = newDate
				foundMeeting[0].SM_activities  = newActivities
				foundMeeting[0].SM_suggestions = newSuggestions
				foundMeeting[0].SM_challenges  = newChallenges
				return True

		return False


	def deleteMeeting(self,date,idSprint):
		'''Permite eliminar una reunión de un sprint segun la fecha'''
		#checkTypeDate = type(date) == DateTime
		checkTypeIdSprint = type(idSprint) == int

		if checkTypeIdSprint:
			checkSprintId = MIN_ID_SPRINT <= idSprint

			# Si encuentra una reunion con esa fecha en ese sprint
			if checkSprintId:
				foundMeeting = self.searchIdMeeting(date,idSprint)

				if foundMeeting != []:
					for m in foundMeeting:
						db.session.delete(m)
					db.session.commit()
					return True

		return False

# Fin Clase meeting



