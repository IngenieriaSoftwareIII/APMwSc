# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

# Declaracion de constantes.
CONST_MAX_USER     = 16
CONST_MAX_FULLNAME = 50
CONST_MAX_PASSWORD = 200
CONST_MAX_EMAIL    = 30
CONST_MIN_LONG     = 1
CONST_MIN_PASSWORD = 1


class user(object):
    '''Clase que permite manejar usuarios de manera persistente'''
    
    def getAllUsers(self):
        '''Permite obtener todos los productos de la tabla'''
        
        result = clsUser.query.all()
        return result

    def searchUser(self,username):
        '''Permite buscar un usuario por su nombre'''
        
        if (type(username) != str):
            return []
        else:
            long_username = len(username)
            if (long_username >CONST_MAX_USER or long_username < CONST_MIN_LONG):
                return []
            else:
                auser = clsUser.query.filter_by(U_username = username).all()
                return auser
 
    def insertUser(self, fullname, username, password, email, idActor):
        '''Permite insertar un usuario en la tabla'''
        
        checkName     = type(fullname) == str
        checkUserName = type(username) == str
        checkPassword = type(password) == str
        checkEmail    = type(email) == str
        checkActor    = type(idActor) == int
        
        if checkName and checkUserName and checkPassword and checkEmail and checkActor:
            checkLongUser     = CONST_MIN_LONG <= len(username) <= CONST_MAX_USER
            checkLongFullname = CONST_MIN_LONG <= len(fullname) <= CONST_MAX_FULLNAME
            checkLongPassword = CONST_MIN_PASSWORD <= len(password) <=  CONST_MAX_PASSWORD
            checkLongEmail    = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL

            if checkLongUser and checkLongFullname and checkLongPassword and checkLongEmail:
                auser = clsUser.query.filter_by(U_username = username).all()
                checkIdActor = clsActor.query.filter_by(A_idActor = idActor).all()

                if auser == [] and checkIdActor != []:
                    newUser = clsUser(fullname,username,password,email,idActor)
                    db.session.add(newUser)
                    db.session.commit()
                    return True
        return False
        

    def updateUser(self, username, new_fullname, new_password, new_email, new_idActor):   
        '''Permite actualizar los datos de un usuario'''  
        
        checkUsername    = type(username) == str  
        checkNewFullname = type(new_fullname) == str
        checkNewPassword = type(new_password) == str
        checkNewEmail    = type(new_email) == str
        checkNewActor    = type(new_idActor) == int

        if checkUsername and checkNewFullname and checkNewPassword and checkNewEmail and checkNewActor:
            checkLongNewFullname = CONST_MIN_LONG <= len(new_fullname) <= CONST_MAX_FULLNAME
            checkLongNewPassword = CONST_MIN_LONG <= len(new_password) <=  CONST_MAX_PASSWORD
            checkLongNewEmail    = CONST_MIN_LONG <= len(new_email) <= CONST_MAX_EMAIL
 
            if checkLongNewFullname and checkLongNewPassword and  checkLongNewEmail:
                auser    = clsUser.query.filter_by(U_username = username).all()        
                checkIdActor = clsActor.query.filter_by(A_idActor = new_idActor).all()        

                if auser != []  and checkIdActor != []:
                    checkUauser[0].U_fullname = new_fullname
                    auser[0].U_password = new_password
                    auser[0].U_email    = new_email
                    auser[0].U_idActor  = new_idActor
                    db.session.commit()
                    return True
        return False    
     
     
    def deleteUser(self,username):
        '''Permite eliminar un usuario de la tabla'''
        
        checkUsername = type(username) == str  
        
        if checkUsername:
            checkLongUser = CONST_MIN_LONG <= len(username) <= CONST_MAX_USER
            if checkLongUser: 
                auser = clsUser.query.filter_by(U_username = username).all()
                if auser != []: 
                    for i in auser:    
                        db.session.delete(i)
                    db.session.commit()
                    return True
        return False


    def findEmail(self,email):
        '''Permite saber si un email esta en la base de datos'''
        
        aemail = clsUser.query.filter_by(U_email=email).all()
        return aemail != []
        
 
    def isFound(self,username):
        '''Permite saber si un usuario esta en la base de datos'''
        
        auser = clsUser.query.filter_by(U_username = username).all()
        return auser != []
        
# Fin Clase user