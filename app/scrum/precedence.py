# -*- coding: utf-8 -*-. 

import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

class precedence(object):
    def getAllPrecedences(self, idPila):
        '''Obtener todas las precedencias de la pila con id: idPila'''

        existsBacklog = clsBacklog.query.filter_by(BL_idBacklog = idPila).first()
        if existsBacklog != []:
            found = clsPrecedence.query.filter_by(P_idPila = idPila).all()
            return found
        return ([])

    def insertPrecedence(self, idFirstTask, idSecondTask, idPila):
        '''Insertar prelacion a la base de datos'''
        if (idFirstTask != None and idSecondTask != None):
            if (idFirstTask != idSecondTask):
                if self.doesNotMakeLoops(idFirstTask, idSecondTask) and not self.existPrecedence(idFirstTask,idSecondTask):
                    newPrecedence = clsPrecedence(idFirstTask, idSecondTask, idPila)
                    db.session.add(newPrecedence)
                    db.session.commit()
                    return True
                else:
                    print('Error')
            else:
                print('Error')
        else:
            print ('Error')
        return

    def deletePrecedence(self, idFirstTask, idSecondTask):
        '''Borrar prelacion de la base de datos'''

        exists = clsPrecedence.query.filter_by(P_idFirstTask = idFirstTask, P_idSecondTask = idSecondTask).first()
        if exists is not None :
            db.session.delete(exists)
            db.session.commit()
            return True
        return

    def existPrecedence(self, idFirstTask, idSecondTask):
        '''Permite saber si existe una precedencia'''
        
        typeFirst   = (type(idFirstTask) == int)
        typeSecond  = (type(idSecondTask) == int)

        if (typeFirst and typeSecond):
            found = clsPrecedence.query.filter_by(P_idFirstTask = idFirstTask, P_idSecondTask = idSecondTask).first()
            if found:
                return True
            else:
                return False

    def searchTaskByPrec(self, idTask):
        '''Permite obtener la lista de prelaciones donde idTask es antecedente'''

        typeid = (type(idTask) == int)
        if typeid:
            found = clsPrecedence.query.filter_by(P_idFirstTask = idTask).all()
            return found
        return([])

    def searchTaskByCons(self, idTask):
        '''Permite obtener la lista de prelaciones donde idTask es consecuente'''

        typeid = (type(idTask) == int)
        if typeid:
            found = clsPrecedence.query.filter_by(P_idSecondTask = idTask).all()
            return found
        return([])

    def doesNotMakeLoops(self, idFirstTask, idSecondTask):
        '''Evita los ciclos entre prelaciones'''

        typeFirst   = (type(idFirstTask) == int)
        typeSecond  = (type(idSecondTask) == int)
        noHayCiclo  = True 

        if (typeFirst and typeSecond):
            if (idFirstTask == idSecondTask):
                noHayCiclo = False
                return noHayCiclo
            else:
                secondTaskPrecedences = self.searchTaskByPrec(idSecondTask)
                if (secondTaskPrecedences != []):
                    for precedence in secondTaskPrecedences:
                        noHayCiclo = self.doesNotMakeLoops(idFirstTask,precedence.P_idSecondTask)

        return noHayCiclo

