# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from time import sleep

class Culminacion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Culminacion(self):
        driver = self.driver
        sleep(1)
        driver.get(self.base_url + "/#/VLogin")
        sleep(1)
        driver.find_element_by_id("fLogin_usuario").clear()
        sleep(1)
        driver.find_element_by_id("fLogin_usuario").send_keys("dueno")
        sleep(1)
        driver.find_element_by_id("fLogin_clave").clear()
        sleep(1)
        driver.find_element_by_id("fLogin_clave").send_keys("Carlos.2533")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("+Producto").click()
        sleep(1)
        driver.find_element_by_id("fPila_nombre").clear()
        sleep(1)
        driver.find_element_by_id("fPila_nombre").send_keys("Prod")
        sleep(1)
        driver.find_element_by_id("fPila_descripcion").clear()
        sleep(1)
        driver.find_element_by_id("fPila_descripcion").send_keys("producto")
        sleep(1)
        Select(driver.find_element_by_id("fPila_escala")).select_by_visible_text("Entre 1 y 20")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[4]").click()
        sleep(1)
        driver.find_element_by_link_text("+Actor").click()
        sleep(1)
        driver.find_element_by_id("fActor_nombre").clear()
        sleep(1)
        driver.find_element_by_id("fActor_nombre").send_keys("actor1")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("+Accion").click()
        sleep(1)
        driver.find_element_by_id("fAccion_descripcion").clear()
        sleep(1)
        driver.find_element_by_id("fAccion_descripcion").send_keys("accion1")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("+Objetivo").click()
        sleep(1)
        driver.find_element_by_id("fObjetivo_descripcion").clear()
        sleep(1)
        driver.find_element_by_id("fObjetivo_descripcion").send_keys("obj1")
        sleep(1)
        Select(driver.find_element_by_id("fObjetivo_transversal")).select_by_visible_text("No")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("Historias").click()
        sleep(1)
        driver.find_element_by_link_text("Crear").click()
        sleep(1)
        driver.find_element_by_id("fHistoria_codigo").clear()
        sleep(1)
        driver.find_element_by_id("fHistoria_codigo").send_keys("1a")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Obligatoria")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_accion")).select_by_visible_text("accion1")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_prioridad")).select_by_visible_text("19")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("Detalles").click()
        sleep(1)
        driver.find_element_by_id("fHistoria_iniciado").click()
        sleep(1)
        driver.find_element_by_id("fHistoria_completed").click()
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("Detalles").click()
        sleep(1)
        driver.find_element_by_link_text("+Tarea").click()
        sleep(1)
        Select(driver.find_element_by_id("fTarea_miembro")).select_by_visible_text("Sin asignacion")
        sleep(1)
        driver.find_element_by_id("fTarea_descripcion").clear()
        sleep(1)
        driver.find_element_by_id("fTarea_descripcion").send_keys("tarea1")
        sleep(1)
        Select(driver.find_element_by_id("fTarea_categoria")).select_by_visible_text("Crear un diagrama UML (1)")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("Detalles").click()
        sleep(1)
        driver.find_element_by_id("fTarea_iniciado").click()
        sleep(1)
        driver.find_element_by_id("fTarea_completed").click()
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
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
