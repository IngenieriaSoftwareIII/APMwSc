# -*- coding: utf-8 -*-. 

import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

# Declaracion de constantes.
NOMBREUSR_TAM_MAX = 16
NOMBRE_TAM_MAX    = 50
CORREO_TAM_MAX    = 30
CLAVE_TAM_MAX     = 200
CLAVE_TAM_MIN     = 1
TAM_MIN           = 1


# Id de los roles permitidos al momento de registrarse
idRoles = [1,2,3] 


class usuario(object):
    '''Clase que permite manejar usuarios de manera persistente'''
    

    def obtenerTodosLosUsuarios(self):
        '''Permite obtener todos los usuarios de la tabla'''
        
        usuarios = clsUsuario.query.all()
        return usuarios



    def buscarUsuario(self, nombreUsuario):
        '''Permite buscar un usuario por su nombre de usuario'''
        
        verificarNombreUsuario = type(nombreUsuario) == str

        if not verificarNombreUsuario:
            return []
        else:
            tamano_nombreUsuario = len(nombreUsuario)

            if (tamano_nombreUsuario > NOMBREUSR_TAM_MAX or tamano_nombreUsuario < TAM_MIN):
                return []
            else:
                oUsuario = clsUsuario.query.filter_by(U_nombreUsuario = nombreUsuario).all()
                return oUsuario


 
    def insertarUsuario(self, nombre, nombreUsuario, clave, correo, rol):
        '''Permite insertar un usuario en la tabla de usuarios registrados'''
        
        # Verificamos que los tipos de los parametros son correctos
        verificarNombre        = type(nombre)        == str
        verificarNombreUsuario = type(nombreUsuario) == str
        verificarClave         = type(clave)         == str
        verificarCorreo        = type(correo)        == str
        verificarRol           = type(rol)           == int
        
        if verificarNombre and verificarNombreUsuario and verificarClave and verificarCorreo and verificarRol:
            # Verificamos las longitudes de los parametros
            verificarNombreUsuario = TAM_MIN       <= len(nombreUsuario) <= NOMBREUSR_TAM_MAX
            verificarNombre        = TAM_MIN       <= len(nombre)        <= NOMBRE_TAM_MAX
            verificarClave         = CLAVE_TAM_MIN <= len(clave)         <= CLAVE_TAM_MAX
            verificarCorreo        = TAM_MIN       <= len(correo)        <= CORREO_TAM_MAX

            if verificarNombreUsuario and verificarNombre and verificarClave and verificarCorreo:
                # Verificamos si el nombre de usuario ya existe
                oUsuario     = clsUsuario.query.filter_by(U_nombreUsuario = nombreUsuario).all()

                # Verificamos si el id del rol es valido
                verificarRol = rol in idRoles

                if oUsuario == [] and verificarRol:

                    nuevoUsuario = clsUsuario(nombre,nombreUsuario,clave,correo,rol)
                    db.session.add(nuevoUsuario)
                    db.session.commit()
                    return True
        return False
        


    def actualizarUsuario(self, nombreUsuario, nuevoNombre, nuevaClave, nuevoCorreo, nuevoRol):   
        '''Permite actualizar los datos de un usuario ya registrado en la aplicacion'''  
        
        # Verificamos que los tipos de los parametros son correctos
        verificarNombreUsuario = type(nombreUsuario) == str  
        verificarNuevoNombre   = type(nuevoNombre)   == str
        verificarNuevaClave    = type(nuevaClave)    == str
        verificarNuevoCorreo   = type(nuevoCorreo)   == str
        verificarNuevoRol      = type(nuevoRol)      == int

        if verificarNombreUsuario and verificarNuevoNombre and verificarNuevaClave and verificarNuevoCorreo and verificarNuevoRol:

            # Verificamos las longitudes de los parametros
            verificarNuevoNombre = TAM_MIN <= len(nuevoNombre) <= NOMBRE_TAM_MAX
            verificarNuevaClave  = TAM_MIN <= len(nuevaClave)  <=  CLAVE_TAM_MAX
            verificarNuevoCorreo = TAM_MIN <= len(nuevoCorreo) <= CORREO_TAM_MAX
 
            if verificarNuevoNombre and verificarNuevaClave and  verificarNuevoCorreo:
                # Verificamos si el nombre de usuario existe
                oUsuario = clsUsuario.query.filter_by(U_nombreUsuario = nombreUsuario).all()  

                # Verificamos si el id del rol es valido     
                verificarRol = nuevoRol in idRoles        

                if oUsuario != []  and verificarRol:

                    oUsuario[0].U_nombreCompleto = nuevoNombre
                    oUsuario[0].U_clave          = nuevaClave
                    oUsuario[0].U_correo         = nuevoCorreo
                    oUsuario[0].U_idRol          = nuevoRol
                    db.session.commit()
                    return True
        return False    
     

     
    def borrarUsuario(self, nombreUsuario):
        '''Permite eliminar un usuario de la tabla de usuarios registrados'''
        
        # Verificamos que los tipos de los parametros son correctos
        verificarNombreUsuario = type(nombreUsuario) == str  
        
        if verificarNombreUsuario:

            # Verificamos las longitudes de los parametros
            verificarNombreUsuario = TAM_MIN <= len(nombreUsuario) <= NOMBREUSR_TAM_MAX

            if verificarNombreUsuario: 

                # Verificamos si el nombre de usuario existe
                oUsuario = clsUsuario.query.filter_by(U_nombreUsuario = nombreUsuario).all()

                if oUsuario != []: 

                    for i in oUsuario:    
                        db.session.delete(i)
                    db.session.commit()
                    return True
        return False


 
    def estaNombreUsuario(self,nombreUsuario):
        '''Permite saber si un usuario esta registrado en la aplicacion'''
        
        oUsuario = clsUsuario.query.filter_by(U_nombreUsuario = nombreUsuario).all()
        return oUsuario != []



    def obtenerUsuariosPorIdRol(self, idRol):
        '''Permite obtener los usuarios que estan asignados a un rol.
           Recordar que los roles son 1: Product Owner, 2: Scrum Master, 3: Team Member'''

        oUsuario = clsUsuario.query.filter_by(U_idRol = idRol).all()
        return oUsuario
        
# Fin Clase user