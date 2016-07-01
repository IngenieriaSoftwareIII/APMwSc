# -*- coding: utf-8 -*-
import sys
import unittest
from time                           import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

# Ruta que permite utilizar el módulo user.py
sys.path.append('../app/scrum')
from backLog    import *
from user       import *
from role       import *

class TestEquipo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_equipo(self):
        driver = self.driver

        aBacklog   = backlog()
        result     = aBacklog.deleteProduct('Test Product Equipo')
        everybacklog = clsBacklog.query.all()
        number= len(everybacklog) + 1


        aUser = user()

        
        # Creamos el backlog
        _backlog  = backlog()
        _backlog.insertBacklog('Backlog','Prueba',2)
        findId    = _backlog.findName('Backlog')
        idBacklog = findId[0].BL_idBacklog 
        # Creamos el actor
        actor = role()
        actor.insertActor('Actor','Descripcion',idBacklog)
        result    = actor.findNameActor('Actor',idBacklog)
        idActor   = result[0].A_idActor
        # Creamos el usuario
        _user = user()
        _user.insertUser('fullname','userr','password1234','prueba@user.com',idActor)

        uuu = user()
        uuu.insertUser('abcddd', 'abc', 'Password1234.', 'a@bf.c', idActor)
        #print (uuu.U_idActor)


        # Usuario inicia sesión
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys('andrea')
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys('@Andread92')
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep (2)

        # Se crea un nuevo producto
        driver.find_element_by_link_text("Nuevo").click()
        driver.find_element_by_id("fPila_nombre").send_keys("Test Product Equipo")
        driver.find_element_by_id("fPila_descripcion").clear()
        driver.find_element_by_id("fPila_descripcion").send_keys("Producto Prueba")
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Entre 1 y 20")
        sleep (2)
        driver.find_element_by_css_selector("option[value=\"1\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()

        # Ver producto
        sleep(2)
        #driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[3]").click()
        driver.get(self.base_url + "/#/VProducto/" + str(number))
        sleep (2) 

        # Agregar un usuario al producto
        driver.find_element_by_link_text("Equipo").click()
        sleep(2)
        driver.find_element_by_link_text("+Miembro").click()
        Select(driver.find_element_by_id("fEquipo_miembro")).select_by_visible_text("userr")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        Select(driver.find_element_by_id("fEquipo_rol")).select_by_visible_text("Desarrollador")
        driver.find_element_by_css_selector("#fEquipo_rol > option[value=\"0\"]").click()
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        #driver.find_element_by_link_text("Regresar").click()

        #sleep(3)
        # Modificar un usuario del producto
        #driver.find_element_by_link_text("Equipo").click()
        sleep(3)
        Select(driver.find_element_by_id("fEquipo_rol")).select_by_visible_text("Desarrollador")
        driver.find_element_by_css_selector("#fEquipo_rol > option[value=\"1\"]").click()
        sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        #driver.find_element_by_link_text("Regresar").click()

        sleep(3)
        #driver.find_element_by_link_text("Equipo").click()
        driver.find_element_by_link_text("-Miembro").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)
        #driver.find_element_by_link_text("+Miembro").click()
        #Select(driver.find_element_by_id("fEquipo_miembro")).select_by_visible_text("patricia")
        #driver.find_element_by_css_selector("option[value=\"3\"]").click()
        #Select(driver.find_element_by_id("fEquipo_rol")).select_by_visible_text("Scrum master")
        
        #driver.find_element_by_link_text("Regresar").click()
        
        result     = aBacklog.deleteProduct('Test Product Equipo')
        _user.deleteUser('userr')
        actor.deleteActor('Actor',idBacklog)
        _backlog.deleteProduct('Backlog')
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
