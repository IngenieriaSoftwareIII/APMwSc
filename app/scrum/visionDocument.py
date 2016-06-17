# -*- coding: utf-8 -*-.

import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import clsVisionDocument, clsBacklog, db

class visionDocument(object):
    ''' Clase que permite dado un id backlog asociar los datos del documento vision de manera persistente '''

    def insertVisionDocument(self,idBacklog,intro,proposito,moti,estado,alcance,fund,valores):
        '''Inserta los datos del documento vision en la base de datos'''
        foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
        if foundBacklog:
            foundDocument = self.searchVisionDocument(idBacklog)
            if not foundDocument:
                newAccion = clsVisionDocument(idBacklog,intro,proposito,moti,estado,alcance,fund,valores)
                db.session.add(newAccion)
                db.session.commit()
                return True
        return False

    def updateVisionDocument(self,idBacklog,intro,proposito,moti,estado,alcance,fund,valores):
        '''Actualiza los datos del documento vision'''
        foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()
        if foundBacklog:
            foundDocument = self.searchVisionDocument(idBacklog)
            if foundDocument:
                foundDocument.VD_introduccion = intro
                foundDocument.VD_proposito = proposito
                foundDocument.VD_motivacion = moti
                foundDocument.VD_estado = estado
                foundDocument.VD_alcance = alcance
                foundDocument.VD_fundamentacion = fund
                foundDocument.VD_valores = valores
                db.session.commit()
                return True
        return False

    def searchVisionDocument(self,idBacklog):
        '''Dado el id de un producto, devuelve el idVisionDocumento asociado'''
        foundBacklog = clsBacklog.query.filter_by(BL_idBacklog=idBacklog).all()
        if foundBacklog:
            foundVisionDocument = clsVisionDocument.query.filter_by(VD_idBacklog=idBacklog).first()

            return foundVisionDocument

        return []
