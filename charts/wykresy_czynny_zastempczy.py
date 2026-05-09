
import matplotlib.pyplot as plt
import numpy as np
start = 0   # początek odcinka [mm]
end = 48     # koniec odcinka [mm]
Mt = 22.0      # moment skręcający [kNm]
Mb_max = 34.11 # maksymalny moment gnący [kNm]

# Nachylenie momentu gnącego na odcinku rosnącym
slope = Mb_max / (end - start)

# Oś x tylko dla rosnącej części (od start do mid)
d = np.linspace(start, 48, 200)
d2 = np.linspace(98, 48, 200)
# Moment gnący rosnący liniowo
Mb = slope * (d - start)

# Moment zastępczy
Mz = np.sqrt(Mb**2 +  ( 0.47*Mt)**2)

# Dane
x = [185, 98 ] +d2.tolist() + [48, 0]
y1 = [10.34, 10.34] + Mz.tolist() + [34.11, 0]

x.reverse()
y1.reverse()
# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x, y1, marker='', label=r'$M_{gz}$')

# Etykiety osi
plt.xlabel('l [mm]')
plt.ylabel(r'$M_g$ [Nm]')

# Tytuł i legenda
plt.title('Wykres momentów zastępczych Wału czynnego')
plt.legend()

# Siatka
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
