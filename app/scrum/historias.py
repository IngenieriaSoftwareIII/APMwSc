# -*- coding: utf-8 -*-

from flask                           import request, session, Blueprint, json
from app.scrum.backLog               import *
from app.scrum.userHistory           import *
from app.scrum.role                  import *
from app.scrum.accions               import *
from app.scrum.objective             import *
from app.scrum.objectivesUserHistory import *
from app.scrum.actorsUserHistory     import *
from app.scrum.task                  import *
from app.scrum.precedence            import *
from sqlalchemy.ext.baked            import Result
from datetime                        import datetime
import time

historias = Blueprint('historias', __name__)


@historias.route('/historias/ACambiarPrioridades', methods=['POST'])
def ACambiarPrioridades():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Prioridades reasignadas']}, ]
    res     = results[0]

    # Obtenemos el id del producto.
    idPila  = int(session['idPila'])

    list = params['lista']

    oHistory = userHistory()

    for hist in list:
        idHistory   = hist['idHistoria']
        priority    = hist['prioridad']
        oHistory.updatePriority(idHistory,priority)

    res['label']  = res['label']+'/'+str(idPila)
    res['idPila'] = idPila

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res     = results[1]

    # Obtenemos el id del producto.
    idPila  = int(session['idPila'])

    # Extraemos los parametros.
    codeHistory = params['codigo']
    idSuperHist = params['super']
    idType      = params['tipo']
    idActor     = params['actores']
    idAccion    = params['accion']
    idObjective = params['objetivos']
    priority    = params['prioridad']

    if idActor != [] and idObjective != []:
        oUserHistory = userHistory()

        started = False
        startingDate = None

        completed = False
        finishingDate = None

        # Insertamos los datos de la historia
        inserted     = oUserHistory.insertUserHistory(codeHistory,idSuperHist,idType,idAccion,idPila,priority,started,startingDate,completed,finishingDate)

        # Asociamos los actores y objetivos a la historia.
        if inserted:
            oObjUserHist = objectivesUserHistory()
            oActUserHist = actorsUserHistory()
            result       = oUserHistory.searchUserHistory(codeHistory,idPila)
            idInserted   = result[0].UH_idUserHistory
            insertedAct  = False
            insertedObj  = False

            # Insertamos los nuevos objetivos seleccionados
            for idobj in idObjective:
                insertedObj  = oObjUserHist.insertObjectiveAsociatedInUserHistory(idobj,idInserted)

            # Insertamos los nuevos actores seleccionados
            for idact in idActor:
                insertedAct  = oActUserHist.insertActorAsociatedInUserHistory(idact,idInserted)

            # Verificamos que se crearon todos los componentes de la historia.
            if insertedAct and insertedObj and inserted:
                actorsList     = oActUserHist.idActorsAsociatedToUserHistory(idInserted)
                objectivesList = oObjUserHist.idObjectivesAsociatedToUserHistory(idInserted)

                if actorsList != [] and objectivesList != []:
                    res = results[0]

    res['label'] = res['label'] + '/'+str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    return json.dumps(res)



@historias.route('/historias/AElimHistoria')
def AElimHistoria():
    #GET parameter
    results = [{'label':'/VHistorias', 'msg':['Historia eliminada']}, {'label':'/VHistorias', 'msg':['No se pudo eliminar esta historia']}, ]
    res = results[1]

    # Obtenemos el id del producto y de la historia.
    idPila      = int(session['idPila'])
    idHistoria  = int(session['idHistoria'])

    # Conseguimos la historia a eliminar
    oUserHistory = userHistory()
    found        = oUserHistory.searchIdUserHistory(idHistoria)

    if (found != []):
        # Verificamos si la historia no es una épica
        if (not oUserHistory.isEpic(idHistoria)):
            # Conseguimos los actores asosciados a la historia
            oActorsUserHistory = actorsUserHistory()
            resultActors = oActorsUserHistory.idActorsAsociatedToUserHistory(idHistoria)

            if (resultActors != []):
                # Eliminamos los actores asociados a la historia
                for actor in resultActors:
                    oActorsUserHistory.deleteActorAsociatedInUserHistory(actor, idPila)

                # Conseguimos los objetivos asosciados a la historia
                oObjUserHistory = objectivesUserHistory()
                resultObjectives = oObjUserHistory.idObjectivesAsociatedToUserHistory(idHistoria)

                if (resultObjectives != []):
                    # Eliminamos los objetivos asociados a la historia
                    for objetivo in resultObjectives:
                        oObjUserHistory.deleteObjectiveAsociatedInUserHistory(objetivo, idPila)

                    # Conseguimos las tareas asociadas a la historia
                    aTarea     = task()
                    resultTask = aTarea.taskAsociatedToUserHistory(idHistoria)

                    if (resultTask != []):
                        # Eliminamos las tareas asociados a la historia
                        for tasky in resultTask:
                            aTarea.deleteTask(tasky.HW_description)

                    # Eliminamos la historia de usuario
                    deleted = oUserHistory.deleteUserHistory(found[0].UH_idUserHistory)

                    if deleted:
                        res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistorias', 'msg':['Error al modificar historia']}, ]
    res     = results[1]

    # Obtenemos el id del Producto.
    idPila  = int(session['idPila'])

    # Extraemos los valores
    oUserHist    = userHistory()
    oObjUserHist = objectivesUserHistory()
    oActUserHist = actorsUserHistory()

    idHistory    = params['idHistoria']
    idSupHist    = params['super']
    idaccion     = params['accion']
    idBacklog    = params['idPila']
    idActors     = params['actores']
    codeHist     = params['codigo']
    idObjectives = params['objetivos']
    type         = params['tipo']
    priority     = params['prioridad']
    idPila       = params['idPila']


    started     = params['iniciado']
    startingDate = params['fechaInicio']

    completed     = params['completed']
    finishingDate = params['fechaFin']

    try:
        startingDate_object = datetime.strptime(startingDate, '%d/%m/%Y')
        finishingDate_object = datetime.strptime(finishingDate, '%d/%m/%Y')
    except ValueError:
        res     = results[1]
        res['label'] = res['label'] + '/'+str(idPila)
        return json.dumps(res)

    subHistories = oUserHist.historySuccesors(idHistory)

    if not(idSupHist in subHistories):

        # Actualizamos los datos de la historia
        if startingDate_object.date() <= finishingDate_object.date():
            updated = oUserHist.updateUserHistory(idHistory, codeHist, idSupHist, type, idaccion, priority, \
                                                  started, startingDate_object, completed, finishingDate_object)
        else:
            updated = None
            res = results[1]
            res['msg'][0] = res['msg'][0] + ": La fecha de culminación debe ser mayor o igual que la de inicio."

        if updated:
            # Buscamos los actores asociados
            idActorsList = oActUserHist.idActorsAsociatedToUserHistory(idHistory)
            # Eliminamos los actores asociados
            for id in idActorsList:
                insertedAct = oActUserHist.deleteActorAsociatedInUserHistory(id,idHistory)
            # Insertamos los nuevos actores seleccionados
            for id in idActors:
                insertedAct = oActUserHist.insertActorAsociatedInUserHistory(id,idHistory)

            # Buscamos los objetivos asociados
            idObjectivesList = oObjUserHist.idObjectivesAsociatedToUserHistory(idHistory)
            # Eliminamos los objetivos asociados
            for id in idObjectivesList:
                insertedObj = oObjUserHist.deleteObjectiveAsociatedInUserHistory(id,idHistory)
            # Insertamos los nuevos objetivos seleccionados
            for id in idObjectives:
                insertedAct = oObjUserHist.insertObjectiveAsociatedInUserHistory(id,idHistory)

            if not oUserHist.isEpic:
                result = oUserHist.updatePriority(priority)

            res = results[0]

    res['label'] = res['label'] + '/'+str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

# @historias.route('/historias/ACompletarHistoria', methods=['GET'])
# def ACompletarHistoria():
#     params  = request.get_json()
#     idHistory    = request.args.get('idHistoria')
#     results = [{'label':'/VHistoria/'+idHistory, 'msg':['La historia fue marcada como completada']}, {'label':'/VHistoria/'+idHistory, 'msg':['Error al modificar historia']}, ]
#     res     = results[1]

#     # Obtenemos el id del Producto.
#     idPila  = int(session['idPila'])

#     # Extraemos los valores
#     oUserHist    = userHistory()

#     completed = oUserHist.completeHistory(int(idHistory))
#     if completed == True:
#         res = results[0]
#     return json.dumps(res)

# @historias.route('/historias/AIncompletarHistoria', methods=['GET'])
# def AIncompletarHistoria():
#     params  = request.get_json()
#     idHistory    = request.args.get('idHistoria')
#     results = [{'label':'/VHistoria/'+idHistory, 'msg':['La historia fue marcada como incompleta']}, {'label':'/VHistoria/'+idHistory, 'msg':['Error al modificar historia']}, ]
#     res     = results[1]

#     # Obtenemos el id del Producto.
#     idPila  = int(session['idPila'])

#     # Extraemos los valores
#     oUserHist    = userHistory()

#     incompleted = oUserHist.incompleteHistory(int(idHistory))
#     if incompleted == True:
#         res = results[0]
#     return json.dumps(res)


@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
    res = {}

    # Obtenemos el id del producto.
    idPila = int(request.args.get('idPila',1))

    if "actor" in session:
        res['actor']=session['actor']

    scale = {1:'Alta',2:'Media',3:'Baja'}

    # Obtenemos los datos asociados al producto
    oBacklog      = backlog()
    oObjective    = objective()

    actorList     = oBacklog.actorsAsociatedToProduct(idPila)
    accionList    = oBacklog.accionsAsociatedToProduct(idPila)
    objectiveList = oBacklog.objectivesAsociatedToProduct(idPila)
    historyList   = oBacklog.userHistoryAsociatedToProduct(idPila)

    # Obtenemos todos los objetivos que son no trasnversales.
    for object in objectiveList:
        idObjective = object.O_idObjective
        transverse  = oObjective.verifyObjectiveTransverse(idObjective)
        if int(transverse) == 1:
            objectiveList.remove(object)

    # Hallamos el tipo de escala seleccionado para el producto.
    typeScale = oBacklog.scaleType(idPila)

    # Obtenemos el tipo de escala asociado al producto (id,valor)
    resultScale = []
    if typeScale == 1:
        resultScale = [(i,scale[i]) for i in range(1,3+1)]
    elif typeScale == 2:
        resultScale = [(i,i) for i in range(1,20+1)]

    # Valores dependientes del proyecto.
    res['fHistoria_opcionesActores']       = [{'key':act.A_idActor ,'value':act.A_nameActor }for act in actorList]
    res['fHistoria_opcionesAcciones']      = [{'key':acc.AC_idAccion,'value':acc.AC_accionDescription}for acc in accionList]
    res['fHistoria_opcionesAcciones'].append({'key':0,'value':'Seleccione una acción'})
    res['fHistoria_opcionesObjetivos']     = [{'key':obj.O_idObjective ,'value':obj.O_descObjective}for obj in objectiveList]
    res['fHistoria_opcionesHistorias']     = [{'key':hist.UH_idUserHistory,'value':hist.UH_codeUserHistory}for hist in historyList]
    res['fHistoria_opcionesHistorias'].append({'key':0,'value':'Ninguno'})
    res['fHistoria_opcionesTiposHistoria'] = [{'key':1,'value':'Opcional'},{'key':2,'value':'Obligatoria'}]
    res['fHistoria_opcionesTiposHistoria'].append({'key':0,'value':'Seleccione un tipo de acción'})
    res['fHistoria_opcionesPrioridad']     = [{'key':scale[0], 'value':scale[1]}for scale in resultScale]
    res['fHistoria_opcionesPrioridad'].append({'key':0,'value':'Seleccione una prioridad'})
    res['fHistoria'] = {'super':0, 'idPila':idPila,'actores':[],'objetivos':[],'accion':0,'tipo':0,'prioridad':0}
    res['idPila']    = idPila

    return json.dumps(res)



@historias.route('/historias/VDesempeno')
def VDesempeno():
    #GET parameter
    idHistoria = request.args['idHistoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idHistoria'] = int(idHistoria)

    #Action code ends here
    return json.dumps(res)



@historias.route('/historias/VHistoria')
def VHistoria():
    #GET parameter
    res = {}

    # Obtenemos el id del producto y de la historia.
    idPila    = int(session['idPila'])
    idHistory = int(request.args.get('idHistoria'))

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    scale = {0:'No tiene escala asignada por ser Épica',1:'Alta',2:'Media',3:'Baja'}

    oBacklog      = backlog()
    oObjective    = objective()
    oTarea        = task()
    oUserHist     = userHistory()
    oActUserHist  = actorsUserHistory()
    oObjUserHist  = objectivesUserHistory()

    # Obtenemos la historia que queremos modificar.
    history = oUserHist.searchIdUserHistory(idHistory)
    history = history[0]

    # Obtenemos todas las acciones, actores y objetivos asociados al producto.
    actorList     = oBacklog.actorsAsociatedToProduct(idPila)
    accionList    = oBacklog.accionsAsociatedToProduct(idPila)
    objectiveList = oBacklog.objectivesAsociatedToProduct(idPila)

    # Obtenemos todas las historias de usuarios excepto la actual
    historias =  oUserHist.getAllUserHistoryId(idPila)
    for hist in historias:
        if hist.UH_idUserHistory == idHistory:
            historias.remove(hist)
            break

    # Obtenemos todos los objetivos que son no trasnversales.
    for object in objectiveList:
        idObjective = object.O_idObjective
        transverse  = oObjective.verifyObjectiveTransverse(idObjective)
        if int(transverse) == 1:
            objectiveList.remove(object)

    taskList = oTarea.getAllTask(idHistory)

    # Obtenemos los actores asociados a una historia de usuario.
    actors = oActUserHist.idActorsAsociatedToUserHistory(idHistory)

    # Obtenemos los objetivos asociados a una historia de usuario.
    objectives = oObjUserHist.idObjectivesAsociatedToUserHistory(idHistory)

    # Obtenemos la escala asociada a la historia (la que se selecciono para el producto)
    typeScale = oBacklog.scaleType(idPila)

    # Obtenemos la escala asignada a la historia actual
    numScale  = history.UH_scale

    # Obtenemos las pruebas de la historia actual
    testsList = oUserHist.testsAsociatedToUserHistory(idHistory)

    resultScale = []
    if numScale == 0:
        resultScale = [(0,scale[0])]
    else:
        # Obtenemos el tipo de escala asociado al producto (id,valor)
        if typeScale == 1:
            resultScale = [(i,scale[i]) for i in range(1,3+1)]
        elif typeScale == 2:
            resultScale = [(i,i) for i in range(1,20+1)]

    res['fHistoria_opcionesHistorias']     = [{'key':hist.UH_idUserHistory,'value':hist.UH_codeUserHistory}for hist in historias]
    res['fHistoria_opcionesHistorias'].append({'key':0,'value':'Ninguno'})
    res['fHistoria_opcionesTiposHistoria'] = [{'key':1,'value':'Opcional'},{'key':2,'value':'Obligatoria'}]
    res['fHistoria_opcionesActores']       = [{'key':act.A_idActor,'value':act.A_nameActor}for act in actorList]
    res['fHistoria_opcionesAcciones']      = [{'key':acc.AC_idAccion,'value':acc.AC_accionDescription}for acc in accionList]
    res['fHistoria_opcionesObjetivos']     = [{'key':obj.O_idObjective,'value':obj.O_descObjective}for obj in objectiveList]
    res['fHistoria_opcionesPrioridad']     = [{'key':scale[0], 'value':scale[1]}for scale in resultScale]

    startingDate_object_new = datetime.strftime(history.UH_fechaInicio, '%d/%m/%Y')
    finishingDate_object_new = datetime.strftime(history.UH_fechaFin, '%d/%m/%Y')

    res['fHistoria'] = {'super':history.UH_idSuperHistory , 'idHistoria':idHistory, 'idPila':history.UH_idBacklog,
                        'codigo':history.UH_codeUserHistory,'actores':actors, 'accion':history.UH_idAccion,
                        'objetivos':objectives, 'tipo':history.UH_accionType, 'prioridad':history.UH_scale,
                        'iniciado': history.UH_iniciado, 'fechaInicio': startingDate_object_new,
                        'completed': history.UH_completed, 'fechaFin': finishingDate_object_new}

    res['data2'] = [{'idTarea':tarea.HW_idTask, 'descripcion':tarea.HW_description}for tarea in taskList]

    res['pruebas'] = [{'idTarea':test.AT_idAT,
                        'descripcion':test.AT_description,
                        'url': test.AT_urlScript} for test in testsList]

    session['idHistoria'] = idHistory
    res['idHistoria'] = idHistory
    session['idPila'] = idPila
    res['idPila']     = idPila

    return json.dumps(res)


@historias.route('/historias/VHistorias')
def VHistorias():
    #GET parameter
    res = {}

    # Obtenemos el id del producto y de la historia.
    idPila = int(request.args.get('idPila',1))

    if "actor" in session:
        res['actor'] = session['actor']

    oTask             = task()
    oActor            = role()
    oAccion           = accions()
    oObjective        = objective()
    oBacklog          = backlog()
    oUserHistory      = userHistory()
    oActUserHist      = actorsUserHistory()
    oObjUserHIst      = objectivesUserHistory()

    # Obtenemos las historias asociadas al producto idPila.
    userHistoriesList = oBacklog.userHistoryAsociatedToProduct(idPila)

    pesos          = []
    userHistories  = []
    options        = {1:'podria ',2:'puede '}
    priorities     = {0:'Epica',1:'Alta',2:'Media',3:'Baja'}
    priorities2    = {i:str(i)for i in range(1,20+1)}
    priorities2[0] = 'Epica'

    # Obtenemos el tipo de escala seleccionada en el producto asociado a la historia.
    typeScale = oBacklog.scaleType(idPila)

    # Obtenemos los valores de cada historia en un diccionario y almacenamos esos
    # diccionarios en un arreglo.
    for hist in userHistoriesList:
        result = oUserHistory.transformUserHistory(hist.UH_idUserHistory)
        userHistories.append(result)
        tupla = (hist.UH_idUserHistory,oTask.historyWeight(hist.UH_idUserHistory))
        pesos.append(tupla)

    # Obtenemos el maximo de la escala
    if typeScale == 1:
        iterations = 3
    elif typeScale == 2:
        iterations = 20

    historiesSortedByPriority = []
    # Ordenamos las tuplas por prioridad
    for i in range(iterations + 1):
        idsHistories = []
        for hist in userHistories:

            if hist['priority'] == i:
                # Convertimos a escala Alta, Media, Baja si es necesario
                if typeScale == 1:
                    hist['priority'] = priorities[i]
                elif typeScale == 2:
                    hist['priority'] = priorities2[i]
                historiesSortedByPriority.append(hist)
                # Almacenamos los ids de las historias ordenadas
                idsHistories.append(hist['idHistory'])

        # Eliminamos de userHistories las historias ordenadas.
        for id in idsHistories:
            for hist in userHistories:
                if hist['idHistory'] == id:
                    userHistories.remove(hist)
                    break


    res['data0']      = [{'idHistoria':hist['idHistory'],
                          'prioridad' :hist['priority'],
                          'peso'      :oTask.lookup(pesos,hist['idHistory']),
                          'enunciado' :'En tanto ' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives']}for hist in historiesSortedByPriority]
    session['idPila'] = idPila
    res['idPila']     = idPila

    return json.dumps(res)



@historias.route('/historias/VPrioridades')
def VPrioridades():
    #GET parameter
    res = {}

    # Obtenemos el id del producto.
    idPila    = int(session['idPila'])

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    oActor            = role()
    oAccion           = accions()
    oObjective        = objective()
    oBacklog          = backlog()
    oUserHistory      = userHistory()
    oActUserHist      = actorsUserHistory()
    oObjUserHIst      = objectivesUserHistory()

    # Obtenemos las historias de usuario asociadas al producto.
    userHistoriesList = oBacklog.userHistoryAsociatedToProduct(idPila)

    userHistories = []
    options       = {1:'podría ',2:'puede '}
    scale         = {1:'Alta',2:'Media',3:'Baja'}

    # Obtenemos el tipo de escala asociada al producto.
    typeScale = oBacklog.scaleType(idPila)

    # Obtenemos el tipo de escala asociado al producto (id,valor) y elvalor maximo de la escala
    if typeScale == 1:
        iterations  = 3
        resultScale = [(i,scale[i]) for i in range(1,3+1)]
    elif typeScale == 2:
        iterations  = 20
        resultScale = [(i,i) for i in range(1,20+1)]

    # Obtenemos los valores de cada historia en un diccionario y almacenamos esos
    # diccionarios en un arreglo.
    for hist in userHistoriesList:
        epic = oUserHistory.isEpic(hist.UH_idUserHistory)
        if not epic:
            result = oUserHistory.transformUserHistory(hist.UH_idUserHistory)
            userHistories.append(result)

    historiesSortedByPriority = []
    # Ordenamos las tuplas por prioridad
    for i in range(iterations + 1):
        for hist in userHistories:
            if hist['priority'] == i:
                historiesSortedByPriority.append(hist)
                userHistories.remove(hist)

    #Escala dependiente del proyecto
    res['fPrioridades_opcionesPrioridad'] = [{'key':scale[0], 'value':scale[1]}for scale in resultScale]
    res['fPrioridades'] = {'idPila':idPila,'lista':[{'idHistoria':hist['idHistory'],'prioridad':hist['priority'], 'enunciado':'En tanto ' + hist['actors'] + hist['accions'] + ' para ' + hist['objectives']}for hist in historiesSortedByPriority]}
    res['idPila']       = idPila

    return json.dumps(res)

## ROUTES MAGOCA
@historias.route('/historias/APrelaciones', methods=['POST'])
def APrelaciones():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrelaciones', 'msg':['Cambios almacenados']}, {'label':'/VPrelaciones', 'msg':['Error al guardar prelaciones']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    oPrecedence = precedence()
    # Obtenemos prelaciones ya existentes en el producto
    previous = oPrecedence.getAllPrecedences(session['idPila'])
    # Buscamos que precedencias fueron eliminadas y agregadas por el usuario e ignoramos las que no fueron cambiadas
    for object in previous:
        esta = False
        for i in params['lista']:
            if (object.P_idFirstTask == int(i['antecedente']) and object.P_idSecondTask == int(i['consecuente'])):
                esta = True
                params['lista'].remove(i)
        if not esta: # Fue eliminada
            oPrecedence.deletePrecedence(object.P_idFirstTask, object.P_idSecondTask) #Podria eliminar el objeto directamente, sin el deletePrecedence

    for i in params['lista']: # Los que van a ser agregados
        if (int(i['antecedente']) == int(i['consecuente'])): # Este if se puede quitar porque se esta haciendo la verficiacion en insertPrecedence
            print('Error, la historia no debe prelarse a si misma')
        else:
            oPrecedence.insertPrecedence(int(i['antecedente']), int(i['consecuente']), session['idPila'])

    res['label'] = res['label'] + '/' + repr(1)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@historias.route('/historias/VPrelaciones')
def VPrelaciones():
    #GET parameter
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario'] = session['usuario']

    # Obtenemos el id del producto y de la historia.
    idPila = request.args['idPila']

    oBacklog          = backlog()
    oUserHistory      = userHistory()
    oTask             = task()
    oPrecedence       = precedence()


    #Hacer query para obtener las prelaciones que existen ya en este producto y devolverlas en fPrelaciones
    lista = []
    precedenceList = oPrecedence.getAllPrecedences(idPila)
    for object in precedenceList:
        lista.append({'antecedente':object.P_idFirstTask, 'consecuente':object.P_idSecondTask})

    res['fPrelaciones'] = {'lista':lista}

    #res['fPrelaciones'] = {'lista':[
    #  {'antecedente':1, 'consecuente':2},
    #  {'antecedente':2, 'consecuente':3}]}



    res['idPila'] = idPila

    #Hacer query para obtener las tareas de esta historia y devolverlas con su id y valor en una lista
    userHistoriesList = oBacklog.userHistoryAsociatedToProduct(int(idPila))
    taskList = []
    #tasks = []

    #Se obtienen todas las tareas de las historias de usuarios
    for hist in userHistoriesList:
        taskList.extend(oTask.taskAsociatedToUserHistory(hist.UH_idUserHistory))

    #Se transforman las tareas para la vista
    #for listaT in taskList:
    #    for tarea in listaT:
    #    tasks.append(tarea)

    res['fPrelaciones_listaTareas'] = [{'key':tarea.HW_idTask, 'value':tarea.HW_description + ' | historia:' + oUserHistory.getUHCodeFromId(tarea.HW_idUserHistory)}for tarea in taskList]

    #Action code ends here
    return json.dumps(res)



#Use case code starts here


#Use case code ends here
