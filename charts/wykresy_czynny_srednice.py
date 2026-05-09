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


y3 = np.full(200, 22)
#obliczanie średnic

d1 = np.cbrt((32*y1)/(np.pi*80000000))*1000
d2 = np.cbrt((10*y2)/(80000000))*1000
d3 = np.cbrt((10*y3)/85000000) *1000



# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x1, d1, marker='', color='blue') 
plt.plot(x2, d2, color='blue')
plt.plot(x3, d3, marker='', color='blue')
plt.plot([48, 48], [max(d1), max(d2)])
# Etykiety osi
plt.xlabel('l [mm]')
plt.ylabel('d [mm]')

# Tytuł i legenda
plt.title('Wykres średnic wału czynnego')
plt.legend()

# Siatka
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
