# -*- coding: utf-8 -*-.

import sys
import datetime
import json

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

from objective   import *
from role        import *
from accions     import *
from sprintClass import *
import userHistory
import archivos

# Declaracion de constantes.
DESC_TAM_MAX   = 140
DESC_TAM_MIN   = 1
NOMBRE_TAM_MAX = 50
NOMBRE_TAM_MIN = 1
ID_MIN = 1

# Estructuras relacionadas a las escalas de los productos.
scale_type  = [1, 2]
scale_alta  = [i for i in range(1, 7)]
scale_media = [i for i in range(7, 13)]
scale_baja  = [i for i in range(13, 21)]
scale_type1 = [i for i in range(0, 4)]
scale       = {0: 0, 1: 1, 2: 10, 3: 20}

class backlog(object):
    '''Clase que permite (completar)'''

    def obtenerTodosLosProductos(self):
        '''Permite obtener todos los productos de la tabla'''

        productos = clsBacklog.query.all()
        return productos



    def buscarProductosPorNombre(self, nombre):
        '''Permite buscar los productos con el nombre dado'''

        # Verificamos que el tipo de los datos es correcto
        verificarNombre = type(nombre) == str

        if verificarNombre:
            # Verificamos que la longitud de los datos sea correcta
            verificarNombre = NOMBRE_TAM_MIN <= len(nombre) <= NOMBRE_TAM_MAX

            if verificarNombre:
                oProducto = clsBacklog.query.filter_by(BL_name = nombre).all()
                return oProducto
        return []



    def buscarProductoPorId(self, idProducto):
        '''Permite buscar un producto por su id'''

        verificarProducto = type(idProducto) == int
        encontrado = None

        if verificarProducto:
            encontrado = clsBacklog.query.filter_by(BL_idBacklog = idProducto).first()
        return encontrado



    def insertarProducto(self, nombre, descripcion, escala):
        '''Permite insertar un producto'''

        # Verificamos que el tipo de los datos es correcto
        verificarNombre = type(nombre)      == str
        verificarDesc   = type(descripcion) == str
        verificarEscala = type(escala)      == int

        if verificarNombre and verificarDesc and verificarEscala:

            # Verificamos que la longitud de los datos sea correcta
            verificarNombre = NOMBRE_TAM_MIN <= len(nombre)      <= NOMBRE_TAM_MAX
            verificarDesc   = DESC_TAM_MIN   <= len(descripcion) <= DESC_TAM_MAX

            # Verificamos que la escala es correcta
            verificarEscala = escala in scale_type

            if verificarNombre and verificarDesc and verificarEscala:

                nuevoProducto = clsBacklog(nombre, descripcion, escala)
                db.session.add(nuevoProducto)
                db.session.commit()
                return True
        return False



    def modifyBacklog(self, name, new_name, new_description, new_scale,new_status):
        '''Permite actualizar los valores de un producto'''

        checkTypeName = type(name) == str
        checkTypeNewName = type(new_name) == str
        checkTypeDescription = type(new_description) == str
        checkTypeScale = type(new_scale) == int
        checkTypeStatus = isinstance(new_status, int)

        if checkTypeName and checkTypeNewName and checkTypeDescription and checkTypeScale and checkTypeStatus:
            checkLongName = NOMBRE_TAM_MIN <= len(name) <= NOMBRE_TAM_MAX
            checkLongNewName = NOMBRE_TAM_MIN <= len(
                new_name) <= NOMBRE_TAM_MAX
            checkLongNewDesc = DESC_TAM_MIN <= len(
                new_description) <= DESC_TAM_MAX
            checkNewScale = new_scale in scale_type
            checkNewStatus = new_status in (1,2,3)

            if checkLongName and checkLongNewName and checkLongNewDesc and checkNewScale and checkNewStatus:
                foundName = self.findName(name)
                foundNewName = self.findName(new_name)

                if foundName != [] and (foundNewName == [] or new_name == name):
                    idBacklog = foundName[0].BL_idBacklog
                    foundUserHistory = clsUserHistory.query.filter_by(
                        UH_idBacklog=idBacklog).all()
                    currentScale = foundName[0].BL_scaleType
                    updateHist = True

                    if currentScale == new_scale:
                        updateHist = True
                    else:
                        if foundUserHistory == []:
                            updateHist = True
                        else:
                            for hist in foundUserHistory:
                                updateHist = self.updateScaleType(
                                    hist.UH_idUserHistory, new_scale)
                                if updateHist == False:
                                    break
                    if updateHist:
                        newBacklog = clsBacklog.query.filter_by(
                            BL_name=name).first()
                        newBacklog.BL_name = new_name
                        newBacklog.BL_description = new_description
                        newBacklog.BL_scaleType = new_scale
                        newBacklog.BL_statusType = new_status
                        db.session.commit()
                        return True
        return False



    def deleteProduct(self, name):
        '''Permite eliminar un producto de la tabla'''

        checkTypeName = type(name) == str

        if checkTypeName:
            checkLongName = NOMBRE_TAM_MIN <= len(name) <= NOMBRE_TAM_MAX
            foundName = self.findName(name)

            if foundName != []:
                tupla = clsBacklog.query.filter_by(BL_name=name).first()
                db.session.delete(tupla)
                db.session.commit()
                return True
        return False



    def scaleType(self, idBacklog):
        '''Permite obtener el tipo de escala seleccionado para un producto'''

        checkTypeId = type(idBacklog) == int

        if checkTypeId:
            found = clsBacklog.query.filter_by(BL_idBacklog=idBacklog).all()

            if found != []:
                scale = found[0].BL_scaleType
                return scale
        return ([])



    def actorsAsociatedToProduct(self, idBacklog):
        ''' Permite obtener una lista de los Actores asociados a una pila de Producto'''

        checkTypeId = type(idBacklog) == int

        if checkTypeId:
            found = clsActor.query.filter_by(A_idBacklog=idBacklog).all()
            return found
        return([])



    def accionsAsociatedToProduct(self, idBacklog):
        ''' Permite obtener una lista de las acciones asociados a una pila de Producto'''

        checkTypeId = type(idBacklog) == int

        if checkTypeId:
            found = clsAccion.query.filter_by(AC_idBacklog=idBacklog).all()
            return found
        return([])



    def filesAssociatedToProduct(self, idBacklog):
        ''' Permite obtener una lista de los archivos asociados a una pila de Producto'''

        checkTypeId = type(idBacklog) == int

        if checkTypeId:
            found = clsArchivos.query.filter_by(
                AR_idBacklog=idBacklog).all()
            return found
        return([])



    def searchFile(self, idBacklog, nameArchive):
        ''' Permite revisar si hay un archivo en el mismo backlog con el mismo nombre'''

        checkTypeId = type(idBacklog) == int
        checkTypeName = type(nameArchive) == str

        if checkTypeId and checkTypeName:

            if checkTypeId:
                found = clsArchivos.query.filter_by(
                    AR_idBacklog=idBacklog, AR_nameArch=nameArchive).all()

                if found == []:
                    return False

                return True

        return False



    def objectivesAsociatedToProduct(self, idBacklog):
        ''' Permite obtener una lista de los Objetivos asociados a una pila de Producto'''

        checkTypeId = type(idBacklog) == int

        if checkTypeId:
            found = clsObjective.query.filter_by(O_idBacklog=idBacklog).all()
            return found
        return([])



    def sprintsAsociatedToProduct(self,idBacklog):
        ''' Permite obtener una lista de los Sprints asociados a una pila de Producto'''

        checkTypeId = type(idBacklog) == int

        if checkTypeId:
            found = clsSprint.query.filter_by(S_idBacklog = idBacklog).all()
            return found
        return([])



    def userHistoryAsociatedToProduct(self, idBacklog):
        ''' Permite obtener una lista de los historias de usuario asociadas a una pila de Producto'''

        checkTypeId = type(idBacklog) == int

        if checkTypeId:
            found = clsUserHistory.query.filter_by(
                UH_idBacklog=idBacklog).all()
            return found
        return([])



    def updateScaleType(self, idUserHistory, new_scale):
        """Permite actualizar el valor actual de la escala de una historia de usuario"""

        checkTypeId = type(idUserHistory) == int
        checkTypeScale = type(new_scale) == int and new_scale in scale

        if checkTypeId and checkTypeScale:
            foundUH = clsUserHistory.query.filter_by(
                UH_idUserHistory=idUserHistory).first()

            if foundUH != None:

                if new_scale == 1:

                    if foundUH.UH_scale in scale_alta:
                        foundUH.UH_scale = 1
                    elif foundUH.UH_scale in scale_media:
                        foundUH.UH_scale = 2
                    elif foundUH.UH_scale in scale_baja:
                        foundUH.UH_scale = 3
                    db.session.commit()
                    return True

                elif new_scale == 2:

                    if foundUH.UH_scale in scale_type1:
                        foundUH.UH_scale = scale[foundUH.UH_scale]
                        db.session.commit()
                        return True
        return False



    def getProductBackup(self, idBacklog):
        '''Permite crear un backup en JSON del producto'''

        checkTypeId = type(idBacklog) == int
        product = None
        jsonProduct = {}

        oBacklog = backlog()

        if checkTypeId:
            product = clsBacklog.query.filter_by(BL_idBacklog=idBacklog).first()

        if product:
            jsonProduct = {
                "id": product.BL_idBacklog,
                "nombre": product.BL_name,
                "decripcion": product.BL_description,
                "escala": product.BL_scaleType,
                "estado": product.BL_statusType,
            }

            objectives = oBacklog.objectivesAsociatedToProduct(idBacklog)
            actors = oBacklog.actorsAsociatedToProduct(idBacklog)
            actions = oBacklog.accionsAsociatedToProduct(idBacklog)
            carreras = oBacklog.sprintsAsociatedToProduct(idBacklog)
            historias = oBacklog.userHistoryAsociatedToProduct(idBacklog)
            files = oBacklog.filesAssociatedToProduct(idBacklog)

            oObjective = objective()
            oActor = role()
            oAction = accions()
            oSprint = sprints()
            oUserHistory = userHistory.userHistory()
            oFiles = archivos.archivos()

            jsonProduct['objetivos'] = [oObjective.toJson(objective.O_idObjective) for objective in objectives]
            jsonProduct['actores'] = [oActor.toJson(actor.A_idActor) for actor in actors]
            jsonProduct['acciones'] = [oAction.toJson(action.AC_idAccion) for action in actions]
            jsonProduct['sprints'] = [oSprint.toJson(sprint.S_idSprint, idBacklog) for sprint in carreras]
            jsonProduct['historias'] = [oUserHistory.toJson(history.UH_idUserHistory) for history in historias]
            jsonProduct['archivos'] = [oFiles.toJson(archivo.AR_idArchivos) for archivo in files]

        return json.dumps(jsonProduct)


# Fin Clase Backlog