# -*- coding: utf-8 -*-.

import sys
import datetime
import time

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *
import backLog

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
        oBackLog = backLog.backlog()
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

    def toJson(self, idArchive):

        checkTypeId = type(idArchive) == int
        found = None
        jsonFile = {}

        if checkTypeId:
            found = clsArchivos.query.filter_by(AR_idArchivos=idArchive).first()

        if found:
            jsonFile = {
                "id": found.AR_idArchivos,
                "nombre": found.AR_nameArch,
                "url": found.AR_url,
                "fecha": time.mktime(found.AR_dateArch.timetuple()),
                "idBacklog": found.AR_idBacklog,
                "etiqueta": found.AR_etiqueta
            }

        return jsonFile

# Fin Clase Archivos
