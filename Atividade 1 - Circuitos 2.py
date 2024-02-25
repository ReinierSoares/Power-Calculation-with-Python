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

# Funcoes para calcular tensao, corrente e potencia
def voltage(t):
    return Vrms * np.sqrt(2) * np.sin(w * t)

def current(t, Z, phi):
    return (Vrms / Z) * np.sqrt(2) * np.sin((w * t) + phi)

def power(t, Z, phi):
    return (Vrms * Vrms / Z) * np.cos(phi) * (1 - np.cos(2 * w * t)) - (Vrms * Vrms / Z )* np.sin(phi) * np.sin(2 * w * t)

# Tempo
t = np.linspace(0, 5/f, 5000)  # Cinco ciclos de 60 Hz

# Plotagem das formas de onda para cada carga
plt.figure(figsize=(12, 8))

# Carga puramente resistiva (R)
Z_R = R
phi_R = 0
plt.subplot(311)
plt.plot(t, voltage(t), label='Tensao (V)')
plt.plot(t, current(t, Z_R, phi_R), label='Corrente (A)')
plt.plot(t, power(t, Z_R, phi_R), label='Potencia (W)')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Linha no eixo x
plt.title('Carga puramente resistiva')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()

# Carga puramente indutiva (L)
Z_L = XL
phi_L = np.pi / 2
plt.subplot(312)
plt.plot(t, voltage(t), label='Tensao (V)')
plt.plot(t, current(t, Z_L, phi_L), label='Corrente (A)')
plt.plot(t, power(t, Z_L, phi_L), label='Potencia (W)')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Linha no eixo x
plt.title('Carga puramente indutiva')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()

# Carga puramente capacitiva (C)
Z_C = XC
phi_C = -np.pi / 2
plt.subplot(313)
plt.plot(t, voltage(t), label='Tensao (V)')
plt.plot(t, current(t, Z_C, phi_C), label='Corrente (A)')
plt.plot(t, power(t, Z_C, phi_C), label='Potencia (W)')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Linha no eixo x
plt.title('Carga puramente capacitiva')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
