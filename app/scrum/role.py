# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from backLog import *

# Declaracion de constantes.
CONST_MAX_NAME_ACTOR        = 50
CONST_MIN_NAME_ACTOR        = 1
CONST_MIN_ACTOR_DESCRIPTION = 1
CONST_MAX_ACTOR_DESCRIPTION = 140
CONST_MIN_ID                = 0


class role(object):
    '''Clase que permite manejar los Actores de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla actor esta vacia'''
        aActor = clsActor.query.all()
        return (aActor == [])


    def getAllRoles(self):
        '''Permite obtener todos los roles'''
        return (clsActor.query.all())
    

    def insertActor(self,nameActor,actordescription,idBacklog):
        '''Permite insertar un actor'''
        
        checkTypeName        = type(nameActor) == str
        checkTypeDescription = type(actordescription) == str
        checkTypeId          = type(idBacklog) == int
        
        if checkTypeName  and checkTypeDescription and checkTypeId:
            checkLongName        = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR
            checkLongDescription = CONST_MIN_ACTOR_DESCRIPTION <= len(actordescription) <= CONST_MAX_ACTOR_DESCRIPTION
            checkLongId                = CONST_MIN_ID <= idBacklog            
            
            if checkLongName and checkLongDescription:
                foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
                
                if foundBacklog != [] or idBacklog == 0:
                    foundActors   = clsActor.query.filter_by(A_idBacklog = idBacklog).all()
                    foundActorNameDesc = []
                    for act in foundActors:
                        if (act.A_nameActor.lower() == nameActor.lower()) and (act.A_actorDescription.lower()  == actordescription.lower()):
                            foundActorNameDesc.append(act)
                            break
                         
                    if foundActorNameDesc == []:
                        newActor = clsActor(nameActor, actordescription, idBacklog)
                        db.session.add(newActor)
                        db.session.commit()
                        return True                        
        return False


    def findNameActor(self, nameActor,idBacklog):
        '''Permite buscar un elemento en la tabla de actores'''
        
        checkTypeName = type(nameActor) == str
        checkTypeId   = type(idBacklog) == int
        foundActor    = []
        
        if checkTypeName and checkTypeId:
            checkLenName = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR
            checkId      = CONST_MIN_ID <= idBacklog 
            
            if  checkLenName and checkId:
                foundActor = clsActor.query.filter_by(A_idBacklog = idBacklog,A_nameActor = nameActor).all()
        return foundActor
    
    
    def findIdActor(self, idActor):
        '''Permite buscar un elemento en la tabla de actores por su id'''
        
        checkIdActor = type(idActor) == int and idActor >= CONST_MIN_ID
        foundActor   = []
        
        if checkIdActor:
                foundActor = clsActor.query.filter_by(A_idActor = idActor).all()
        return foundActor
              

    def updateActor(self, nameActor, newNameActor, newDescription,idBacklog):
        '''Permite modificar un nombre de la clase actor'''
    
        checkTypeName        = type(nameActor) == str
        checkTypeNewActor    = type(newNameActor) == str
        checkTypeDescription = type(newDescription) == str
        checkTypeIdBacklog   = type(idBacklog) == int
    
        if checkTypeName and checkTypeNewActor and checkTypeDescription and checkTypeIdBacklog:
            checkLongnameActor      = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR
            checkLongNewnameActor   = CONST_MIN_NAME_ACTOR <= len(newNameActor) <= CONST_MAX_NAME_ACTOR
            checkLongNewDescription = CONST_MIN_ACTOR_DESCRIPTION <= len(newDescription) <= CONST_MAX_ACTOR_DESCRIPTION
            checkLongIdBacklog      = CONST_MIN_ID <= idBacklog 
            
            if checkLongnameActor and checkLongNewnameActor  and checkLongNewDescription and checkLongIdBacklog:    
                foundnameActor = clsActor.query.filter_by(A_idBacklog = idBacklog,A_nameActor = nameActor).all()
                foundNewActor  = clsActor.query.filter_by(A_idBacklog = idBacklog,A_nameActor = newNameActor).all()
                
                if foundnameActor != [] and (foundNewActor == [] or nameActor == newNameActor):
                    updateActor = clsActor.query.filter_by(A_idBacklog = idBacklog,A_nameActor = nameActor).first()
                    updateActor.A_nameActor        = newNameActor
                    updateActor.A_actorDescription = newDescription
                    db.session.commit()
                    return True
        return False   
    

    def deleteActor(self,nameActor,idBacklog):
        '''Permite eliminar un actor dado su nombre'''

        checkTypeName      = type(nameActor) == str
        checkTypeIdBacklog = type(idBacklog) == int   
                
        if checkTypeName and checkTypeIdBacklog:
            
            checkLongNameActor = CONST_MIN_NAME_ACTOR <= len(nameActor) <= CONST_MAX_NAME_ACTOR 
            checkLongIdBacklog = CONST_MIN_ID <= idBacklog 
            
            if checkLongNameActor and checkLongIdBacklog:
                oActor = clsActor.query.filter_by(A_idBacklog = idBacklog,A_nameActor = nameActor).all()
                
                if oActor != []:
                    tupla = clsActor.query.filter_by(A_nameActor = nameActor).first()    
                    db.session.delete(tupla)
                    db.session.commit()
                    return True
        return False
    
# Fin Clase Actor
