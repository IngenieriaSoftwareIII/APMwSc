# -*- coding: utf-8 -*-
from flask             import request, session, Blueprint, json
from app.scrum.backLog import *


prod = Blueprint('prod', __name__)


@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res     = results[1]
    
    if params != {}:    
        # Extraemos los parámetros
        prodName  = params['nombre']
        prodDesc  = params['descripcion']
        prodScale = params['escala']
        
        oBacklog = backlog()
        inserted = oBacklog.insertBacklog(prodName,prodDesc,prodScale)
        
        if inserted:
            # Obtenemos el producto insertado
            result = oBacklog.findName(prodName)
            res['idPila'] = result[0].BL_idBacklog 
        
            if result:
                res = results[0]
        
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']}, {'label':'/VProductos', 'msg':['Error al modificar el producto']}]
    res     = results[1]
    
    # Obtenemos los parámetros
    newname        = params['nombre']
    newdescription = params['descripcion']
    newscale       = params['escala']
    idPila         = params['idPila'] 
    newstatus      = params['Estado']

    oBacklog = backlog()
    
    # Buscamos el producto a modificar
    result = oBacklog.findIdProduct(idPila)
    result = oBacklog.modifyBacklog(result.BL_name, newname, newdescription, newscale, newstatus)      
    
    if result:
        res = results[0]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    res = {}
    # Buscamos el id del producto.
    idPila = int(request.args.get('idPila',1))
      
    if "actor" in session:
        res['actor']=session['actor']
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    res['fPila_opcionesEscala'] = [ { 'key'   : 1
                                    , 'value' : 'Alta/Media/Baja'
                                    }
                                  , { 'key'   : 2
                                    , 'value' : 'Entre 1 y 20'
                                    }
                                  , { 'key'   : 0
                                    , 'value' : 'Seleccione un tipo de escala'
                                    }
                                  ]
    res['fPila'] = {'escala':0}

    return json.dumps(res)



@prod.route('/prod/VProducto')
def VProducto():
    #GET parameter
    res = {}
    # Obtenemos el id del producto
    idPila = int(request.args.get('idPila', 1))
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Obtenemos los datos asociados al producto
    oBacklog   = backlog()
    actorsList = oBacklog.actorsAsociatedToProduct(idPila)
    accionList = oBacklog.accionsAsociatedToProduct(idPila)
    objectList = oBacklog.objectivesAsociatedToProduct(idPila)
    
    # Mostramos los datos en la vista.
    res['data3'] = [{'idActor':act.A_idActor,'descripcion':act.A_nameActor + ' : ' + act.A_actorDescription}for act in actorsList]
    res['data5'] = [{'idAccion':acc.AC_idAccion , 'descripcion':acc.AC_accionDescription}for acc in accionList]
    res['data7'] = [{'idObjetivo':obj.O_idObjective, 'descripcion':obj.O_descObjective } for obj in objectList]
      
    # Buscamos el producto actual
    result = oBacklog.findIdProduct(idPila)
     
    # Mostramos los valores seleccionados
    res['fPila'] = {'idPila':idPila,'nombre': result.BL_name,'descripcion':result.BL_description,'escala':result.BL_scaleType, 'Estado' : result.BL_statusType}
    res['fPila_opcionesEscala'] = [{'key':1,'value':'Alta/Media/Baja'}, {'key':2,'value':'Entre 1 y 20'}]
    res['fPila_opcionesEstado']=[{'key':1,'value':'Por iniciar'}, {'key':2,'value':'En construcción'}, {'key':3,'value':'Culminado'}]
    
    # Guardamos el id del producto
    session['idPila'] = idPila
    res['idPila']     = idPila
    
    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
        
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    # Obtenemos la lista de productos
    oBacklog    = backlog() 
    productList = oBacklog.getAllProducts()
    
    res['data0'] = [{'idPila':prod.BL_idBacklog,'nombre':prod.BL_name, 'descripcion': prod.BL_description, 'prioridad': prod.BL_scaleType}for prod in productList]

    return json.dumps(res)


#Use case code starts here


#Use case code ends here