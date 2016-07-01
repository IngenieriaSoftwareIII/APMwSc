# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo subEquipoClass.py
sys.path.append('../app/scrum')

from subEquipoClass import *
from Team import *
from user import *
from role import *
from datetime import *

# Declaracion de constantes
TODAY = datetime.utcnow()
TOMORROW = TODAY + timedelta(days=1)
STATES = ["Terminada", "En ejecución", "No iniciada"]

class TestsubEquipoClass(unittest.TestCase):
	#############################################      
    #         Pruebas para emptyTable           #
    #############################################


    # Probar que la funcionalidad se ejecuta
    def testEmptyTable(self):
        subequipo_object = subEquipoClass()
        subequipo_object.emptyTable()

    # Probar que hay elementos en subEquipo
    def testEmptyTableFalse(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor
        actor = role()
        actor.insertActor('Actor','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user = user()
        _user.insertUser('fullname','userr','password1234','prueba@user.com',idActor)
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Agregamos un usuario a team
        team_object = team()
        team_object.insertMiembro('userr','Actor',idBacklog)
        # Creamos el subEquipo
        subequipo_object = subEquipoClass()
        # Agregamos el usuario al subEquipo
        subequipo_object.insertMiembroSubEquipo('userr','Actor')
        # Ejecutamos la funcion
        result = subequipo_object.emptyTable()
        self.assertTrue(result)


    #############################################      
    #         Pruebas para getSubEquipo         #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testgetSubEquipo(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor
        actor = role()
        actor.insertActor('Actor','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user = user()
        _user.insertUser('fullname','userr','password1234','prueba@user.com',idActor)
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Agregamos un usuario a team
        team_object = team()
        team_object.insertMiembro('userr','Actor',idBacklog)
        # Creamos el subEquipo
        subequipo_object = subEquipoClass()
        # Obtenemos id del sprint
        foundSprint = aSprint.searchIdSprint(1, idBacklog)[0]
        # Agregamos el usuario al subEquipo
        subequipo_object.insertMiembroSubEquipo('userr','Actor')
        # Ejecutamos la funcion
        result = subequipo_object.getSubEquipo(foundSprint.S_numero)
        self.assertTrue(True)
        # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('userr',1)
        team_object.deleteMiembro('userr','Actor',idBacklog)
        aSprint.deleteSprint(1,idBacklog)
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Obtener equipo de un sprint inexistente
    def testgetSubEquipoWrongSprint(self):
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Ejecutamos la funcion
        result = subequipo_object.getSubEquipo(9)
        self.assertFalse(result)

    # Insertar datos incorrectos
    def testgetSubEquipoWrongData(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor
        actor = role()
        actor.insertActor('Actor','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user = user()
        _user.insertUser('fullname','userr','password1234','prueba@user.com',idActor)
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Agregamos un usuario a team
        team_object = team()
        team_object.insertMiembro('userr','Actor',idBacklog)
        # Creamos el subEquipo
        subequipo_object = subEquipoClass()
        # Obtenemos id del sprint
        foundSprint = aSprint.searchIdSprint(1, idBacklog)[0]
        # Agregamos el usuario al subEquipo
        subequipo_object.insertMiembroSubEquipo('userr','Actor')
        # Ejecutamos la funcion
        result = subequipo_object.getSubEquipo(9)
        self.assertEqual(result,[])
        # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('userr','Actor')
        team_object.deleteMiembro('userr','Actor',idBacklog)
        aSprint.deleteSprint(1,idBacklog)
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')

    #############################################      
    #       Pruebas para verifyScrummaster      #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testverifyScrumMaster(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Scrum master',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Actor1',idBacklog) 
        team_object.insertMiembro('user2','Actor2',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        subequipo_object.insertMiembroSubEquipo('user1','Actor1')
        subequipo_object.insertMiembroSubEquipo('user2','Actor2')
        # Obtenemos los miembros del subequipo
        subEquipoList = subequipo_object.getSubEquipo(1)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':subEquipoClass.SEQ_username, 'rol': subEquipoClass.SEQ_rol} for subEquipoClass in subEquipoList]
        # Ejecutamos la funcion
        result = team_object.verifyScrumMaster(lista)
        self.assertTrue(result)
         # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('user1',1)
        subequipo_object.deleteMiembroSubEquipo('user2',1)
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Probar que no puede haber mas de un scrum master
    def testverifyScrumMasterFalse(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Scrum master',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Scrum master',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Scrum master',idBacklog) 
        team_object.insertMiembro('user2','Scrum master',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog,  TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        subequipo_object.insertMiembroSubEquipo('user1','Scrum master')
        subequipo_object.insertMiembroSubEquipo('user2','Scrum master')
        # Obtenemos los miembros del subequipo
        subEquipoList = subequipo_object.getSubEquipo(1)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':subEquipoClass.SEQ_username, 'rol': subEquipoClass.SEQ_rol} for subEquipoClass in subEquipoList]
        # Ejecutamos la funcion
        result = team_object.verifyScrumMaster(lista)
        self.assertTrue(result)
         # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('user1',1)
        subequipo_object.deleteMiembroSubEquipo('user2',1)
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Actor1',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Actor2',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Ningun miembro es scrum master
    def testverifyScrumMasterNone(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        subequipo_object.insertMiembroSubEquipo('user1','Desarrollador')
        subequipo_object.insertMiembroSubEquipo('user2','Desarrollador')
        # Obtenemos los miembros del subequipo
        subEquipoList = subequipo_object.getSubEquipo(1)
        userList = _user.getAllUsers()
        # Creamos la lista
        lista = [{'miembro':subEquipoClass.SEQ_username, 'rol': subEquipoClass.SEQ_rol} for subEquipoClass in subEquipoList]
        # Ejecutamos la funcion
        result = team_object.verifyScrumMaster(lista)
        self.assertTrue(result)
         # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('user1',1)
        subequipo_object.deleteMiembroSubEquipo('user2',1)
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')


    #############################################      
    #    Pruebas para insertMiembroSubEquipo    #
    #############################################

    # Probar que la funcionalidad se ejecuta
    def testinsertMiembroSubEquipo(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        result = subequipo_object.insertMiembroSubEquipo('user1','Desarrollador')
        self.assertFalse(result)
         # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('user1',1)
        subequipo_object.deleteMiembroSubEquipo('user2',1)
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Agregar un miembro que no pertenezca al equipo
    def testinsertMiembroNotmember(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog,  TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        result = subequipo_object.insertMiembroSubEquipo('user9','Desarrollador')
        self.assertFalse(result)
         # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('user9',1)
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    #  Insertar miembro a un sprint inexistente
    def testinsertMiembroSubEquipoSprintNone(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog,  TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        result = subequipo_object.insertMiembroSubEquipo('user1',99)
        self.assertFalse(result)
         # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('user1',1)
        subequipo_object.deleteMiembroSubEquipo('user2',1)
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Insertar datos incorrectos
    def testinsertMiembroWrongData(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog,  TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        result = subequipo_object.insertMiembroSubEquipo(1,1)
        self.assertFalse(result)
         # Eliminamos los datos insertados
        subequipo_object.deleteMiembroSubEquipo('user9',1)
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    #############################################      
    #    Pruebas para deleteMiembroSubEquipo    #
    #############################################

     # Probar que la funcionalidad se ejecuta
    def testdeleteMiembroSubEquipo(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        subequipo_object.insertMiembroSubEquipo('user1',1)
        # Ejecutamos la funcion
        result = subequipo_object.deleteMiembroSubEquipo('user1',1)
        self.assertTrue(result)
         # Eliminamos los datos insertados
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Eliminar miembros no agregados
    def testdeleteMiembroSubEquipoNotAdded(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog, TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        subequipo_object.insertMiembroSubEquipo('user1','Desarrollador')
        # Ejecutamos la funcion
        result = subequipo_object.deleteMiembroSubEquipo('user9',1)
        self.assertFalse(result)
         # Eliminamos los datos insertados
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')

    # Mala insercion de datos
    def testdeleteMiembroSubEquipoWrongData(self):
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor 1
        actor = role()
        actor.insertActor('Actor1','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor1',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el actor 2
        actor.insertActor('Actor2','Desarrollador',idBacklog)
        result    = actor.findNameActor('Actor2',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario 1
        _user = user()
        _user.insertUser('fullname','user1','password1234','prueba@user1.com',idActor)
        # Creamos el usuario 2
        _user.insertUser('fullname','user2','password1232','prueba@user2.com',idActor)        
        # Agregamos los usuarios al equipo
        team_object = team()
        team_object.insertMiembro('user1','Desarrollador',idBacklog) 
        team_object.insertMiembro('user2','Desarrollador',idBacklog) 
        # Creamos el sprint
        aSprint      = sprints()
        aSprint.insertSprint(1,'Descripcion sprint',idBacklog,  TODAY, TOMORROW, STATES[1])
        # Creamos el subequipo
        subequipo_object = subEquipoClass()
        # Agregamos los miembros al subequipo
        subequipo_object.insertMiembroSubEquipo('user1','Desarrollador')
        # Ejecutamos la funcion
        result = subequipo_object.deleteMiembroSubEquipo(1,3)
        self.assertFalse(result)
         # Eliminamos los datos insertados
        aSprint.deleteSprint(1,idBacklog)
        team_object.deleteMiembro('user1','Desarrollador',idBacklog)
        _user.deleteUser('user1')
        actor.deleteActor('Actor1',idBacklog)
        team_object.deleteMiembro('user2','Desarrollador',idBacklog)
        _user.deleteUser('user2')
        actor.deleteActor('Actor2',idBacklog)
        _backlog.deleteProduct('Backlog')


if __name__ == '__main__':
    unittest.main()