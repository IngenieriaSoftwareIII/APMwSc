# -*- coding: utf-8 -*-
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("dueno")
        sleep(1)
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("Carlos.2533")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(1)
        driver.find_element_by_link_text("Ver").click()
        sleep(1)
        driver.find_element_by_link_text("Historias").click()
        sleep(1)
        driver.find_element_by_link_text("Crear").click()
        sleep(1)
        driver.find_element_by_id("fHistoria_codigo").clear()
        sleep(1)
        driver.find_element_by_id("fHistoria_codigo").send_keys("1a")
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_actores")).select_by_visible_text("actor1");
        Select(driver.find_element_by_id("fHistoria_tipo")).select_by_visible_text("Obligatoria")
        Select(driver.find_element_by_id("fHistoria_accion")).select_by_visible_text("accion1")
        Select(driver.find_element_by_id("fHistoria_objetivos")).select_by_visible_text("objetivo1");
        sleep(1)
        Select(driver.find_element_by_id("fHistoria_prioridad")).select_by_visible_text("18")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)
        driver.find_element_by_link_text("Detalles").click()
        sleep(1)
        driver.find_element_by_id("fHistoria_iniciado").click()
        driver.find_element_by_id("fHistoria_fechini").clear()
        driver.find_element_by_id("fHistoria_fechini").send_keys("26/05/2016")
        sleep(4)
        driver.find_element_by_id("fHistoria_completed").click()
        driver.find_element_by_id("fHistoria_fechafin").clear()
        driver.find_element_by_id("fHistoria_fechafin").send_keys("26/05/2016")
        sleep(5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
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
        driver.find_element_by_id("fTarea_fechini").clear()
        driver.find_element_by_id("fTarea_fechini").send_keys("27/05/2016")
        sleep(4)
        driver.find_element_by_id("fTarea_completed").click()
        sleep(2)
        driver.find_element_by_id("fTarea_fechaFin").clear()
        driver.find_element_by_id("fTarea_fechaFin").send_keys("28/05/2014")
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
