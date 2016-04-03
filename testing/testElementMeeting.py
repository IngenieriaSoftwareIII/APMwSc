# -*- coding: utf-8 -*-.

import sys
import unittest

# Ruta que permite utilizar el módulo elementMeetingClass.py
sys.path.append('../app/scrum')

from sprintClass import *
from meetingClass import *
from elementMeetingClass import *
from role import *
from datetime import *

# Declaracion de constantes
TODAY = datetime.utcnow()
TOMORROW = TODAY + timedelta(days=1)
STATES = ["Terminada", "En ejecución", "No iniciada"]

class TestElementMeeting(unittest.TestCase):

    #############################################
    #         Pruebas para emptyTable           #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testEmptyTable(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        aMeeting.emptyTable()
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #Probar que si la tabla esta vacia, se devuelve TRUE
    #def testEmptyTableTrue(self):
    #    aElement = elementMeeting()
    #    result = aElement.emptyTable()
    #    self.assertTrue(result)

    #Probar que si la tabla no esta vacia, se devuelve FALSE
    def testEmptyTableFalse(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        result = aElement.emptyTable()
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #        Pruebas para insertElement      #
    #############################################

     # Probar que la funcionalidad se ejecuta

    def testInsertElement(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting

        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Probar que inserta con exito
    def testInsertElementTrue(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        result = aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        self.assertTrue(result)


        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Probar que no inserta element si el meeting es invalido
    def testInsertElementFalseInvalidMeeting(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        result = aElement.insertElement('challenges', 'planned', 'done', -23, 'user1')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Probar que no inserta element si los tipos de los parametros son invalidos
    def testInsertElementFalseInvalidTypes(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        result = aElement.insertElement(80085 , [], 1.02 , idAMeeting, 2)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #       Pruebas para updateElement          #
    #############################################

     # Probar que la funcionalidad se ejecuta

    def testUpdateElement(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        aElement.updateElement(elementID, 'newChallenges', 'newPlanned', 'newDone', idAMeeting, 'user1')

        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Probar que actualiza con exito
    def testUpdateElementTrue(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        result = aElement.updateElement(elementID, 'newChallenges', 'newPlanned', 'newDone', idAMeeting, 'user1')
        self.assertTrue(result)


        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Probar que no inserta element si el meeting es invalido
    def testUpdateElementFalseInvalidMeeting(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        result = aElement.updateElement(elementID, 'newChallenges', 'newPlanned', 'newDone', -23, 'user1')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Probar que no actualiza element si los tipos de los parametros son invalidos
    def testUpdateElementFalseInvalidTypes(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        result = aElement.updateElement(elementID, 80085 , [], 1.02 , idAMeeting, 'user1')
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')


    #############################################
    #       Pruebas para deleteElement          #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testDeleteElement(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)#funcionalidad se ejecuta
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #Probar que elimina con exito

    def testDeleteElementTrue(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        # Eliminamos los datos insertados.
        result = aElement.deleteElement(elementID, idAMeeting)
        self.assertTrue(result)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #Probar que no elimina si el element id no es vlido
    def testDeleteElementFalseInvalidElementID(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        # Eliminamos los datos insertados.
        result = aElement.deleteElement(-23, idAMeeting)
        self.assertFalse(result)
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #Probar que no elimina si el meeting id no es vlido
    def testDeleteElementFalseInvalidIdMeeting(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        # Eliminamos los datos insertados.
        result = aElement.deleteElement(elementMeeting, -23)
        self.assertFalse(result)
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Probar que no elimina element si los tipos de los parametros son invalidos
    def testDeleteElementFalseInvalidTypes(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        # Eliminamos los datos insertados.
        result = aElement.deleteElement('elementMeeting', [])
        self.assertFalse(result)
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #       Pruebas para getElements       #
    #############################################

        # Probar que la funcionalidad se ejecuta
    def testGetElements(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        aElement.getElements(idAMeeting)
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #def testGetElementsEmpty(self):
    #    # Creamos el backlog
    #    self.aBacklog  = backlog()
    #    self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
    #    findId         = self.aBacklog.findName('Bxtyllz')
    #    self.idBacklog = findId[0].BL_idBacklog
    #    # Creamos el sprint
    #    aSprint      = sprints()
    #    aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
    #    findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
    #    idASprint = findIdSprint[0].S_idSprint
    #    # Creamos el meeting
    #    aMeeting = meeting ()
    #    date = '2015-02-02'
    #    tipo = 'Presencial'
    #    aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
    #    findIdMeeting = aMeeting.searchMeeting(date, idASprint)
    #    idAMeeting = findIdMeeting[0].SM_idSprintMeeting
    #    # Creamos el elemento
    #    aElement = elementMeeting()
    #    result = aElement.getElements(idAMeeting)
    #    self.assertTrue(result == [])
    #    # Eliminamos los datos insertados.
    #    aMeeting.deleteMeeting(date,idASprint)
    #    aSprint.deleteSprint(1,self.idBacklog)
    #    self.aBacklog.deleteProduct('Bxtyllz')

    def testGetElementsNotEmpty(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        result = aElement.getElements(idAMeeting)
        self.assertTrue(result != [])
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    def testGetElementsEmptyInvalidMeeting(self):
        # Creamos el element
        aElement = elementMeeting()
        result = aElement.getElements(-23)
        self.assertTrue(result == [])

    #############################################
    #  Pruebas para getElementsByUserAndMeeting #
    #############################################

        # Probar que la funcionalidad se ejecuta
    def testGetElementsByUserAndMeeting(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #def testGetElementsByUserAndMeetingEmpty(self):
    #    # Creamos el backlog
    #    self.aBacklog  = backlog()
    #    self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
    #    findId         = self.aBacklog.findName('Bxtyllz')
    #    self.idBacklog = findId[0].BL_idBacklog
    #    # Creamos el sprint
    #    aSprint      = sprints()
    #    aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
    #    findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
    #    idASprint = findIdSprint[0].S_idSprint
    #    # Creamos el meeting
    #    aMeeting = meeting ()
    #    date = '2015-02-02'
    #    tipo = 'Presencial'
    #    aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
    #    findIdMeeting = aMeeting.searchMeeting(date, idASprint)
    #    idAMeeting = findIdMeeting[0].SM_idSprintMeeting
    #    # Creamos el elemento
    #    aElement = elementMeeting()
    #    result = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
    #    self.assertTrue(result == [])
    #    # Eliminamos los datos insertados.
    #    aMeeting.deleteMeeting(date,idASprint)
    #    aSprint.deleteSprint(1,self.idBacklog)
    #    self.aBacklog.deleteProduct('Bxtyllz')

    def testGetElementsByUserAndMeetingNotEmpty(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        result = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        self.assertTrue(result != [])
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    def testGetElementsByUserAndMeetingEmptyInvalidMeeting(self):
        # Creamos el backlog
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
        idASprint = findIdSprint[0].S_idSprint
        # Creamos el meeting
        aMeeting = meeting ()
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        findIdMeeting = aMeeting.searchMeeting(date, idASprint)
        idAMeeting = findIdMeeting[0].SM_idSprintMeeting
        # Creamos el elemento
        aElement = elementMeeting()
        aElement.insertElement('challenges', 'planned', 'done', idAMeeting, 'user1')
        foundElementId = aElement.getElementsByUserAndMeeting('user1',idAMeeting)
        elementID = foundElementId[0].EM_idElementMeeting
        result = aElement.getElementsByUserAndMeeting('user1',-23)
        self.assertTrue(result == [])
        # Eliminamos los datos insertados.
        aElement.deleteElement(elementID, idAMeeting)
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

if __name__ == '__main__':
    unittest.main()