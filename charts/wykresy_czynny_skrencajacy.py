
import matplotlib.pyplot as plt

# Dane
x = [0, 48, 48, 185]

y1 = [0, 0, 22, 22]

# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x, y1, marker='', label=r'$M_{s}$')

# Etykiety osi
plt.xlabel('l [mm]')
plt.ylabel(r'$M_s$ [Nm]')

# Tytuł i legenda
plt.title('Wykres momentów skręcających wału czynnego')
plt.legend()

# Siatka
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
