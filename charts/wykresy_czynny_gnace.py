
import matplotlib.pyplot as plt

# Dane
x = [0, 48, 98,  185]

y1 = [0, 11.564, 0, 0]
y2 = [0, 32, 0, 0]
y3 = [0, 34.11, 0, 0]

# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x, y1, marker='o', label=r'$M_{gzx}$')
plt.plot(x, y2, marker='o', label=r'$M_{gxy}$') 
plt.plot(x, y3, marker='o', label=r'$M_{gw} $ ')

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
