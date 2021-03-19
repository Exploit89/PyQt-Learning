import pandas as pd
import pymssql

def dns_dwh(query):
    """Функция обращения к Хранилищу DNS на чтение
    Параметры:
    query - строка, SQL запрос
    Возвращает - pandas DataFrame с содержанием результата выполнения запроса, названия столбцов из запроса"""
    ADuser = 'PARTNER\khudaibergenov.a'
    ADpassword = 'webmaster89'
    # ADuser = str(os.getenv('SQL_DNS_DWH_LOGIN', None))
    # ADpassword =str(os.getenv('SQL_DNS_DWH_PASSWORD', None))
    conn = pymssql.connect(server='10.0.3.13', user=ADuser, password=ADpassword, database='dns_dwh')
    cursor = conn.cursor()
    cursor.execute(query)
    colnames = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=colnames)
    conn.close()
    return df

dns_dwh('''
    SELECT * FROM access.ObjectDescription
    '''
)