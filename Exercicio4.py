import numpy as np
import matplotlib.pyplot as plt

# Analisando os dados climáticos fornecidos

# Dados dos ciclos
dados_ciclos = [
    {'Temperatura': 20.13, 'Umidade': 58.15, 'Pressao': 1006.4},
    {'Temperatura': 28.51, 'Umidade': 43.73, 'Pressao': 1013.09},
    {'Temperatura': 22.69, 'Umidade': 52.89, 'Pressao': 1005.61},
    {'Temperatura': 25.73, 'Umidade': 45.56, 'Pressao': 1018.6},
    {'Temperatura': 22.84, 'Umidade': 58.86, 'Pressao': 1008.81},
    {'Temperatura': 25.58, 'Umidade': 43.73, 'Pressao': 1013.57},
    {'Temperatura': 23.78, 'Umidade': 40.52, 'Pressao': 1003.59},
    {'Temperatura': 21.35, 'Umidade': 42.62, 'Pressao': 1003.41},
    {'Temperatura': 21.49, 'Umidade': 43.95, 'Pressao': 1017.57},
    {'Temperatura': 27.89, 'Umidade': 43.67, 'Pressao': 1008.01},
    {'Temperatura': 23.26, 'Umidade': 40.79, 'Pressao': 1011.44},
    {'Temperatura': 21.68, 'Umidade': 54.96, 'Pressao': 1001.77},
    {'Temperatura': 28.28, 'Umidade': 46.26, 'Pressao': 1010.88},
    {'Temperatura': 25.29, 'Umidade': 55.15, 'Pressao': 1004.25},
    {'Temperatura': 23.58, 'Umidade': 44.98, 'Pressao': 1011.87},
    {'Temperatura': 25.11, 'Umidade': 56.07, 'Pressao': 1010.73},
    {'Temperatura': 27.95, 'Umidade': 41.3, 'Pressao': 1009.3},
    {'Temperatura': 20.53, 'Umidade': 53.73, 'Pressao': 1016.53},
    {'Temperatura': 25.12, 'Umidade': 54.32, 'Pressao': 1012.03},
    {'Temperatura': 22.18, 'Umidade': 41.78, 'Pressao': 1010.61},
    {'Temperatura': 29.63, 'Umidade': 43.98, 'Pressao': 1004.31},
    {'Temperatura': 29.08, 'Umidade': 52.65, 'Pressao': 1005.62},
    {'Temperatura': 28.02, 'Umidade': 51.48, 'Pressao': 1005.12},
    {'Temperatura': 24.6, 'Umidade': 49.38, 'Pressao': 1011.14},
    {'Temperatura': 23.76, 'Umidade': 41.22, 'Pressao': 1019.36},
    {'Temperatura': 20.19, 'Umidade': 48.8, 'Pressao': 1000.97},
    {'Temperatura': 23.34, 'Umidade': 46.15, 'Pressao': 1014.98},
    {'Temperatura': 20.15, 'Umidade': 46.49, 'Pressao': 1017.57},
    {'Temperatura': 25.52, 'Umidade': 41.09, 'Pressao': 1019.23},
    {'Temperatura': 22.57, 'Umidade': 54.36, 'Pressao': 1013.85}
]

def calcular_estatisticas(dados, grandeza):
    valores = [ciclo[grandeza] for ciclo in dados]
    minimo = min(valores)
    maximo = max(valores)
    media = sum(valores) / len(valores)
    return {
        'Mínimo': minimo,
        'Máximo': maximo,
        'Média': media
    }
    
numero_ciclos_24h = 24 * 60 // 10  # 144 ciclos

# Calcular estatísticas para cada grandeza
estatisticas_temperatura = calcular_estatisticas(dados_ciclos, 'Temperatura')
estatisticas_umidade = calcular_estatisticas(dados_ciclos, 'Umidade')
estatisticas_pressao = calcular_estatisticas(dados_ciclos, 'Pressao')

# Resultados
print(f"Quantidade de ciclos em 24 horas do vigésimo dia: {numero_ciclos_24h}")
print("\nEstatísticas de Temperatura:")
print(f"Mínimo: {estatisticas_temperatura['Mínimo']:.2f}°C")
print(f"Máximo: {estatisticas_temperatura['Máximo']:.2f}°C")
print(f"Média: {estatisticas_temperatura['Média']:.2f}°C")

print("\nEstatísticas de Umidade:")
print(f"Mínimo: {estatisticas_umidade['Mínimo']:.2f}%")
print(f"Máximo: {estatisticas_umidade['Máximo']:.2f}%")
print(f"Média: {estatisticas_umidade['Média']:.2f}%")

print("\nEstatísticas de Pressão:")
print(f"Mínimo: {estatisticas_pressao['Mínimo']:.2f} hPa")
print(f"Máximo: {estatisticas_pressao['Máximo']:.2f} hPa")
print(f"Média: {estatisticas_pressao['Média']:.2f} hPa")