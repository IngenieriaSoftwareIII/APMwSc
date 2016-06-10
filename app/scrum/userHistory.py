# -*- coding: utf-8 -*-. 

import sys
import datetime

# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *

# Declaracion de constantes
CONST_MAX_COD    = 11
CONST_MIN_COD    = 1
CONST_MIN_ID     = 1
CONST_MIN_IDHIST = 0
CONST_MIN_SCALE  = 0
CONST_MAX_SCALE  = 20

arrayType = [1,2]
options   = {1:'podria ',2:'puede '}


class userHistory(object):
    '''Clase que permite manejar las historias de manera persistente'''
    
    def getAllUserHistoryId(self, idBacklog):
        '''Permite obtener todas las historias de usuario asocidas a un producto'''
        
        checkIdBacklog = type(idBacklog) == int
        
        if checkIdBacklog:
            checkLengIdBacklog = idBacklog >= CONST_MIN_ID
            
            if checkLengIdBacklog:
                existIdBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).first()
                
                if existIdBacklog != []:
                    found = clsUserHistory.query.filter_by(UH_idBacklog = idBacklog).all()
                    return found
        return ([])
        
        
    def isEpic(self, idUserHistory):
        '''Clase que permite reconocer las épicas'''
        
        checkId = type(idUserHistory) == int and CONST_MIN_ID <= idUserHistory
        
        if checkId:
            existId = clsUserHistory.query.filter_by(UH_idSuperHistory = idUserHistory).all()
            
            if existId != []:
                return True
        return False
    
    
    def succesors(self,idUserHistory,succ = [],visit = []):
        '''Permite encontrar los sucesores de una historia de usuario'''
        
        if idUserHistory != 0:
            result      = clsUserHistory.query.filter_by(UH_idSuperHistory = idUserHistory).all()
            idHistories = []
            for elem in result:
                idHistories.append(elem.UH_idUserHistory)
    
            for id in idHistories:
                if not(id in visit):
                    succ.append(id)
                    visit.append(id)
                    succ = self.succesors(id,succ,visit)        
        return succ
                            
    
    def historySuccesors(self, idUserHistory):
        '''Permite saber las subhistorias que componen a una historia mas general'''
         
        succ           = []
        checkIdHistory = type(idUserHistory) == int
        
        if checkIdHistory:
            checkLonIdHistory = CONST_MIN_ID <= idUserHistory

            if checkLonIdHistory:
                existId = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).all()
                if existId != []:
                    visited = []
                    self.succesors(idUserHistory,succ,visited)
        return succ
               
                
    def insertUserHistory(self,codeUserHistory,idSuperHistory,accionType,idAccion,idBacklog, priority, iniciado, fechaInicio, completed, fechaFin):
        '''Permite insertar una Historia de usuario'''
        
        checkCodUserHistory = type(codeUserHistory) == str
        checkIdSuperHistory = type(idSuperHistory) == int
        checkTypeAccion     = accionType in arrayType
        checkIdAccion       = type(idAccion) == int
        checkIdBacklog      = type(idBacklog) == int
        checkPriority       = type(priority) == int
        typeIniciado        = (type(iniciado) == bool)
        typeCompleted       = (type(completed) == bool)

        if checkCodUserHistory and checkIdSuperHistory and checkTypeAccion and checkIdAccion and checkIdBacklog and checkPriority and typeIniciado and typeCompleted:
            checkLenCodUserHistory = CONST_MIN_COD <= len(codeUserHistory) <= CONST_MAX_COD
            checkIdSuperHistory = CONST_MIN_IDHIST <= idSuperHistory 
            checkIdAccion       = CONST_MIN_ID <= idAccion 
            checkIdBacklog      = CONST_MIN_ID <= idBacklog 
            checkCodPriority =  CONST_MIN_SCALE <= priority <= CONST_MAX_SCALE
            
            if checkLenCodUserHistory and checkIdSuperHistory and checkIdAccion and checkIdBacklog and checkCodPriority:
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = idSuperHistory).all()
                
                if oUserHistory !=[] or idSuperHistory == 0:
                    oHistorys = clsAccion.query.filter_by(AC_idAccion = idAccion).all()
                    oBacklog  = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
            
                    if oBacklog != [] and oHistorys != []:                         
                        newUserHistory = clsUserHistory(codeUserHistory,idSuperHistory,accionType,idAccion,idBacklog, priority, iniciado, fechaInicio, completed, fechaFin)
                        db.session.add(newUserHistory)
                        db.session.commit()

                        if idSuperHistory != 0:
                            self.updatePriority(idSuperHistory,0)
                        return True
        return False
    
        
    def searchUserHistory(self,codeUserHistory, idBacklog):
        '''Permite encontrar una historia de usuario por codigo'''
        
        typecod = type(codeUserHistory) == str
        typeId  = type(idBacklog) == int
        
        if typecod and typeId:
            checkLenCodeUserHistory = len(codeUserHistory) <= CONST_MAX_COD
            checkIdBacklog          = idBacklog >= CONST_MIN_ID 
 
            if checkLenCodeUserHistory and checkIdBacklog:
                found = clsUserHistory.query.filter_by(UH_codeUserHistory = codeUserHistory,UH_idBacklog = idBacklog).all()
                return found
        return ([])
    
    
    def searchIdUserHistory(self,idUserHistory):
        '''Permite encontrar una historia de usuario por su id'''
        
        checkTypeId = type(idUserHistory) == int
        
        if checkTypeId:
            checkLenIdUserHistory = idUserHistory >= CONST_MIN_ID

            if checkLenIdUserHistory:            
                found = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).all()
                return found
        return ([])    
    

    def updateUserHistory(self,idUserHist,newCodeUserHistory,newIdSuperHistory,newAccionType,newIdAccion,newScale,iniciado,fechaInicio, completed, fechaFin):
        '''Permite modificar una Historia de usuario'''
        
        checkCodUserHistory = type(newCodeUserHistory) == str
        checkIdSuperHistory = type(newIdSuperHistory) == int
        checkTypeAccion     = newAccionType in arrayType
        checkIdAccion       = type(newIdAccion) == int
        checkIdUser         = type(idUserHist) == int
        checkPriority       = type(newScale) == int
        typeIniciado        = (type(iniciado) == bool)
        typeCompleted        = (type(completed) == bool)
                
        if checkCodUserHistory and checkIdSuperHistory and checkTypeAccion and checkIdAccion and checkIdUser and checkPriority and typeIniciado and typeCompleted:
            checkLenCodUserHistory = CONST_MIN_COD <= len(newCodeUserHistory) <= CONST_MAX_COD
            checkIdHistory         = newIdSuperHistory >= CONST_MIN_IDHIST
            checkIdAccion          = newIdAccion >= CONST_MIN_ID

            if checkLenCodUserHistory and checkIdHistory and checkIdAccion:            
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory  = newIdSuperHistory).all()
                      
                if oUserHistory !=[] or newIdSuperHistory == 0:
                    oAccions = clsAccion.query.filter_by(AC_idAccion  = newIdAccion).all()
                    
                    if oAccions != []:
                        result            = clsUserHistory.query.filter_by(UH_idUserHistory  = idUserHist).all()
                        checkSuperHistory = clsUserHistory.query.filter_by(UH_idSuperHistory = idUserHist).all()

                        if result != []:
                            if fechaInicio <= fechaFin:
                                result[0].UH_codeUserHistory = newCodeUserHistory
                                result[0].UH_accionType      = newAccionType
                                result[0].UH_idAccion        = newIdAccion
                                result[0].UH_scale           = newScale
                                result[0].UH_iniciado        = iniciado
                                result[0].UH_fechaInicio     = fechaInicio
                                result[0].UH_completed       = completed
                                result[0].UH_fechaFin        = fechaFin
                                 
                                # Consideramos el caso en que una historia deje de ser epica y se le asigna un valor
                                # arbitrario a la escala
                                if result[0].UH_idSuperHistory != 0 and (checkSuperHistory == [] or newIdSuperHistory == 0):
                                    # Almacenamos el valor de la super historia
                                    idOldSuperHist              = result[0].UH_idSuperHistory
                                    result[0].UH_idSuperHistory = newIdSuperHistory
                                    
                                    # Verificamos si la vieja historia sigue siendo epica
                                    epic = self.isEpic(idOldSuperHist)
                                    if not epic:
                                        self.updatePriority(idOldSuperHist,1)                          
                                # Consideramos el caso normal de modificacion de la historia mas general        
                                elif checkSuperHistory == [] or newIdSuperHistory == 0:
                                    result[0].UH_idSuperHistory = newIdSuperHistory
                                db.session.commit()
                                
                                # Consideramos el caso en que la historia mas general se convierte en epica
                                if newIdSuperHistory != 0:
                                    self.updatePriority(newIdSuperHistory,0)                          
                        return True
        return False
    
    
    def updatePriority(self,idHistory,priority):
        '''Permite actualizar la prioridad de una historia de usuario'''

        checkIdHistory  = type(idHistory) == int
        checkPriority   = type(priority) == int

        if checkIdHistory and checkPriority:
            checkLonIdHistory = CONST_MIN_ID <= idHistory
            checkLonPriority  = 0 <= priority

            if  checkLonIdHistory and checkLonPriority:

                found     = clsUserHistory.query.filter_by(UH_idUserHistory = idHistory).first()
                foundTask = clsTask.query.filter_by(HW_idUserHistory = idHistory).all()
                if found != None:
                    found.UH_scale = priority
                    if (priority == 0) and (foundTask != []):
                        for task in foundTask:
                            db.session.delete(task)
                    db.session.commit()
                    return True
        return False

    def completeHistory(self,idHistory):
        '''Permite marcar una historia como completa'''

        checkIdHistory  = type(idHistory) == int
        if checkIdHistory:
            checkLonIdHistory = CONST_MIN_ID <= idHistory
            if  checkLonIdHistory:
                found     = clsUserHistory.query.filter_by(UH_idUserHistory = idHistory).first()
                if found != None:
                    found.UH_completed = True
                    db.session.commit()
                    return True
        return False

    def incompleteHistory(self,idHistory):
        '''Permite marcar una historia como incompleta'''

        checkIdHistory  = type(idHistory) == int
        if checkIdHistory:
            checkLonIdHistory = CONST_MIN_ID <= idHistory
            if  checkLonIdHistory:
                found     = clsUserHistory.query.filter_by(UH_idUserHistory = idHistory).first()
                if found != None:
                    found.UH_completed = False
                    db.session.commit()
                    return True
        return False


    def accionsAsociatedToUserHistory(self,userHistoryId):
        ''' Permite obtener una lista de los Acciones asociados a una historia de usuario'''
        
        checkTypeId = type(userHistoryId) == int
        
        if checkTypeId:
            checkLonId = CONST_MIN_ID <= userHistoryId
            
            if checkLonId:
                found = clsUserHistory.query.filter_by(UH_idUserHistory = userHistoryId).all()
                return found
        return([])

    def testsAsociatedToUserHistory(self, userHistoryId):
        ''' Permite obtener una lista de las pruebas asociadas a una historia de usuario'''

        checkTypeId = type(userHistoryId) == int

        if checkTypeId:
            checkLonId = CONST_MIN_ID <= userHistoryId

            if checkLonId:
                found = clsAcceptanceTest.query.filter_by(AT_idUserHistory = userHistoryId).all()
                return found
        return([])
    
    
    def searchidUserHistoryIdAccion(self, idAccion):
        '''Permite obtener los ids de las historias de usuario que contiene el idAccion'''
        
        checkIdAccion = type(idAccion) == int
 
        if checkIdAccion:
            checkLonIdAccion = idAccion >= CONST_MIN_ID
            
            if checkLonIdAccion:
                result = clsUserHistory.query.filter_by(UH_idAccion  = idAccion).all()
                return result
        return  ([])
    
    
    def deleteUserHistory(self,idUserHistory):
        '''Permite eliminar una historia segun su ID'''
        
        checkTypeIdHistory = type(idUserHistory) == int
        
        if checkTypeIdHistory:
            checkIdHistory = idUserHistory >= CONST_MIN_ID
            
            if checkIdHistory:
                found = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).all()
                
                if found != []:
                    idSuperHistory = found[0].UH_idSuperHistory
                    for i in found:    
                        db.session.delete(i)          
                    db.session.commit()
                    succesor = self.historySuccesors(idSuperHistory)
                    
                    if (idSuperHistory != 0 and succesor == []):
                        self.updatePriority(idSuperHistory,1)
                    return True
        return False 


    def transformUserHistory(self,idUserHistory):
        '''Permite construir una estructura para representar una historia de usuario'''
        
        historyDict = {}
        checkTypeId = type(idUserHistory) == int
        
        if checkTypeId:
            checkLonId = CONST_MIN_ID <= idUserHistory

            if checkLonId:    
                # Buscamos la historia de usuario.
                foundHistory = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).first()
    
                if foundHistory != None:               
                    # Guardamos el id de la historia.
                    historyDict['idHistory'] = foundHistory.UH_idUserHistory 
                    
                    # Almacenamos en el diccionario el valor de la escala correspondiente.
                    historyDict['priority'] = foundHistory.UH_scale
                    
                    # Almacenamos en el diccionario el valor del resumen.
                    historyDict['resume'] = foundHistory.UH_resume

                    # Obtenemos los id de los actores que componen la historia.
                    result = clsActorsUserHistory.query.filter_by(AUH_idUserHistory = idUserHistory)
                    idActorsList = []
                    for act in result:
                        idActorsList.append(act.AUH_idActor)
                          
                    missingActors = len(idActorsList)
                    actorsString  = ''
                    
                    # Almacenamos los actores asociados a la historia en el diccionario de la historia.
                    for act in idActorsList:
                        result       = clsActor.query.filter_by(A_idActor = act).all()
                        actorsString = actorsString + ' ' + str(result[0].A_nameActor) + ' '
                        
                        if missingActors != 1:
                            actorsString = actorsString + ',' 
                             
                        missingActors = missingActors - 1   
                    historyDict['actors'] = actorsString.lower()
                    
                    # Almacenamos la accion asociada la historia en el diccionario de la historia.
                    idAccions   = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).all()
                    foundAccion = clsAccion.query.filter_by(AC_idAccion  = idAccions[0].UH_idAccion).all()
                
                    # Obtenemos el tipo de accion de la historia.
                    option    = foundHistory.UH_accionType
                    historyDict['actions'] = ' ' + options[option] + str(foundAccion[0].AC_accionDescription).lower() + ' ' 
            
                    # Obtenemos los id de los objetivos que componen la historia.
                    result  = clsObjectivesUserHistory.query.filter_by(OUH_idUserHistory = idUserHistory)
                    idObjectivesList  = []
                    
                    for obj in result:
                        idObjectivesList.append(obj.OUH_idObjective)
                
                    missingObjectives = len(idObjectivesList)
                    objectivesString  = ''
                    
                    # Almacenamos los objetivos asociados a la historia en el diccionario de la historia.
                    for obj in idObjectivesList: 
                        result           = clsObjective.query.filter_by(O_idObjective = obj).all()
                        objectivesString = objectivesString + ' ' + str(result[0].O_descObjective)
                        
                        if missingObjectives != 1:
                            objectivesString = ' ' + objectivesString + ',' 
                             
                        if missingObjectives == 1: 
                            objectivesString = objectivesString + '.'  
                            
                        missingObjectives = missingObjectives - 1
                        
                    historyDict['objectives'] = objectivesString.lower()
                    
                    return historyDict

        return historyDict 

    def assignHistoryResume(self,idUserHistory, historyResume):
        '''Permite agregar un resumen a una historia de usuario'''

        checkTypeIdHistory = type(idUserHistory) == int
        checkTypeHistoryResume = type(historyResume) == str

        if checkTypeIdHistory and checkTypeHistoryResume:
            checkIdHistory = idUserHistory >= CONST_MIN_ID

            if checkIdHistory:

                oHistory = self.searchIdUserHistory(idUserHistory)
                oHistory[0].UH_resume = historyResume

                db.session.commit()

                return True

        return False

    def getUHCodeFromId(self,idUserHistory):
        found = clsUserHistory.query.filter_by(UH_idUserHistory = idUserHistory).first()
        return found.UH_codeUserHistory

# Fin Clase userHistory
