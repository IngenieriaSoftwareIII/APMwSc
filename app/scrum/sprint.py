# -*- coding: utf-8 -*-

from flask import request, session, Blueprint, json
from app.scrum.sprintClass       import *
from app.scrum.backLog           import *
from app.scrum.userHistory       import *
from app.scrum.task              import *
from datetime                    import datetime

sprint = Blueprint('sprint', __name__)

DATE_FORMAT = '%d/%m/%Y'

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

    idPila = request.args.get('idPila',1)
        
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



@sprint.route('/sprint/VSprint')
def VSprint():
    #GET parameter
    res = {}

    # Obtenemos el id del producto y del sprint
    idPila   = int(session['idPila'])
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

    res['fSprint'] = {'idSprint':idSprint, 
                        'numero':sprint.S_numero, 
                        'descripcion':sprint.S_sprintDescription, 
                        'fechini':sprint.S_fechini.strftime(DATE_FORMAT), 
                        'fechfin':sprint.S_fechfin.strftime(DATE_FORMAT), 
                        'state':sprint.S_state }

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





#Use case code starts here


#Use case code ends here

