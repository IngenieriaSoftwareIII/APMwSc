# -*- coding: utf-8 -*-.

import sys
import datetime

# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from userHistory import *

# Declaracion de constantes.
MIN_ID               = 1
MIN_WEIGHT           = 1
MIN_LIST             = 0
MIN_TASK_DESCRIPTION = 1
MAX_TASK_DESCRIPTION = 140


class task(object):
    '''Clase que permite manejar los tasks de manera persistente'''

    def getAllTask(self,HW_idUserHistory):
        '''Permite obtener todas las tareas asociadas a una historia de usuario'''

        typeId  = (type(HW_idUserHistory) == int)

        if (typeId  and HW_idUserHistory  >= MIN_ID):
            otask = clsTask.query.filter_by(HW_idUserHistory = HW_idUserHistory).all()
            return otask
        return ([])

    def insertTask(self, HW_description, C_idCategory, HW_weight, UH_idUserHistory, HW_iniciado, HW_fechaInicio, HW_completed, HW_fechaFin):
        '''Permite insertar una tarea'''

        typedescription = (type(HW_description) == str)
        typeidCategory  = (type(C_idCategory) == int)
        typeWeight      = (type(HW_weight) == int)
        typeid          = (type(UH_idUserHistory) == int)
        typeIniciado    = (type(HW_iniciado) == bool)
        typeCompleted   = (type(HW_completed) == bool)

        if (typedescription and typeidCategory and typeWeight and typeid and typeIniciado and typeCompleted):
            long_HW_description  = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
            min_C_idCategory     = C_idCategory >= MIN_ID
            min_HW_weight        = HW_weight >= MIN_WEIGHT
            min_UH_idUserHistory = UH_idUserHistory >= MIN_ID

            if (long_HW_description and min_C_idCategory and min_HW_weight and min_UH_idUserHistory):
                oUserHistory = clsUserHistory.query.filter_by(UH_idUserHistory = UH_idUserHistory).all()
                oCategory    = clsCategory.query.filter_by(C_idCategory = C_idCategory).all()
                oTask        = clsTask.query.filter_by(HW_description = HW_description).all()
                oHistory     = userHistory()
                esEpica      = (oHistory.isEpic(UH_idUserHistory))

                if ((oUserHistory != []) and (oCategory != []) and (oTask == []) and (not esEpica)):
                    new_task = clsTask(HW_description,C_idCategory,HW_weight,UH_idUserHistory,HW_iniciado,HW_fechaInicio,HW_completed,HW_fechaFin)
                    db.session.add(new_task)
                    db.session.commit()
                    return True
        return False


    def deleteTask(self, HW_description):
        '''Permite eliminar una tarea según su descripción'''

        typedescription = (type(HW_description) == str)

        if typedescription:
            len_description = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION

            if len_description:
                foundid = clsTask.query.filter_by(HW_description = HW_description).all()

                if foundid != []:
                    oTask = clsTask.query.filter_by(HW_description = HW_description).all()
                    for i in oTask:
                        db.session.delete(i)
                    db.session.commit()
                    return True
        return False

    def deleteDoc(self, taskId, documentName):
        '''Permite eliminar una documento según su nombre y id de tarea'''

        foundid = clsTaskDoc.query.filter_by(HWD_idTask = taskId, HWD_docName = documentName ).all()
        if foundid !=[]:
            for i in foundid:
                db.session.delete(i)
            db.session.commit()
            return True
        return False

    # def completeTask(self,idTask):
    #     '''Permite marcar una tarea como completa'''

    #     found     = clsTask.query.filter_by(HW_idTask = idTask).first()
    #     if found != None:
    #         found.HW_completed = True
    #         db.session.commit()
    #         return True
    #     return False

    # def incompleteTask(self,idTask):
    #     '''Permite marcar una tarea como incompleta'''

    #     found     = clsTask.query.filter_by(HW_idTask = idTask).first()
    #     if found != None:
    #         found.HW_completed = False
    #         db.session.commit()
    #         return True
    #     return False

    def taskById(self,idTask):
        '''Permite actualizar la prioridad de una historia de usuario'''

        found     = clsTask.query.filter_by(HW_idTask = idTask).first()
        return found

    def searchTask(self, HW_description):
        '''Permite buscar tareas por su descripcion'''

        typedescription = (type(HW_description) == str)

        if typedescription:
            oTask = clsTask.query.filter_by(HW_description = HW_description).all()
        else:
            oTask = False
        return oTask


    def updateTask(self, HW_description, newDescription, C_idCategory, HW_weight, HW_iniciado, HW_fechaInicio, HW_completed, HW_fechaFin, HW_horasEmpleadas):
        '''Permite actualizar la descripcion de una tarea'''

        typedescription    = (type(HW_description) == str)
        typeNewdescription = (type(newDescription) == str)

        typeidCategory     = (type(C_idCategory) == int)
        typeWeight         = (type(HW_weight) == int)

        typeIniciado    = (type(HW_iniciado) == bool)
        typeCompleted   = (type(HW_completed) == bool)

        if (typedescription and typeNewdescription and typeidCategory and typeWeight):
            long_HW_description = MIN_TASK_DESCRIPTION <= len(HW_description) <= MAX_TASK_DESCRIPTION
            long_newDescription = MIN_TASK_DESCRIPTION <= len(newDescription) <= MAX_TASK_DESCRIPTION
            min_C_idCategory    = C_idCategory >= MIN_ID
            min_HW_weight       = HW_weight >= MIN_WEIGHT
            hours_spent_positive =HW_horasEmpleadas is None  or  HW_horasEmpleadas>0
            

            if (long_HW_description and long_newDescription and min_C_idCategory and min_HW_weight and hours_spent_positive ):
                foundTask = self.searchTask(HW_description)
                foundNew  = self.searchTask(newDescription)
                foundCat  = clsCategory.query.filter_by(C_idCategory = C_idCategory).all()

                if HW_fechaFin is None or  HW_fechaInicio <= HW_fechaFin:
                    if ((foundTask != []) and (foundCat != []) and ((foundNew == []) or (HW_description == newDescription))):
                        oTask                = clsTask.query.filter_by(HW_description = HW_description).first()
                        oTask.HW_description = newDescription
                        oTask.HW_idCategory  = C_idCategory
                        oTask.HW_weight      = HW_weight
                        oTask.HW_iniciado   = HW_iniciado
                        if HW_iniciado:
                            oTask.HW_fechaInicio = HW_fechaInicio
                        else:
                            oTask.HW_fechaInicio = None
                        oTask.HW_completed   = HW_completed
                        if HW_completed:
                            oTask.HW_fechaFin = HW_fechaFin
                        else:
                            oTask.HW_fechaFin = None
                        if  (HW_completed and HW_iniciado):
                            oTask.HW_horasEmpleadas = HW_horasEmpleadas
                        else:
                            oTask.HW_horasEmpleadas = None
                        db.session.commit()
                        return True
        return False


    def taskAsociatedToUserHistory(self,idUserHistory):
        ''' Permite obtener una lista de las tareas asociadas a una historia de usuario'''

        checkTypeId = type(idUserHistory) == int

        if checkTypeId:
            found = clsTask.query.filter_by(HW_idUserHistory  = idUserHistory).all()
            return found
        return([])


    def historyWeight(self,idUserHistory):
        ''' Permite obtener la suma de todos los pesos de las tareas correspondientes a una historia de usuario '''

        checkTypeId  = type(idUserHistory) == int
        peso         = 0
        oUserHistory = userHistory()
        esEpica      = oUserHistory.isEpic(idUserHistory)

        if not esEpica:

            if checkTypeId:
                taskList = self.taskAsociatedToUserHistory(idUserHistory)

                if taskList != []:
                    for task in taskList:
                        peso = peso + task.HW_weight
        else:
            peso = ''
        return peso


    def lookup(self,tupleList,idUserHistory):
        ''' Permite obtener el valor asociado a una clave en una lista de tuplas '''

        checkTypeId    = type(idUserHistory) == int
        checkTypeList  = type(tupleList)     == list
        checkTypeTuple = True

        if checkTypeList and checkTypeId:
            long_list = len(tupleList) > MIN_LIST

            if long_list:
                for tupla in tupleList:
                    checkTypeTuple = checkTypeTuple and (type(tupla) == tuple)

                    if checkTypeTuple:
                        if tupla[0] == idUserHistory:
                            return tupla[1]
        return ('')

    def getTaskById(self, taskID):
        ''' Permite obtener una tarea dado su ID'''
        return clsTask.query.filter_by(HW_idTask = taskID).first()

    def findIdTask(self, idTask):
        checkTypeId = type(idTask) == int
        found = None

        if checkTypeId:
            found = clsTask.query.filter_by(HW_idTask=idTask).first()
            return found

        return None


    def insertUserTask(self, idTask, idEquipo):
        checkTypeidTask = type(idTask) == int
        checkTypeidEquipo = type(idEquipo) == int

        if checkTypeidTask and checkTypeidEquipo:
            found = self.findIdTask(idTask)
            if found != None:
                idUserHistory = found.HW_idUserHistory
                found2 = clsUserHistory.query.filter_by(UH_idUserHistory=idUserHistory).first()

                if found2 != None:
                    idBacklog = found2.UH_idBacklog
                    found3 = clsEquipo.query.filter_by(EQ_idEquipo=idEquipo,EQ_idBacklog=idBacklog).first()

                    if found3 != None:
                        found.HW_idEquipo = idEquipo
                        db.session.commit()
                        return True
        return False

    def deleteUserTask(self, idTask):
        checkTypeidTask = type(idTask) == int

        if checkTypeidTask:
            found = self.findIdTask(idTask)
            if found != []:

                found.HW_idEquipo = None
                db.session.commit()
                return True
        return False


#Fin clase Task