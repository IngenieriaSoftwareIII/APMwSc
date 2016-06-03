from flask            import Flask, request, session
from flask.ext.script import Manager, Server
from random           import SystemRandom
from datetime         import timedelta

app = Flask(__name__, static_url_path='')
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = False,
    host = '0.0.0.0', port = 8080)
)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

#Application code starts here


#Application code ends here

from app.scrum.ident import ident
app.register_blueprint(ident)
from app.scrum.prod import prod
app.register_blueprint(prod)
from app.scrum.mast import mast
app.register_blueprint(mast)
from app.scrum.dev import dev
app.register_blueprint(dev)
from app.scrum.actor import actor
app.register_blueprint(actor)
from app.scrum.objetivo import objetivo
app.register_blueprint(objetivo)
from app.scrum.accion import accion
app.register_blueprint(accion)
from app.scrum.historias import historias
app.register_blueprint(historias)
from app.scrum.tareas import tareas
app.register_blueprint(tareas)
from app.scrum.cates import cates
app.register_blueprint(cates)
from app.scrum.equipo import equipo
app.register_blueprint(equipo)
from app.scrum.anexo import anexo
app.register_blueprint(anexo)
from app.scrum.sprint import sprint
app.register_blueprint(sprint)
from app.scrum.equipo import equipo
app.register_blueprint(equipo)
from app.scrum.pruebaAceptacion import pruebaAceptacion
app.register_blueprint(pruebaAceptacion)
from app.scrum.documento import documento
app.register_blueprint(documento)


if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()

