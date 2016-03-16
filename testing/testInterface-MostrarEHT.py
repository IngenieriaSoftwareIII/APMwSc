# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from time import sleep

class TestInterfaceMostrarEHT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_interface_mostrar_e_h_t(self):
        driver = self.driver

        # Usuario inicia sesión
        driver.get(self.base_url + "/#/VLogin")
        sleep(1)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("ascander")
        sleep(1)

        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("C0ntr4sen4.")
        sleep(1)

        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        
        driver.find_element_by_link_text("Ver").click()
        sleep(2)

        driver.find_element_by_link_text("Sprints").click()
        sleep(2)

        driver.find_element_by_link_text("Ver").click()
        sleep(2)

        driver.find_element_by_link_text("+Asignar Historia").click()
        sleep(2)

        Select(driver.find_element_by_id("fSprintHistoria_historia")).select_by_visible_text("H1 Epica")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(4)

        # Se asigna una nueva tarea al primer sprint de la lista
        #driver.find_element_by_link_text("+Asignar Tarea").click()
        #sleep(2)
        #Select(driver.find_element_by_id("fSprintTarea_tarea")).select_by_visible_text("Tarea 1 H2")
        #sleep(1)
        #driver.find_element_by_xpath("//button[@type='submit']").click()
        #sleep(2)

        # Se guarda el sprint modificado
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)

        # Ver segundo Sprint de la lista agrega una historia
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[2]").click()
        sleep(2)
        driver.find_element_by_link_text("+Asignar Historia").click()
        sleep(2)

        Select(driver.find_element_by_id("fSprintHistoria_historia")).select_by_visible_text("H3")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)

        # Se guarda el sprint modificado
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        driver.find_element_by_xpath("(//a[contains(text(),'Ver')])[2]").click()
        sleep(3)

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