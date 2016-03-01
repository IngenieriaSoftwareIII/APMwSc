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
			checkSprintId = MIN_ID <= idSprint

			# Si todas las longitudes son correctas
			if checkActivityLong and checkSusggestionLong and checkChallengeLong and checkSprintId:
				
				# Verifico que el sprint exista
				foundSprint = clsSprint.query.filter_by(S_idSprint = idSprint)
				
				# Verifico que la fecha no se repita
				if foundSprint != []:
					foundDate = clsSprintMeeting.query.filter_by(SM_meetingDate = date).all()

					for d in foundDate:
						if d.SM_meetingDate  == date:
							return False

					# Si la fecha no se repite
					newMeeting = clsSprintMeeting(date,activities,suggestions,challenges,idSprint)
					db.session.add(newMeeting)
					db.session.commit()
					return True

		return False

	def updateMeeting(self, newDate, newActivities, newSuggestions, newChallenges, idSprint):
		'''Permite actualizar los datos de una reunión diaria'''   
		#checkTypeDate 			= type(date) == DateTime
		checkTypeNewActivities     = type(newActivities) == str
		checkTypeNewSuggestions    = type(newSuggestions) == str
		checkTypeNewChallenges     = type(newChallenges) == str
		checkTypeIdSprint      	   = type(idSprint) == int
		
		if checkTypeNewActivities and checkTypeNewSuggestions and checkTypeNewChallenges and checkSprintId:


		return False

	def searchMeeting(self, date, idSprint):
		'''Permite buscar reuniones por su fecha'''
		#checkTypeDate = type(date) == DateTime
		checkTypeIdSprint = type(idSprint) == int
		foundMeeting       = []

		if checkTypeIdSprint:
			foundMeeting = clsSprintMeeting.query.filter_by(SM_meetingDate = date, SM_idSprint = idSprint).all()
		return foundMeeting


	def deleteMeeting(self,date,idSprint):
		'''Permite eliminar una reunión de un sprint segun la fecha'''
		#checkTypeDate = type(date) == DateTime
		checkTypeIdSprint = type(idSprint) == int

		if checkTypeIdSprint:
			checkSprintId = MIN_ID <= idSprint

			if checkSprintId:
				foundMeeting = searchIdMeeting(date,idSprint)
				
				if foundMeeting != []:
					for m in foundMeeting:
						db.session.delete(m)
					db.session.commit()
					return True

		return False

# Fin Clase meeting



