from archivos import *
import os
from flask import request, session, Blueprint, json, send_file
from datetime import datetime

app = Flask(__name__)
anexo = Blueprint('anexo', __name__)

# Where files are going to be uploaded
app.config['UPLOADED_FILES_DEST'] = 'uploadedFiles/'


@anexo.route('/anexo/AAnexo/<path:idPila>', methods=['POST'])
def AAnexo(idPila):
    # Access to POST/PUT fields using request.form['name']
    # Access to file fields using request.files['name']
    results = [{'label': '/VAnexo', 'msg': ['Documento anexado']},
               {'label': '/VAnexo', 'msg': ['Error al guardar anexo']}, ]
    res = results[0]
    # Action code goes here, res should be a list with a label and a message

    etiqueta = request.form['nombre']
    print('Nombre del anexo: ' + etiqueta)

    file = request.files['contenido']

    print('Archivo: ' + file.filename)

    intIdPila = int(idPila)

    file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], file.filename))
    date = datetime.utcnow()
    url = str(app.config['UPLOADED_FILES_DEST'] + file.filename)
    c = archivos()

    c.insertArchive(file.filename, url, date, intIdPila, etiqueta)

    res['label'] = res['label'] + '/' + str(idPila)

    # Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@anexo.route('/anexo/AElimAnexo/')
def AElimAnexo():
    # POST/PUT parameters
    params = request.get_json()

    results = [{'label': '/VAnexo', 'msg': ['Anexo eliminado']},
               {'label': '/VAnexo', 'msg': ['Error al eliminar anexo']}, ]
    res = results[0]
    # Action code goes here, res should be a list with a label and a message

    attachementId = int(request.args['id'])

    oArchivo = archivos().findIdArchives(attachementId)

    # Delete physical file
    os.remove(oArchivo.AR_url)

    # Delete file information in the database
    archivos().deleteArchive(attachementId)

    # Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@anexo.route("/anexo/ADescargar/<path:filename>", methods=['GET'])
def download(filename):
    """Downloads a file."""
    return send_file(filename, as_attachment=True)


@anexo.route('/anexo/VAnexo/')
def VAnexo():
    # GET parameter
    idPila = int(request.args['idPila'])
    res = {}
    if "actor" in session:
        res['actor'] = session['actor']
    # Action code goes here, res should be a JSON structure

    emptyBacklog = backLog.backlog()

    # oBacklog = emptyBacklog.findIdProduct(idPila)
    filesList = emptyBacklog.filesAssociatedToProduct(idPila)

    res['data1'] = [
        {'idAnexo': file.AR_idArchivos,
         'nombre': file.AR_etiqueta,
         'url': file.AR_url,
         'fecha': file.AR_dateArch,
         'etiqueta': file.AR_etiqueta,
         'idBacklog': file.AR_idBacklog
         } for file in filesList]
    res['fAnexo'] = {}
    res['idPila'] = idPila

    # Action code ends here
    return json.dumps(res)

# Use case code starts here


# Use case code ends here
