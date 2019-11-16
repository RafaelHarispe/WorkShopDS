import pandas as pd
def data_frame_siniestros():
	return pd.read_excel('data\Siniestros.xlsx', sheet_name = 'Clientes', index_col = 'Cliente')
