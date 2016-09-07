# -*- coding: utf-8 -*-

from flask                  import request, session, Blueprint, json

from app.scrum.usuarioClase import *
from app.scrum.loginClase   import *

from app.scrum.role         import *
from app.scrum.category     import *

ident = Blueprint('ident', __name__)


@ident.route('/ident/AIdentificar', methods=['POST'])
def AIdentificar():
    #POST/PUT parameters.
    params  = request.get_json()

    results = [{'label':'/VProductos', 'msg':['Bienvenido dueño del producto'], "actor":"duenoProducto"},
               {'label':'/VProductos', 'msg':['Bienvenido Maestro Scrum'], "actor":"maestroScrum"},
               {'label':'/VProductos', 'msg':['Bienvenido Desarrollador'], "actor":"desarrollador"},
               {'label':'/VLogin',     'msg':['Datos de identificación incorrectos']}]

    # Asignamos un mensaje a mostrar por defecto
    res = results[3]

    if request.method == 'POST':
        nombreUsuario = params['usuario']
        clave         = params['clave']

        # Buscamos el usuario en la base de datos
        oUsuario          = usuario()
        usuarioEncontrado = oUsuario.buscarUsuario(nombreUsuario)

        if usuarioEncontrado:
            claveCifrada = usuarioEncontrado[0].U_clave

            # Chequeamos la clave
            oLogin  = login();
            esClaveValida = oLogin.verificarClave(claveCifrada, clave)

            if esClaveValida:
                # Mostramos el nombre de usuario en la aplicación
                nombre        = usuarioEncontrado[0].U_nombreCompleto
                nombreUsuario = usuarioEncontrado[0].U_nombreUsuario
                session['usuario'] = {'nombre': nombre.title(),'username': nombreUsuario}

                # Verificamos el rol del usuario
                rolUsuario = usuarioEncontrado[0].U_idRol

                if rolUsuario == 1: res = results[0]
                if rolUsuario == 2: res = results[1]
                if rolUsuario == 3: res = results[2]

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

    # Asignamos un mensaje a mostrar por defecto
    res = results[1]

    if request.method == 'POST':

        # Extraemos los datos
        nuevoNombreUsuario = params['nombre']
        nuevoNombre        = params['usuario']
        nuevaClave         = params['clave']
        nuevoCorreo        = params['correo']
        nuevoRol           = params['actorScrum']

        oLogin   = login() 
        oUsuario = usuario()

        #Verificamos si el tipo de rol es correcto
        esRolValido = nuevoRol in [1,2,3]

        estaNuevoNombreUsuario = oUsuario.estaNombreUsuario(nuevoNombreUsuario)
        esClaveCorrecta        = oLogin.claveValida(nuevaClave)
        claveCifrada           = oLogin.encriptarClave(nuevaClave)

        if not esClaveCorrecta:
            res           = results[1]
            res['msg'][0] = res['msg'][0] + ": Formato inválido para la contraseña."

        if not estaNuevoNombreUsuario and esClaveCorrecta and esRolValido:
            estaInsertado = oUsuario.insertarUsuario(nuevoNombreUsuario,nuevoNombre,claveCifrada,nuevoCorreo,nuevoRol)

            if estaInsertado:
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

        # Se crean categorias para las tareas
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

        print('Se cargaron las categorias.')

    return json.dumps(res)



@ident.route('/ident/VRegistro')
def VRegistro():

    res = {}

    if "actor" in session:
        res['actor'] = session['actor']

    res['fUsuario_opcionesActorScrum'] = [{'key':0,'value':'Seleccione un rol'},
                                          {'key':1,'value':'Dueño de producto'},
                                          {'key':2,'value':'Maestro Scrum'},
                                          {'key':3,'value':'Miembro del equipo de desarrollo'}] 

    return json.dumps(res)