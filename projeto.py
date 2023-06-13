#Percorrendo os arquivos da pasta Vendas
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("Vendas")

tabela_total = pd.DataFrame()

#Importar as bases de dados de vendas
for arquivo in lista_arquivo:
    # se tem "Vendas" no nome do arquivo, então
    if "Vendas" in arquivo:
        #Importar o arquivo
        tabela = pd.read_csv("D:\Projetos\Estudos\python-vendas\Vendas\\" + arquivo)
        tabela_total = pd.concat([tabela_total, tabela])

#Tratar / Compilar as bases de dados
print(tabela_total)

#Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

#Calcular o produto que mais faturou (em faturamento)
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]

tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

#Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]]
print(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento") 
#passei com a variável tabela_lojas justamente por ela ser o índice da tabela, o "Loja" não iria funcionar, igual foi com o faturamento.
grafico.show()

