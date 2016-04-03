# -*- coding: utf-8 -*-

from flask import request, session, Blueprint, json
from app.scrum.category import *
from app.scrum.model    import *
#from _operator import length_hint

cates = Blueprint('cates', __name__)


@cates.route('/cates/ACrearCategoria', methods=['POST'])
def ACrearCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría creada.']}, {'label':'/VCategorias', 'msg':['Error al intentar crear categoría.']}, ]
    res = results[1]

    if params != {}:    
        # Extraemos los parámetros
        cateName    = params['nombre']
        cateWeight  = params['peso']
        
        # Insertamos el nuevo elemento
        cCategory = category()
        inserted = cCategory.insertCategory(cateName,cateWeight)
        
        if inserted:
            res = results[0]  
            
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AElimCategoria')
def AElimCategoria():
    #GET parameter
    idCategoria = request.args['idCategoria']
    results = [{'label':'/VCategorias', 'msg':['Categoría eliminada.']}, {'label':'/VCategorias', 'msg':['Error al intentar eliminar categoría.']}, ]
    res = results[1]

    # Convertimos el parámetro del id en entero
    idCate = int(idCategoria)
    
    # Buscamos la categoría que vamos a eliminar
    cCategory = category()
    cateFound = cCategory.searchIdCategory(idCate)

    # Eliminamos la categoría
    if (cateFound != []):
        deleted = cCategory.deleteCategory(cateFound[0].C_nameCate)  
        if deleted:
            res = results[0]
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AModifCategoria', methods=['POST'])
def AModifCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría actualizada.']}, {'label':'/VCategorias', 'msg':['Error al intentar modificar categoría.']}, ]
    res = results[1]

    # Obtenemos los parámetros    
    newNameCategory = params['nombre']
    newWeight       = params['peso']
    idCategory      = params['idCategoria']
    
    # Buscamos la categoría a modificar
    cCategory = category()    
    showCate = cCategory.searchIdCategory(idCategory)

    # Modificamos la categoría
    result  = cCategory.updateCategory(showCate[0].C_nameCate,newNameCategory,newWeight)

    if result:
        res = results[0]    

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/VCategoria')
def VCategoria():
    #GET parameter
    idCategoria = request.args['idCategoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['idCategoria'] = int(idCategoria)

    # Obtenemos el id de la categoría
    idCate = int(idCategoria)
    
    # Buscamos la tupla asociada al id capturado
    cCategory = category()
    showCate  = cCategory.searchIdCategory(idCate)
    
    # Mostramos los datos en la vista     
    res['fCategoria'] = {'idCategoria':showCate[0].C_idCategory, 'peso':showCate[0].C_weight, 
                         'nombre':showCate[0].C_nameCate}

    # Guardamos el id de la categoría
    session['idCategoria'] = int(idCategoria)
    
    return json.dumps(res)



@cates.route('/cates/VCategorias')
def VCategorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    # Obtenemos una lista con los datos asociados a las categorías
    cateList  = clsCategory.query.all()        
    
    # Mostramos los datos en la vista
    ListaCompleta = []
    for i in cateList:
        ListaCompleta.append((i.C_idCategory,i.C_nameCate,i.C_weight))
    
    decorated = [(tup[2], tup) for tup in ListaCompleta]
    decorated.sort()
    
    res['data0'] = [{'idCategoria':cat[1][0],'nombre':cat[1][1],'peso':cat[1][2]} for cat in decorated]

    return json.dumps(res)



#Use case code starts here


#Use case code ends here