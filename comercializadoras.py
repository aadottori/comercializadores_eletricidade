from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from trataDados import *

matriz_infos = []

def comercio():
    firefox = webdriver.Firefox()
    firefox.get('http://www2.aneel.gov.br/aplicacoes/Agente_Comercializador/Default_Action_Agente_Comercializador.cfm')

    path_botao_pesquisar = '/html/body/form/center/table/tbody/tr[3]/td/input'
    quantidade_empresas = 363

    empresas_bichadas = []
    empresas = []

    for id in range(1, quantidade_empresas+1):
        try:
            firefox.find_element_by_xpath('/html/body/form/center/table/tbody/tr[2]/td/select/option['+str(id)+']').click()
            firefox.find_element_by_xpath(path_botao_pesquisar).click()
            time.sleep(0.5)

            path_empresa = '/html/body/form/center/center/table/tbody/tr[1]/td'
            path_endereco = '/html/body/form/center/center/table/tbody/tr[2]/td'
            path_TelefoneFaxEmail = '/html/body/form/center/center/table/tbody/tr[3]/td[1]'
            path_sede = '/html/body/form/center/center/table/tbody/tr[3]/td[2]'
            path_representantes = '/html/body/form/center/center/table/tbody/tr[4]/td'
            path_CgcCnpj = '/html/body/form/center/center/table/tbody/tr[5]/td[1]'
            path_registroMAE = '/html/body/form/center/center/table/tbody/tr[5]/td[2]'
            path_processo = '/html/body/form/center/center/table/tbody/tr[6]/td'

            empresa = firefox.find_element_by_xpath(path_empresa).text
            endereco = firefox.find_element_by_xpath(path_endereco).text

            telefone_fax_email = firefox.find_element_by_xpath(path_TelefoneFaxEmail).text
            telefone = telefone_fax_email.split('\n')[0]
            fax = telefone_fax_email.split('\n')[1]
            email = telefone_fax_email.split('\n')[2]

            sede = firefox.find_element_by_xpath(path_sede).text
            representantes = firefox.find_element_by_xpath(path_representantes).text
            cgccnpj = firefox.find_element_by_xpath(path_CgcCnpj).text
            registroMAE = firefox.find_element_by_xpath(path_registroMAE).text
            processo = firefox.find_element_by_xpath(path_processo).text

        except:
            try:
                firefox.find_element_by_xpath('/html/body/form/center/table/tbody/tr[2]/td/select/option['+str(id)+']').click()
                firefox.find_element_by_xpath(path_botao_pesquisar).click()
                time.sleep(1)

                path_empresa = '/html/body/form/center/center/table/tbody/tr[1]/td'
                path_endereco = '/html/body/form/center/center/table/tbody/tr[2]/td'
                path_TelefoneFaxEmail = '/html/body/form/center/center/table/tbody/tr[3]/td[1]'
                path_sede = '/html/body/form/center/center/table/tbody/tr[3]/td[2]'
                path_CgcCnpj = '/html/body/form/center/center/table/tbody/tr[4]/td[1]'
                path_registroMAE = '/html/body/form/center/center/table/tbody/tr[4]/td[2]'
                path_processo = '/html/body/form/center/center/table/tbody/tr[5]/td'

                empresa = firefox.find_element_by_xpath(path_empresa).text
                endereco = firefox.find_element_by_xpath(path_endereco).text
                
                telefone_fax_email = firefox.find_element_by_xpath(path_TelefoneFaxEmail).text
                telefone = telefone_fax_email.split('\n')[0]
                fax = telefone_fax_email.split('\n')[1]
                email = telefone_fax_email.split('\n')[2]
                
                sede = firefox.find_element_by_xpath(path_sede).text
                representantes = 'Representantes: '
                cgccnpj = firefox.find_element_by_xpath(path_CgcCnpj).text
                registroMAE = firefox.find_element_by_xpath(path_registroMAE).text
                processo = firefox.find_element_by_xpath(path_processo).text

            except:
                try:
                    empresas_bichadas.append(empresa)
                except:
                    empresas_bichadas.append(id)

        info = [empresa, endereco, telefone, fax, email, sede, representantes, cgccnpj, registroMAE, processo]
        
        info = list(map(limpa,info))

        matriz_infos.append(info)
        print(matriz_infos)

matriz = comercio()

comercializadoras = pd.DataFrame(matriz, columns=['Empresa', 'Endereço', 'Telefone', 'Fax', 'E-Mail', 'Sede', 'Representante(s)', 'CGC/CNPJ', 'Registro no MAE', 'Processo'])

comercializadoras.to_csv(r'/home/comercializadoras.csv')

if __name__ == "__main__":
    comercio()