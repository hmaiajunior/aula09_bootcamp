import pandas as pd
import os
import glob

# Uma funcao de extract que le e consolida os json

from log import log_decorator

@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(df_total)
    return df_total

# uma funcao que transforma

@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

# uma funcao que da load em csv ou parquet
"""
parametro que vai ser ou "csv" ou "parquert" ou "os dois"
"""
@log_decorator
def carregar_dados(df: pd.DataFrame, formatos: list):
    for formato in formatos:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)


@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)

# Usar a estrutura abaixo para ir realizado os testes da ETL enquanto vai desenvolvendo
            
# if __name__ == "__main__":
#     pasta_argumento: str = 'data'
#     data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
#     data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
#     formato_de_saida: list = ["csv","parquet"]
#     carregar_dados(data_frame_calculado, formato_de_saida)