import pandas as pd
import numpy as np

def limpa(info):
    try:
        info = info.split(' ', 1)[1]
        if info == '':
            return np.nan
        else:
            return info
    except:
        return np.nan

def limpa_telefone_fax_email(info):
    try:
        info = info.split(' ', 1)[1]
        if info == '' or ' ':
            return np.nan
        return info
    except:
        return np.nan
        
columns_names = ['Empresa', 'Endereço', 'Telefone', 'Fax', 'E-Mail', 'Sede', 'Representante(s)', 'CGC/CNPJ', 'Registro no MAE', 'Processo']



