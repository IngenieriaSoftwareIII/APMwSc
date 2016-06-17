
# -*- coding: utf-8 -*-.

# Se importan las librerias necesarias.
import os
import datetime

from flask                 import Flask
from flask.ext.migrate     import Migrate, MigrateCommand
from flask.ext.sqlalchemy  import SQLAlchemy
from flask.ext.script      import Manager

from sqlalchemy import *

# Conexion con la base de datos.
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'apl.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Instancia de la aplicacion.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# Instancia de la base de datos.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Definicion de la Base de Datos.


class clsBacklog(db.Model):
    '''Clase que define el modelo Backlog'''

    __tablename__ = 'backlog'
    BL_idBacklog    = db.Column(db.Integer, primary_key=True, index=True)
    BL_name         = db.Column(db.String(50), unique=True)
    BL_description  = db.Column(db.String(140))
    BL_scaleType    = db.Column(db.Integer)
    BL_statusType   = db.Column(db.Integer)
    BL_refObjective = db.relationship('clsObjective', backref='backlog', lazy='dynamic', cascade="all, delete, delete-orphan")
    BL_refActor     = db.relationship('clsActor', backref='backlog', lazy='dynamic', cascade="all, delete, delete-orphan")
    BL_refAccion    = db.relationship('clsAccion', backref='backlog', lazy='dynamic', cascade="all, delete, delete-orphan")
    BL_refSprint    = db.relationship('clsSprint',backref = 'backlog',lazy = 'dynamic',cascade = "all, delete, delete-orphan")
    BL_refUserHist  = db.relationship('clsUserHistory', backref='backlog', lazy='dynamic', cascade="all, delete, delete-orphan")
    BL_refArchivos  = db.relationship('clsArchivos', backref='backlog', lazy='dynamic', cascade="all, delete, delete-orphan")
    BL_refVisionDoc = db.relationship('clsVisionDocument', backref='backlog', lazy='dynamic', cascade="all, delete, delete-orphan")

    def __init__(self, name, description, scaleType):
        '''Constructor del modelo Backlog'''
        self.BL_name        = name
        self.BL_description = description
        self.BL_scaleType   = scaleType

    def __repr__(self):
        '''Representacion en string del modelo Bakclog'''
        return '<idBacklog %r, name %r, scaleType %r>' % (self.BL_idBacklog, self.BL_name, self.BL_scaleType)


class clsArchivos(db.Model):
    '''Clase que define los archivos de cada proyecto '''

    __tablename__ = 'archivos'
    AR_idArchivos = db.Column(db.Integer, primary_key=True, index=True)
    AR_nameArch   = db.Column(db.String(50), unique=False)
    AR_url        = db.Column(db.String(200), nullable=False)
    AR_dateArch   = db.Column(db.DateTime, default=datetime.datetime.now())
    AR_idBacklog  = db.Column(db.String(50), db.ForeignKey('backlog.BL_idBacklog'))
    AR_etiqueta   = db.Column(db.String(100))

    def __init__(self, nameArch, url, dateArch, idBacklog, etiqueta):
        '''Constructor del modelo Archivos'''
        self.AR_nameArch  = nameArch
        self.AR_url       = url
        self.AR_dateArch  = dateArch
        self.AR_idBacklog = idBacklog
        self.AR_etiqueta  = etiqueta

    def __repr__(self):
        '''Representacion en string del modelo Archivo'''
        return '<idArchive %r, name %r, url %r, date %r, idBacklog %r, etiqueta %r >' % (self.AR_idArchivos, self.AR_nameArch, self.AR_url, self.AR_dateArch, self.AR_idBacklog, self.AR_etiqueta)


class clsActor(db.Model):
    '''Clase que define el modelo Actor'''

    __tablename__ = 'actors'
    A_idActor = db.Column(db.Integer, primary_key=True)
    A_nameActor = db.Column(db.String(50))
    A_actorDescription = db.Column(db.String(140))
    A_idBacklog = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
    A_refUser = db.relationship(
        'clsUser', backref='actors', lazy='dynamic', cascade="all, delete, delete-orphan")
    A_refActorsUserHist = db.relationship(
        'clsActorsUserHistory', backref='actors', lazy='dynamic', cascade="all, delete, delete-orphan")

    def __init__(self, nameActor, actorDescription, idBacklog):
        '''Constructor del modelo Actor'''
        self.A_nameActor = nameActor
        self.A_actorDescription = actorDescription
        self.A_idBacklog = idBacklog

    def __repr__(self):
        '''Respresentacion en string del modelo Actor'''
        return '<IdActor %r, Nombre %r, Descripcion %r, IdBacklog %r>' % (self.A_idActor, self.A_nameActor, self.A_actorDescription, self.A_idBacklog)

class clsUser(db.Model):
    '''Clase que define el modelo Usuario'''

    __tablename__ = 'user'
    U_fullname = db.Column(db.String(50))
    U_username = db.Column(db.String(16), primary_key=True, index=True)
    U_password = db.Column(db.String(200))
    U_email = db.Column(db.String(30), unique=True)
    U_idActor = db.Column(db.Integer, db.ForeignKey('actors.A_idActor'))

    def __init__(self, fullname, username, password, email, idActor):
        '''Constructor del modelo usuario'''
        self.U_fullname = fullname
        self.U_username = username
        self.U_password = password
        self.U_email = email
        self.U_idActor = idActor

    def __repr__(self):
        '''Representacion en string del modelo Usuario'''
        return '<fullname %r, username %r, email %r>' % (self.U_fullname, self.U_username, self.U_email)


class clsEquipo(db.Model):
    '''Clase que define el modelo Equipo'''

    __tablename__ = 'equipo'
    EQ_idEquipo         = db.Column(db.Integer, primary_key = True)
    EQ_username         = db.Column(db.String(16), db.ForeignKey('user.U_username'))
    EQ_rol              = db.Column(db.String(140))
    EQ_idBacklog         = db.Column(db.Integer,db.ForeignKey('backlog.BL_idBacklog'))

    def __init__(self, username,rol,idBacklog):
        '''Constructor del modelo Equipo'''
        self.EQ_username        = username
        self.EQ_rol             = rol
        self.EQ_idBacklog       = idBacklog

    def __repr__(self):
        '''Respresentacion en string del modelo Equipo'''
        return '<IdEquipo %r, Nombre de Usuario %r, Rol %r, IdBacklog %r>' %(self.EQ_idEquipo, self.EQ_username , self.EQ_rol, self.EQ_idBacklog)

class clsSubEquipo(db.Model):
    '''Clase que define el modelo Sub Equipo'''

    __tablename__ = 'SubEquipo'
    SEQ_idSubEquipo         = db.Column(db.Integer, primary_key = True)
    SEQ_username         = db.Column(db.String(16), db.ForeignKey('user.U_username'))
    SEQ_rol              = db.Column(db.String(140))
    SEQ_idSprint          = db.Column(db.Integer,db.ForeignKey('sprint.S_idSprint'))

    def __init__(self, username,rol,idSprint):
        '''Constructor del modelo Equipo'''
        self.SEQ_username        = username
        self.SEQ_rol             = rol
        self.SEQ_idSprint        = idSprint

    def __repr__(self):
        '''Respresentacion en string del modelo Sub Equipo'''
        return '<IdSubEquipo %r, Nombre de Usuario %r, Rol %r, IdSprint %r>' %(self.SEQ_idSubEquipo, self.SEQ_username , self.SEQ_rol, self,self.SEQ_idSprint)


class clsObjective(db.Model):
    '''Clase que define el modelo Objective'''

    __tablename__ = 'objectives'
    O_idObjective    = db.Column(db.Integer, primary_key=True)
    O_descObjective  = db.Column(db.String(140))
    O_idBacklog      = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
    O_objType        = db.Column(db.String(5))
    O_objFunc        = db.Column(db.Boolean)
    O_refObjUserHist = db.relationship('clsObjectivesUserHistory', backref='objectives', lazy='dynamic', cascade="all, delete, delete-orphan")

    def __init__(self, descObjective, idBacklog,objFunc, objType):
        '''Constructor del modelo Objective'''
        self.O_descObjective = descObjective
        self.O_idBacklog     = idBacklog
        self.O_objType       = objType
        self.O_objFunc       = objFunc

    def __repr__(self):
        '''Respresentación en string del modelo Objective'''
        return '<IdObjetivo %r, Descripcion %r, IdBacklog %r>' % (self.O_idObjective, self.O_descObjective, self.O_idBacklog)


class clsAccion(db.Model):
    '''Clase que define el modelo Accion'''

    __tablename__ = 'accions'
    AC_idAccion          = db.Column(db.Integer, primary_key=True)
    AC_accionDescription = db.Column(db.String(140))
    AC_idBacklog         = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
    AC_refUserHistory    = db.relationship('clsUserHistory', backref='accions', lazy='dynamic', cascade="all, delete, delete-orphan")

    def __init__(self, accionDescription, idBacklog):
        '''Constructor del modelo Accion'''
        self.AC_accionDescription = accionDescription
        self.AC_idBacklog         = idBacklog

    def __repr__(self):
        '''Respresentación en string del modelo accion'''
        return '<IdAccion %r, Descripcion %r, IdBacklog %r>' % (self.AC_idAccion, self.AC_accionDescription, self.AC_idBacklog)


class clsUserHistory(db.Model):
    '''Clase que define el modelo de tabla userHistory'''

    __tablename__ = 'userHistory'
    UH_idUserHistory     = db.Column(db.Integer, primary_key=True, index=True)
    UH_codeUserHistory   = db.Column(db.String(11), index=True)
    UH_idSuperHistory    = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'), nullable=True)
    UH_accionType        = db.Column(db.Integer)
    UH_idAccion          = db.Column(db.Integer, db.ForeignKey('accions.AC_idAccion'))
    UH_idBacklog         = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
    UH_scale             = db.Column(db.Integer, index=True)
    UH_refActorsUserHist = db.relationship('clsActorsUserHistory', backref='userHistory', lazy='dynamic', cascade="all, delete, delete-orphan")
    UH_refTareaUserHist  = db.relationship('clsTask', backref='userHistory', lazy='dynamic', cascade="all, delete, delete-orphan")
    UH_refObjUserHist    = db.relationship('clsObjectivesUserHistory', backref='userHistory', lazy='dynamic', cascade="all, delete, delete-orphan")
    UH_resume            = db.Column(db.String(200), nullable=True)
    UH_idSprint          = db.Column(db.Integer, db.ForeignKey('sprint.S_idSprint'))
    UH_iniciado          = db.Column(db.Boolean,  default = False)
    UH_fechaInicio       = db.Column(db.DateTime, default = datetime.datetime.now())
    UH_completed         = db.Column(db.Boolean,  default = False)
    UH_fechaFin          = db.Column(db.DateTime, default = datetime.datetime.now())


    def __init__(self, codeUserHistory, idSuperHistory, accionType, idAccion, idBacklog, scale, iniciado, fechaInicio, completed, fechaFin):
        self.UH_codeUserHistory = codeUserHistory
        self.UH_idSuperHistory  = idSuperHistory
        self.UH_accionType      = accionType
        self.UH_idAccion        = idAccion
        self.UH_idBacklog       = idBacklog
        self.UH_scale           = scale
        self.UH_idSprint        = None
        self.UH_resume          = None
        self.UH_iniciado        = iniciado
        self.UH_fechaInicio     = fechaInicio
        self.UH_completed       = completed
        self.UH_fechaFin        = fechaFin

    def __repr__(self):
        '''Representacion en string de la Historia de Usuario'''
        return ( '<idUserHistory %r, codeUserHistory %r, idSuperHistory %r, scale %r, idSPrint %r'+
                 ', resume %r, iniciado %r, fechaInicio %r, completed %r, fechaFin %r >') %\
                   ( self.UH_idUserHistory
                   , self.UH_codeUserHistory
                   , self.UH_idSuperHistory
                   , self.UH_scale
                   , self.UH_idSprint
                   , self.UH_resume
                   , self.UH_iniciado
                   , self.UH_fechaInicio
                   , self.UH_completed
                   , self.UH_fechaFin
                   )


class clsAcceptanceTest(db.Model):
    '''Clase que define el modelo de la tabla AcceptanceTest'''
    __tablename__       = 'acceptanceTest'
    AT_idAT             = db.Column(db.Integer, primary_key = True, index = True)
    AT_idUserHistory    = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))
    AT_description      = db.Column(db.String(200))
    AT_urlScript        = db.Column(db.String(200), nullable=False)

    def __init__(self, idUserHistory, description, urlScript):
        '''Constructor del modelo AcceptanceTest'''
        self.AT_idUserHistory   = idUserHistory
        self.AT_description = description
        self.AT_urlScript   = urlScript

    def __repr__(self):
        '''Representacion en string del modelo AcceptanceTest'''
        return ('<idAT %r, idUserHistory %r, description %r, urlScript %r >') %\
                 (self.AT_idAT, self.AT_idUserHistory, self.AT_description, self.AT_urlScript)



class clsActorsUserHistory(db.Model):
    '''Clase que define el modelo de tabla actorsUserHistory'''

    __tablename__ = 'actorsUserHistory'
    AUH_idActorsUserHist = db.Column(db.Integer, primary_key=True, index=True)
    AUH_idActor          = db.Column(db.Integer, db.ForeignKey('actors.A_idActor'))
    AUH_idUserHistory    = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))

    def __init__(self, idActor, idUserHistory):
        self.AUH_idActor       = idActor
        self.AUH_idUserHistory = idUserHistory

    def __repr__(self):
        '''Representacion en string de los id's a los actores y sus historias'''
        return '<idActor %r, idUserHistory %r>' % (self.AUH_idActor, self.AUH_idUserHistory)


class clsObjectivesUserHistory(db.Model):
    '''Clase que define el modelo de tabla ObjectivesUserHistory'''

    __tablename__ = 'objectivesUserHistory'
    OUH_idObjectivesUserHist = db.Column(db.Integer, primary_key=True, index=True)
    OUH_idObjective          = db.Column(db.Integer, db.ForeignKey('objectives.O_idObjective'))
    OUH_idUserHistory        = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))

    def __init__(self, idObjective, idUserHistory):
        self.OUH_idObjective   = idObjective
        self.OUH_idUserHistory = idUserHistory

    def __repr__(self):
        '''Representacion en string de los id's a los roles y sus historias'''
        return '<idObjective %r, idUserHistory %r>' % (self.OUH_idObjective, self.OUH_idUserHistory)

class clsAcceptanceCriteria(db.Model):
    '''Clase que representa los criterios de aceptacion para las historia de usuario'''

    __tablename__ = 'acceptanceCriteria'
    HAC_idAcceptanceCriteria = db.Column(db.Integer, primary_key=True, index=True)
    HAC_description          = db.Column(db.String(140), index=True)
    HAC_enunciado            = db.Column(db.String(140))
    HAC_idUserHistory        = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))
    HAC_idSprint             = db.Column(db.Integer, db.ForeignKey('sprint.S_idSprint'))

    def __init__(self, idUserHistory, description, enunciado):
        self.HAC_description   = description
        self.HAC_enunciado     = enunciado
        self.HAC_idUserHistory = idUserHistory
        self.HAC_idSprint      = None

    def __repr__(self):
        '''Representacion en string del criterio de aceptacion'''
        return '<HAC_idAcceptanceCriteria %r, HAC_idUserHistory %r, HAC_idSprint %r>' %\
               (self.HAC_idAcceptanceCriteria, self.HAC_idUserHistory, self.HAC_idSprint)

class clsTask(db.Model):
    '''Clase que define el modelo de la tabla Task'''

    __tablename__ = 'task'
    HW_idTask        = db.Column(db.Integer, primary_key=True, index=True)
    HW_description   = db.Column(db.String(140), unique=True, index=True)
    HW_weight        = db.Column(db.Integer)
    HW_idCategory    = db.Column(db.Integer, db.ForeignKey('category.C_idCategory'))
    HW_idUserHistory = db.Column(db.Integer, db.ForeignKey('userHistory.UH_idUserHistory'))
    HW_idEquipo      = db.Column(db.Integer, db.ForeignKey('equipo.EQ_idEquipo'))
    HW_idSprint      = db.Column(db.Integer, db.ForeignKey('sprint.S_idSprint'))
    HW_estimatedTime = db.Column(db.Integer)
    HW_horasEmpleadas = db.Column(db.Integer)
    HW_iniciado      = db.Column(db.Boolean, default=False)
    HW_fechaInicio   = db.Column(db.DateTime, default=datetime.datetime.now())
    HW_completed     = db.Column(db.Boolean, default = False)
    HW_fechaFin      = db.Column(db.DateTime, default=datetime.datetime.now())
    HW_refPrecedenceFirst  = db.relationship( 'clsPrecedence'
                                            , backref      = 'FirstTask'
                                            , lazy         = 'dynamic'
                                            , cascade      = "all, delete, delete-orphan"
                                            , foreign_keys = "clsPrecedence.P_idFirstTask"
                                            )

    HW_refPrecedenceSecond = db.relationship('clsPrecedence'
                                            , backref      = 'SecondTask'
                                            , lazy         = 'dynamic'
                                            , cascade      = "all, delete, delete-orphan"
                                            , foreign_keys = "clsPrecedence.P_idSecondTask"
                                            )
    
    def __init__(self, description, idCategory, weight, idUserHistory, iniciado, fechaInicio, completed, fechaFin):
        self.HW_description   = description
        self.HW_idCategory    = idCategory
        self.HW_weight        = weight
        self.HW_idUserHistory = idUserHistory
        self.HW_idSprint      = None
        self.HW_iniciado      = iniciado
        self.HW_fechaInicio   = fechaInicio
        self.HW_completed     = completed
        self.HW_fechaFin      = fechaFin
        self.HW_estimatedTime = 1
        self.HW_horasEmpleadas= None


    def getCompleted(self):
        return self.HW_completed

    def __repr__(self):
        '''Representacion en string de la Tarea'''
        return '<HW_ idTask  %r,HW_idCategory %r, HW_weight %r ,HW_idUserHistory %r, HW_idEquipo %r, HW_idSprint %r, \
                 HW_iniciado %r, HW_fechaInicio %r, HW_completed %r, HW_fechaFin %r>' % (self.HW_idTask, self.HW_idCategory, \
                    self.HW_weight, self.HW_idUserHistory, elf.HW_idEquipo, self.HW_idSprint, self.HW_iniciado, self.HW_fechaInicio, \
                    self.HW_completed, self.HW_fechaFin)


class clsCategory(db.Model):
    '''Clase que define el modelo de la tabla Category'''

    __tablename__ = 'category'
    C_idCategory      = db.Column(db.Integer, primary_key=True, index=True)
    C_nameCate        = db.Column(db.String(50), unique=True, index=True)
    C_weight          = db.Column(db.Integer, index=True)
    C_refTaskCategory = db.relationship('clsTask', backref='category', lazy='dynamic', cascade="all, delete, delete-orphan")

    def __init__(self, nameCate, weight):
        self.C_nameCate = nameCate
        self.C_weight   = weight

    def __repr__(self):
        '''Representacion en string de la Categoria'''
        return '<C_idCategory  %r, C_nameCate %r, C_weight %r>' % (self.C_idCategory, self.C_nameCate, self.C_weight)

class clsSprint(db.Model):
    '''Clase que define el modelo de la tabla Sprint'''

    __tablename__ = 'sprint'
    S_idSprint          = db.Column(db.Integer, primary_key = True, index = True)
    S_numero            = db.Column(db.Integer)
    S_sprintDescription = db.Column(db.String(140))
    S_idBacklog         = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
    S_refUserHistory    = db.relationship('clsUserHistory', backref='sprint', lazy='dynamic', cascade="all, delete, delete-orphan")
    S_refTask           = db.relationship('clsTask', backref='sprint', lazy='dynamic', cascade="all, delete, delete-orphan")
    S_fechini           = db.Column(db.DateTime, default=datetime.datetime.now())
    S_fechfin           = db.Column(db.DateTime, default=datetime.datetime.now())
    S_state             = db.Column(db.String(30))

    def __init__(self, numero, sprintDescription, idBacklog, fechini, fechfin, state):
        self.S_numero            = numero
        self.S_sprintDescription = sprintDescription
        self.S_idBacklog         = idBacklog
        self.S_fechini           = fechini
        self.S_fechfin           = fechfin
        self.S_state             = state

    def __repr__(self):
        '''Representacion en string del Sprint'''
        return '<S_idSprint %r, S_numero %r, S_sprintDescription %r, S_idBacklog %r, S_fechini %r, S_fechfin %r, S_state %r>' % (self.S_idSprint, self.S_numero, self.S_sprintDescription, self.S_idBacklog, self.S_fechini, self.S_fechfin, self.S_state)


class clsSprintMeeting(db.Model):
    '''Clase que define el modelo de las reuniones diarias'''
    __tablename__ = 'meeting'
    SM_idSprintMeeting  = db.Column(db.Integer, primary_key = True, index = True)
    SM_meetingDate      = db.Column(db.String(12))
    SM_activities       = db.Column(db.String(300))
    SM_suggestions      = db.Column(db.String(300))
    SM_challenges       = db.Column(db.String(300))
    SM_typeMeeting      = db.Column(db.String(300))
    SM_idSprint         = db.Column(db.Integer, db.ForeignKey('sprint.S_idSprint'))
    def __init__(self, meetingDate, activities, suggestions, challenges, idSprint, typeM):
        self.SM_meetingDate     = meetingDate
        self.SM_activities      = activities
        self.SM_suggestions     = suggestions
        self.SM_challenges      = challenges
        self.SM_idSprint        = idSprint
        self.SM_typeMeeting     = typeM


    def __repr__(self):
        '''Representacion en string del Meeting'''
        return '<SM_idSprintMeeting %r, SM_meetingDate %r,  SM_activities %r, SM_idSprint %r, SM_typeMeeting %r>' % (self.SM_idSprintMeeting, self.SM_meetingDate, self.SM_activities, self.SM_idSprint, self.SM_typeMeeting)


class clsElementMeeting(db.Model):
    '''Clase que define el modelo de un elemento de una reunión'''
    __tablename__          = "elementMeeting"
    EM_idElementMeeting    = db.Column(db.Integer, primary_key = True, index = True)
    EM_challenges          = db.Column(db.String(300))
    EM_planned             = db.Column(db.String(300))
    EM_done                = db.Column(db.String(300))
    EM_meeting             = db.Column(db.Integer, db.ForeignKey('meeting.SM_idSprintMeeting'))
    EM_user                = db.Column(db.String(16), db.ForeignKey('equipo.EQ_username'))

    def __init__(self,challenges,planned,done,user,meeting):
        self.EM_challenges = challenges
        self.EM_planned    = planned
        self.EM_done       = done
        self.EM_meeting    = meeting
        self.EM_user       = user

    def __repr__(self):
        '''Representacion en string del ElementMeeting'''
        return '<EM_idElementMeeting %r, EM_challenges %r,  EM_planned %r, EM_done %r, EM_meeting %r, EM_user %r>' % (self.EM_idElementMeeting, self.EM_challenges, self.EM_planned, self.EM_done, self.EM_meeting, self.EM_user)


class clsPrecedence(db.Model):
    '''Clase que define el modelo de la tabla Precedence'''

    __tablename__ = 'precedence'
    P_idPrecedence = db.Column(db.Integer, primary_key=True, index=True)
    P_idFirstTask = db.Column(db.Integer, db.ForeignKey('task.HW_idTask'))
    P_idSecondTask = db.Column(db.Integer, db.ForeignKey('task.HW_idTask'))
    P_idPila = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))

    def __init__(self, firstTask, secondTask, idPila):
        self.P_idFirstTask = firstTask
        self.P_idSecondTask = secondTask
        self.P_idPila = idPila

    def __repr__(self):
        '''Representacion en string de la Categoria'''
        return '<P_idPrecedence  %r, P_idFirstTask %r, P_idSecondTask %r>' % (
            self.P_idPrecedence, self.P_idFirstTask, self.P_idSecondTask)


class clsTaskDoc(db.Model):
    '''Clase que define el modelo de la tabla TaskDoc'''

    __tablename__      = 'taskDoc'
    HWD_idTaskDoc      = db.Column(db.Integer, primary_key=True, index=True)
    HWD_idTask         = db.Column(db.Integer, db.ForeignKey('task.HW_idTask'))
    HWD_docName        = db.Column(db.String(50), unique=True, index=True)
    HWD_docDescription = db.Column(db.String(140), unique=False, index=True)

    def __init__(self, idTask, docName, docDescription):
        self.HWD_idTask = idTask
        self.HWD_docName = docName
        self.HWD_docDescription = docDescription

    def getName(self):
        return self.HWD_docName

    def getDescription(self):
        return self.HWD_docDescription

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        '''Representacion en string del documento de la Tarea'''
        return '<HWD_ idTaskDoc  %r,HWD_idTask %r, HWD_docName %r ,HWD_docDescription %r>' % (
            self.HWD_idTaskDoc, self.HWD_idTask, self.HWD_docName, self.HWD_docDescription)


def taskDocs_by_taskId(taskID):
    return clsTaskDoc.query.filter(clsTaskDoc.HWD_idTask == taskID).all()

class clsVisionDocument(db.Model):
    ''' Clase que define el modelo de tabla de documento Vision '''

    __tablename__ = 'visionDocument'
    VD_idVisionDocument = db.Column(db.Integer, primary_key=True, index=True)
    VD_idBacklog        = db.Column(db.Integer, db.ForeignKey('backlog.BL_idBacklog'))
    VD_introduccion     = db.Column(db.Text)
    VD_proposito        = db.Column(db.Text)
    VD_motivacion       = db.Column(db.Text)
    VD_estado           = db.Column(db.Text)
    VD_alcance          = db.Column(db.Text)
    VD_fundamentacion   = db.Column(db.Text)
    VD_valores          = db.Column(db.Text)

    def __init__(self, idBacklog, introduccion,proposito,motivacion,estado,alcance,fundamentacion,valores):
        self.VD_idBacklog = idBacklog
        self.VD_introduccion = introduccion
        self.VD_proposito = proposito
        self.VD_motivacion = motivacion
        self.VD_estado = estado
        self.VD_alcance = alcance
        self.VD_fundamentacion = fundamentacion
        self.VD_valores = valores

    def __repr__(self):
        '''Representacion en string del documento vision'''
        return '<idVisionDocument %r, idBacklog %r, introduccion %r>' % (self.VD_idVisionDocument, self.VD_idBacklog, self.VD_introduccion)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
db.create_all()  # Creamos la base de datos

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    meta = MetaData(engine)
    historiaDeUsuario = Table('userHistory', meta, autoload=True)
    completed = Column('UH_completed', db.Boolean)
    completed.create(historiaDeUsuario)
except:
    pass

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    meta = MetaData(engine)
    tareaTable = Table('task', meta, autoload=True)
    completedTask = Column('HW_completed', db.Boolean)
    completedTask.create(tareaTable)
except:
    pass


db.create_all()  # Creamos la base de datos

