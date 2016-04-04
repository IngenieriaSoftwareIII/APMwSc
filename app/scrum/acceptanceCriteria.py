# -*- coding: utf-8 -*-. 

import sys

sys.path.append('app/scrum')

from userHistory import *

MAX_ACCEPTANCE_DESCRIPTION = 140

class acceptanceCriteria(object):
    '''Clase que permite manejar los criterios de aceptacion de manera persistente'''

    def findIdAcceptanceCriteria(self, idHAC):
            '''Permite encontrar un criterio de aceptacion dado un id'''
            checkTypeIdHAC = type(idHAC) == int
            found = None

            if checkTypeIdHAC:
                found = clsAcceptanceCriteria.query.filter_by(HAC_idAcceptanceCriteria=idHAC).first()
            return found

    def insertAcceptanceCriteria(self,idUserHistory,description):
        '''Permite insertar un nuevo criterio de aceptacion'''

        checkTypeidUserHistory  = type(idUserHistory)   == int
        checkTypeDescription    = type(description)     == str

        if checkTypeidUserHistory and checkTypeDescription:
            oUserStory = userHistory()
            foundUserHistory = oUserStory.searchIdUserHistory(idUserHistory)

            if len(description) > MAX_ACCEPTANCE_DESCRIPTION:
                return False

            if foundUserHistory != []:
                foundAC = clsAcceptanceCriteria.query.filter_by(HAC_idUserHistory = idUserHistory).all()

                for elem in foundAC:
                    if elem.HAC_description == description:
                        return False

                newHAC = clsAcceptanceCriteria(idUserHistory,description)
                db.session.add(newHAC)
                db.session.commit()
                return True

        return False


    def deleteAcceptanceCriteria(self,idHAC):
        '''Permite eliminar un nuevo criterio de aceptacion'''
        checkTypeidHAC = type(idHAC) == int

        if checkTypeidHAC:
            found = self.findIdAcceptanceCriteria(idHAC)

            if found != [] and found != None:
                db.session.delete(found)
                db.session.commit()
                return True

        return False

    def modifyAcceptanceCriteria(self,idHAC,description):
        '''Permite modificar un nuevo criterio de aceptacion'''
        checkTypeidHAC = type(idHAC) == int

        if checkTypeidHAC:
            if description == None:
                return True

            checkTypeDescription = type(description) == str
            if checkTypeDescription:
                found = self.findIdAcceptanceCriteria(idHAC)
                if len(description) > MAX_ACCEPTANCE_DESCRIPTION:
                    return False
                if found != [] and hasattr(found, 'HAC_description'):
                    found.HAC_description = description
                    db.session.commit()
                    return True
        return False

    def getACById(self, acceptanceCriteriaID):
        ''' Permite obtener un criterio de aceptación dado su ID'''
        return clsAcceptanceCriteria.query.filter_by(HAC_idAcceptanceCriteria = acceptanceCriteriaID).first()

    def getAceptanceCriteriaID(self, idUserHistory,description):
        ''' Permite obtener el id del criterio de aceptacion de acuerdo ol id de historia y descripcion'''
        criterio = clsAcceptanceCriteria.query.filter_by(HAC_idUserHistory = idUserHistory, HAC_description = description).first()
        if criterio:
            return criterio.HAC_idAcceptanceCriteria
        return []