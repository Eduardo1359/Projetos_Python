import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# ==============================
# 1) Ler o CSV
# ==============================
df = pd.read_csv("C:/Users/Eduardo/OneDrive/Documentos/ecommerce_estatistica1.csv")

# ==============================
# 2) Criar gráficos com Plotly
# ==============================
# Gráfico de dispersão: relação entre quantidade vendida e preço
scatter_fig = px.scatter(
    df,
    x="Qtd_Vendidos",
    y="Preço",
    color="Marca",
    title="Relação entre Quantidade Vendida e Preço"
)

# Histograma: distribuição dos preços
hist_fig = px.histogram(
    df,
    x="Preço",
    nbins=20,
    title="Distribuição dos Preços"
)

# Gráfico de barras: preço médio por material
bar_fig = px.bar(
    df.groupby("Material", as_index=False)["Preço"].mean(),
    x="Material",
    y="Preço",
    title="Preço Médio por Material"
)

# ==============================
# 3) Criar aplicação Dash
# ==============================
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Dashboard de E-commerce", style={"textAlign": "center"}),

    dcc.Graph(
        id="scatter-plot",
        figure=scatter_fig
    ),

    dcc.Graph(
        id="histogram",
        figure=hist_fig
    ),

    dcc.Graph(
        id="bar-chart",
        figure=bar_fig
    )
])

# ==============================
# 4) Rodar servidor
# ==============================
if __name__ == "__main__":
    app.run(debug=True)

