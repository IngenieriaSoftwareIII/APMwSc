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
    #Action code goes here, res should be a list with a label and a message

    idPila  = int(session['idPila'])
    lista = params['lista']
    
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
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    idPila   = int(session['idPila'])
   
    oTeam = team()
    teamList = oTeam.getTeam(idPila)
    oUser = user()
    userList = oUser.getAllUsers()

    res['fEquipo'] = {'lista':[{'miembro':team.EQ_username, 'rol': team.EQ_rol, 'id': team.EQ_idEquipo} for team in teamList]}
    res['usuario'] = session['usuario']
    res['idPila'] = idPila

    res['fEquipo_opcionesRol'] =[
        {'key':'Desarrollador', 'value':'Desarrollador'},
        {'key':'Scrum master', 'value':'Scrum master'},
      ]

    print("Aquii",userList)

    res['fEquipo_opcionesMiembros'] =[{'key':user.U_username,'value': user.U_username} for user in userList]

    #Action code ends here
    return json.dumps(res)


#Use case code starts here


#Use case code ends here

