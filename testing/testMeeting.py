# -*- coding: utf-8 -*-.

import sys
import unittest

# Ruta que permite utilizar el módulo Team.py
sys.path.append('../app/scrum')

from sprintClass import *
from meetingClass import *
from role import *
from datetime import *

# Declaracion de constantes
TODAY = datetime.utcnow()
TOMORROW = TODAY + timedelta(days=1)
STATES = ["Terminada", "En ejecución", "No iniciada"]

class TestMeeting(unittest.TestCase):

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
        aMeeting.emptyTable()
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    # Pruebas de tabla vacia
#    def testEmptyTableTrue(self):
#        aMeeting = meeting()
#        self.assertTrue(aMeeting.emptyTable())

    # Prueba de tabla no vacia
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
        self.assertFalse(aMeeting.emptyTable())
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #        Pruebas para searchMeeting         #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testSearchMeeting(self):
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
        date = '2015-02-02'
        aMeeting = meeting()
        tipo = 'Presencial'
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1',tipo, idASprint)
        aMeeting.searchMeeting(date,idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    def testSearchMeetingTrue(self):
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
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1',tipo, idASprint)
        result = aMeeting.searchMeeting(date,idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

#    def testSearchMeetingFalseInvalidDate(self):
#        # Creamos el backlog
#        self.aBacklog  = backlog()
#        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
#        findId         = self.aBacklog.findName('Bxtyllz')
#        self.idBacklog = findId[0].BL_idBacklog
#        # Creamos el sprint
#        aSprint      = sprints()
#        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
#        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
#        idASprint = findIdSprint[0].S_idSprint
#        # Creamos el meeting
#        date = datetime.date(2015,8,9)
#        date1 = datetime.date(2015,8,10)
#        aMeeting = meeting()
#        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', idASprint)
#        result = aMeeting.searchMeeting(date1,idASprint)
#        self.assertFalse(result)
#        # Eliminamos los datos insertados.
#        self.aBacklog.deleteProduct('Bxtyllz')
#        aSprint.deleteSprint(1,self.idBacklog)
#        aMeeting.deleteMeeting(date,idASprint)

    def testSearchMeetingFalseInvalidSprint(self):
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
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1',tipo, idASprint)
        result = aMeeting.searchMeeting(date,-1)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        self.aBacklog.deleteProduct('Bxtyllz')
        aSprint.deleteSprint(1,self.idBacklog)
        self.assertFalse(result)

    #############################################
    #        Pruebas para insertMeeting         #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testInsertMeeting(self):
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
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    def testInsertMeetingTrue(self):
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
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting = meeting()
        result = aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

#    def testInsertMeetingFalseInvalidDate(self):
#        # Creamos el backlog
#        self.aBacklog  = backlog()
#        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
#        findId         = self.aBacklog.findName('Bxtyllz')
#        self.idBacklog = findId[0].BL_idBacklog
#        # Creamos el sprint
#        aSprint      = sprints()
#        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
#        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
#        idASprint = findIdSprint[0].S_idSprint
#        # Creamos el meeting
#        date = datetime.date(2020,8,9)
#        aMeeting = meeting()
#        result = aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', idASprint)
#        self.assertFalse(result)
#        # Eliminamos los datos insertados.
#        self.aBacklog.deleteProduct('Bxtyllz')
#        aSprint.deleteSprint(1,self.idBacklog)
#        aMeeting.deleteMeeting(date,idASprint)

    def testInsertMeetingFalseInvalidSprint(self):
        # Creamos el meeting
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting = meeting()
        result = aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', tipo,-1)
        self.assertFalse(result)

    def testInsertMeetingFalseInvalidTypes(self):
        # Creamos el meeting
        date = '2015-02-02'
        tipo = 'Presencial'
        aMeeting = meeting()
        result = aMeeting.insertMeeting(date, 0, 2.5, [],tipo, 1)
        self.assertFalse(result)

    #############################################
    #       Pruebas para updateMeeting          #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testUpdateMeetings(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        date1 = '02/03/2016'
        date2= '2016-03-02'
        tipo1 = 'Presencial'
        tipo2 = 'no presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo1, idASprint)
        aMeeting.updateMeeting(date, date1, 'A1', 'S1', 'C1',tipo2, idASprint,1)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date2,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    def testUpdateMeetingsTrue(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        date1 = '02/03/2016'
        date2= '2016-03-02'
        tipo1 = 'presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1', tipo1,idASprint)
        result = aMeeting.updateMeeting(date, date1, 'A1', 'S1', 'C1',tipo1, idASprint,1)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date2,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertFalse(result)

#    def testUpdateMeetingsMaxDateFalse(self):
#        # Creamos el backlog
#        self.aBacklog  = backlog()
#        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
#        findId         = self.aBacklog.findName('Bxtyllz')
#        self.idBacklog = findId[0].BL_idBacklog
#        # Creamos el sprint
#        aSprint      = sprints()
#        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog, TODAY, TOMORROW, STATES[1])
#        findIdSprint = aSprint.searchIdSprint(1, self.idBacklog)
#        idASprint = findIdSprint[0].S_idSprint
#        # Creamos el meeting
#        date = datetime.date(2015,8,9)
#        date1 = datetime.date(2020,12,12)
#        aMeeting = meeting()
#        aMeeting.insertMeeting(date, 'A1', 'S1', 'C1', idASprint)
#        result = aMeeting.updateMeeting(date, date1, 'A1', 'S1', 'C1', idASprint)
#        self.assertFalse(result)
#        # Eliminamos los datos insertados.
#        self.aBacklog.deleteProduct('Bxtyllz')
#        aSprint.deleteSprint(1,self.idBacklog)
#        aMeeting.deleteMeeting(date1,idASprint)

    def testUpdateMeetingsFalseInvalidIdSprint(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        date1 = '02/03/2016'
        date2= '2016-03-02'
        tipo1 = 'presencial'
        tipo2 = 'no presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo1, idASprint)
        result = aMeeting.updateMeeting(date, date1, 'A1', 'S1', 'C1',tipo2, -1, 1)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date2,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertFalse(result)

    def testUpdateMeetingsFalseInvalidTypes(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        date1 = '02/03/2016'
        date2= '2016-03-02'
        tipo1 = 'presencial'
        tipo2 = 'no presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo1, idASprint)
        result = aMeeting.updateMeeting(date, date1, 0, 2.5, [],tipo2, idASprint,1)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date2,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertFalse(result)

    #############################################
    #         Pruebas para getMeetings          #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testGetMeetings(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        tipo = 'presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo, idASprint)
        aMeeting.getMeetings(idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date0,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    def testGetMeetingsEmpty(self):
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
        aMeeting = meeting()
        result = aMeeting.getMeetings(idASprint)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result == [])

    def testGetMeetingsNotEmpty(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        tipo = 'presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo, idASprint)
        result = aMeeting.getMeetings(idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date0,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result != [])

    def testGetMeetingsEmptyInvalidIdSprint(self):
        # Creamos el meeting
        aMeeting = meeting()
        result = aMeeting.getMeetings(-1)
        self.assertTrue(result == [])

    #############################################
    #        Pruebas para deleteMeeting         #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testDeleteMeeting(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        tipo = 'presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo, idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date0,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')

    def testDeleteMeetingTrue(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        tipo = 'presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1', tipo,idASprint)
        result = aMeeting.deleteMeeting(date0,idASprint)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertTrue(result)

    def testDeleteMeetingFalseInvalidDate(self):
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
        ## Creamos el meeting
        date0 = '2015-02-02'
        date = '02/02/2015'
        date1 = '02/03/2015'
        date2 = '2015-02-03'
        tipo = 'presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo, idASprint)
        result = aMeeting.deleteMeeting(date2,idASprint)
        # Eliminamos los datos insertados.
        aMeeting.deleteMeeting(date2,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertFalse(result)

    def testDeleteMeetingFalseInvalidSprintNumber(self):
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
        date0 = '2015-02-02'
        date = '02/02/2015'
        tipo = 'presencial'
        aMeeting = meeting()
        aMeeting.insertMeeting(date0, 'A1', 'S1', 'C1',tipo, idASprint)
        # Eliminamos los datos insertados.
        result = aMeeting.deleteMeeting(date,-1)
        aMeeting.deleteMeeting(date0,idASprint)
        aSprint.deleteSprint(1,self.idBacklog)
        self.aBacklog.deleteProduct('Bxtyllz')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
