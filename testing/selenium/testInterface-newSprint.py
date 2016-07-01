# -*- encoding: utf-8 -*
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
from time                           import sleep
assert browser.current_url == 'http://0.0.0.0:5000/#/VProductos'
sleep(2)

## Create new Sprint
browser.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Sprints')])").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'+Sprint')])").click()
sleep(2)
number = browser.find_element_by_id('fSprint_numero')
number.send_keys('1')
description = browser.find_element_by_id('fSprint_descripcion')
description.send_keys('Ejemplo de un nuevo Sprint con fecha de inicio y culminacion correcta')
sleep(2)
start_date = browser.find_element_by_id('fSprint_fechini')
start_date.send_keys('19/05/2016')
sleep(1)
finish_date = browser.find_element_by_id('fSprint_fechfin')
finish_date.send_keys('26/05/2016')
sleep(1)
browser.find_element_by_xpath("//select[@id='fSprint_state']/option[@value='No iniciada']").click()
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(2)

## Modificacion de un Sprint con fecha incorrecta
browser.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
sleep(2)
description = browser.find_element_by_id('fSprint_descripcion')
description.clear()
sleep(1)
description.send_keys('Ejemplo de modificacion de un Sprint con fecha de inicio y culminacion incorrectas')
sleep(3)
start_date = browser.find_element_by_id('fSprint_fechini')
start_date.clear()
start_date.send_keys('27/04/2016')
sleep(1)
finish_date = browser.find_element_by_id('fSprint_fechfin')
finish_date.clear()
finish_date.send_keys('03/04/2016')
sleep(2)
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(2)

## Modificacion de un Sprint con fecha correcta
browser.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
sleep(2)
description = browser.find_element_by_id('fSprint_descripcion')
description.clear()
sleep(1)
description.send_keys('Ejemplo de modificacion de un Sprint con fecha de inicio y culminacion correctas')
sleep(3)
start_date = browser.find_element_by_id('fSprint_fechini')
start_date.clear()
start_date.send_keys('01/03/2016')
sleep(1)
finish_date = browser.find_element_by_id('fSprint_fechfin')
finish_date.clear()
finish_date.send_keys('10/03/2016')
sleep(2)
browser.find_element_by_xpath("//select[@id='fSprint_state']/option[@value='Terminada']").click()
sleep(2)
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(2)

