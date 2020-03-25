from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def comercio():
    firefox = webdriver.Firefox()
    firefox.get('http://www2.aneel.gov.br/aplicacoes/Agente_Comercializador/Default_Action_Agente_Comercializador.cfm')

    path_botao_pesquisar = '/html/body/form/center/table/tbody/tr[3]/td/input'
    quantidade_empresas = 363

    for id in range(1, quantidade_empresas+1):
        firefox.find_element_by_xpath('/html/body/form/center/table/tbody/tr[2]/td/select/option['+str(id)+']').click()
        firefox.find_element_by_xpath(path_botao_pesquisar).click()
        time.sleep(1)

if __name__ == "__main__":
    comercio()