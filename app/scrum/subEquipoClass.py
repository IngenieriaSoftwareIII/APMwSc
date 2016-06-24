# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from sprint import *
from equipo import *

# Declaracion de constantes.
CONST_MAX_NAME_USERNAME = 17
CONST_MIN_NAME_USERNAME = 1


class subEquipoClass(object):
    '''Clase que permite manejar los SubEquipos de manera persistente'''
    
    def emptyTable(self):
        '''Permite saber si la tabla sub equipo esta vacia'''
        aSubEquipo = clsSubEquipo.query.all()
        return (aSubEquipo == [])

    def getSubEquipo(self,idSprint):
        '''Entrega la lista de miembros de un sub equipo'''

        aSubEquipo = clsSubEquipo.query.filter_by(SEQ_idSprint = idSprint).all()

        return aSubEquipo

    def deleteMiembroSubEquipo(self, username,idSprint):
        '''Permite eliminar un miembro de un sub equipo'''
        checkTypeUsername = type(username) == str
        checkTypeIdSprint = type(idSprint) == int
        
        if checkTypeUsername and checkTypeIdSprint:
            checkLongName = CONST_MIN_NAME_USERNAME <= len(username) <= CONST_MAX_NAME_USERNAME
            checkLongIdSprint = CONST_MIN_ID <= idSprint               
             
            if checkLongName:
                foundSprint = clsSprint.query.filter_by(S_idSprint = idSprint).all()
               
                if foundSprint != [] or idSprint == 0:
                    foundUser = clsUser.query.filter_by(U_username = username).all()

                    if foundUser != []:
                        foundMiembro = clsSubEquipo.query.filter_by(SEQ_username = username,SEQ_idSprint = idSprint).all()
                        
                        if foundMiembro != []:
                            for i in foundMiembro:
                                db.session.delete(i)
                            db.session.commit()
                            return True


        return False 

    def insertMiembroSubEquipo(self,username,idSprint):
        '''Permite insertar un miembro a un sub equipo'''
        
        checkTypeUsername = type(username) == str
        checkTypeIdSprint = type(idSprint) == int
        
        if checkTypeUsername and checkTypeIdSprint:
            checkLongName     = CONST_MIN_NAME_USERNAME <= len(username) <= CONST_MAX_NAME_USERNAME
            checkLongIdSprint = CONST_MIN_ID <= idSprint           
             
            if checkLongName:
                foundSprint = clsSprint.query.filter_by(S_idSprint = idSprint).all()
               
                if foundSprint != [] or idSprint == 0:
                    foundUser = clsUser.query.filter_by(U_username = username).all()
                   
                    if foundUser != []:
                        foundMiembro = clsSubEquipo.query.filter_by(SEQ_username = username,SEQ_idSprint = idSprint).all()                    
                        
                        if foundMiembro == []:
                            newMiembro = clsSubEquipo(username,idSprint)
                            db.session.add(newMiembro)
                            db.session.commit()
                            return True

        return False


    def actualizar(self,lista,idSprint):
        '''Permite actualizar la tabla sub equipo'''
        
        checkTypeId = type(idSprint) == int
        checkLongId = CONST_MIN_ID <= idSprint 
        
        if checkTypeId and checkLongId:
            
            oldMmebers = clsSubEquipo.query.filter_by(SEQ_idSprint = idSprint).all()
               
            for o in oldMmebers:
                if o.SEQ_username not in lista:
                    self.deleteMiembroSubEquipo(o.SEQ_username,idSprint)

            for new in lista:
                self.insertMiembroSubEquipo(new,idSprint)

            return True

        return False

# Fin Clase Team