# -*- coding: utf-8 -*-

#from flask                           import request, session, Blueprint, json
#from sqlalchemy.ext.baked            import Result
#from datetime                        import datetime

import time
import datetime
import os
import ast
from uuid   import uuid4

#Importaciones necesarias para extraer los datos de la base de datos.
from user                     import *
from backLog                  import *
from userHistory              import *
from role                     import *
from accions                  import *
from objective                import *
from objectivesUserHistory    import *
from actorsUserHistory        import *
from task                     import *
from precedence               import *
from sprintClass              import * 
from app.scrum.subEquipoClass import *
from Team                     import *

#Importaciones necesarias para dar formato al documento.
from reportlab.pdfbase            import pdfmetrics
from reportlab.pdfbase.ttfonts    import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus           import BaseDocTemplate
from reportlab.platypus           import Frame
from reportlab.platypus           import NextPageTemplate
from reportlab.platypus           import PageBreak
from reportlab.platypus           import PageTemplate
from reportlab.platypus           import Paragraph
from reportlab.platypus           import Spacer
from reportlab.platypus           import Table
from reportlab.lib.colors         import lightgrey, lightslategray, black
from reportlab.lib.enums          import TA_CENTER,TA_RIGHT, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes      import letter
from reportlab.lib.styles         import getSampleStyleSheet
from reportlab.lib.styles         import ParagraphStyle
from reportlab.lib.units          import cm

styles = {}         #Estilos usados en el documento.
story  = []         #Lista de elementos agregados al documento.
table_styles = []   #Estilos usados para las tablas.
respond = ''


#-------------------- Fuentes usadas en el documento --------------------------
#==============================================================================

#Registramos Times New Roman y Arial Bold como fuentes permitida
pdfmetrics.registerFont(TTFont('Arial Bold',os.path.abspath('./fonts/Arial Bold.ttf')))
registerFontFamily('Arial Bold',bold='Arial Bold')

pdfmetrics.registerFont(TTFont('Arial',os.path.abspath('./fonts/Arial.ttf')))
registerFontFamily('Arial',bold='Arial')

pdfmetrics.registerFont(TTFont('Times New Roman',os.path.abspath('./fonts/Times New Roman.ttf')))
registerFontFamily('Times New Roman',bold='Times New Roman')


#----------------------------- Estilos Parrafo --------------------------------
#==============================================================================

#Definimos lo estilos para la información mostrada
styles['default'] = ParagraphStyle('default',
    fontName='Arial',
    fontSize=10,
    leading=15,
    leftIdent=0,
    rightIdent=0,
    firstLineIdent=0,
    alignment=TA_LEFT,
    spaceBefore=0,
    spaceAfter=0,
    bulletFontName='Times-Roman',
    bulletFontSize=5,
    bulletIdent=0,
    textColor='black',
    backColor=None,
    wordWrap=None,
    borderWidth=0,
    borderPadding=0,
    borderColor=None,
    borderRadius=None,
    allowWidows=1,
    alllowOrphans=0,
    textTarnsform=None,  #'uppercase' \ 'lowercase' \ None
    endDots=None,
    splitLongWords=1,
    )

styles['tittle'] = ParagraphStyle('tittle',
    parent=styles['default'],
    fontName  = 'Arial Bold',
    fontSize  = 14,
    alignment = TA_CENTER,
    )

styles['subtittle'] = ParagraphStyle('subtittle',
    parent=styles['default'],
    fontName  = 'Arial Bold',
    alignment = TA_LEFT,
    )

styles['header'] = ParagraphStyle('subtittle',
    parent=styles['default'],
    fontName  = 'Arial Bold',
    alignment = TA_CENTER,
    )

styles['tittlePage'] = ParagraphStyle('tittle',
    parent=styles['default'],
    fontName  = 'Arial Bold',
    fontSize  = 18,
    leading   = 20,
    alignment = TA_RIGHT,
    )

styles['content'] = ParagraphStyle('content',
    parent=styles['default'],
    fontName  = 'Arial',
    alignment = TA_JUSTIFY,
    )

styles['jumpLine'] = ParagraphStyle('jumpLine',
    parent=styles['default'],
    textColor='white'
    )

styles['lista'] = ParagraphStyle('lista',
    parent=styles['default'],
    bulletText=u'●',
    )

#----------------------------- Estilos Tabla ----------------------------------
#==============================================================================

#Para el encabezado de las tablas.
stylesTable0 = [('ALIGN',(0,0),(-1,-1),'RIGHT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('BOX',(0,0),(-1,-1),1,black),
                ('INNERGRID',(0,0),(-1,-1),1,black),
                ('BACKGROUND',(0,0),(-1,0),lightgrey)]

#Para el contenido de las tablas.
stylesTable1 = [('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('BOX',(0,0),(-1,-1),1,black),
                ('INNERGRID',(0,0),(-1,-1),1,black)]

#Para el encabezado de la tabla de historias de usuario.
stylesTable2 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'TOP'),
                ('BACKGROUND',(0,0),(-1,-1),lightgrey),
                ('GRID',(0,0),(-1,-1),1.5,black),
                ('BOX',(0,0),(-1,-1),1.5,black)]

#Para las epicas.
stylesTable3 = [('ALIGN',(0,0),(-1,-1),'LEFT'),    
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('LINEABOVE',(0,0),(-1,0),1.5,black),
                ('LINEBEFORE',(0,0),(0,0),1.5,black),
                ('LINEAFTER',(-1,-1),(-1,-1),1.5,black),
                ('GRID',(0,0),(-1,-1),0.8,black)]

#Para las historias que son parte de una epica.
stylesTable4 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('LINEBEFORE',(0,0),(0,0),1.5,black),
                ('LINEAFTER',(-1,-1),(-1,-1),1.5,black),
                ('GRID',(0,0),(-1,-1),0.8,black)]

#Para la ultima historia que es parte de una epica.
stylesTable5 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('LINEBEFORE',(0,0),(0,0),1.5,black),
                ('LINEAFTER',(-1,-1),(-1,-1),1.5,black),
                ('LINEBELOW',(0,0),(-1,0),5,black),
                ('GRID',(0,0),(-1,-1),0.8,black)]

#Para las historias de usuario que no son parte de una epica.
stylesTable6 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('BOX',(0,0),(-1,-1),1.5,black),
                ('GRID',(0,0),(-1,-1),0.8,black)]

#Para tabla con grid simple.
stylesTable7 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('BOX',(0,0),(-1,-1),1,black),
                ('GRID',(0,0),(-1,-1),1,black)]

#Para la tabla de pila del sprint cuando hay que mostrar mas integrantes del 
#subequipo
stylesTable8 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('BOX',(0,0),(-1,-1),1,black),
                ('GRID',(0,0),(-1,-1),1,black),
                ('BACKGROUND',(0,0),(0,0),lightgrey)]


#----------------------- Generar Documento Vision -----------------------------
#==============================================================================

def generateDocument(idProduct,path):

    width, height = letter #Tipo de hoja del documento.
    documentName  = path + "Documento-Vision.pdf" #Ruta donde se creara el documento. 


    #----------------------- Funciones especiales -----------------------------

    def header(canvas,document):
        '''Permite definir el encabezado del documento vision'''
        canvas.saveState()
        canvas.setLineWidth(width=1)
        canvas.setStrokeColor(black)

        #Dibujamos la tabla. rect(x, y, ancho, alto)
        canvas.rect(2*cm   , height - 13, width - 130, 22, fill=False, stroke=True) 
        #canvas.rect(12.3*cm, height - 13, 190        , 22, fill=False, stroke=True)      
        canvas.rect(2*cm   , height - 26, width - 130, 13, fill=False, stroke=True)  
        canvas.rect(12.3*cm, height - 26, 190        , 13, fill=False, stroke=True)  
        canvas.rect(2*cm   , height - 39, width - 130, 13, fill=False, stroke=True) 

        canvas.setFont('Arial',10)
        canvas.drawString(2.1*cm, height - 1, "Título del proyecto: ") 

        canvas.setFont('Arial Bold',10)
        canvas.drawString(5.2*cm, height - 1, projectName)

        canvas.setFont('Arial',10)
        canvas.drawString(2.1*cm,  height - 23, "Artefacto: ") 

        canvas.setFont('Arial Bold',10)
        canvas.drawString(3.7*cm,  height - 23, "Documento de Visión") 

        canvas.setFont('Arial',10)
        canvas.drawString(12.4*cm, height - 23, "Fecha: ")      

        canvas.setFont('Arial Bold',10)
        canvas.drawString(13.6*cm, height - 23, currentDate)  

        canvas.setFont('Arial',10)
        canvas.drawString(2.1*cm,  height - 36, "Método de desarrollo de Software: Scrum")
        canvas.restoreState()


    def footer(canvas,document):
        '''Permite definir el pie de pagina del documento vision'''
        canvas.saveState()
        canvas.setFont('Arial',10)

        if (document.page != 1):
            canvas.drawString(width - 180, 1 * cm, "Página %d" %document.page)
        canvas.restoreState()


    def insertJumpLine(statement,interval):
        '''Permite insertar saltos de linea en un string para que se ajuste a un espacio
           determinado'''
        split = False
        n     = len(statement) // interval
                          
        #Establecemos saltos de linea para que el contenido no se salga de la tabla.
        for i in range(n,0,-1):
            for j in range(i*interval,-1,-1):
                j -= 1
                if statement[j] == " ":
                   statement = statement[:j] + "\n" + statement[j+1:]
                   break
                if j == 0:
                    split = True

        if split:
            n    = len(statement)
            acum = 0

            for i in range(0,n+1,1):
                if i == acum:
                    statement = statement[:i] + "\n" + statement[i+1:]
                    acum += interval

        return statement


    def days_between(d1, d2):
        '''Permite calcular los dias transcurridos entre dos fechas dadas'''
        return abs((d2 - d1).days)


    #----------------------------- Clases a usar ------------------------------
    oUser        = user() 
    oTeam        = team()   
    oBacklog     = backlog()
    oSprint      = sprints()
    oActor       = role()
    oAccion      = accions()
    oObjective   = objective()
    oUserHistory = userHistory()
    oTask        = task()
    oActUserHist = actorsUserHistory()
    oObjUserHist = objectivesUserHistory()
    oSubTeam     = subEquipoClass()  


    #------------------------------ Fecha actual ------------------------------
    i = datetime.datetime.now()
    day   = i.day
    month = i.month
    year  = i.year

    currentDate  = str(day) + "/" + str(month) + "/" + str(year) 


    #---------------------------- Datos del proyecto --------------------------
    result = oBacklog.findIdProduct(idProduct)
    projectName        = result.BL_name
    projectDescription = result.BL_description
    projectScaleType   = result.BL_scaleType


    #------------------ Datos de las historias de usuario ---------------------

    #Obtenemos las historias asociadas al producto.
    userHistoriesList = oBacklog.userHistoryAsociatedToProduct(idProduct)
    
    weights        = []
    userHistories  = []
    epics          = []
    options        = {1:'podria ',2:'puede '}
    priorities     = {0:'Epica',1:'Alta',2:'Media',3:'Baja'}
    priorities2    = {i:str(i)for i in range(1,20+1)}
    priorities2[0] = 'Epica'

    #Obtenemos primero las epicas y las almacenamos en un arreglo.
    for hist in userHistoriesList:
        if oUserHistory.isEpic(hist.UH_idUserHistory):
            result = oUserHistory.transformUserHistory(hist.UH_idUserHistory)
            result['code'] = hist.UH_codeUserHistory
            epics.append(result)

    #Obtenemos los valores de las historias de usuario y sus pesos.
    for hist in userHistoriesList:
        if not oUserHistory.isEpic(hist.UH_idUserHistory):
            result = oUserHistory.transformUserHistory(hist.UH_idUserHistory)
            result['code'] = hist.UH_codeUserHistory
            userHistories.append(result)

            tupla  = (hist.UH_idUserHistory,oTask.historyWeight(hist.UH_idUserHistory))
            weights.append(tupla)

    if projectScaleType == 1:
        for hist in userHistories:
            hist['priority'] = priorities[hist['priority']]


    #------------------ Personas y roles del proyecto -------------------------
    teamList  = oTeam.getTeam(idProduct)


    #------------------ Descripcion de la metodologia -------------------------
    section1      = "Descripción de la metodología"
    introduction  = "Este documento describe la implementación del método de desarrollo de software scrum para la gerencia del desarrollo el proyecto APMwSc."
    porpose       = ""       
    motivation    = ""
    projectStatus = ""
    scope         = ""

    #-------- Descripción General del Método de Desarrollo de Software ----
    section2   = "Descripción General del Método de Desarrollo de Software"
    groundwork = ""
    teamworkValues = ""


    #-------------------- Construccion del Documento --------------------------
    #==========================================================================

    #----------------------------- Portada ------------------------------------
    story.append(Spacer(0,20))
    story.append(Paragraph(projectName + ": " + projectDescription, styles['tittlePage']))
    story.append(PageBreak())

    #-------------------------- Introduccion ----------------------------------
    story.append(Spacer(0,5))
    story.append(Paragraph(section1, styles['tittle']))
    story.append(Spacer(0,15))
    story.append(Paragraph("1. Introducción", styles['subtittle'])) 
    story.append(Spacer(0,10))
    story.append(Paragraph(introduction, styles['content']))   

    story.append(PageBreak()) 

    #------------------- Personas y Roles del proyecto ------------------------

    if teamList != []:
    
        story.append(Paragraph("2. Personas y roles del proyecto", styles['subtittle']))
        story.append(Spacer(0,10))
        
        #Cabecera de la tabla.
        t1 = Paragraph("Persona", styles['header'])
        t2 = Paragraph("Contacto", styles['header'])
        t3 = Paragraph("Rol", styles['header'])

        tam_colums      = [6.3*cm,6.3*cm,4.2*cm]
        dataTable       = [[t1,t2,t3]]
        t_roles_persons = Table(dataTable,tam_colums,style=stylesTable0,hAlign='CENTER')
        story.append(t_roles_persons)

        #Mostramos los miembros del equipo asociado al producto.

        for e in teamList:
            u = oUser.searchUser(e.EQ_username)

            if e.EQ_rol == "Product owner":
                dataTable = [[u[0].U_fullname,u[0].U_email,"Dueño del Producto"]]
                t_roles_persons = Table(dataTable,tam_colums,style=stylesTable1,hAlign='CENTER')
                story.append(t_roles_persons)

            if e.EQ_rol == "Scrum master":
                dataTable = [[u[0].U_fullname,u[0].U_email,"Maestro Scrum"]]
                t_roles_persons = Table(dataTable,tam_colums,style=stylesTable1,hAlign='CENTER')
                story.append(t_roles_persons)

        story.append(Spacer(0,20))
        dataTable       = [[t1,t2,t3]]
        t_roles_persons = Table(dataTable,tam_colums,style=stylesTable0,hAlign='CENTER')
        story.append(t_roles_persons)

        for e in teamList:
            u = oUser.searchUser(e.EQ_username)

            if e.EQ_rol == "Team member":
                dataTable = [[u[0].U_fullname,u[0].U_email,"Miembro del Equipo"]]
                t_roles_persons = Table(dataTable,tam_colums,style=stylesTable1,hAlign='CENTER')
                story.append(t_roles_persons)

        story.append(Spacer(0,25))
        #story.append(PageBreak())

    #---------------------------- Pila del producto ---------------------------

    #Lista donde se almacenara el orden en que fueron mostradas las historias y epicas.
    historiesListId = []
    
    if userHistories != [] or epics != []:
        story.append(Paragraph("4. Artefactos", styles['subtittle']))
        story.append(Spacer(0,10))
        story.append(Paragraph("Pila del producto", styles['content'])) 

        #Cabecera de la tabla.
        t1 = Paragraph("ID", styles['header'])
        t2 = Paragraph("Prioridad", styles['header'])
        t3 = Paragraph("Épicas e Historias de Usuario", styles['header'])

        tam_colums       = [2.2*cm,2.2*cm,12.4*cm]
        dataTableHist    = [[t1,t2,t3]]
        t_user_histories = Table(dataTableHist,tam_colums,style=stylesTable2,hAlign='CENTER')
        story.append(t_user_histories)

        tam_colums1 = [2.3*cm,14.5*cm]

        #Mostramos las epicas.
        for e in epics:
            #Construimos el enunciado.
            statement = "En tanto" + e['actors'] + e['actions'] + "para" + e['objectives']
            historiesListId.append(e['idHistory'])

            #Establecemos saltos de linea para que el contenido no se salga de la tabla.
            statement = insertJumpLine(statement,75)

            dataTableHist    = [[e['code'],statement]]
            t_user_histories = Table(dataTableHist,tam_colums1,style=stylesTable3,hAlign='CENTER')
            story.append(t_user_histories)

            #Eliminamos la epica que ya mostramos.
            epics.remove(e)


    	    #Obtenemos los hijos de la epica y los mostramos asociados a la epica.
            succesors = oUserHistory.succesors(e['idHistory'])

            cantSuc = len(succesors)
    		
            for h in succesors:
                result  = oUserHistory.transformUserHistory(h)
                result1 = oUserHistory.searchIdUserHistory(h)
                result['code'] = result1[0].UH_codeUserHistory
    		    
                if projectScaleType == 1:
                    result['priority'] = priorities[result['priority']]

                #Construimos el enunciado.
                statement = "En tanto" + result['actors'] + result['actions'] + "para" + result['objectives']
                historiesListId.append(result['idHistory'])

                #Establecemos saltos de linea para que el contenido no se salga de la tabla.
                statement = insertJumpLine(statement,65)

                cantSuc -= 1
     
                dataTableHist    = [[result['code'], result['priority'],statement]]

                if cantSuc != 1:
                    t_user_histories = Table(dataTableHist,tam_colums,style=stylesTable4,hAlign='CENTER')
                else:
                    t_user_histories = Table(dataTableHist,tam_colums,style=stylesTable5,hAlign='CENTER')
                story.append(t_user_histories)
                userHistories.remove(result)
      
        #Mostramos las historias de usuario que no son parte de una epica.
        for hist in userHistories:
            #Construimos el enunciado.
            statement = "En tanto" + hist['actors'] + hist['actions'] + "para" + hist['objectives']
            historiesListId.append(hist['idHistory'])

            #Establecemos saltos de linea para que el contenido no se salga de la tabla.
            statement = insertJumpLine(statement,75)

            dataTableHist    = [[hist['code'], hist['priority'],statement]]
            t_user_histories = Table(dataTableHist,tam_colums,style=stylesTable6,hAlign='CENTER')
            story.append(t_user_histories)

        story.append(Spacer(0,25))
        #story.append(PageBreak())

    #-------------------------------- Objetivos -------------------------------
    #Obtenemos todos los objetivos asociados al producto.
    objsList = oObjective.getAllObjectives(idProduct)

    if objsList != []:
        story.append(Paragraph("4.2 Objetivos", styles['content'])) 

        #Cabecera de la tabla.
        t1 = Paragraph("ID", styles['header'])
        t2 = Paragraph("Objetivo", styles['header'])
        t3 = Paragraph("ID Historia", styles['header'])

        tam_colums   = [2.2*cm,11.9*cm,2.7*cm]
        dataTableObj = [[t1,t2,t3]]
        t_user_obj   = Table(dataTableObj,tam_colums,style=stylesTable0,hAlign='CENTER')
        story.append(t_user_obj)

        #Mostramos los objetivos asociados a las historias de usuario.
        idObj = 0
        objectivesListId = []
        for h in historiesListId:
            hist = oUserHistory.searchIdUserHistory(h)
            code = hist[0].UH_codeUserHistory

            objs = oObjUserHist.idObjectivesAsociatedToUserHistory(h)

            for o in objs:
                obj  = oObjective.searchIdObjective(o)
                desc = obj[0].O_descObjective + "."
                idObj += 1
                objectivesListId.append(o)

                #Establecemos saltos de linea para que el contenido no se salga de la tabla.
                desc = insertJumpLine(desc,70)

                dataTableObj = [[idObj,desc,code]]
                t_user_obj   = Table(dataTableObj,tam_colums,style=stylesTable7,hAlign='CENTER')
                story.append(t_user_obj)

        #Mostramos los objetivos transversales y los que no estan asociados a una historia.

        #Obtenemos solo los ids
        objsIdList = []
        for o in objsList:
            objsIdList.append(o.O_idObjective)

        conj1 = set(objsIdList)
        conj2 = set(objectivesListId)
        conj  = conj1 - conj2
        remainObjects = list(conj)

        for o in remainObjects:
            obj  = oObjective.searchIdObjective(o)
            desc = obj[0].O_descObjective + "."
            idObj += 1
                          
            #Establecemos saltos de linea para que el contenido no se salga de la tabla.
            desc = insertJumpLine(desc,70)

            dataTableObj = [[idObj,desc," "]]
            t_user_obj   = Table(dataTableObj,tam_colums,style=stylesTable7,hAlign='CENTER')
            story.append(t_user_obj)

        story.append(Spacer(0,25))
        #story.append(PageBreak())

    #------------------------------ Pila del sprint ---------------------------
   
    #Obtenemos los sprints asociados al producto
    sprintsList = oSprint.getAllSprintsAsociatedToProduct(idProduct)

    if sprintsList != []:

        story.append(Paragraph("4.3 Pila del sprint", styles['content'])) 

        #Cabecera de la tabla.
        t1 = Paragraph("ID", styles['header'])
        t2 = Paragraph("Historia de Usuario", styles['header'])
        t3 = Paragraph("T/E", styles['header'])

        for s in sprintsList:

            estimatedTime = oSprint.getEstimatedTime(s.S_numero, idProduct)

            tam_colums       = [2.7*cm,12.6*cm,1.5*cm]
            dataTableSprint  = [[t1,t2,t3]]
            t_user_sprints   = Table(dataTableSprint,tam_colums,style=stylesTable0,hAlign='CENTER')
            story.append(t_user_sprints)
            
            t4 = Paragraph("Sprint " + str(s.S_numero),styles['subtittle'])

            tam_colums1      = [16.8*cm]
            tam_row          = [0.6*cm]
            dataTableSprint  = [[t4]] 
            t_user_sprints   = Table(dataTableSprint,tam_colums1,tam_row,style=stylesTable7,hAlign='CENTER')
            story.append(t_user_sprints)

            #Obtenemos las historias asociadas al sprint.
            userHistoryList = oSprint.getAssignedSprintHistory(s.S_numero,idProduct)

            for uH in userHistoryList:
                hist      = oUserHistory.transformUserHistory(uH.UH_idUserHistory)
                code      = uH.UH_codeUserHistory 
                statement = "En tanto" + hist['actors'] + hist['actions'] + "para" + hist['objectives']

                #Establecemos saltos de linea para que el contenido no se salga de la tabla.
                statement = insertJumpLine(statement,77)
             
                dataTableSprint = [[code,statement, str(estimatedTime) + "h"]]
                t_user_sprints  = Table(dataTableSprint,tam_colums,style=stylesTable7,hAlign='CENTER')
                story.append(t_user_sprints)

            #Obtenemos el subequipo del sprint.
            subTeamList = oSubTeam.getSubEquipo(s.S_idSprint)

            if subTeamList != []:
                n = len(subTeamList)

                memberSubTeam = ""

                for s in subTeamList:
                    member = s.SEQ_username
                    member = oUser.searchUser(member)
                    member = member[0].U_fullname
                    memberSubTeam += member 
                    n -= 1

                    if n != 0:
                        memberSubTeam += ", "
                    if n == 0:
                        memberSubTeam += "."

                t5 = Paragraph("Responsables", styles['content'])
                tam_colums2 = [2.7*cm,14.1*cm]

                members = insertJumpLine(memberSubTeam,90)

                dataTableSprint = [[t5,members]]
                t_user_sprints  = Table(dataTableSprint,tam_colums2,style=stylesTable8,hAlign='CENTER')
                story.append(t_user_sprints)
            story.append(Spacer(0,20))

        story.append(Spacer(0,25))
        #story.append(PageBreak())


    #--------------------------- Sprint planificado ---------------------------

    if sprintsList != []:

        for s in sprintsList:

            story.append(Paragraph("4.4 Sprint planificado", styles['content'])) 

            #Obtenemos las historias asociadas al sprint.
            userHistoryList = oSprint.getAssignedSprintHistory(s.S_numero,idProduct)

            fini =s.S_fechini
            dayIni   = fini.day
            monthIni = fini.month
            yearIni  = fini.year

            fchini = str(dayIni) + "/" + str(monthIni) + "/" + str(yearIni)

            ffin =s.S_fechfin
            dayFin   = ffin.day
            monthFin = ffin.month
            yearFin  = ffin.year

            fchfin = str(dayFin) + "/" + str(monthFin) + "/" + str(yearFin)

            duration = days_between(fini,ffin)

            #Cabecera de la tabla.
            t1 = Paragraph("Sprint "  + str(s.S_numero), styles['subtittle'])
            t2 = Paragraph("Duración:  "  + str(duration) + " d", styles['subtittle'])
            t3 = Paragraph("Inicio:  " + fchini, styles['subtittle'])
            t4 = Paragraph("Cierre:  " + fchfin, styles['subtittle'])

            tam_colums = [4.8*cm,4*cm,4*cm,4*cm]

            dataTableSprintPlan = [[t1,t2,t3,t4]]
            t_user_sprintsPlan  = Table(dataTableSprintPlan,tam_colums,style=stylesTable0,hAlign='CENTER')
            story.append(t_user_sprintsPlan)


	#--------------------------- Estructura Documento -------------------------
	#==========================================================================

    #Frame que contendrá el contenido de una hoja.
    frame_page    = Frame(78, 50, width - 166, 697, id="page")

    #Creamos el pageTemplates para header y footer. Le asignamos los frames y los canvas.
    PT_structure = PageTemplate(id='structure', frames=[frame_page],
		                    onPage=header, onPageEnd=footer)

    #Definimos el documento y de tamano carta. Creamos el DocTamplate a partir  
    #del BaseDocTemplate.
    document = BaseDocTemplate(documentName,pageSize=letter, 
		                   pageTemplates=[PT_structure],
		                   tittle="Documento-Vision", author="APMwSc")
	#Construimos el PDF
    document.build(story)
    return respond
