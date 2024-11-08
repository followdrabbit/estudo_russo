import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Dados de exemplo
tempo_medio_atual = 10  # em horas
tempo_alvo = 5         # em horas
historico_tempo = [9.8, 10.2, 10, 10.1, 9.9, 10.3, 10.1, 10, 9.8, 10.2]  # Histórico de tempos médios

# 1. Barra de Progresso
def barra_progresso(tempo_medio, tempo_alvo):
    fig, ax = plt.subplots(figsize=(8, 4))  # Aumentar o tamanho do gráfico
    ax.barh(['Tempo Médio'], [tempo_medio], color='orange', edgecolor='black', label='Tempo Médio Atual')
    ax.barh(['Tempo Alvo'], [tempo_alvo], color='green', edgecolor='black', label='Tempo Alvo')
    ax.set_xlim(0, max(tempo_medio, tempo_alvo) + 2)
    ax.set_xlabel('Horas')
    ax.legend()
    ax.set_title("Barra de Progresso do Tempo Médio")

    # Ajuste das margens para evitar corte de texto
    plt.subplots_adjust(left=0.2)  # Aumenta o espaço à esquerda
    plt.savefig('barra_progresso.png', bbox_inches='tight')  # Salva o gráfico com margens ajustadas
    plt.close(fig)


# 2. Gráfico de Velocímetro
def grafico_velocimetro(tempo_medio, tempo_alvo):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=tempo_medio,
        gauge={'axis': {'range': [0, 10]},
               'steps': [
                   {'range': [0, tempo_alvo], 'color': "green"},
                   {'range': [tempo_alvo, tempo_medio], 'color': "yellow"},
                   {'range': [tempo_medio, 10], 'color': "red"}],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': tempo_medio}},
        title={'text': "Gráfico de Velocímetro"}
    ))
    fig.write_html('grafico_velocimetro.html')  # Salvar o gráfico como HTML

# 3. Gráfico de Linha
def grafico_linha(historico_tempo):
    fig, ax = plt.subplots(figsize=(8, 4))  # Aumenta o tamanho do gráfico
    ax.plot(historico_tempo, marker='o', color='b', label="Tempo Médio")
    ax.axhline(y=tempo_medio_atual, color='orange', linestyle='--', label="Média Atual (8h)")
    ax.axhline(y=5, color='green', linestyle='--', label="Tempo Alvo (5h)")  # Ajusta o tempo alvo para 5 horas
    ax.set_xlabel("Período")
    ax.set_ylabel("Horas")
    ax.legend()
    ax.set_title("Gráfico de Linha - Tempo Médio ao Longo do Tempo")
    plt.savefig('grafico_linha.png', bbox_inches='tight')  # Salva o gráfico com bordas ajustadas
    plt.close(fig)


# 4. Gráfico de Rosca
def grafico_rosca(tempo_medio, tempo_alvo):
    labels = ['Abaixo do Alvo', 'Alvo Alcançado', 'Acima do Alvo']
    values = [tempo_alvo, tempo_medio - tempo_alvo, 10 - tempo_medio]
    colors = ['green', 'yellow', 'red']
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors, startangle=90, wedgeprops={'width': 0.3, 'edgecolor': 'black'})
    ax.set_title("Gráfico de Rosca - Tempo Médio")
    plt.savefig('grafico_rosca.png')  # Salvar o gráfico
    plt.close(fig)

# 5. Indicador de Semáforo
def indicador_semaforo(tempo_medio, tempo_alvo):
    fig, ax = plt.subplots(figsize=(5, 3))  # Ajuste de tamanho
    if tempo_medio < tempo_alvo:
        cor = 'green'
        status = "Abaixo do Alvo"
    elif tempo_medio == tempo_alvo:
        cor = 'yellow'
        status = "Dentro do Alvo"
    else:
        cor = 'red'
        status = "Acima do Alvo"
    
    # Texto centralizado na tela
    ax.text(0.5, 0.5, status, horizontalalignment='center', verticalalignment='center', 
            color=cor, fontsize=20, weight='bold', transform=ax.transAxes)
    
    ax.axis('off')  # Remove eixos para focar apenas no texto
    ax.set_title("Indicador de Semáforo", fontsize=16, pad=20)
    plt.savefig('indicador_semaforo.png', bbox_inches='tight')  # Salva o gráfico e ajusta bordas
    plt.close(fig)

# Gerar e salvar todos os gráficos
barra_progresso(tempo_medio_atual, tempo_alvo)
grafico_velocimetro(tempo_medio_atual, tempo_alvo)
grafico_linha(historico_tempo)
grafico_rosca(tempo_medio_atual, tempo_alvo)
indicador_semaforo(tempo_medio_atual, tempo_alvo)
