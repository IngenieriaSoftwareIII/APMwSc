# -*- coding: utf-8 -*-

#from flask                           import request, session, Blueprint, json
#from sqlalchemy.ext.baked            import Result
#from datetime                        import datetime

import time
import os
import ast
from uuid   import uuid4

#Importaciones necesarias para extraer los datos de la base de datos.
from backLog               import *
from userHistory           import *
from role                  import *
from accions               import *
from objective             import *
from objectivesUserHistory import *
from actorsUserHistory     import *
from task                  import *
from precedence            import *

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

#Definimos el estilo de la tabla
stylesTable1 = [('ALIGN',(0,0),(-1,-1),'RIGHT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('BOX',(0,0),(-1,-1),1,black),
                ('INNERGRID',(0,0),(-1,-1),1,black),
                ('BACKGROUND',(0,0),(-1,0),lightgrey)]

stylesTable2 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'TOP'),
                ('BACKGROUND',(0,0),(0,0),lightgrey)]

stylesTable3 = [('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'TOP'),
                ('BOX',(0,0),(-1,-1),1,black),
                ('GRID',(0,0),(1,2),1,lightgrey),
                ('GRID',(2,3),(3,3),1,black),
                ('BACKGROUND',(0,0),(0,0),lightgrey)]


#----------------------- Generar Documento Vision -----------------------------
#==============================================================================

def generateDocument(idProduct,idHistory,path):

    width, height = letter #Tipo de hoja del documento.
    documentName  = path + "Documento-Vision.pdf" #Ruta donde se creara el documento. 


    #----------------------- Funciones especiales -----------------------------

    def header(canvas,document):
        '''Permite definir el encabezado del documento vision'''
        canvas.saveState()
        canvas.setFont('Arial',10)
        canvas.setLineWidth(width=1)
        canvas.setStrokeColor(black)

        #Dibujamos la tabla. rect(x, y, ancho, alto)
        canvas.rect(3.1*cm, height   , width - 320, 22, fill=False, stroke=True) 
        canvas.rect(3.1*cm, height   , width - 184, 22, fill=False, stroke=True) 
     
        canvas.rect(3.1*cm, height-13, width - 320, 13, fill=False, stroke=True)  
        canvas.rect(13.4*cm, height-13, 136, 13, fill=False, stroke=True)  

        canvas.rect(3.1*cm, height-26, width - 184, 13, fill=False, stroke=True) 
        canvas.drawString(3.2*cm, height + 13, "Título del proyecto: " + projectName) 
        canvas.drawString(3.2*cm, height - 10, "Artefacto: Documento de Visión")
        canvas.drawString(13.5*cm, height - 10, "Fecha: " + currentDate)
        canvas.drawString(3.2*cm, height - 24, "Método de desarrollo de Software: Scrum")
        canvas.restoreState()


    def footer(canvas,document):
        '''Permite definir el pie de pagina del documento vision'''
        canvas.saveState()
        canvas.setFont('Arial',10)
        if (document.page != 1):
            canvas.drawString(width - 180, 1 * cm, "Página %d" %document.page)
        canvas.restoreState()

    #Importamos las clases a usar.
    oBacklog     = backlog()
    oActor       = role()
    oAccion      = accions()
    oObjective   = objective()
    oUserHistory = userHistory()
    oTask        = task()
    oActUserHist = actorsUserHistory()
    oObjUserHist = objectivesUserHistory()


    #------------------ Datos del proyecto --------------------------------

    result = oBacklog.findIdProduct(idProduct)
    projectName        = result.BL_name
    projectDescription = result.BL_description
    projectScaleType   = result.BL_scaleType


    #-------------- Datos de las historias de usuario ---------------------

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

    #------------------ Personas y roles del proyecto ---------------------

    #------------------ Descripcion de la metodologia ---------------------
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

    #======================================================================
    
    currentDate  = "03/06/2016"
    

    steakholders = [["Aldrix Marfil","aldrixmarfil@gmail.com","Scrum Master"], ["Mónica Figuera","11-10328@usb.ve", "Product Owner"], ["Jonnathan Chiu", "ngjonnathan@gmail.com", "Team Member"]]

    #-------------------- Construccion del Documento ----------------------
    #======================================================================

    #Portada
    story.append(Spacer(0,20))
    story.append(Paragraph(projectName + ": " + projectDescription, styles['tittlePage']))
    story.append(PageBreak())

    #Introduccion
    story.append(Spacer(0,5))
    story.append(Paragraph(section1, styles['tittle']))
    story.append(Spacer(0,15))
    story.append(Paragraph("1. Introducción", styles['subtittle'])) 
    story.append(Spacer(0,10))
    story.append(Paragraph(introduction, styles['content']))    

    #Personas y Roles del proyecto.
    story.append(PageBreak())
    story.append(Paragraph("2. Personas y roles del proyecto", styles['subtittle']))
    story.append(Spacer(0,10))
    
    t1 = Paragraph("Persona", styles['subtittle'])
    t2 = Paragraph("Contacto", styles['subtittle'])
    t3 = Paragraph("Rol", styles['subtittle'])

    dataTable = [[t1,t2,t3],
                 [steakholders[0][0],steakholders[1][1],steakholders[2][2]]]

    tam_colums = [6*cm,6*cm,5*cm]
    tam_rows   = [0.75*cm,0.75*cm]
    t_roles_persons = Table(dataTable,tam_colums,tam_rows,style=stylesTable1,hAlign='CENTER')
    story.append(t_roles_persons)
    story.append(PageBreak())

    #Tabla de historias de usuario.
    story.append(Paragraph("4. Artefactos", styles['subtittle']))
    story.append(Spacer(0,10))
    story.append(Paragraph("Pila del producto", styles['content'])) 

    t1 = Paragraph("ID", styles['subtittle'])
    t2 = Paragraph("Prioridad", styles['subtittle'])
    t3 = Paragraph("Épicas e Historias de Usuario", styles['subtittle'])

    tam_colums       = [2*cm,2*cm,12*cm]
    dataTableHist    = [[t1,t2,t3]]
    t_user_histories = Table(dataTableHist,tam_colums,style=stylesTable3,hAlign='CENTER')
    story.append(t_user_histories)

    tam_colums1 = [2*cm,14*cm]

    for e in epics:
        #Construimos el enunciado.
        statement = "En tanto" + e['actors'] + e['actions'] + "para" + e['objectives']

        n = len(statement) // 78
		   
        #Establecemos saltos de linea para que el contenido no se laga de la tabla.
        for i in range(n,0,-1):
            for j in range(n*78,0,-1):
                if statement[j] == " ":
                    statement = statement[:j] + "\n" + statement[j:] 
                    break
                if j == (n-1)*78: statement = statement[:n*78] + "\n" + statement[n*78:]

        dataTableHist    = [[e['code'],statement]]
        t_user_histories = Table(dataTableHist,tam_colums1,style=stylesTable3,hAlign='CENTER')
        story.append(t_user_histories)

        #Eliminamos la epica que ya mostramos.
        epics.remove(e)


	    #Obtenemos los hijos de la epica y los mostramos.
        succesors = oUserHistory.succesors(e['idHistory'])
		
        for h in succesors:
            result  = oUserHistory.transformUserHistory(h)
            result1 = oUserHistory.searchIdUserHistory(h)
            result['code'] = result1[0].UH_codeUserHistory
		    
            if projectScaleType == 1:
                result['priority'] = priorities[result['priority']]

            #Construimos el enunciado.
            statement = "En tanto" + result['actors'] + result['actions'] + "para" + result['objectives']

            n = len(statement) // 68
                       
            #Establecemos saltos de linea para que el contenido no se salga de la tabla.
            for i in range(n,0,-1):
                
                for j in range(i*68,0,-1):
                    print(i,j)
                    if statement[j] == " ":
                       
                    #    print(i*68,statement[:j] + "\n")
                    #    statement = statement[:j] + "\n" + statement[j:] 
                        #print(statement + "\n")
                        break
            print("\n")

            dataTableHist    = [[result['code'], result['priority'],statement]]
            t_user_histories = Table(dataTableHist,tam_colums,style=stylesTable3,hAlign='CENTER')
            story.append(t_user_histories)
            userHistories.remove(result)
  
    for hist in userHistories:
        #Construimos el enunciado.
        statement = "En tanto" + hist['actors'] + hist['actions'] + "para" + hist['objectives']

        n = len(statement) // 78
               
        #Establecemos saltos de linea para que el contenido no se laga de la tabla.
        for i in range(n,0,-1):
            for j in range(n*78,0,-1):
                if statement[j] == " ":
                    statement = statement[:j] + "\n" + statement[j:] 
                    break
                if j == (n-1)*78: statement = statement[:n*78] + "\n" + statement[n*78:] 

        dataTableHist    = [[hist['code'], hist['priority'],statement]]
        t_user_histories = Table(dataTableHist,tam_colums,style=stylesTable3,hAlign='CENTER')
        story.append(t_user_histories)


	#--------------------------- Estructura Documento -----------------------------
	#==============================================================================

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
    return True
