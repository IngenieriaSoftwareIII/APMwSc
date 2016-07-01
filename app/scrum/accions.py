# -*- coding: utf-8 -*-.

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *

# Declaracion de constantes.
MIN_ID                 = 1
MIN_ACCION_DESCRIPTION = 1
MAX_ACCION_DESCRIPTION = 140

class accions(object):
    '''Clase que permite manejar las acciones de manera persistente'''

    def insertAccion(self,accionDescription,idBacklog):
        '''Permite insertar una Accion asociada a un producto'''

        checkTypeDescription = type(accionDescription) == str
        checkTypeId          = type(idBacklog) == int

        if checkTypeDescription and checkTypeId:
            checkLongAccionDescription = MIN_ACCION_DESCRIPTION <= len(accionDescription) <= MAX_ACCION_DESCRIPTION
            checkLongId                = MIN_ID <= idBacklog

            if checkLongAccionDescription and checkLongId:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()

                if foundBacklog != []:
                    foundAccions = clsAccion.query.filter_by(AC_idBacklog = idBacklog).all()
                    foundAccionDesc = []
                    for desc in foundAccions:
                        if desc.AC_accionDescription.lower()  == accionDescription.lower():
                            foundAccionDesc.append(desc)
                            break

                    if foundAccionDesc == []:
                        newAccion = clsAccion(accionDescription,idBacklog)
                        db.session.add(newAccion)
                        db.session.commit()
                        return True
        return False


    def searchAccion(self, accionDescription, idBacklog):
        '''Permite buscar acciones por su descripcion'''

        checkTypeId   = type(idBacklog) == int
        checkTypeDesc = type(accionDescription) == str
        foundAccion   = []

        if checkTypeId and checkTypeDesc:
            checkLenDesc = MIN_ACCION_DESCRIPTION <= len(accionDescription) <= MAX_ACCION_DESCRIPTION
            checkId      = MIN_ID <= idBacklog

            if checkLenDesc and checkId:
                foundAccion = clsAccion.query.filter_by(AC_idBacklog = idBacklog,AC_accionDescription = accionDescription).all()
        return foundAccion


    def searchIdAccion(self, idAccion):
        '''Permite buscar acciones por su id'''

        checkTypeIdAccion = type(idAccion) == int
        foundAccion       = []

        if checkTypeIdAccion:
            checkId = idAccion >= MIN_ID
            if checkId:
                foundAccion = clsAccion.query.filter_by(AC_idAccion  = idAccion).all()
        return foundAccion


    def updateAccion(self, accionDescription,newDescription,idBacklog):
        '''Permite actualizar la descripcion de una accion'''

        checkTypeDescription    = type(accionDescription) == str
        checkTypeNewdescription = type(newDescription) == str
        checkTypeIdBacklog      = type(idBacklog) == int

        if checkTypeDescription and checkTypeNewdescription and checkTypeIdBacklog:
            checkLongAccionDescription = MIN_ACCION_DESCRIPTION <= len(accionDescription) <= MAX_ACCION_DESCRIPTION
            checkLongNewDescription    = MIN_ACCION_DESCRIPTION <= len(newDescription) <= MAX_ACCION_DESCRIPTION
            checkLongIdBacklog         = MIN_ID <= idBacklog

            if checkLongAccionDescription and checkLongNewDescription and checkLongIdBacklog:
                foundAccion = clsAccion.query.filter_by(AC_idBacklog = idBacklog,AC_accionDescription = accionDescription).all()
                foundNew    = clsAccion.query.filter_by(AC_idBacklog = idBacklog,AC_accionDescription = newDescription).all()

                if foundAccion != [] and (foundNew == [] or accionDescription == newDescription):
                    foundAccion[0].AC_accionDescription = newDescription
                    db.session.commit()
                    return True
        return False


    def deleteAccion(self, accionDescription,idBacklog):
        '''Permite eliminar una accion segun su id'''

        checkTypeDescription = type(accionDescription) == str
        checkTypeIdBacklog   = type(idBacklog) == int

        if checkTypeDescription and checkTypeIdBacklog:
            checkLenDescription = MIN_ACCION_DESCRIPTION <= len(accionDescription) <= MAX_ACCION_DESCRIPTION
            checkLongIdBacklog  = MIN_ID <= idBacklog

            if checkLenDescription and checkLongIdBacklog:
                found = clsAccion.query.filter_by(AC_accionDescription = accionDescription,AC_idBacklog = idBacklog).all()

                if found != []:
                    for i in found:
                        db.session.delete(i)
                    db.session.commit()
                    return True
        return False

    def toJson(self, idAccion):
        '''Permite buscar acciones por su id'''

        checkTypeIdAccion = type(idAccion) == int
        foundAccion       = None
        jsonAction        = {}

        if checkTypeIdAccion:
            checkId = idAccion >= MIN_ID
        if checkId:
            foundAccion = clsAccion.query.filter_by(AC_idAccion  = idAccion).all()

        if foundAccion:
            jsonAction = {
                "id": foundAccion[0].AC_idAccion,
                "description": foundAccion[0].AC_accionDescription
            }

        return jsonAction


# Fin Clase Accion
