# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.keys import Keys
import getpass

def Inicio_de_sesion():
	user=raw_input("User: ")
	password=getpass.getpass("Password: ")
	driver = webdriver.Chrome(executable_path=r'/Users/miguelestrada/Downloads/chromedriver')
	driver.get('http://escolares.ucaribe.edu.mx:8082/sigmaav2/sistema/loginInicio')

	form = driver.find_element_by_class_name('form-signin')
	Usuario = form.find_element_by_xpath('/html/body/div[2]/form/div/span[2]/input')
	Usuario.send_keys(user)

	Contrasena = form.find_element_by_xpath('/html/body/div[2]/form/div/input')
	Contrasena.send_keys(password)
	driver.find_element_by_xpath('/html/body/div[2]/form/button').click()
	return driver

def Carga_de_Materias(driver):
	driver = driver
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/ul[2]/li[5]/a').click()
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/ul[2]/li[5]/ul/li/a').click()
	num = 3
	Materia_Cargada(driver,num)


def Materia_Cargada(driver,num):
	driver = driver
	if num != 0:
		element_father = driver.find_element_by_xpath('/html/body/center')
		all_options_tables = element_father.find_elements_by_tag_name('table')
		for option in all_options_tables:
			all_options_tr = option.find_elements_by_tag_name('tr')
			for option_tr in all_options_tr:
				if option_tr.text.find("1") > -1:
					if option_tr.text.find("Cerezo Acevedo / Estela") > -1:
						if option_tr.text.find("A-04") > -1:
							if option_tr.text.find("19:00-20:00") > -1:
								print "********** MATERIA ENCONTRADA **********"
								print option_tr.text
								print "****************************************"
								driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/ul[2]/li[5]/a').click()
								driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/ul[2]/li[5]/ul/li/a').click()
								if num == 1:
									element_father = driver.find_element_by_xpath('/html/body/center')
									all_options_tables = element_father.find_elements_by_tag_name('table')
								Materia_Cargada(driver,num-1)


def Numero_de_Materias():
	# num_materias = raw_input("Cuantas materias cargaras?: ")
	# materias = []
	# materias = [range(4) for i in range(int(num_materias))]
	# for i in range(len(materias)):
	# 	print materias[i]
	# Matriz = [["1","Cerezo Acevedo / Estela","A-04","19:00-20:00"],
	# 		  ["1","Cerezo Acevedo / Estela","A-04","19:00-20:00"],
	# 		  ["1","Cerezo Acevedo / Estela","A-04","19:00-20:00"]]
	# for i in range(len(Matriz)):
	# 	print Matriz[i]	
	# print Matriz[1][2]
	# return Matriz

driver = Inicio_de_sesion()
Carga_de_Materias(driver)


					