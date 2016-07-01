# -*- coding: utf-8 -*-

from flask               import request, session, Blueprint, json
from app.scrum.objective import *
from app.scrum.backLog   import *
from app.scrum.objectivesUserHistory   import *

objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res     = results[1]
    
    # Obtenemos el id del producto
    idPila  = int(session['idPila'])
    
    if request.method == 'POST':
    
        # Extraemos los parámetros
        newDescription      = params['descripcion']
        transverseObjective = params['transversal']
        funcionalObjective  = params['funcional']
        
        oObjective = objective()
        result     = oObjective.insertObjective(newDescription,idPila,funcionalObjective,transverseObjective)

        if result:
            res = results[0]

    res['label'] = res['label'] + '/' + str(idPila)
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
            
    return json.dumps(res)



@objetivo.route('/objetivo/AElimObjetivo')
def AElimObjetivo():
    #GET parameter
    results = [{'label':'/VProducto', 'msg':['Objetivo eliminado']}, {'label':'/VProducto', 'msg':['No se pudo eliminar este objetivo']}, ]
    res     = results[1] 
    
    # Obtenemos el id del producto
    idPila       = int(session['idPila'])
    idObjective  = int(session['idObjective'])
    
    # Conseguimos el objetivo a eliminar  
    oObjetivo    = objective()
    found = oObjetivo.searchIdObjective(idObjective) 
    
    oObjUserHistory = objectivesUserHistory()
    result = oObjUserHistory.searchidUserHistoryIdObjective(idObjective)
    
    # Verificamos si el objetivo está asociado a una historia
    if (result == []):
        deleted = oObjetivo.deleteObjective(found[0].O_descObjective,idPila) 

        if deleted:
            res = results[0]  

    res['label'] = res['label'] +  '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VProducto', 'msg':['Error al modificar objetivo']}, ]
    res     = results[1] 
    
    # Obtenemos el id del producto
    idPila  = int(session['idPila'])
    
    # Extraemos los parámetros
    idObjetivo     = params['idObjetivo']  
    newDescription = params['descripcion'] 
    newType        = params['transversal']
    newFunc        = params['funcional'] 
        
    # Conseguimos el objetivo a modificar
    oObjetivo    = objective()
    objetivoDesc = oObjetivo.searchIdObjective(idObjetivo) 

    # Modificamos la descripción del objetivo    
    result       = oObjetivo.updateObjective(objetivoDesc[0].O_descObjective , newDescription,newType,newFunc,idPila) 

    if result:
        res = results[0]
        
    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
            
    return json.dumps(res)



@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto y del objetivo
    idPila      = int(session['idPila'])
    idObjective = int(request.args.get('idObjetivo'))
    boolean = {0:False,1:True}
    
    if "actor" in session:
        res['actor']=session['actor']
        
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    res['usuario'] = session['usuario']
    
    # Determinamos el tipo de objetivo a través de su id
    oObjective = objective()
    result     = oObjective.searchIdObjective(idObjective)
    try:
        number     = int(result[0].O_objType)
    except TypeError:
        number = 0
    if result[0].O_objFunc is None:
        funcional  = 0
    else:
        funcional = result[0].O_objFunc
    print(funcional)
    istransver = boolean.get(number,-1)
    

    # Mostramos los objetivos en la vista
    res['fObjetivo_opcionesFuncional'] = [{'key':True, 'value':'Si'},{'key':False, 'value':'No'}]
    res['fObjetivo_opcionesTransversalidad'] = [{'key':True, 'value':'Si'},{'key':False, 'value':'No'}]
    res['fObjetivo'] = {'idObjetivo':idObjective, 'descripcion':result[0].O_descObjective , 'transversal':istransver,
                        'funcional':funcional
    }    
    res['idPila']    = idPila
    session['idObjective'] = idObjective

    return json.dumps(res)



@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    #GET parameter
    res = {}
    
    # Obtenemos el id del producto
    idPila = request.args.get('idPila',1)
    
    if "actor" in session:
        res['actor']=session['actor']
        
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
   
    res['fObjetivo_opcionesTransversalidad'] = [{'key':True, 'value':'Si'},
                                                {'key':False, 'value':'No'},]
    res['fObjetivo_opcionesFuncional'] = [{'key':True, 'value':'Si'},
                                                {'key':False, 'value':'No'}]
    res['fObjetivo'] = {'transversal':False, 'funcional':False} 
    res['idPila']    = idPila   

    return json.dumps(res)




#Use case code starts here


#Use case code ends here
