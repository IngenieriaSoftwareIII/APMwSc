# -*- encoding: utf-8 -*
from time                           import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://0.0.0.0:5000')

assert 'scrum' in browser.title
## Login
user = browser.find_element_by_id('fLogin_usuario')
user.send_keys('whosthemark')
password = browser.find_element_by_id('fLogin_clave')
password.send_keys('ve@7IVlv' + Keys.RETURN)
sleep(1)
assert browser.current_url == 'http://0.0.0.0:5000/#/VProductos'
sleep(2)

## Create new Sprint
browser.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Historias')])").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Crear')])").click()
codigo = browser.find_element_by_id('fHistoria_codigo')
codigo.send_keys('1')
sleep(1)
browser.find_element_by_xpath("//select[@id='fHistoria_actores']/option[@value='0']").click()
sleep(1)
browser.find_element_by_xpath("//select[@id='fHistoria_tipo']/option[@value='0']").click()
sleep(1)
browser.find_element_by_xpath("//select[@id='fHistoria_accion']/option[@value='0']").click()
browser.find_element_by_xpath("//select[@id='fHistoria_objetivos']/option[@value='0']").click()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
browser.find_element_by_xpath("//select[@id='fHistoria_prioridad']/option[@value='5']").click()
sleep(2)
browser.find_element_by_xpath("//button[@type='submit']").click()
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(3)

browser.find_element_by_xpath("(//a[contains(text(),'Detalles')])[1]").click()
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
browser.find_element_by_id('fHistoria_iniciado').click()
sleep(1)
browser.find_element_by_id('fHistoria_iniciado').click()
sleep(1)
browser.find_element_by_id('fHistoria_iniciado').click()
sleep(1)
start_date = browser.find_element_by_id('fHistoria_fechini')
start_date.clear()
start_date.send_keys('30/03/2016')
sleep(2)
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(2)

browser.find_element_by_xpath("(//a[contains(text(),'Detalles')])[1]").click()
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
browser.find_element_by_id('fHistoria_iniciado').click()
sleep(2)
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(2)
