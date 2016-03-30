# -*- coding: utf-8 -*-.

import sys
import datetime

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *
from backLog import *

# Declaracion de constantes.
CONST_MAX_NAME = 50
CONST_MIN_NAME = 1


class archivos(object):
    '''Clase que permite manejar los archivos'''

    def getAllArchives(self):
        result = clsArchivos.query.all()
        return result

    def findName(self, name):

        checkTypeName = type(name) == str
        if checkTypeName:
            checkLongName = CONST_MIN_NAME <= len(name) <= CONST_MAX_NAME

            if checkLongName:
                oArchivos = clsArchivos.query.filter_by(AR_nameArch=name).all()
                return oArchivos
        return []

    def findIdArchives(self, idArchive):

        checkTypeId = type(idArchive) == int
        found = None

        if checkTypeId:
            found = clsArchivos.query.filter_by(
                AR_idArchivos=idArchive).first()
        return found

    def insertArchive(self, name, url, dateAr, idbacklog, etiqueta):
        oBackLog = backlog()
        checkTypeName = type(name) == str
        checkTypeUrl = type(url) == str
        checkTypeBacklog = type(idbacklog) == int
        checkTypeEtiqueta = type(etiqueta) == str

        if checkTypeName and checkTypeUrl and checkTypeBacklog and checkTypeEtiqueta:

            checkIdBacklog = clsBacklog.query.filter_by(
                BL_idBacklog=idbacklog).all()

            x = oBackLog.searchFile(idbacklog, name)

            if x:
                print('Archivo repetido')

            if not x and checkIdBacklog != []:

                newArch = clsArchivos(name, url, dateAr, idbacklog, etiqueta)
                newArch.url = url

                db.session.add(newArch)
                db.session.commit()

                return True

        return False

    def deleteArchive(self, idArchivos):

        found = self.findIdArchives(idArchivos)

        if found != []:

            db.session.delete(found)
            db.session.commit()
            return True

        return False


# Fin Clase Archivos
