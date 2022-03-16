import sqlite3


def create_table_query(table_name, columns):
    columns_str = ', '.join([f"{k} {v}" for k, v in columns.items()])
    command = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})'
    return command


def insert_into_table(table, data):
    keys = ', '.join(data.keys())
    values = ', '.join(map(repr, data.values()))
    query = f"INSERT INTO {table} {keys} VALUES {values}"
    return query


connection = sqlite3.connect('test.db')

print('Open Database successfuly')

table_name = "COMPANY"
columns = {
    'ID':             'INT PRIMARY KEY NOT NULL',
    'NAME':           'TEXT NOT NULL',
    'AGE':            'INT NOT NULL',
    'ADDRESS':        'CHAR(50)',
    'SALARY':         'REAL'
}
persion = {
    'ID':             '1',
    'NAME':           'Paul',
    'AGE':            '32',
    'ADDRESS':        'California',
    'SALARY':         '20000.00'
}


cmd = create_table_query(table_name, columns)
query1 = insert_into_table(table_name, persion )
print(query1)

connection.execute(cmd)
print('table create successfuly')
