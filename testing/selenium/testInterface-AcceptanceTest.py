# -*- encoding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://0.0.0.0:5000')

assert 'scrum' in browser.title
## Login
user = browser.find_element_by_id('fLogin_usuario')
user.send_keys('marcos')
password = browser.find_element_by_id('fLogin_clave')
password.send_keys('ve@7IVlv' + Keys.RETURN)
from time                           import sleep
assert browser.current_url == 'http://0.0.0.0:5000/#/VProductos'
sleep(2)

## Create acceptance test
browser.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Historias')])").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Detalles')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'+Prueba')])").click()
sleep(2)
description = browser.find_element_by_id('fPrueba_descripcion')
description.send_keys('Ejemplo de descripcion en prueba de aceptacion')
sleep(2)
fileUpload = browser.find_element_by_id('fPrueba_contenido')
fileUpload.send_keys("/home/marcos/soft2/venv3/APMwSc/testing/testInterface-AcceptanceTest.py")
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(2)

## Delete acceptance test
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'-prueba')])[1]").click()
browser.execute_script("window.scrollTo(0, 0);")
sleep(2)

## Create another acceptance test
browser.find_element_by_xpath("(//a[contains(text(),'+Prueba')])").click()
sleep(2)
description = browser.find_element_by_id('fPrueba_descripcion')
description.send_keys('Segundo ejemplo de descripcion en prueba de aceptacion')
sleep(2)
fileUpload = browser.find_element_by_id('fPrueba_contenido')
fileUpload.send_keys("/home/marcos/soft2/venv3/APMwSc/testing/testInterface-AcceptanceTest.py")
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(2)

## Download script
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
browser.find_element_by_xpath("(//a[contains(text(),'Descargar script')])[1]").click()
