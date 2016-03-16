# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from time import sleep

class Resume2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_resume2(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        sleep(1)
        driver.find_element_by_id("fLogin_usuario").clear()
        sleep(1)
        driver.find_element_by_id("fLogin_usuario").send_keys("mfiguera")
        sleep(1)
        driver.find_element_by_id("fLogin_clave").clear()
        sleep(1)
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
        Select(driver.find_element_by_id("fSprintHistoria_historia")).select_by_visible_text("H2")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        driver.find_element_by_link_text("+Asignar Resumen").click()
        sleep(2)
        driver.find_element_by_id("fResumenHistoria_Resumen").clear()
        sleep(1)
        driver.find_element_by_id("fResumenHistoria_Resumen").send_keys("En esta historia se discutieron puntos importantes")
        sleep(2)
        Select(driver.find_element_by_id("fResumenHistoria_Historia")).select_by_visible_text("H2")
        sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
    
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