
import matplotlib.pyplot as plt

# Dane
x = [-87, 0, 0, 98]

y1 = [0, 0, 147.16, 147.16]
y1.reverse()
# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x, y1, marker='', label=r'$M_{s}$')

# Etykiety osi
plt.xlabel('l [mm]')
plt.ylabel(r'$M_s$ [Nm]')

# Tytuł i legenda
plt.title('Wykres momentów skręcających wału biernego')
plt.legend()

# Siatka
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
