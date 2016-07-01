# -*- coding: utf-8 -*-

import sys
import unittest
from time                           import sleep

from selenium                       import webdriver
from selenium.common.exceptions     import NoAlertPresentException
from selenium.common.exceptions     import NoSuchElementException
from selenium.webdriver.support.ui  import Select

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')

from backLog   import *
from user      import *
from role      import * 
from accions   import *
from objective import *
from userHistory import *
from category import *


class CasosPrueba(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_casos_prueba(self):
        driver = self.driver
        
        # Eliminamos los datos de prueba introducidos
        
        oBacklog   = backlog()
        oUser      = user()
        oActor     = role()
        oAccion    = accions()
        oObjective = objective()
        oHistory   = userHistory()
        oCategory  = category() 

        result     = oUser.deleteUser('usuario')
        result     = oBacklog.deleteProduct('Producto 1')
        result     = oCategory.deleteCategory('Categoria1') 
           
        # Casos de prueba para registrar un usuario en la aplicacion.
        
        driver.get(self.base_url + "/#/VRegistro")
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Usuario Prueba")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("usuario")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("1234.ABC")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("1234.ABC")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuarioP@gmail.com")
        Select(driver.find_element_by_id("fUsuario_actorScrum")).select_by_visible_text("Dueño de producto")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Casos de prueba para el inicio de sesion de un usuario.
        
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("usuario")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("1234.ABC")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
      
        # Caso de prueba para Crear categorias
        driver.find_element_by_link_text(u"Categorías de tareas").click()
        driver.find_element_by_id("fCategoria_nombre").clear()
        driver.find_element_by_id("fCategoria_nombre").send_keys("Categoria1")
        driver.find_element_by_id("fCategoria_peso").clear()
        driver.find_element_by_id("fCategoria_peso").send_keys("2")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)
        driver.find_element_by_xpath("(//a[contains(text(),'Regresar')])").click()
        sleep(2)
        
        # Casos de prueba para agregar Producto
        driver.find_element_by_link_text("+Producto").click()
        driver.find_element_by_id("fPila_nombre").clear()
        driver.find_element_by_id("fPila_nombre").send_keys("Producto 1")
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("Nuevo Producto")
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Alta/Media/Baja")
        sleep(3)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
         
        # Casos de prueba ver datos de un producto.
        sleep(2)
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[3]").click()
        sleep(2)
         
        # Caso de prueba para crear un actor.
        driver.find_element_by_link_text("+Actor").click()       
        driver.find_element_by_id("fActor_nombre").clear()
        driver.find_element_by_id("fActor_nombre").send_keys("Actor1")
        sleep(3)
        driver.find_element_by_id("taTextElement").send_keys("Actor nuevo")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Caso de prueba para ver el actor.      
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
        sleep(3)
    
        # Caso de prueba para modificar el actor.
        driver.find_element_by_id("taTextElement").clear()
        driver.find_element_by_id("taTextElement").send_keys("Nuevo actor 1")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)

        # Caso de prueba para crear una accion.
        sleep(3)
        driver.find_element_by_link_text("+Accion").click()
        driver.find_element_by_id("fAccion_descripcion").clear()
        driver.find_element_by_id("fAccion_descripcion").send_keys("Accion")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
           
        # Caso de prueba para ver la accion.
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[2]").click()
        sleep(3)
         
        # Caso de prueba para modificar la accion.
        driver.find_element_by_id("fAccion_descripcion").clear()
        driver.find_element_by_id("fAccion_descripcion").send_keys("Accion 1")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
    
        # Caso de prueba para crear un objetivo.
        driver.find_element_by_link_text("+Objetivo").click()
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("Objetivo2")
        sleep(2)
        Select(driver.find_element_by_id("fObjetivo_transversal")).select_by_visible_text("No")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
         
        # Caso de prueba para ver el Objetivo
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[3]").click()
        sleep(3)
         
        # Caso de prueba para modificar el objetivo.
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("Objetivo1")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
         
        # Caso para agregar Historia_Epica
        driver.find_element_by_link_text("Historias").click()
        sleep(2)
        driver.find_element_by_link_text("Crear").click()
        sleep(1)
        driver.find_element_by_id("fHistoria_codigo").clear()   
        driver.find_element_by_id("fHistoria_codigo").send_keys("H1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_actores")).select_by_visible_text("Actor1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Opcional")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_accion")).select_by_visible_text("Accion 1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_objetivos")).select_by_visible_text("Objetivo1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_prioridad")).select_by_visible_text("Alta")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
 
       # Caso para modificar historia
        driver.find_element_by_link_text("Detalles").click()
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Obligatoria")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
         
       # Creamos Historia
        driver.find_element_by_link_text("Crear").click()
        sleep(2)
        driver.find_element_by_id("fHistoria_codigo").clear()   
        driver.find_element_by_id("fHistoria_codigo").send_keys("H2")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_super")).select_by_visible_text("H1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_actores")).select_by_visible_text("Actor1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Obligatoria")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_accion")).select_by_visible_text("Accion 1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_objetivos")).select_by_visible_text("Objetivo1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_prioridad")).select_by_visible_text("Alta")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)
        
        # Caso para agregar tarea a una historia
        driver.find_element_by_xpath("(//a[contains(text(),'Detalles')])[2]").click()
        sleep(1)
        driver.find_element_by_link_text("+Tarea").click()
        sleep(1)
        driver.find_element_by_id("fTarea_descripcion").clear()
        driver.find_element_by_id("fTarea_descripcion").send_keys("Tarea1")
        Select(driver.find_element_by_id("fTarea_categoria")).select_by_visible_text("Categoria1 (2)")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Caso que modifica una tarea
        driver.find_element_by_link_text("Detalles").click()
        driver.find_element_by_id("fTarea_peso").clear()
        driver.find_element_by_id("fTarea_peso").send_keys("3")
        driver.find_element_by_id("fTarea_peso").click()
        driver.find_element_by_id("fTarea_descripcion").clear()
        driver.find_element_by_id("fTarea_descripcion").send_keys("Nueva tarea")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        driver.find_element_by_xpath("(//a[contains(text(),'Regresar')])").click()
        sleep(2)
        
        # Caso Eliminar Tarea
        driver.find_element_by_xpath("(//a[contains(text(),'Detalles')])[2]").click()
        sleep(2)
        driver.find_element_by_link_text("Detalles").click()
        sleep(2)
        driver.find_element_by_link_text("-Tarea").click()
        sleep(3)
        driver.find_element_by_xpath("(//a[contains(text(),'Regresar')])").click()
        sleep(2)
        
        # Caso Cambiar Prioridades
        driver.find_element_by_link_text("Cambiar prioridades").click()
        Select(driver.find_element_by_id("fPrioridades_prioridad")).select_by_visible_text("Baja")
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        # Eliminar Historia
        driver.find_element_by_xpath("(//a[contains(text(),'Detalles')])[2]").click()
        sleep(2)
        driver.find_element_by_link_text("-Historia").click()
        sleep(2)
        
        # Eliminar Historia
        driver.find_element_by_xpath("(//a[contains(text(),'Detalles')])[1]").click()
        sleep(2)
        driver.find_element_by_link_text("-Historia").click()
        sleep(2)
        
        # Regresamos a la vista de producto
        driver.find_element_by_xpath("(//a[contains(text(),'Regresar')])").click()
        sleep(2)
        # ver el objetivo
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[3]").click()
        sleep(3)     
         
        # Caso de prueba para eliminar el objetivo
        driver.find_element_by_link_text("-Objetivo").click()
        sleep(2)
        
        # Ver accion
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[2]").click()
        sleep(3)     
         
        # Caso de prueba para eliminar accion
        driver.find_element_by_link_text("-Accion").click()
        sleep(2)
        
        # Ver actor
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
        sleep(3)
        
        # Caso de prueba para eliminar acctor
        driver.find_element_by_link_text("-Actor").click()
        sleep(2)   
        
        # Caso de Prueba Salir
        driver.find_element_by_link_text("Salir").click()
        sleep(2)
        
        result    = oBacklog.deleteProduct('Producto 1')
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
     
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()