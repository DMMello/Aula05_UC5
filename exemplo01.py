#pip install pandas sqlalchemy pymysql
from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password ='root'
database ='db_loja'

engine = create_engine(F'mysql+pymysql://{user}:{password}@{host}/{database}')

#leitura dos dados da tabela de produtos
df_estoque = pd.read_sql('tb_produtos', engine)
#print somente os 5 primeiros
# print(df_estoque.head())

#calcula o valor de estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
print(df_estoque)
print(30*'*')

#calcula o valor de estoque por linha
print(f"Total geral em estoque: R$ {df_estoque['TotalEstoque'].sum()}")