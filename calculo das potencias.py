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

def power(t, Z, phi):
    return (Vrms * Vrms / Z) * np.cos(phi) * (1 - np.cos(2 * w * t)) - (Vrms * Vrms / Z )* np.sin(phi) * np.sin(2 * w * t)

# Tempo
t = np.linspace(0, 5/f, 5000)  # Cinco ciclos de 60 Hz

# Calculo das potencias para cada carga
Z_R = R
phi_R = 0
P_R = power(t, Z_R, phi_R)

Z_L = XL
phi_L = np.pi / 2
P_L = power(t, Z_L, phi_L)

Z_C = XC
phi_C = -np.pi / 2
P_C = power(t, Z_C, phi_C)

# Plotagem das potencias em um unico grafico
plt.figure(figsize=(12, 6))

plt.plot(t, P_R, label='Potencia Resistiva')
plt.plot(t, P_L, label='Potencia Indutiva')
plt.plot(t, P_C, label='Potencia Capacitiva')

plt.title('Potencias em um Circuito RLC em Série')
plt.xlabel('Tempo (s)')
plt.ylabel('Potencia (W)')
plt.legend()

plt.grid(True)
plt.show()
