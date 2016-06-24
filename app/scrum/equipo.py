from flask import request, session, Blueprint, json
from app.scrum.backLog import *
from app.scrum.user import *
from app.scrum.Team import *

equipo = Blueprint('equipo', __name__)

@equipo.route('/equipo/AActualizarEquipo', methods=['POST'])
def AActualizarEquipo():
    #POST/PUT parameters
    params = request.get_json()

    results = [{'label':'/VEquipo', 'msg':['Equipo actualizado']}, {'label':'/VEquipo', 'msg':['Error al actualizar el equipo']}, ]
    res = results[1]
    
    idPila = int(session['idPila'])

    teamMembers  = params['miembros']
    scrumMaster  = params['scrum']
    productOwner = params['productOwner']

    lista = []

    lista.append({'miembro':productOwner,'rol':'Product owner'})
    lista.append({'miembro':scrumMaster,'rol':'Scrum master'})

    for m in teamMembers:
        lista.append({'miembro':m, 'rol':'Team member'})   
    
    oTeam = team()
    exito = oTeam.actualizar(lista,idPila)

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



@equipo.route('/equipo/VEquipo')
def VEquipo():
    #GET parameter
    res = {}

    idPila = int(session['idPila'])
   
    oTeam = team()
    oUser = user()

    #Obtenemos la lista de usuarios asignados al equipo.
    teamList = oTeam.getTeam(idPila)
    teamMembers  = []
    productOwner = ''
    scrumMaster  = ''

    for m in teamList:
        if m.EQ_rol == "Product owner":
            productOwner = m.EQ_username
        if m.EQ_rol == "Scrum master":
            scrumMaster = m.EQ_username
        if m.EQ_rol == "Team member":
            teamMembers.append(m.EQ_username)

    #Obtenemos los usuarios registrados como product owner.
    productOwnerList = oUser.getUserByIdActor(1)

    #Obtenemos los usuarios registrados como scrum masters.
    scrumMastersList = oUser.getUserByIdActor(2)

    #Obtenemos los usuarios registrados como desarrolladores.
    teamMembersList = oUser.getUserByIdActor(3)
    

    res['fEquipo'] = {'productOwner':productOwner,'scrum':scrumMaster,'miembros':teamMembers,'id':idPila}
    res['usuario'] = session['usuario']
    res['idPila']  = idPila

    res['fEquipo_opcionesProductOwner'] = [{'key': user.U_username,'value': user.U_fullname} for user in productOwnerList]
    res['fEquipo_opcionesScrum']        = [{'key': user.U_username,'value': user.U_fullname} for user in scrumMastersList]
    res['fEquipo_opcionesMiembros']     = [{'key': user.U_username,'value': user.U_fullname} for user in teamMembersList]

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'

    return json.dumps(res)


#Use case code starts here


#Use case code ends here

