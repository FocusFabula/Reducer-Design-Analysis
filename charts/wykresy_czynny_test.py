import numpy as np
import matplotlib.pyplot as plt

# Dane
x = [0, 48 ]

y1 = [0, 11.564, 0, 0]
y2 = [0, 32]
y3 = [0, 34.11]

x1 = np.linspace(0, 48)
x2 = np.linspace(48, 98)
x3 = np.linspace(98, 185, 200)

a1, b1 = np.polyfit([0, 48], [0, 34.11], 1)
a2, b2 = np.polyfit([48, 98], [34.11, 0], 1)

def zginianie(x):
    return a1 * x +b1
zginanie_f = np.vectorize(zginianie)
y1 = zginanie_f(x1)


def skrencanie_zginianie(x):
    return np.sqrt(((x*a2 + b2))**2 +((0.94*22)**2))
v_f = np.vectorize(skrencanie_zginianie)
y2 = v_f(x2)


y3 = np.full(200, 22*0.94)


# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x2, y2, marker='', color='blue') 
plt.plot(x1, y1, color='blue')
plt.plot(x3, y3, marker='', color='blue')
plt.plot([48, 48], [34.11, max(y2)], color='blue')
# Etykiety osi
plt.xlabel('l [mm]')
plt.ylabel(r'$M_g$ [Nm]')

# Tytuł i legenda
plt.title('Wykres momentów gnących Wału czynnego')
plt.legend()

# Siatka
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
