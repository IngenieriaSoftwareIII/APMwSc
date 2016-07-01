import time
import unittest

from selenium import webdriver


class testPrecedenceSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def wait(self):
        time.sleep(4) 

    def testPrelaciones(self):

        #self.wait()
        driver = self.driver
        driver.get("http://0.0.0.0:5000/#/VLogin")
        #self.wait()
        user = driver.find_element_by_name("usuario")
        user.send_keys("T3l3p1zz4@")

        password = driver.find_element_by_name("clave")
        password.send_keys("T3l3p1zz4@")
        #self.wait() 
        password.submit()

        #Vamos a prelaciones
        #self.wait()
        driver.get("http://0.0.0.0:5000/#/VProducto/1")
        #self.wait()
        driver.get("http://0.0.0.0:5000/#/VHistorias/1")
        #self.wait()
        driver.get("http://0.0.0.0:5000/#/VPrelaciones/1")

        #Creo

        #driver.find_element_by_link_text("+Prelación").click();
        self.wait()
        antecedente = driver.find_element_by_id("fPrelaciones_antecedente")
        for option in antecedente.find_elements_by_tag_name('option'):
            if option.text == 'Tarea 13 | historia:Historia 1':
                option.click()
                break

        self.wait()
        consecuente = driver.find_element_by_id("fPrelaciones_consecuente")
        for option in consecuente.find_elements_by_tag_name('option'):
            if option.text == 'Tarea 37 | historia:Historia 1':
                option.click()
                break

        consecuente.submit()

        #Modifico
        self.wait()
        antecedente = driver.find_element_by_id("fPrelaciones_antecedente")
        for option in antecedente.find_elements_by_tag_name('option'):
            if option.text == 'Tarea 37 | historia:Historia 1':
                option.click()
                break

        self.wait()
        consecuente = driver.find_element_by_id("fPrelaciones_consecuente")
        for option in consecuente.find_elements_by_tag_name('option'):
            if option.text == 'ALF 1 | historia:Historia 1':
                option.click()
                break

        consecuente.submit()

        #Elimino
        self.wait()
        driver.find_element_by_link_text("-Prelación").click();
        self.wait()
        #driver.find_element_by_tag_name("button").click();
        self.wait()

    def tearDown(self):
        self.wait()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()