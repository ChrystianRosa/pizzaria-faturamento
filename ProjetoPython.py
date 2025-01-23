import pandas as pd
import os

# Caminhos dos arquivos CSV
arquivo1 = r"C:\Users\chrys\Documents\ProjetosPythonVS\archive\order_details.csv"
arquivo2 = r"C:\Users\chrys\Documents\ProjetosPythonVS\archive\orders.csv"
arquivo3 = r"C:\Users\chrys\Documents\ProjetosPythonVS\archive\pizza_types.csv"
arquivo4 = r"C:\Users\chrys\Documents\ProjetosPythonVS\archive\pizzas.csv"

# Ler os arquivos CSV
df_order_details = pd.read_csv(arquivo1)
df_orders = pd.read_csv(arquivo2)
df_pizza_types = pd.read_csv(arquivo3, encoding="latin1")  # Alterar a codificação aqui
df_pizzas = pd.read_csv(arquivo4)

# Combinar detalhes do pedido com pedidos
df_combined = pd.merge(df_order_details, df_orders, how="inner", on="order_id")

# Combinar com informações de pizzas
df_combined = pd.merge(df_combined, df_pizzas, how="inner", on="pizza_id")

# Combinar com informações de tipos de pizza
df_combined = pd.merge(df_combined, df_pizza_types, how="inner", on="pizza_type_id")

# Removendo uma única coluna chamada 'coluna_a_ser_removida'
df_combined = df_combined.drop(columns=["order_details_id"])

# Substituir os pontos (.) por vírgulas (,) na coluna de preços
if "price" in df_combined.columns:
    # Garantir que a coluna "price" está no formato correto
    df_combined["price"] = df_combined["price"].astype(float).round(2)
    # Converter para string e substituir pontos por vírgulas
    df_combined["price"] = df_combined["price"].apply(lambda x: str(x).replace(".", ","))

# Salvar o resultado em um único arquivo
caminho_saida = os.path.expanduser("~/Desktop/dados_combinados.csv")
df_combined.to_csv(caminho_saida, index=False)

print(f"Bases de dados combinadas com sucesso! Arquivo salvo em: {caminho_saida}")
