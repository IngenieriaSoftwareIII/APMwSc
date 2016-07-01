import time
import unittest

from selenium import webdriver


class testSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def wait(self):
        time.sleep(4) 

    def testPrelaciones(self):

        #self.wait()
        driver = self.driver
        driver.get("http://127.0.0.1:5000/#/VLogin")
        self.wait()
        user = driver.find_element_by_name("usuario")
        user.send_keys("oskarg")

        password = driver.find_element_by_name("clave")
        password.send_keys("1234Abcd.")
        self.wait()
        password.submit()

        #Vamos a una Historia
        self.wait()
        driver.get("http://127.0.0.1:5000/#/VProducto/1")
        self.wait()
        driver.get("http://127.0.0.1:5000/#/VHistorias/1")
        self.wait()
        driver.get("http://127.0.0.1:5000/#/VHistoria/7")

        # Marco como completa
        self.wait()
        driver.find_element_by_name("complete").click()


        # Marco como incompleta
        self.wait()
        driver.find_element_by_name("incomplete").click()


    def tearDown(self):
        self.wait()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()