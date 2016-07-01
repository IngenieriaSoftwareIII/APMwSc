# -*- encoding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://0.0.0.0:5000')
assert 'scrum' in browser.title

# browser.find_element_by_xpath("(//a[contains(text(),'Registrarse')])").click()
# nombre_completo = browser.find_element_by_id('fUsuario_nombre')
# nombre_completo.send_keys('Reinaldo Verdugo')

# usuario = browser.find_element_by_id('fUsuario_usuario')
# usuario.send_keys('reiverdugo')

# usuario_clave = browser.find_element_by_id('fUsuario_clave')
# usuario_clave.send_keys('ve@7IVlv')

# usuario_clave = browser.find_element_by_id('fUsuario_clave2')
# usuario_clave.send_keys('ve@7IVlv')

# usuario_correo = browser.find_element_by_id('fUsuario_correo')
# usuario_correo.send_keys('verdugoreinaldo@gmail.com')

# browser.find_element_by_xpath("//select[@id='fUsuario_actorScrum']/option[@value='2']").click()
# browser.find_element_by_xpath("//button[@type='submit']").click()
# sleep(2)
user = browser.find_element_by_id('fLogin_usuario')
user.send_keys('reiverdugo')
password = browser.find_element_by_id('fLogin_clave')
password.send_keys('ve@7IVlv' + Keys.RETURN)
from time                           import sleep
assert browser.current_url == 'http://0.0.0.0:5000/#/VProductos'

sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Ver')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Historias')])").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Detalles')])[1]").click()
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'+Tarea')])").click()
sleep(2)
descripcion = browser.find_element_by_id('fTarea_descripcion')
descripcion.send_keys('Para el desarrollador de la aplicacion')

browser.find_element_by_xpath("//select[@id='fTarea_categoria']/option[@value='1']").click()
sleep(2)
peso_tarea = browser.find_element_by_id('fTarea_peso')
peso_tarea.send_keys(Keys.RETURN)
sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Detalles')])[1]").click()
sleep(2)
browser.find_element_by_xpath("//select[@id='fTarea_miembro']/option[@value='2']").click()
sleep(2)
browser.find_element_by_xpath("//button[@type='submit']").click()	
assert browser.current_url == 'http://0.0.0.0:5000/#/VHistoria/7'
