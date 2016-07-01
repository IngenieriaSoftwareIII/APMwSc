# -*- coding: utf-8 -*-

from flask                  import request, session, Blueprint, json
from app.scrum.role         import *
from app.scrum.accions      import *
from app.scrum.objective    import *
from app.scrum.user         import *
from app.scrum.login        import *
from app.scrum.category     import *
from app.scrum.task         import *
from app.scrum.userHistory  import *

ident = Blueprint('ident', __name__)

@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters.
    params  = request.get_json()

    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño del producto'], "actor":"duenoProducto"},
               {'label':'/VProductos', 'msg':['Bienvenido Maestro Scrum'], "actor":"maestroScrum"},
               {'label':'/VProductos', 'msg':['Bienvenido Desarrollador'], "actor":"desarrollador"},
               {'label':'/VLogin',     'msg':['Datos de identificación incorrectos']}]
    res     = results[3]

    if request.method == 'POST':
        userName     = params['usuario']
        userPassword = params['clave']

        # Buscamos el usuario en la base de datos
        oUser     = user()
        userLogin = oUser.searchUser(userName)

        if userLogin:
            encriptPassword = userLogin[0].U_password
            # Chequeamos el password
            oLogin  = login();
            isValid = oLogin.check_password(encriptPassword, userPassword)

            if isValid:
                # Mostramos el nombre en la aplicación
                fullname = userLogin[0].U_fullname
                username = userLogin[0].U_username 
                session['usuario'] = {'nombre': fullname.title(),'username': username}

                # Verificamos el rol del usuario
                rolUser = userLogin[0].U_idActor

                if rolUser == 1: res = results[0]
                if rolUser == 2: res = results[1]
                if rolUser == 3: res = results[2]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@ident.route('/ident/ARegistrar', methods=['POST'])
def ARegistrar():
    #POST/PUT parameters
    params  = request.get_json()
    results = [{'label':'/VLogin'   , 'msg':['Felicitaciones, Ya estás registrado en la aplicación']},
               {'label':'/VRegistro', 'msg':['Error al tratar de registrarse']} ]
    res     = results[1]


    if request.method == 'POST':

        # Extraemos los datos
        newName     = params['nombre']
        newUser     = params['usuario']
        newPassword = params['clave']
        newEmail    = params['correo']
        newActor    = params['actorScrum']

        oLogin = login() 
        oUser  = user()

        checkNewUser     = oUser.isFound(newUser)
        checkNewEmail    = oUser.findEmail(newEmail)
        checkNewPassword = oLogin.validPassword(newPassword)
        encriptPassword  = oLogin.encript(newPassword)

        if (not checkNewPassword):
            res = results[1]
            res['msg'][0] = res['msg'][0] + ": Formato incorrecto para las contraseñas"

        if (not checkNewUser) and checkNewPassword and (not checkNewEmail):
            result = oUser.insertUser(newName,newUser,encriptPassword,newEmail,newActor)
            if result:
                res = results[0]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@ident.route('/ident/VLogin')
def VLogin():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    session.pop('usuario', None)

    # Se precargan valores en la base de datos
    oCate    = category()
    oActor   = role()
    isEmpty  = oActor.emptyTable()

    if isEmpty:
        print('Cargando datos de prueba...')
        #Se crean categorias para las tareas
        result1  = oCate.insertCategory('Implementar una acción',2)
        result2  = oCate.insertCategory('Implementar una vista',2)
        result3  = oCate.insertCategory('Implementar una regla de negocio o un método de una clase',2)
        result4  = oCate.insertCategory('Migrar la base de datos',2)
        result5  = oCate.insertCategory('Crear un diagrama UML',1)
        result6  = oCate.insertCategory('Crear datos inciales',1)
        result7  = oCate.insertCategory('Crear un criterio de aceptación',1)
        result8  = oCate.insertCategory('Crear una prueba de aceptación',2)
        result9  = oCate.insertCategory('Actualizar un elemento implementado en otra tarea',1)
        result10 = oCate.insertCategory('Escribir el manual en línea de una página',1)

        oLogin = login()
        oUser  = user()
        #Creamos usuarios con los tres posibles roles
        password         = 'Sabeys.2008'
        encriptPassword  = oLogin.encript(password)

        oActor.insertActor('Dueno','Dueño del Producto',0)
        oActor.insertActor('Maestro Scrum','Maestro Scrum',0)
        oActor.insertActor('Miembro del Equipo','Miembro del Equipo',0)

        #Corregido error de los actores por defecto, deberian ir en la tabla de Actores
        #result = oUser.insertUser('Dueno','admin',encriptPassword,'productOwner@gmail.com',1)
        #result = oUser.insertUser('Maestro Scrum','scrum',encriptPassword,'scrumMaster@gmail.com',2)
        #result = oUser.insertUser('Equipo de Trabajo','team',encriptPassword,'teamMember@gmail.com',3)

        print('Se cargaron los datos.')

    return json.dumps(res)



@ident.route('/ident/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor'] = session['actor']

    res['fUsuario_opcionesActorScrum'] = [
      {'key':2,'value':'Maestro Scrum'},
      {'key':1,'value':'Dueño de producto'},
      {'key':3,'value':'Miembro del equipo de desarrollo'},
      {'key':0,'value':'Seleccione un rol'}
    ]

    return json.dumps(res)


#Use case code starts here


#Use case code ends here
