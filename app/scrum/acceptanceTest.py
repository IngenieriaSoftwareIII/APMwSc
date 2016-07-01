# -*- coding: utf-8 -*-. 

import sys

sys.path.append('app/scrum')

from userHistory import *

class acceptanceTest(object):
    '''Clase que permite manejar las pruebas de aceptacion de manera persistente'''

    def getAllAcceptanceTestByUserHistory(self, idUserHistory):
        '''Permite obtener las pruebas de aceptacion asociadas a una historia de usuario'''
        found = clsAcceptanceTest.query.filter_by(AT_idUserHistory = idUserHistory).all()

        return found


    def findIdAcceptanceTest(self, idAT):
        '''Permite encontrar una prueba de aceptacion dado un id'''
        checkTypeIdAT = type(idAT) == int
        found = None

        if checkTypeIdAT:
            found = clsAcceptanceTest.query.filter_by(AT_idAT=idAT).first()
        return found

    def insertAcceptanceTest(self,idUserHistory,description,urlScript):
        '''Permite insertar una nueva prueba de aceptacion'''

        checkTypeidUserHistory  = type(idUserHistory)   == int
        checkTypeDescription    = type(description)     == str
        checkTypeUrlScript      = type(urlScript)       == str

        if checkTypeidUserHistory and checkTypeDescription and checkTypeUrlScript:
            oUserStory = userHistory()
            foundUserHistory = oUserStory.searchIdUserHistory(idUserHistory)
            foundUrlScript = clsAcceptanceTest.query.filter_by(AT_urlScript = urlScript).first()

            if foundUserHistory != [] and foundUrlScript == None:
                newAT = clsAcceptanceTest(idUserHistory,description,urlScript)
                db.session.add(newAT)
                db.session.commit()
                return True

        return False


    def deleteAcceptanceTest(self,idAT):
        '''Permite eliminar una nueva prueba de aceptacion'''
        checkTypeidAT = type(idAT) == int

        if checkTypeidAT:
            found = self.findIdAcceptanceTest(idAT)

            if found != [] and found != None:
                db.session.delete(found)
                db.session.commit()
                return True

        return False

    def modifyAcceptanceTest(self,idAT,description,urlScript):
        '''Permite modificar una nueva prueba de aceptacion'''
        checkTypeidAT = type(idAT) == int

        if checkTypeidAT:
            if description == None and urlScript == None:
                return True


            if urlScript == None and description != None:
                checkTypeDescription = type(description) == str
                if checkTypeDescription:
                    found = self.findIdAcceptanceTests(idAT)
                    if found != []:
                        found.AT_description = description
                        db.session.commit()
                        return True

            if description == None and urlScript != None:
                checkTypeUrlScript = type(urlScript) == str
                if checkTypeUrlScript:
                    found = self.findIdAcceptanceTests(idAT)
                    if found != []:
                        found.AT_urlScript = urlScript
                        db.session.commit()
                        return True

            if description != None and urlScript != None:
                checkTypeDescription = type(description) == str
                checkTypeUrlScript = type(urlScript) == str
                if checkTypeDescription and checkTypeUrlScript:
                    found = self.findIdAcceptanceTests(idAT)
                    if found != []:
                        found.AT_description = description
                        found.AT_urlScript = urlScript
                        db.session.commit()
                        return True

        return False