
import matplotlib.pyplot as plt

# Dane
x = [-87, 0, 48, 98]


y1 = [0, 5.82, 0, 0]
y1.reverse()
y2 = [0, 15.96, 0, 0]
y2.reverse()
y3 = [0, 17, 0, 0]
y3.reverse()

# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x, y1, marker='o', label=r'$M_{gzy}$')
plt.plot(x, y2, marker='o', label=r'$M_{gxy}$') 
plt.plot(x, y3, marker='o', label=r'$M_{gw} $ ')

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
