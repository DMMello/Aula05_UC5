# #pip install pandas openpyxl
# from sqlalchemy import create_engine
# import pandas as pd

# host = 'localhost'
# user = 'root'
# password = 'root'
# database = 'db_vendas'

# engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# #carregar dados da tabela 'tb_clientes' do banco exemplo3 mysql
# query_clientes = 'SELECT id_cliente, NOME, email from tb_clientes'
# df_clientes = pd.read_sql(query_clientes, engine)
# # print(df_clientes)

# # # # #carregar dados da tabela 'pedidos' do arquivo excel
# df_pedidos = pd.read_excel('tb_pedidos.xlsx')
# # print(df_clientes)

# #relacionar os dados usando merge
# df_relacionado = pd.merge(df_pedidos, df_clientes, on = 'id_cliente', how='inner')

# #ordernar o dataframe relacionado pela coluna 'id_cliente'
# df_relacionado = df_relacionado.sort_values(by='nome')

# #exibir o resultado
# print(df_relacionado)


# pip install pandas openpyxl sqlalchemy pymysql

from sqlalchemy import create_engine
import pandas as pd

# Definindo as variáveis de conexão
host = 'localhost'
user = 'root'
password = 'root'
database = 'db_vendas'

# Criando a engine de conexão
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Carregar dados da tabela 'tb_clientes' do banco MySQL
query_clientes = 'SELECT id_cliente, NOME, email FROM tb_clientes'
df_clientes = pd.read_sql(query_clientes, engine)

# Carregar dados da tabela 'pedidos' do arquivo Excel
df_pedidos = pd.read_excel('tb_pedidos.xlsx')

# Relacionar os dados usando 'merge' (realizando a junção dos DataFrames)
df_relacionado = pd.merge(df_pedidos, df_clientes, on='id_cliente', how='inner')

# Ordenar o DataFrame relacionado pela coluna 'NOME' (certifique-se de que o nome está correto)
df_relacionado = df_relacionado.sort_values(by='NOME')

print(df_relacionado())