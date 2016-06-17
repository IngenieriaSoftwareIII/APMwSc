# -*- coding: utf-8 -*-
import os
from flask                 import request, session, Blueprint, json, render_template, redirect
from app.scrum.backLog     import *
from app.scrum.userHistory import *
from app.scrum.task        import *
from app.scrum.model       import *
from app.scrum.Team        import *
from datetime              import datetime

from werkzeug import secure_filename

tareas = Blueprint('tareas', __name__)
basedir=os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))+"/static"


@tareas.route('/tareas/ACrearTarea', methods=['POST'])
def ACrearTarea():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea creada']}, {'label':'/VHistoria', 'msg':['No se pudo crear tarea.']}, ]
    res     = results[0]

    # Obtenemos el id de la historia actual
    idHistory = int(session['idHistoria'])

    # Extraemos los parámetros
    taskDesc    = params['descripcion']
    idCategoria = params['categoria']
    taskPeso    = params['peso']

    if 'iniciado' in params:
        started = params['iniciado']
    else:
        started = False

    if 'fechaInicio' in params:
            startingDate= params['fechaInicio']
            try:
                startingDate_object = datetime.strptime(startingDate, '%d/%m/%Y')
            except ValueError:
                res     = results[1]
                res['label'] = res['label'] + '/'+str(idHistory)
                return json.dumps(res)
    else:
        startingDate_object = None

    if 'completed' in params:
        completed = params['completed']
    else:
        completed = False

    if 'fechaFin' in params:
            finishingDate = params['fechaFin']
            try:
                finishingDate_object = datetime.strptime(finishingDate, '%d/%m/%Y')
            except ValueError:
                res     = results[1]
                res['label'] = res['label'] + '/'+str(idHistory)
                return json.dumps(res)
    else:
        finishingDate_object = None

    oBackLog    = backlog()
    oTask       = task()

    if 'miembro' in params:
        miembro = params['miembro']
    else:
        miembro = None

    insert   = oTask.insertTask(taskDesc, idCategoria, taskPeso, idHistory, started, startingDate_object, completed, finishingDate_object)
    if insert:
        res = results[0]

        insertedTask = oTask.searchTask(taskDesc)[0]

        if miembro == None or miembro < 0:
            oTask.deleteUserTask(int(insertedTask.HW_idTask))
        else:
            oTask.insertUserTask(int(insertedTask.HW_idTask), int(miembro))

    else:
        res = results[1]
    res['label'] = res['label'] + '/' + str(idHistory)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AElimTarea')
def AElimTarea():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea borrada']}, {'label':'/VHistoria', 'msg':['No se pudo eliminar la tarea']}, ]
    res     = results[1]

    # Obtenemos los parámetros
    idHistoria = int(session['idHistoria'])
    idTarea    = int(session['idTarea'])

    # Eliminamos la tarea
    oTarea     = task()
    result     = clsTask.query.filter_by(HW_idTask = idTarea).first()
    delete     = oTarea.deleteTask(result.HW_description)

    if delete:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idHistoria)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@tareas.route('/tareas/AElimDoc')
def AElimDoc():
    #POST/PUT parameters
    params  = request.get_json()
    results = [ { 'label' : '/VHistoria'
                , 'msg'   : ['Documento borrado']
                }
              , { 'label' : '/VHistoria'
                , 'msg'   : ['No se pudo eliminar el documento']
                } 
              ]
    res     = results[1]

    # Obtenemos los parámetros
    docName = request.args.get('name')
    taskId  = request.args.get('tarea')
    docsDir = basedir + "/TaskDocuments"
    dirName = docsDir + "/" + taskId

    # Eliminamos la tarea
    oTarea     = task()
    delete     = oTarea.deleteDoc(taskId,docName)
    if os.path.exists(dirName + "/" + docName):
        os.remove(dirName + "/" + docName)
    if delete:
        res = results[0]

    res['label'] = res['label'] + '/' + str(taskId)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AModifTarea', methods=['POST'])
def AModifTarea():
    #POST/PUT parameters
    params  = request.get_json()
    results =   [ { 'label' : '/VHistoria'
                  , 'msg'   : ['Tarea modificada']
                  }
                , { 'label' : '/VHistoria'
                  , 'msg'   : ['Error al modificar tarea']
                  }
                ]
    res     = results[1]

    # Obtenemos los parámetros
    idHistoria          = int(session['idHistoria'])
    new_description     = params['descripcion']
    idTarea             = params['idTarea'    ]
    new_idCategoria     = params['categoria'  ]
    new_taskPeso        = params['peso'       ]
    new_estimatedTime   = params['tiempo'     ]
    new_miembro         = params['miembro'    ]
    started             = params['iniciado'   ]
    startingDate        = params['fechaInicio']
    completed           = params['completed'  ]
    finishingDate       = params['fechaFin'   ]
    hours_spent = params['Horas_Trabajadas']

    try:
        startingDate_object = datetime.strptime(startingDate, '%d/%m/%Y')
        finishingDate_object = datetime.strptime(finishingDate, '%d/%m/%Y')
    except ValueError:
        res     = results[1]
        res['label'] = res['label'] + '/'+str(idHistoria)
        return json.dumps(res)

    # Buscamos la tarea a modificar
    oTarea   = task()
    result   = clsTask.query.filter_by(HW_idTask = idTarea).first()
    # Modificamos la tarea
    if startingDate_object.date() <= finishingDate_object.date():

        modify = oTarea.updateTask( result.HW_description
                                  , new_description
                                  , new_idCategoria
                                  , new_taskPeso
                                  , new_estimatedTime
                                  , started
                                  , startingDate_object
                                  , completed
                                  , finishingDate_object
                                  ,hours_spent
                                  )

    else:
        modify = None
        res = results[1]
        res['msg'][0] = res['msg'][0] + ": La fecha de culminación debe ser mayor o igual que la de inicio."

    if new_miembro == None or new_miembro < 0:
        oTarea.deleteUserTask(int(idTarea))
    else:
        oTarea.insertUserTask(int(idTarea), int(new_miembro))

    if modify:
        res = results[0]

    res['label'] = res['label'] + '/' + str(idHistoria)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@tareas.route('/tareas/ACompletarTarea', methods=['GET'])
def ACompletarTarea():
    params  = request.get_json()
    idTarea    = request.args.get('idTarea')
    results = [ { 'label' : '/VTarea/' + idTarea
                , 'msg'   : ['La tarea fue marcada como completada']
                }
              , { 'label' : '/VTarea/' + idTarea
                , 'msg'   : ['Error al modificar tarea']
                }
              ]
    res     = results[1]

    # Obtenemos el id del Producto.
    idPila  = int(session['idPila'])

    # Extraemos los valores
    oTarea    = task()

    completed = oTarea.completeTask(int(idTarea))
    if completed == True:
        res = results[0]
    return json.dumps(res)

@tareas.route('/tareas/AIncompletarTarea', methods=['GET'])
def AIncompletarTarea():
    params  = request.get_json()
    idTarea    = request.args.get('idTarea')
    results = [ { 'label' : '/VTarea/' + idTarea
                , 'msg'   : ['La tarea fue marcada como incompleta']
                }
              , { 'label' : '/VTarea/' + idTarea
                , 'msg'   : ['Error al modificar tarea']
                }
              ]
    res     = results[1]

    # Obtenemos el id del Producto.
    idPila  = int(session['idPila'])

    # Extraemos los valores
    oTarea    = task()

    incompleted = oTarea.incompleteTask(int(idTarea))
    if incompleted == True:
        res = results[0]
    return json.dumps(res)


@tareas.route('/tareas/VCrearTarea')
def VCrearTarea():
    #GET parameter
    res = {}
    # Obtenemos el id de la historia actual
    idHistory = int(request.args.get('idHistoria'))

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    # Buscamos la historia actual
    oUserHistory = userHistory()
    hist         = oUserHistory.searchIdUserHistory(idHistory)

    res['usuario']        = session['usuario']
    res['codHistoria']    = hist[0].UH_codeUserHistory

    # Obtenemos una lista con los datos asociados a las categorías
    cateList    = clsCategory.query.all()

    idTarea     = request.args.get('idTarea')
    result      = clsTask.query.filter_by(HW_idTask = idTarea).first()
    cateList    = clsCategory.query.all()
    oTeam       = team()
    found       = clsUserHistory.query.filter_by(UH_idUserHistory = idHistory).first()
    miembroList = oTeam.getTeam(found.UH_idBacklog)

    # Mostramos los datos en la vista
    ListaCompleta = []
    for i in cateList:
        ListaCompleta.append((i.C_idCategory,i.C_nameCate,i.C_weight))

    decorated = [(tup[2], tup) for tup in ListaCompleta]
    decorated.sort()

    res['fTarea_opcionesCategoria'] = [ { 'key':cat[1][0]
                                        , 'value':cat[1][1] + " (" + str(cat[1][2]) + ")"
                                        , 'peso':cat[1][2]
                                        } for cat in decorated
                                      ]

    res['fTarea_opcionesMiembro'] = [ { 'key'   : -1
                                      , 'value' : 'Sin asignacion'
                                      }
                                    ] + [ 
                                      { 'key'   : miembro.EQ_idEquipo 
                                      , 'value' : miembro.EQ_username
                                      } for miembro in miembroList
                                    ]

    res['fTarea']         = {'idHistoria' : idHistory}
    res['idHistoria']     = idHistory
    session['idHistoria'] = idHistory
    

    return json.dumps(res)


@tareas.route('/tareas/VTarea')
def VTarea():
    #GET parameter

    # Obtenemos el id de la historia y de la tarea
    idTarea     = int(request.args['idTarea'])
    idHistoria  = int(request.args['idHistoria'])

    found       = clsUserHistory.query.filter_by(UH_idUserHistory = idHistoria).first()
    codHistoria = found.UH_codeUserHistory

    res = {}
    if "actor" in session:
        res['actor'] = session['actor']

    idTarea         = request.args.get('idTarea')
    oTarea          = task()
    result          = clsTask.query.filter_by(HW_idTask = idTarea).first()
    categoryList    = clsCategory.query.all()
    oTeam           = team()
    miembroList     = oTeam.getTeam(found.UH_idBacklog)

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    res['usuario']      = session['usuario']
    res['codHistoria']  = codHistoria

    res['fTarea_opcionesCategoria'] = [ { 'key'   : cat.C_idCategory
                                        , 'value' : cat.C_nameCate + " (" + str(cat.C_weight) + ")"
                                        , 'peso'  : result.HW_weight
                                        } for cat in categoryList
                                      ]

    res['fTarea_opcionesMiembro'] = [ { 'key'   : -1
                                      , 'value' : 'Sin asignacion'
                                      }
                                    ] + [ 
                                      { 'key'   : miembro.EQ_idEquipo 
                                      , 'value' : miembro.EQ_username
                                      } for miembro in miembroList
                                    ]
    try:
        startingDate_object_new = datetime.strftime(result.HW_fechaInicio, '%d/%m/%Y')
    except TypeError:
        startingDate_object_new = datetime.strftime(datetime.now(), '%d/%m/%Y')
    
    try:
        finishingDate_object_new = datetime.strftime(result.HW_fechaFin, '%d/%m/%Y')
    except TypeError:
        finishingDate_object_new = datetime.strftime(datetime.now(), '%d/%m/%Y')

    res['fTarea'] = { 'idHistoria'  : idHistoria
                    , 'idTarea'     : idTarea
                    , 'descripcion' : result.HW_description
                    , 'categoria'   : result.HW_idCategory
                    , 'peso'        : result.HW_weight
                    , 'miembro'     : result.HW_idEquipo
                    , 'tiempo'      : result.HW_estimatedTime
                    , 'iniciado'    : result.HW_iniciado
                    , 'fechaInicio' : startingDate_object_new
                    , 'completed'   : result.HW_completed
                    , 'fechaFin'    : finishingDate_object_new 
                    ,'Horas_Trabajadas':result.HW_horasEmpleadas 
                    }

    session['idTarea']    = idTarea
    res    ['idTarea']    = idTarea
    res    ['idHistoria'] = idHistoria

    documentos = taskDocs_by_taskId(idTarea)
    if documentos is None:
        print("documentos esta vacio")
        res = {'msg' : 'No hay documentos para adjuntos a esta tarea'}
    else:
        docsJson = []
        for documento in documentos:
            docsJson.append( { 'name'        : documento.getName()
                             , 'descripcion' : documento.getDescription()
                             , 'url'         : 'TaskDocuments/' + idTarea + '/' + documento.getName()
                             })
        res['documentos'] = docsJson

    return json.dumps(res)

@tareas.route('/tareas/upload', methods=['POST'])
def upload():
    file = request.files['file']
    idTask = request.form.get('idTarea')
    docDescription = request.form.get('docDescription')
    if file and allowed_file(file.filename):
        docName = file.filename
        docsDir=basedir+"/TaskDocuments"
        dirName=docsDir+"/"+idTask

        #verifica si existe la carpeta TaskDocuments, caso contrario la crea
        if not(os.path.exists(docsDir)):
            os.mkdir(docsDir)
        #verifica si existe la carpeta especifica de la tarea, caso contrario la crea
        if not(os.path.exists(dirName)):
            os.mkdir(dirName)
        if os.path.exists(dirName+"/"+docName):
            i = 1
            original = docName
            while os.path.exists(dirName+"/"+docName):
                docName = original+"("+str(i)+")"
                print(docName)
                i += 1
        file.save(os.path.join(dirName, docName))
        try:
            taskDoc = clsTaskDoc(idTask,docName,docDescription)
            taskDoc.save()
        except:
            print("error al guardar el documento")
        return redirect("#/VTarea/"+idTask)

def allowed_file(filename):
    return True#'.' in filename and \
  #         filename.rsplit('.', 1)[1] in get_extensions()




#Use case code ends here

