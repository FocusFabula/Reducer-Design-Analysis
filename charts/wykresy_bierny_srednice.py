import numpy as np
import matplotlib.pyplot as plt

# Dane
x = [0, 48 ]

y1 = [0, 11.564, 0, 0]
y2 = [0, 32]
y3 = [0, 34.11]

x1 = np.linspace(-87, 0, 200)
x2 = np.linspace(0, 48, 200)
x3 = np.linspace(48, 98, 200)

a1, b1 = np.polyfit([0, 48], [0, 17], 1)
a2, b2 = np.polyfit([48, 98], [17, 0], 1)


y1 = np.full(200, 147.26)

def zginianie(x):
    return a2 * x +b2
zginanie_f = np.vectorize(zginianie)
y3 = zginanie_f(x3)


def skrencanie_zginianie(x):
    return np.sqrt(((x*a1 + b1)/0.94 )**2 +((147.26**2)))
v_f = np.vectorize(skrencanie_zginianie)
y2 = v_f(x2)



d3 = np.cbrt((32*y3)/(np.pi*80000000))*1000
d2 = np.cbrt((10*y2)/(80000000))*1000
d1 = np.cbrt((10*y1)/ 80000000) *1000



# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x1, d1, marker='', color='blue') 
plt.plot(x2, d2, color='blue')
plt.plot(x3, d3, marker='', color='blue')
plt.plot([48, 48], [max(d3), max(d2)])

# Etykiety osi
plt.xlabel('l [mm]')
plt.ylabel(r'$M_g$ [Nm]')

# Tytuł i legenda
plt.title('Wykres momentów gnących Wału biernego')
plt.legend()

# Siatka
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
