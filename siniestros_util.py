import pandas as pd
import getpass
import json


with open('FieldsMapper.json', 'r') as f:
    fieldsemantic = json.load(f)

def data_frame_siniestros():
	#password = getpass.getpass()
	df = pd.read_excel('data\Siniestros.xlsx', sheet_name = 'Clientes', index_col = 'Cliente')
	df.rename(columns = fieldsemantic, inplace = True)	
	return df
