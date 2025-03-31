import numpy as np  
import matplotlib.pyplot as plt

def f(x):
    return x**3 + x - 2 

def metodo_bissecao (f, a, b, precisao):
    if f(a) * f(b) >= 0:
        return "Não existe raiz no intervalo"
    
    iteracoes = []
    iteracao = 0
    erro = b - a
    
    while erro > precisao:
        iteracao += 1
        m = ( a + b ) / 2  
        
        # Avaliação da função no ponto médio
        f_m = f(m)
        
        # Armazenar informações dessa iteração
        iteracoes.append({
            'iteracao': iteracao,
            'a': a,
            'b': b,
            'm': m,
            'f(m)': f_m,
            'erro': erro
        })
        
        # Critério de parada pela precisão
        if abs(f_m) < precisao:
            break
        
        # Determinar o novo intervalo
        if f(a) * f_m < 0:
            b = m
        else:
            a = m
            
        erro = b - a
    
    # Exibir tabela de iterações
    print("Método da Bisseção para f(x) = x³ - x - 2")
    print("=" * 80)
    print(f"{'Iteração':^10} | {'a':^10} | {'b':^10} | {'m':^10} | {'f(m)':^15} | {'Erro':^15}")
    print("-" * 80)
    
    for it in iteracoes:
        print(f"{it['iteracao']:^10} | {it['a']:^10.6f} | {it['b']:^10.6f} | {it['m']:^10.6f} | {it['f(m)']:^15.6f} | {it['erro']:^15.6f}")
    
    # Resultado final
    m_final = (a + b) / 2
    print("=" * 80)
    print(f"Raiz aproximada: x ≈ {m_final:.6f}")
    print(f"f({m_final:.6f}) = {f(m_final):.8f}")
    print(f"Erro final: {erro:.8f}")
    print(f"Número de iterações: {iteracao}")
    
    # Plotagem
    plotar_bissecao(f, iteracoes, m_final)
    
    return m_final

def plotar_bissecao(f, iteracoes, raiz):
    # Plotar a função
    x = np.linspace(0, 2.5, 1000)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(12, 8))
    
    # Gráfico da função
    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'b-', label='f(x) = x³ - x - 2')
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.scatter([raiz], [f(raiz)], color='red', s=100, label=f'Raiz ≈ {raiz:.6f}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.title('Método da Bisseção - Função')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    # Gráfico da convergência
    plt.subplot(2, 1, 2)
    iteracoes_num = [it['iteracao'] for it in iteracoes]
    erros = [it['erro'] for it in iteracoes]
    plt.semilogy(iteracoes_num, erros, 'ro-', label='Erro por iteração')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.title('Convergência do Método da Bisseção')
    plt.xlabel('Iteração')
    plt.ylabel('Erro (escala log)')
    
    plt.tight_layout()
    plt.show()

# Parâmetros do problema
a = 1
b = 2
precisao = 1e-4

# Executar o método da bisseção
raiz = metodo_bissecao(f, a, b, precisao)