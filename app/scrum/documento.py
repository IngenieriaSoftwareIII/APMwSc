from flask import request, session, Blueprint, json
from generateVisionDocument import *


documento = Blueprint('documento', __name__)


@documento.route('/documento/ACrearDocumento', methods=['POST'])
def ACrearDocumento():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCrearDocumento', 'msg':['Error al crear el Documento']}, {'label':'/VProducto', 'msg':['Documento creado exitosamente']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    if request.method == 'POST':
        introduccion   = params['introduccion']
        proposito      = params['proposito']
        motivacion     = params['motivacion']
        estado         = params['estado']
        alcance        = params['alcance']
        fundamentacion = params['fundamentacion']
        valores        = params['valores']

        pathDocument = "./static/temp/"
        result = generateDocument(1,1,pathDocument)

    # Cambiar result dependiendo del resultado
    res = results[0]

    if result:
        res = results[1]

    idPila  = int(session['idPila'])
    res['label'] = res['label'] + '/' + str(idPila)
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@documento.route('/documento/VCrearDocumento')
def VCrearDocumento():
    #GET parameter
    idPila = int(request.args['idPila'])
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, add to JSON structure res values for the tamplate

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['fDocumento'] = {'idPila':idPila}

    res['idPila'] = idPila

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

