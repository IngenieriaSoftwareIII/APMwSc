from flask import request, session, Blueprint, json
from app.scrum.sprintClass       import *
from app.scrum.meetingClass      import *
from app.scrum.elementMeetingClass   import *
from app.scrum.backLog           import *
from app.scrum.subEquipoClass           import *
from app.scrum.userHistory       import *
from app.scrum.user              import *
from app.scrum.task              import *
from app.scrum.acceptanceCriteria import *
from datetime import datetime, timedelta
from random import randint
sprint = Blueprint('sprint', __name__)

DATE_FORMAT = '%Y-%m-%d'

@sprint.route('/sprint/AActualizarEquipoSprint', methods=['POST'])
def AActualizarEquipoSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEquipoSprint', 'msg':['Sub Equipo actualizado']}, {'label':'/VEquipoSprint', 'msg':['Error al actualizar el Sub equipo']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idSprint  = int(session['idSprint'])
    idPila  = int(session['idPila'])
    obTeam = team()
    idEquipo = obTeam.getTeamId(idPila)

    lista = params['lista']    
    oTeam = subEquipoClass()
    exito = oTeam.actualizar(lista,idSprint)
    if exito:
        res = results[0]
    res['label'] = res['label'] + '/' + repr(1)
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@sprint.route('/sprint/VEquipoSprint')
def VEquipoSprint():
    #GET parameter
    idSprint = int(session['idSprint'])
    idPila  = int(session['idPila'])
    res = {}
    #Action code goes here, res should be a JSON structure
    if "actor" in session:
        res['actor']=session['actor']
   # #Action code goes here, res should be a JSON structure
    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
   
    obTeam = team()
    teamList = obTeam.getTeamDevs(idPila)
    oTeam = subEquipoClass()
    SubteamList = oTeam.getSubEquipo(idSprint)

    res['fEquipo'] = {'lista':[{'miembro':team.SEQ_username, 'rol': team.SEQ_rol} for team in SubteamList]}
    res['usuario'] = session['usuario']
    res['idSprint'] = idSprint

    res['fEquipo_opcionesRol'] =[
        {'key':'Desarrollador', 'value':'Desarrollador'}
      ]

    res['fEquipo_opcionesMiembros'] =[{'key':user.EQ_username,'value': user.EQ_username} for user in teamList]

    #Action code ends here
    return json.dumps(res)




@sprint.route('/sprint/ACrearElementoMeeting', methods=['POST'])
def ACrearElementoMeeting():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VReunion', 'msg':['Detalle de la reunión creado']}, {'label':'/VCrearElementoMeeting', 'msg':['Error al crear un detalle a la reunión']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message
    usuario = session['usuario']['username']
    oUser = user()
    #print(usuario)
    challenges = params['challenge']
    planed = params['planed']
    done = params['done']
    idReunion = int(session['idReunion'])
    oElementMeeting = elementMeeting()
    exito = oElementMeeting.insertElement(challenges, planed, done, idReunion, usuario)
    if exito:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idReunion)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/ACrearReunionSprint', methods=['POST'])
def ACrearReunionSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Reunión creada']}, {'label':'/VCrearReunionSprint', 'msg':['Error creando reunion']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idPila  = int(session['idPila'])
    idSprint = int(session['idSprint'])
    fecha = params['Fecha']
    actividades = params['Actividades']
    sugerencias = params['Sugerencias']
    tipo = params['Tipo']
    if tipo == 1:
        tipo = 'Presencial'
    else:
        tipo = 'No Presencial'
    retos = params['Retos']


    oMeeting = meeting()
    exito = oMeeting.insertMeeting(fecha,actividades,sugerencias,retos,tipo,idSprint) #AGREGAR NUEVO ATRIBUTO
    #print(exito)
    #print(fecha)
    if exito:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@sprint.route('/sprint/ACrearSprint', methods=['POST'])
def ACrearSprint():
    #POST/PUT parameters
    params   = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint creado']}, {'label':'/VCrearSprint', 'msg':['Error al crear Sprint']}, ]
    res     = results[1]

    # Obtenemos el id del producto
    idPila  = int(session['idPila'])

    if request.method == 'POST':
        # Extraemos los parámetros
        newNumero      = params['numero']
        newDescription = params['descripcion']
        newState = params ['state']

        # Parse las fechas
        try:
            newFechini = datetime.strptime(params['fechini'], DATE_FORMAT)
            newFechfin = datetime.strptime(params['fechfin'], DATE_FORMAT)
        except ValueError:
            res = results[1]
            res['label'] = res['label'] + '/' + str(idPila)
            return json.dumps(res)

        oSprint = sprints()
        result  = oSprint.insertSprint(newNumero, newDescription, idPila, newFechini, newFechfin, newState)

        if result:
            res = results[0]

        # Creamos el subEquipo
        # Obtengo Todos los desarrolladores del Equipo
        oTeam      = team()
        teamList = oTeam.getTeamDevs(idPila)
        oSubTeam = subEquipoClass()
        idSprint = oSprint.getSprintId(newNumero,idPila)

        for member in teamList:
            oSubTeam.insertMiembroSubEquipo(member.EQ_username,member.EQ_rol,idSprint)

    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/AElimSprint')
def AElimSprint():
     #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VSprints', 'msg':['Sprint eliminado']}, {'label':'/VSprint', 'msg':['Error al eliminar Sptrint']}, ]
    res     = results[1]

    # Obtenemos el id del producto
    idPila       = int(session['idPila'])

    # Obtenemos el id del sprint
    #idSprint = int(params['idSprint'])
    idSprint = int(session['idSprint'])

    # Conseguimos el sprint a eliminar
    oSprint  = sprints()
    found    = oSprint.searchIdSprint(idSprint,idPila)

    if (found != []):
        deleted = oSprint.deleteSprint(found[0].S_numero, found[0].S_idBacklog)

    if deleted:
            res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@sprint.route('/sprint/AElimSprintHistoria')
def AElimSprintHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Historia Eliminado']}, {'label':'/VSprint', 'msg':['Error al eliminar historia']}, ]
    res = results[1]

    idSprint = int(session['idSprint'])
    idPila = int(session['idPila'])
    idHistoriaEliminar = int(request.args['id'])

    oSprint  = sprints()
    oUserHistory = userHistory()
    oTask = task()
    deletedHistoryID=[]
    if oSprint.deleteAssignedSprintHistory(idSprint,idPila,idHistoriaEliminar):
        # Chequeamos si es epica, si lo es eliminamos sus hijos
        deletedHistoryID.append(idHistoriaEliminar)
        if oUserHistory.isEpic(idHistoriaEliminar):
            for idHistoria in oUserHistory.historySuccesors(idHistoriaEliminar):
                oSprint.deleteAssignedSprintHistory(idSprint,idPila, idHistoria)
                deletedHistoryID.append(idHistoria)

        # Eliminamos sus tareas
        for idHistoria in deletedHistoryID:
            tareas = oTask.taskAsociatedToUserHistory(idHistoria)
            for tarea in tareas:
                oSprint.deleteAssignedSprintTask(idSprint, idPila, tarea.HW_idTask)

        res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    return json.dumps(res)


@sprint.route('/sprint/AModifElementoMeeting', methods=['POST'])
def AModifElementoMeeting():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VReunion', 'msg':['Detalle Modificado con éxito']},{'label':'/VReunion', 'msg':['Error al modificar detalle']} ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    challenges = params['challenge']
    planed = params['planed']
    done = params['done']
    idReunion = session['idReunion']
    idElementMeeting = session['idElementMeeting']
    res['usuario'] = session['usuario']
    oElementMeeting = elementMeeting()
    anElement = oElementMeeting.getElementID(idElementMeeting, idReunion)[0]
    exito = oElementMeeting.updateElement(anElement.EM_idElementMeeting, challenges, planed, done, idReunion, anElement.EM_user)
    if exito:
        res = results[0]
    res['label'] = res['label'] + '/' + str(idReunion)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/AModifReunionSprint', methods=['POST'])
def AModifReunionSprint():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Reunión de sprint modificada'], "actor":"desarrollador"}, {'label':'/VSprint', 'msg':['Error al modificar reunión'], "actor":"desarrollador"}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idPila  = int(session['idPila'])
    idReunion  = params['idReunion']
    idSprint = int(params['idSprint'])
    #fecha = params['Fecha']
    actividades = params['Actividades']
    sugerencias = params['Sugerencias']
    retos = params['Retos']
    tipo = params['Tipo'] #NUEVO ATRIBUTO OJO!!! AGREGAR A LA LLAMADA DE LA FUNCION DE ABAJO (updateMeeting)

    oMeeting = meeting()
    result = oMeeting.getMeetingID(idReunion,idSprint)

    exito = oMeeting.updateMeeting(result[0].SM_meetingDate,result[0].SM_meetingDate,actividades,sugerencias,retos,tipo,idSprint,idReunion)

    if exito:
        res = results[0]

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    idSprint = 1
    res['label'] = res['label'] + '/' + str(idSprint)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    res['idSprint'] = idSprint
    session['idReunion'] = idReunion

    return json.dumps(res)

@sprint.route('/sprint/AElimSprintTarea')
def AElimSprintTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Tarea eliminada']}, {'label':'/VSprint', 'msg':['Error al eliminar tarea']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idSprint = int(session['idSprint'])
    idPila = int(session['idPila'])
    idTareaEliminar = int(request.args['id'])

    oSprint  = sprints()
    if oSprint.deleteAssignedSprintTask(idSprint,idPila,idTareaEliminar):
        res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@sprint.route('/sprint/AModifSprint', methods=['POST'])
def AModifSprint():
    #POST/PUT parameters
    params = request.get_json()

    results = [{'label':'/VSprints', 'msg':['Sprint modificado']}, {'label':'/VSprints', 'msg':['Error al guardar Sprint']}, ]
    res = results[0]

    idPila   = int(session['idPila'])
    idSprint = int(session['idSprint'])
    newSprintNumber = int(params['numero'])
    newDescription  = str(params['descripcion'])
    newState = params['state']

    # Parse las fechas
    try:
        newFechini = datetime.strptime(params['fechini'], DATE_FORMAT)
        newFechfin = datetime.strptime(params['fechfin'], DATE_FORMAT)
    except ValueError:
        res = results[1]
        res['label'] = res['label'] + '/' + str(idPila)
        return json.dumps(res)

    res['label'] = res['label'] + '/' + str(idPila)
    oSprint = sprints()
    result  = oSprint.updateSprint(idSprint, idPila, newSprintNumber, newDescription, newFechini, newFechfin, newState)

    if not result:
        res = results[1]
        res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    res['idPila'] = idPila


    return json.dumps(res)

@sprint.route('/sprint/AResumenHistoria', methods=['POST'])
def AResumenHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Resumen agregado exitosamente!']}, {'label':'/VResumenHistoria', 'msg':['Error agregando resumen de historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    print(params)

    idSprint = int(session['idSprint'])
    idUserHistory = int(params['Historia'])
    resume = str(params['Resumen'])

    res['label'] = res['label'] + '/' + str(idSprint)
    oUserHistory = userHistory()
    result = oUserHistory.assignHistoryResume(idUserHistory, resume)

    if not result:
        res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#

@sprint.route('/sprint/ASprintHistoria', methods=['POST'])
def ASprintHistoria():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Historia Asignado']}, {'label':'/VSprint', 'msg':['Error al Asignar Historia']}, ]
    res     = results[1]

    idSprint   = int(params['idSprint'])
    idPila     = params['idPila']
    idHistoria = params['historia']

    oSprint      = sprints()
    oTask        = task()
    oUserHistory = userHistory()

    #Lista usada para obtener los ids de las historias asigndas
    historiesList = []

    if oSprint.asignSprintHistory(idSprint,idPila, idHistoria):
        historiesList.append(idHistoria)

        # Chequeamos si es epica, si lo es agregamos las sub-historias
        if oUserHistory.isEpic(idHistoria):
            for idHistoria in oUserHistory.historySuccesors(idHistoria):
                oSprint.asignSprintHistory(idSprint,idPila, idHistoria)
                historiesList.append(idHistoria)

        totalResult = True
        #Obtenemos las tareas asociadas a cada historia de usuario asignada
        for idHist in historiesList:
            taskList = oTask.getAllTask(idHist)

            if taskList != []:
                for t in taskList:
                    result = oSprint.asignSprintTask(idSprint,idPila, t.HW_idTask)
                    totalResult = totalResult and result

    #if totalResult:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@sprint.route('/sprint/VCrearElementoMeeting')
def VCrearElementoMeeting():
    #GET parameter
    #idReunion = request.args['idReunion']
    idReunion = int(request.args.get('idReunion',1))
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    session['idReunion'] = idReunion
    res['idReunion'] = idReunion

    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VCrearReunionSprint')
def VCrearReunionSprint():
    #GET parameter
    res = {}

    idPila = int(request.args.get('idPila',1))

    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']
    res['idPila']  = idPila
    res['idSprint'] = session['idSprint']
    
    res['fReunion_OpcionesTipo'] =[
        {'key':1, 'value':'Presencial'},
        {'key':2, 'value':'No Presencial'},
    ]


    #Action code ends here
    return json.dumps(res)


@sprint.route('/sprint/ASprintTarea', methods=['POST'])
def ASprintTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Tarea asignada']}, {'label':'/VSprint', 'msg':['Error al asignar tarea']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    idSprint = int(params['idSprint'])
    idPila = params['idPila']
    idTarea = params['tarea']

    oSprint = sprints()

    #Obtenemos las tareas asociadas a cada historia de usuario
    if oSprint.asignSprintTask(idSprint,idPila, idTarea):
        res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@sprint.route('/sprint/VCrearSprint')
def VCrearSprint():
   #GET parameter
    res = {}

    idPila = int(request.args.get('idPila',1))

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['fSprint'] = {'idPila':idPila}
    res['usuario'] = session['usuario']
    res['idPila']  = idPila

    return json.dumps(res)


@sprint.route('/sprint/VResumenHistoria')
def VResumenHistoria():
    #GET parameter
    # idSprint = request.args['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    res['usuario'] = session['usuario']

    idPila = int(session['idPila'])
    idSprint = int(session['idSprint'])
#
    oSprint = sprints()
    historiasSprint = oSprint.getAssignedSprintHistory(idSprint, idPila)
    res['fResumenHistoria_opcionesHistoria'] = [
        {'key':historia.UH_idUserHistory,'value':historia.UH_codeUserHistory} for historia in historiasSprint
    ]

    res['idSprint'] = idSprint
    res['fSprintHistoria'] = {'idPila':idPila, 'idSprint':idSprint}

    #Action code ends here
    return json.dumps(res)




@sprint.route('/sprint/VElementoMeeting')
def VElementoMeeting():
    #GET parameter
    idMeeting = int(request.args['idMeeting'])
    idReunion = session['idReunion']
    print(idReunion)
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']
    u = session['usuario']['username']

    oElementMeeting = elementMeeting()
    anElement = oElementMeeting.getElementID(idMeeting,idReunion)[0]
    res['fElementoMeeting'] = {
        'challenge' : anElement.EM_challenges,
        'planed' : anElement.EM_planned,
        'done' : anElement.EM_done,
#      'challenge' :'Carrera inicial. Modelo de datos, MVC, identificación',
#      'planed':'planificado',
#      'done':'realizado',
#      'idReunion':1,
#      'idUser':1,
      }
    res['idElementMeeting'] = anElement.EM_idElementMeeting
    session['idElementMeeting'] = anElement.EM_idElementMeeting
    res['idReunion'] =  idReunion
    session['idReunion'] =  idReunion

    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VReunion')
def VReunion():
    #GET parameter
    idReunion = int(request.args.get('id', 1))

    idSprint = session['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    oMeeting = meeting()
    result  = oMeeting.getMeetingID(idReunion,idSprint)

    oElementMeeting = elementMeeting()
    elements  = oElementMeeting.getElements(idReunion)
    res['data4'] = [{'id': e.EM_idElementMeeting, 'user': e.EM_user} for e in elements]

    res['fReunion'] = {'idReunion':idReunion,'idSprint':idSprint, 'Actividades':result[0].SM_activities, 'Sugerencias':result[0].SM_suggestions,'Retos':result[0].SM_challenges, 'Tipo':result[0].SM_typeMeeting}
    res['idReunion'] = idReunion
    session['idReunion'] = idReunion
    res['idSprint'] = idSprint
    #Action code ends here
    return json.dumps(res)



@sprint.route('/sprint/VSprint')
def VSprint():
    #GET parameter
    res = {}

    # Obtenemos el id del producto y del sprint
    idPila   = int(session['idPila'])
    print("Argumentos: ")
    print(request.args)
    idSprint = int(request.args.get('idSprint',1))
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Buscamos el actor actual

    oSprint      = sprints()
    oBacklog     = backlog()
    oUserHistory = userHistory()
    sprint       = oSprint.searchIdSprint(idSprint,idPila)[0]

    res['fSprint'] = { 'idSprint':idSprint
                     , 'numero':sprint.S_numero
                     , 'descripcion':sprint.S_sprintDescription
                     , 'fechini':sprint.S_fechini.strftime(DATE_FORMAT)
                     , 'fechfin':sprint.S_fechfin.strftime(DATE_FORMAT)
                     , 'state':sprint.S_state
                     }

    #Obtenes las historias asignadas al sprint
    listaHistorias = oSprint.getAssignedSprintHistory(idSprint, idPila)
    userHistories  = []

    #Acomodamos la escala asociada a la historia
    priorities     = {0:'Epica',1:'Alta',2:'Media',3:'Baja'}
    priorities2    = {i:str(i)for i in range(1,20+1)}
    priorities2[0] = 'Epica'

    # Obtenemos el tipo de escala seleccionada en el producto asociado a la historia.
    typeScale = oBacklog.scaleType(idPila)

    #Obtenemos los valores de cada historia en un diccionario y almacenamos esos diccionarios en un arreglo.
    for hist in listaHistorias:
        result = oUserHistory.transformUserHistory(hist.UH_idUserHistory)

        if typeScale == 1:
            result['priority'] = priorities[hist.UH_scale]
        elif typeScale == 2:
            result['priority'] = priorities2[hist.UH_scale]
        userHistories.append(result)

    #Lista de Historias
    res['data6'] = [
        {'idHistoria':hist['idHistory'],
         'prioridad' :hist['priority'],
         'enunciado' :'En tanto ' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives'],
         'resumen'   :hist['resume']}for hist in userHistories
    ]

    listaTareas = oSprint.getAssignedSprintTask(idSprint, idPila) # Tareas asignadas al Sprint
    #Lista de tareas
    res['data8'] = [{'idTarea':tarea.HW_idTask, 'descripcion':tarea.HW_description}for tarea in listaTareas]

    session['idSprint'] = idSprint
    res['idSprint'] = idSprint
    res['idPila'] = idPila

    oMeeting = meeting()
    result  = oMeeting.getMeetings(idSprint)
    res['data5'] = [{'id':res.SM_idSprintMeeting, 'fecha':res.SM_meetingDate, 'actividades':res.SM_activities,'tipo':res.SM_typeMeeting } for res in result]  

    session['idSprint'] = idSprint
    res['idSprint'] = idSprint

    session['idPila'] = idPila
    res['idPila'] = idPila

    #print(res['data4'])

    #Lista de criterios
    listaCriterios = oSprint.getAssignedSprintAC(idSprint, idPila) # Criterios de aceptación asignados al Sprint
    
    res['data11'] = [{ 'idCriterio' : criterio.HAC_idAcceptanceCriteria
                     , 'historia'   : clsUserHistory.query.filter_by(UH_idUserHistory = criterio.HAC_idUserHistory).first().UH_codeUserHistory
                     , 'descripcion': criterio.HAC_description
                     , 'enunciado'  : criterio.HAC_enunciado
                     } for criterio in listaCriterios]    

    return json.dumps(res)



@sprint.route('/sprint/VSprintHistoria')
def VSprintHistoria():
    #GET parameter
    idSprint = request.args['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    res['usuario'] = session['usuario']

    idPila = int(session['idPila'])

    oUserHistory = userHistory()
    historiasProducto = oUserHistory.getAllUserHistoryId(idPila)
    res['fSprintHistoria_opcionesHistoria'] = [
        {'key':historia.UH_idUserHistory,'value':historia.UH_codeUserHistory} for historia in historiasProducto
    ]

    res['idSprint']= idSprint
    res['fSprintHistoria'] = {'idPila':idPila, 'idSprint':idSprint}

    return json.dumps(res)



@sprint.route('/sprint/VSprintTarea')
def VSprintTarea():
    #GET parameter
    idSprint = request.args['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)

    idPila = int(session['idPila'])
    idSprint = int(request.args['idSprint'])
    oSprint = sprints()
    listaHistorias = oSprint.getAssignedSprintHistory(idSprint, idPila) #Obtenemos las historias asignadas al sprint
    oTask = task()

    #Obtenemos Todas las tareas asociadas a todas nuestras historias
    listaTareas = []
    for historia in listaHistorias:
        tareas = oTask.taskAsociatedToUserHistory(historia.UH_idUserHistory) #Lista de tareas asociada a la historia
        for tarea in tareas:
            listaTareas.append(tarea) #Agregamos todas las tareas de la lista de tareas

    res['fSprintTarea_opcionesTarea'] = [{'key':tarea.HW_idTask,'value':tarea.HW_description}for tarea in listaTareas]
    res['fSprintTarea'] = {'idPila':idPila, 'idSprint':idSprint}

    res['idSprint']= idSprint
    res['usuario'] = session['usuario']

    return json.dumps(res)



@sprint.route('/sprint/VSprints')
def VSprints():
     #GET parameter
    res = {}

    # Obtenemos el id del producto.
    idPila = int(request.args.get('idPila',1))

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']

    oBacklog   = backlog()
    sprintList = oBacklog.sprintsAsociatedToProduct(idPila)
    res['data1'] = [{'numero':spr.S_numero,
                    'descripcion':spr.S_sprintDescription,
                    'fechini':spr.S_fechini.strftime(DATE_FORMAT),
                    'fechfin':spr.S_fechfin.strftime(DATE_FORMAT),
                    'state':spr.S_state } for spr in sprintList]


    session['idPila'] = idPila
    res['idPila']     = idPila

    return json.dumps(res)

########## CRITERIOS DE ACEPTACIÓN ##########

@sprint.route('/sprint/ACriterioHistoria', methods=['POST'])
def ACriterioHistoria():

    numCriteria = clsAcceptanceCriteria.query.order_by(clsAcceptanceCriteria.HAC_idAcceptanceCriteria).all()
    if numCriteria == []:
        criterio = 1
    else:
        for elem in numCriteria:
            x = elem.HAC_idAcceptanceCriteria
        criterio = x + 1

    #POST/PUT parameters
    params = request.get_json()
    
    idPila          = params['idPila']
    idSprint        = int(session['idSprint'])
    idUserHistory   = int(params['Historia'])
    description     = str(params['Descripcion'])
    enunciado       = str(params['Enunciado'])

    results = [{'label':'/VSprint', 'msg':['Criterio agregado exitosamente']}, {'label':'/VCriterioHistoria/'+str(idSprint), 'msg':['Error al asignar criterio a la historia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/' + str(idSprint)

    oSprint = sprints()
    oAcceptanceCriteria = acceptanceCriteria()

    insert = oAcceptanceCriteria.insertAcceptanceCriteria(idUserHistory, description, enunciado)

    result = False
    if insert:
        result = oSprint.assignSprintAcceptanceCriteria(idSprint, idPila, criterio);

    if not result:
        res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/AElimCriterioHistoria')
def AElimCriterioHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VSprint', 'msg':['Criterio de aceptación eliminado']}, {'label':'/VSprint', 'msg':['Error al eliminar el criterio de aceptación']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idSprint = int(session['idSprint'])
    idPila = int(session['idPila'])
    idCriterioEliminar = int(request.args['id'])

    oAcceptanceCriteria = acceptanceCriteria()
    if oAcceptanceCriteria.deleteAcceptanceCriteria(idCriterioEliminar):
        res = results[0]

    res['label'] = res['label'] + '/' + str(idSprint)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@sprint.route('/sprint/VCriterioHistoria')
def VCriterioHistoria():
    #GET parameter
    #idSprint = request.args['idSprint']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    res['usuario'] = session['usuario']

    idPila = int(session['idPila'])
    idSprint = int(session['idSprint'])
# 
    oSprint = sprints()
    historiasSprint = oSprint.getAssignedSprintHistory(idSprint, idPila)
    res['fCriterioHistoria_opcionesHistoria'] = [
        {'key':historia.UH_idUserHistory,'value':historia.UH_codeUserHistory} for historia in historiasSprint
    ]

    res['idSprint'] = idSprint
    res['idPila']  = idPila
    res['fCriterioHistoria'] = {'idPila':idPila, 'idSprint':idSprint}

    #Action code ends here
    return json.dumps(res)

@sprint.route('/sprint/VDesempeno')
def VDesempeno():
    #GET parameter
    idSprint = request.args['idSprint']
    idPila = int(session["idPila"])
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    if 'usuario' not in session:
        res['logout'] = '/'
        return json.dumps(res)
    print(idPila)
    oSprint = sprints()
    #Retrieve the sprint from the DB
    asociated_sprint = oSprint.searchIdSprint(int(idSprint),idPila)[0]
    
    #Calculate duration (in days)
    sprint_start_date=asociated_sprint.S_fechini
    sprint_end_date=asociated_sprint.S_fechfin
    sprint_time=(sprint_end_date-sprint_start_date).days
    
    #Sprint
    sprint_tasks = oSprint.getAssignedSprintTask(int(idSprint),idPila)
    sprint_index = map(lambda x: ((x.HW_fechaFin-sprint_start_date).days+1,x.HW_weight),sprint_tasks) 
    sprint_index = dict(sprint_index)
    print(sprint_index,sprint_time)
    sprint_tasks_total= sum(map(lambda x: x.HW_weight ,sprint_tasks))
    ideal_delta= sprint_tasks_total//sprint_time
    sprint_tasks_total_real=sprint_tasks_total
    #Building the bdchart
    rows = [{"c":[{ "v": "Dia 1"},{"v": sprint_tasks_total,},{"v": sprint_tasks_total,}]}]
    for x in range(2,sprint_time):
        sprint_tasks_total-=ideal_delta
        sprint_tasks_total_real-=sprint_index.get(x,0)
        rows.append({"c":[{ "v": "Dia %s"%x},{"v":sprint_tasks_total_real, },{"v": sprint_tasks_total,}]})
    sprint_tasks_total_real-=sprint_index.get(x+1,0)
    rows.append({"c":[{ "v": "Dia %s"%(x+1)},{"v":sprint_tasks_total_real, },{"v": 0,}]})
    #Building the JSON to be sent
    data={"cols": [{ "id":"days","label":"Dias del sprint","type":"string","p":{}},
              {"id": "actual_hours","label": "Peso de las tareas","type": "number","p": {}},
              {"id": "ideal_hours","label": "Pesos estimados","type": "number", "p": {}},
              ]}
    data['rows']=rows
    
    bdchart = {
          "type": "ComboChart",
          "options": {
                "title": "Burn down chart del Sprint",
                "vAxis": {
                  "title": "Peso acumulado de las tareas"
                },
                "hAxis": {
                  "title": "Dias"
                },
                "seriesType":"bars",
                "series":{1:{'type': 'line'}, 0: {'color': '#000000'}},
            },
            "formatters": {}
        }
    bdchart["data"]=data
    res['usuario'] = session['usuario']
    res['idSprint']=idSprint
    res['bdchart']=bdchart

    #Action code ends here
    return json.dumps(res)



#Use case code starts here


#Use case code ends here

