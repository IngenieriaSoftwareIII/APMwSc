# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

sys.path.append('../app/scrum')
from backLog import *


class TestInterfaceSprint(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_interface_sprint(self):
        driver = self.driver

        everybacklog = clsBacklog.query.all()
        number= len(everybacklog) + 1 

        # Usuario inicia sesión
        driver.get(self.base_url + "/#/VLogin")
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

        # Se modifica un sprint ya existente
        driver.find_element_by_id("fSprint_descripcion").clear()
        driver.find_element_by_id("fSprint_descripcion").send_keys("Sprint 1, Producto 1")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)        
        
        # Se crea un nuevo sprint
        driver.find_element_by_link_text("+Sprint").click()
        sleep(2)

        driver.find_element_by_id("fSprint_numero").clear()
        driver.find_element_by_id("fSprint_numero").send_keys("15")
        sleep(2)

        driver.find_element_by_id("fSprint_descripcion").clear()
        driver.find_element_by_id("fSprint_descripcion").send_keys("Sprint 3 Producto 1")
        sleep(2)

        driver.find_element_by_id("fSprint_numero").clear()
        driver.find_element_by_id("fSprint_numero").send_keys("14")
        sleep(2)

        driver.find_element_by_id("fSprint_descripcion").clear()
        driver.find_element_by_id("fSprint_descripcion").send_keys("Sprint 3, Producto 1")
        driver.find_element_by_xpath("//button[@type='submit']").click()
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