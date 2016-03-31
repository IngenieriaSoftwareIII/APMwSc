# -*- coding: utf-8 -*-. 

import sys

sys.path.append('app/scrum')

from userHistory import *

class acceptanceCriteria(object):
    '''Clase que permite manejar las pruebas de aceptacion de manera persistente'''

    def findIdAcceptanceCriteria(self, idHAC):
            '''Permite encontrar un criterio de aceptacion dado un id'''
            checkTypeIdHAC = type(idHAC) == int
            found = None

            if checkTypeIdHAC:
                found = clsAcceptanceTest.query.filter_by(HAC_HAC_idAcceptanceCriteria=idHAC).first()
            return found

    def insertAcceptanceTest(self,idUserHistory,description):
        '''Permite insertar un nuevo criterio de aceptacion'''

        checkTypeidUserHistory  = type(idUserHistory)   == int
        checkTypeDescription    = type(description)     == str

        if checkTypeidUserHistory and checkTypeDescription:
            oUserStory = userHistory()
            foundUserHistory = oUserStory.searchIdUserHistory(idUserHistory)

            if foundUserHistory != []:
                newHAC = clsAcceptanceCriteria(idUserHistory,description)
                db.session.add(newHAC)
                db.session.commit()
                return True

        return False


    def deleteAcceptanceTest(self,idHAC):
        '''Permite eliminar una nueva prueba de aceptacion'''
        checkTypeidHAC = type(idHAC) == int

        if checkTypeidHAC:
            found = self.findIdAcceptanceCriteria(idHAC)

            if found != [] and found != None:
                db.session.delete(found)
                db.session.commit()
                return True

        return False

    def modifyAcceptanceTest(self,idAT,description):
        '''Permite modificar una nueva prueba de aceptacion'''
        checkTypeidAT = type(idAT) == int

        if checkTypeidAT:
            if description == None:
                return True

            checkTypeDescription = type(description) == str
            if checkTypeDescription:
                found = self.findIdAcceptanceTests(idAT)
                if found != []:
                    found.AT_description = description
                    db.session.commit()
                    return True
        return False