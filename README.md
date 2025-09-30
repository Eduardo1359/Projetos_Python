# Dashboard de E-commerce 📊

Este projeto é um **dashboard interativo** criado com [Dash](https://dash.plotly.com/) e [Plotly](https://plotly.com/python/), que permite visualizar estatísticas do dataset `ecommerce_estatistica.csv`.

---

## 🚀 Como rodar o projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

   > Se não existir o `requirements.txt`, instale manualmente:

   ```bash
   pip install dash plotly pandas
   ```

3. Execute a aplicação:

   ```bash
   python app.py
   ```

4. Abra no navegador:

   ```
   http://127.0.0.1:8050/
   ```

---

## 📂 Estrutura do projeto

```
.
├── app.py                   # Código da aplicação Dash
├── ecommerce_estatistica.csv # Base de dados utilizada
└── README.md                # Este arquivo
```

---

## ✨ Funcionalidades

* Gráfico de dispersão: relação entre quantidade vendida e preço
* Histograma: distribuição dos preços
* Gráfico de barras: preço médio por material
* Dashboard interativo acessível via navegador

---

## 🖼️ Exemplo

Quando rodar o projeto, abra no navegador:
👉 [http://127.0.0.1:8050/](http://127.0.0.1:8050/)
