import numpy as np
import matplotlib.pyplot as plt

# Parametros do circuito
Vrms = 12.0  # Tensao RMS em volts
f = 60.0  # Frequencia em Hz    
R = 10.0  # Resistencia em ohms
L = 0.002  # Indutancia em henries
C = 0.002  # Capacitancia em farads

# Calculo de impedancias e angulos de fase
w = 2 * np.pi * f  # Frequencia angular em radianos por segundo
XL = w * L  # Impedancia indutiva
XC = 1 / (w * C)  # Impedancia capacitiva

# Tempo
t = np.linspace(0, 5/f, 5000)  # Cinco ciclos de 60 Hz

# Funcoes para calcular tensao, corrente e potencia
def voltage(t):
    return Vrms * np.sqrt(2) * np.sin(w * t)

def current(t):
    Z = np.sqrt(R**2 + (XL - XC)**2)
    phi = np.arctan((XL - XC) / R)
    return (Vrms / Z) * np.sqrt(2) * np.sin(w * t + phi)

def power(t):
    Z = np.sqrt(R**2 + (XL - XC)**2)
    phi = np.arctan((XL - XC) / R)
    return (Vrms * Vrms / Z) * np.cos(phi) * (1 - np.cos(2 * w * t)) - (Vrms * Vrms / Z) * np.sin(phi) * np.sin(2 * w * t)

# Plotagem das formas de onda no mesmo gráfico
plt.figure(figsize=(12, 8))

# Tensao (linha azul)
plt.plot(t, voltage(t), label='Tensao (V)')

# Corrente (linha laranja)
plt.plot(t, current(t), label='Corrente (A)')

# Potência (linha verde)
plt.plot(t, power(t), label='Potência (W)')

# Linha horizontal no eixo x
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)

plt.title('Tensão, Corrente e Potência no Circuito RLC em Série')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
