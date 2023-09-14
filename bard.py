import pandas as pd

# Cria um DataFrame com os dados do agronegócio brasileiro
df = pd.DataFrame({
    "Produto": ["Soja", "Cana-de-açúcar", "Milho", "Café", "Arroz", "Feijão", "Carne bovina", "Carne de frango", "Carne suína"],
    "Área de cultivo (ha)": [33.7e6, 10.8e6, 13.7e6, 2.5e6, 13.3e6, 2.1e6, 3.1e6, 8.8e6, 1.1e6],
    "Exportações (US$ milhões)": [32.6e9, 29.1e9, 9.5e9, 5.6e9, 4.4e9, 2.9e9, 11.3e9, 12.1e9, 1.9e9],
    "PIB (US$ bilhões)": [43.6e9, 23.3e9, 14.5e9, 7.2e9, 10.8e9, 6.7e9, 66.8e9, 36.7e9, 23.4e9]
})

# Imprime a tabela
print(df.to_string())
