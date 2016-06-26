# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from datetime import *
from backLog import *
from userHistory import *
from task        import *
from acceptanceCriteria import *
from random import randint

# Declaracion de constantes.
MIN_ID                 = 1
MIN_SPRINT_DESCRIPTION = 1
MAX_SPRINT_DESCRIPTION = 140
MIN_SPRINT_NUMBER = 1
MAX_SPRINT_NUMBER = 1000


def bdchart_time(sprint_tasks,sprint_start_date,sprint_end_date):
	sprint_time=(sprint_end_date-sprint_start_date).days
	fun_time = lambda x: x.HW_estimatedTime
	sprint_time_total = sum(map(fun_time,sprint_tasks))
	sprint_time_total_real= sprint_time_total
	ideal_delta = sprint_time_total/sprint_time
	fun_time = lambda x: ((x.HW_fechaFin-sprint_start_date).days+1,x.HW_estimatedTime,x.HW_horasEmpleadas)
	sprint_index=list(map(fun_time,filter(lambda x: x.HW_fechaFin is not None,sprint_tasks)))
	rows = [{"c":[{ "v": "Dia "+str(i)},{"v": sprint_time_total_real,},{"v": sprint_time_total-ideal_delta*i,}]} for i in range(0,sprint_time+1)]
	
	for x in range(1,sprint_time+1):
		tasks = list(filter(lambda y: y[0]==x,sprint_index))
		print(tasks)
		estimated_of_day = sum(map(lambda z: z[1],tasks))
		real_of_day = sum(map(lambda z: z[2],tasks))
		dif = estimated_of_day-real_of_day
		if dif<0 :
			sprint_time_total_real-=real_of_day
			rows[x-1]['c'][1]['v'] -=dif 
			rows[x]["c"][1]['v']=rows[x-1]['c'][1]['v'] - real_of_day
		else:
			rows[x]["c"][1]['v']=rows[x-1]['c'][1]['v']-estimated_of_day
			
		
	data={"cols":   [ { "id"    : "days"
	                  , "label" : "Dias del sprint"
	                  , "type"  : "string"
	                  , "p"     : {}
	                  }
	                , { "id"    : "actual_hours"
	                  , "label" : "Horas por cumplir"
	                  , "type"  : "number"
	                  , "p"     : {}
	                  }
	                , { "id"    : "ideal_hours"
	                  , "label" : "Horas estimadas"
	                  , "type"  : "number"
	                  , "p"     : {}
	                  }
	                ]
	     }
	data['rows']=rows
	
	bdchart =   { "type"    : "ComboChart"
	            , "options" : 
	                { "title"      : "Burn down chart del Sprint"
	                , "vAxis"      : { "title": "Horas por cumplir" }
	                , "hAxis"      : { "title": "Dias" }
	                , "seriesType" : "bars"
	                , "series"     : { 1 : {'type'  : 'line' }
	                                 , 0 : {'color' : '#000000' }
	                                 }
	                }   
	            , "formatters" : {}
	            }
	bdchart["data"] = data
	return bdchart
		
def bdchart_weight(sprint_tasks,sprint_start_date,sprint_end_date):
	
	sprint_time=(sprint_end_date-sprint_start_date).days
	fun_weight = lambda x: ((x.HW_fechaFin-sprint_start_date).days+1,x.HW_weight)
	sprint_index = filter(lambda x: x.HW_fechaFin is not None, sprint_tasks)
	sprint_index = map(fun_weight,sprint_index) 
	sprint_index = dict(sprint_index)
	sprint_tasks_total= sum(map(lambda x: x.HW_weight ,sprint_tasks))
	ideal_delta= sprint_tasks_total/sprint_time
	sprint_tasks_total_real=sprint_tasks_total
	#Building the bdchart
	rows = [{"c":[{ "v": "Dia 1"},{"v": sprint_tasks_total,},{"v": sprint_tasks_total,}]}]
	for x in range(1,sprint_time):
	    sprint_tasks_total-=ideal_delta
	    sprint_tasks_total_real-=sprint_index.get(x,0)
	    rows.append({"c":[{ "v": "Dia %s"%x},{"v":sprint_tasks_total_real, },{"v": sprint_tasks_total,}]})
	try:
		sprint_tasks_total_real-=sprint_index.get(x+1,0)
	except UnboundLocalError:
		x = sprint_time
		sprint_tasks_total_real-=sprint_index.get(x+1,0)
	rows.append({"c":[{ "v": "Dia %s"%(x+1)},{"v":sprint_tasks_total_real, },{"v": 0,}]})
	#Building the JSON to be sent
	data={"cols":   [ { "id"    : "days"
	                  , "label" : "Dias del sprint"
	                  , "type"  : "string"
	                  , "p"     : {}
	                  }
	                , { "id"    : "actual_hours"
	                  , "label" : "Peso de las tareas"
	                  , "type"  : "number"
	                  , "p"     : {}
	                  }
	                , { "id"    : "ideal_hours"
	                  , "label" : "Pesos estimados"
	                  , "type"  : "number"
	                  , "p"     : {}
	                  }
	                ]
	     }
	data['rows']=rows
	
	bdchart =   { "type"    : "ComboChart"
	            , "options" : 
	                { "title"      : "Burn down chart del Sprint"
	                , "vAxis"      : { "title": "Peso acumulado de las tareas" }
	                , "hAxis"      : { "title": "Dias" }
	                , "seriesType" : "bars"
	                , "series"     : { 1 : {'type'  : 'line' }
	                                 , 0 : {'color' : '#000000' }
	                                 }
	                }   
	            , "formatters" : {}
	            }
	bdchart["data"] = data
	return bdchart


class sprints(object):
	'''Clase que permite manejar los sprints de manera persistente'''

	def insertSprint(self, sprintNumber, sprintDescription, idBacklog, fechini, fechfin, state): 
		'''Permite insertar una Sprint asociado a un producto'''   
		checkTypeDescription = type(sprintDescription) == str
		checkTypeId          = type(idBacklog) == int
		checkTypeNumber      = type(sprintNumber) == int
		checkDuration		 = (fechfin >= fechini)
		checkTypeState		 = type(state) == str

		if checkTypeDescription and checkTypeId and checkTypeNumber and checkDuration and checkTypeState :
			checkSprintNumber          = MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
			checkLongSprintDescription = MIN_SPRINT_DESCRIPTION <= len(sprintDescription) <= MAX_SPRINT_DESCRIPTION
			checkLongId                = MIN_ID <= idBacklog

			if checkSprintNumber and checkLongSprintDescription and checkLongId:
				foundBacklog = clsBacklog.query.filter_by(BL_idBacklog = idBacklog).all()                      
				
				if foundBacklog != []:
					foundSprints = clsSprint.query.filter_by(S_idBacklog = idBacklog).all()

					for num in foundSprints:
						if num.S_numero  == sprintNumber:
							return False
						 
					# Si S_numero no se repite
					newSprint = clsSprint(sprintNumber, sprintDescription, idBacklog, fechini, fechfin, state)

					db.session.add(newSprint)
					db.session.commit()
					return True
		return False



	def updateSprint(self, idSprint, idBacklog, newSprintNumber,newDescription, newfechini, newfechfin, newstate):
		'''Permite actualizar la descripcion de una sprint'''   
		checkTypeId              = type(idSprint) == int
		checkTypeNewSprintNumber = type(newSprintNumber) == int
		checkTypeNewdescription  = type(newDescription) == str
		checkDuration		 = (newfechfin >= newfechini)
		checkTypeState		 = type(newstate) == str

		if checkTypeNewdescription and checkTypeId and checkTypeNewSprintNumber and checkDuration and checkTypeState :
			checkLongNewDescription = MIN_SPRINT_DESCRIPTION <= len(newDescription) <= MAX_SPRINT_DESCRIPTION
			foundSprint             = self.searchIdSprint(idSprint, idBacklog)
			if foundSprint != [] and checkLongNewDescription:
				if foundSprint[0].S_numero != newSprintNumber:
					for num in clsSprint.query.filter_by(S_idBacklog = idBacklog).all():
						if num.S_numero  == newSprintNumber:
							return False
				foundSprint[0].S_sprintDescription = newDescription
				foundSprint[0].S_numero            = newSprintNumber
				foundSprint[0].S_fechini           = newfechini
				foundSprint[0].S_fechfin           = newfechfin
				foundSprint[0].S_state             = newstate
				db.session.commit()
				return True
		return False

	def searchIdSprint(self, sprintNumber, backlog):
		'''Permite buscar sprints por su id'''
		checkTypeIdSprint = type(sprintNumber) == int
		checkTypeBacklog  = type(backlog) == int
		foundSprint       = []

		if checkTypeIdSprint and checkTypeBacklog:
			foundSprint = clsSprint.query.filter_by(S_numero=sprintNumber,S_idBacklog =backlog).all()
		return foundSprint

	def getSprintId(self, sprintNumber, backlog):
		'''retorna el id de un sprint dado su numero ysu backlog'''
		checkTypeIdSprint = type(sprintNumber) == int
		checkTypeBacklog  = type(backlog) == int
		if checkTypeIdSprint and checkTypeBacklog:
			foundSprint       = self.searchIdSprint(sprintNumber,backlog);

			if foundSprint:
				sprintId = clsSprint.query.filter_by(S_numero=sprintNumber,S_idBacklog =backlog).first()
				return sprintId.S_idSprint;
		return -23

	def deleteSprint(self,sprintNumber,idBacklog):
		'''Permite eliminar un Sprint segun su numero en el backlog'''
		checkTypeSprintNumber = type(sprintNumber) == int
		checkTypeidBacklog    = type(idBacklog) == int

		if checkTypeSprintNumber and checkTypeidBacklog:
			checkLenSprintNumber = MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
			checkLongIdBacklog   = MIN_ID <= idBacklog

			if checkLenSprintNumber and checkLongIdBacklog:
				foundSprint = clsSprint.query.filter_by(S_numero=sprintNumber,S_idBacklog=idBacklog).all()
				if foundSprint != []:
					for i in foundSprint:
						db.session.delete(i)
					db.session.commit()
					return True
		return False

	def asignSprintHistory(self, sprintNumber, idBacklog, idUserHistory):
		''' Permite asignar a un Sprint una historia de usuario asociado al producto '''
		checkSprintNumber  = type(sprintNumber)  == int and MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog     = type(idBacklog)     == int and MIN_ID <= idBacklog
		checkidUserHistory = type(idUserHistory) == int and MIN_ID <= idUserHistory
		if checkSprintNumber and checkidBacklog and checkidUserHistory:
			oUserHistory = userHistory()
			history = oUserHistory.searchIdUserHistory(idUserHistory)
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			if history != [] and sprint != []:
				history[0].UH_idSprint = sprint[0].S_idSprint
				db.session.commit()
				return True
		return False

	def getAssignedSprintHistory(self, sprintNumber, idBacklog):
		'''Permite obtener las historias asociados a un determinado Sprint'''

		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog)    == int and MIN_ID <= idBacklog

		if checkSprintNumber and checkidBacklog:
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			found = clsUserHistory.query.filter_by(UH_idSprint = sprint[0].S_idSprint).all()
			return found
		return []

	def deleteAssignedSprintHistory(self, sprintNumber, idBacklog, idUserHistory):
		''' Permite eliminar la asignacion de una historia asociado a un Sprint dado su id'''

		checkSprintNumber  = type(sprintNumber)  == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog     = type(idBacklog)     == int and MIN_ID <= idBacklog
		checkidUserHistory = type(idUserHistory) == int and MIN_ID <= idUserHistory
		
		if checkSprintNumber and checkidBacklog and checkidUserHistory:
			oUserHistory = userHistory()
			history      = oUserHistory.searchIdUserHistory(idUserHistory)
			if history != []:
				history[0].UH_idSprint = None
				history[0].UH_resume   = None
				db.session.commit()
				return True
		return False

	def asignSprintTask(self, sprintNumber, idBacklog, idTask):
		''' Permite asignar a un Sprint una tarea asociado a sus historias'''
		checkSprintNumber = type(sprintNumber) == int and MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog)    == int and MIN_ID <= idBacklog
		checkidTask = type(idTask) == int and MIN_ID <= idTask
		if checkSprintNumber and checkidBacklog and checkidTask:
			oTask  = task()
			tarea  = oTask.getTaskById(idTask)
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			if tarea and sprint:
				tarea.HW_idSprint = sprint[0].S_idSprint
				db.session.commit()
				return True
		return False

	def getAssignedSprintTask(self, sprintNumber, idBacklog):
		'''Permite obtener las Tareas asociados a un determinado Sprint'''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		if checkSprintNumber and checkidBacklog:
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			found = clsTask.query.filter_by(HW_idSprint = sprint[0].S_idSprint).all()
			return found
		return []

	def getEstimatedTime(self, sprintNumber, idBacklog):
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		if checkSprintNumber and checkidBacklog:
		    taskList = self.getAssignedSprintTask(sprintNumber, idBacklog)
		    time = 0
		    for task in taskList:
		        time = time + task.HW_estimatedTime
		    return time
		else:
			return 0

		#Nuevo metodo Sprint 2
	def deleteAssignedSprintTask(self, sprintNumber, idBacklog, idTask):
		''' Permite la asignacion de una historia asociado a un Sprint dado su id'''
		checkSprintNumber = type(sprintNumber) == int and  MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog) == int and MIN_ID <= idBacklog
		checkidTask = type(idTask) == int and MIN_ID <= idTask
		if checkSprintNumber and checkidBacklog and checkidTask:
			oTask = task()
			tarea = oTask.getTaskById(idTask)
			if tarea:
				tarea.HW_idSprint = None
				db.session.commit()
				return True
		return False

	def assignSprintAcceptanceCriteria(self, sprintNumber, idBacklog, idAC):
		''' Permite asignar a un Sprint una criterio de aceptación asociado a sus historias'''
		checkSprintNumber = type(sprintNumber) == int and MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog)    == int and MIN_ID <= idBacklog
		checkidAC = type(idAC) == int and MIN_ID <= idAC
		
		if checkSprintNumber and checkidBacklog and checkidAC:
			oAcceptanceCriteria = acceptanceCriteria()
			criterio = oAcceptanceCriteria.getACById(idAC)
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			if criterio and sprint:
				criterio.HAC_idSprint = sprint[0].S_idSprint
				db.session.commit()
				return True
		return False

	def getAssignedSprintAC(self, sprintNumber, idBacklog):
		'''Permite obtener los criterios de aceptación asociados a un determinado Sprint'''
		checkSprintNumber = type(sprintNumber) == int and MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog)    == int and MIN_ID <= idBacklog

		if checkSprintNumber and checkidBacklog:
			sprint = self.searchIdSprint(sprintNumber, idBacklog)
			found = clsAcceptanceCriteria.query.filter_by(HAC_idSprint = sprint[0].S_idSprint).all()
			return found
		return []

	def deleteAssignedSprintAC(self, sprintNumber, idBacklog, idAC):
		''' Permite la asignacion de una historia asociado a un Sprint dado su id'''
		checkSprintNumber = type(sprintNumber) == int and MIN_SPRINT_NUMBER <= sprintNumber <= MAX_SPRINT_NUMBER
		checkidBacklog    = type(idBacklog)    == int and MIN_ID <= idBacklog
		checkidAC         = type(idAC)         == int and MIN_ID <= idAC

		if checkSprintNumber and checkidBacklog and checkidAC:
			oAcceptanceCriteria = acceptanceCriteria()
			criterio = oAcceptanceCriteria.getACById(idAC)
			if criterio:
				criterio.HAC_idSprint = None
				db.session.commit()
				return True
		return False

# Fin Clase Sprint
