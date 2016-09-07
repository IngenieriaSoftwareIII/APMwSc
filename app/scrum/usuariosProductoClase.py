# -*- coding: utf-8 -*-.

import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

# Declaracion de constantes
NOMBREUSR_TAM_MAX = 16
NOMBREUSR_TAM_MIN = 1
ID_MIN  = 1


class usuariosProducto(object):
    '''Clase que permite manejar los usuarios asociados a un producto de manera persitente'''

    def insertarUsuarioAsociadoAProducto(self, nombreUsuario, idProducto):
        '''Permite asociar un usuario a un producto'''

        # Verificamos que los tipos de los datos son correctos
        verificarUsuario  = type(nombreUsuario) == str
        verificarProducto = type(idProducto) == int

        if verificarUsuario and verificarProducto:

            # Verificamos las longitudes de los datos
            verificarUsuario  = NOMBREUSR_TAM_MIN <= len(nombreUsuario) <= NOMBREUSR_TAM_MAX 
            verificarProducto = idProducto >= ID_MIN

            if verificarUsuario and verificarProducto:
                # Verificamos que el usuario sea valido
                usuarioEncontrado = clsUsuario.query.filter_by(U_nombreUsuario = nombreUsuario).all()

                # Verificamos que el producto sea valido
                productoEncontrado = clsBacklog.query.filter_by(BL_idBacklog = idProducto).all()

                if usuarioEncontrado != [] and productoEncontrado != []:
                    nuevoObjeto = clsUsuariosProducto(nombreUsuario,idProducto)
                    db.session.add(nuevoObjeto)
                    db.session.commit()
                    return True
        return False



    def obtenerIdProductosAsociadosAUsuario(self, nombreUsuario):
        '''Permite obtener los ids de los productos asociados a un usuario registrado'''

        listaIds = []

        # Verificamos que los tipos de los datos son correctos
        verificarUsuario = type(nombreUsuario) == str

        if verificarUsuario:

            # Verificamos las longitudes de los datos
            verificarUsuario = NOMBREUSR_TAM_MIN <= len(nombreUsuario) <= NOMBREUSR_TAM_MAX

            if verificarUsuario:
                
                # Buscamos los productos asociados al usuario
                productosEncontrados = clsUsuariosProducto.query.filter_by(UP_nombreUsuario = nombreUsuario).all()

                if productosEncontrados != []:

                    for obj in productosEncontrados:
                        listaIds.append(obj.UP_idProducto)

        return listaIds



    def obtenerNombresUsuariosAsociadosAProducto(self, idProducto):
        '''Permite obtener el nombre de usuario al cual esta asociado un producto dado'''

        listaNombresUsuario = []

        # Verificamos que los tipos de los datos son correctos
        verificarProducto = type(idProducto) == int

        if verificarProducto:

            # Verificamos que sea positivo
            verificarProducto = idProducto >= ID_MIN

            if verificarProducto:

                usuariosEncontrados = clsUsuariosProducto.query.filter_by(UP_idProducto = idProducto).all()

                if usuariosEncontrados != []:

                    for obj in usuariosEncontrados:
                        listaNombresUsuario.append(obj.UP_nombreUsuario)

        return listaNombresUsuario



    def borrarAsociacionEntreProductoYUsuario(self, nombreUsuario, idProducto):
        '''Permite eliminar una asociacion entre un producto y un usuario'''

        # Verificamos que los tipos de los datos son correctos
        verificarUsuario  = type(nombreUsuario) == str
        verificarProducto = type(idProducto) == int

        if verificarUsuario and verificarProducto:

            # Verificamos las longitudes de los datos
            verificarUsuario  = NOMBREUSR_TAM_MIN <= len(nombreUsuario) <= NOMBREUSR_TAM_MAX 
            verificarProducto = idProducto >= ID_MIN

            if verificarUsuario and verificarProducto:

                # Obtenemos la tupla 
                oUsuarioProducto = clsUsuariosProducto.query.filter_by(UP_nombreUsuario = nombreUsuario, 
                                                                       UP_idProducto = idProducto).all()

                if uoUsuarioProducto != []:

                    for obj in oUsuarioProducto:
                        db.session.delete(obj)
                    db.session.commit()
                    return True
        return False


# Fin Clase usersBacklog