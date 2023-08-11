import pandas as pd

DadosSNeIA = pd.read_csv('MeasuredSNeIADistances.txt', sep=" ", index_col=0)

DadosSNeIA.reset_index(inplace=True)

DadosSNeIA = DadosSNeIA.rename(columns = { 'index':'name', 'name':'z_cmb',   'zcmb':'z_hel', 'zhel':'dz', 'dz':'m_b', 'mb':'dm_b'})

DadosSNeIA.drop(['dz', 'z_hel', 'dmb' ], axis=1, inplace=True)

DadosSNeIA.to_csv('MeasuredSNeIADistances.csv')


if __name__ == '__main__':
	print(DadosSNeIA)
