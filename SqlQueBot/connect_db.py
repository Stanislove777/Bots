import pyodbc
import pandas as pd
import config


def sql_query(num):
	req_list = []
	sql_df = "SELECT did, name, date FROM test_tabl WHERE did = %s" % num

	conn = pyodbc.connect(config.conn_str)

	name_xlsx = num + '.xlsx'
	name_csv = num + '.csv'

	df = pd.read_sql(sql_df, conn)
	df.to_excel(name_xlsx, encoding='utf-8', index=False)
	df.to_csv(name_csv, encoding='utf-8', index=False)