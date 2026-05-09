
import matplotlib.pyplot as plt
import numpy as np
start = 48   # początek odcinka [mm]
end = 98     # koniec odcinka [mm]
Mt = 147.16      # moment skręcający [kNm]
Mb_max = 17 # maksymalny moment gnący [kNm]

# Nachylenie momentu gnącego na odcinku rosnącym
slope =  Mb_max / (end - start)
# Oś x tylko dla rosnącej części (od start do mid)
d = np.linspace(start, 98, 200)

# Moment gnący rosnący liniowo
Mb = slope * (end-d)

# Moment zastępczy
Mz = np.sqrt(((1/0.47)*Mb)**2 +Mt**2)

# Dane
x = [0, 48, 48] +d.tolist() + [98, 148]




y1 = [0, 69.16, 151.54] + Mz.tolist() + [147.16, 147.16]
x.reverse()


# Tworzenie wykresu
plt.figure(figsize=(8, 6))

plt.plot(x, y1, marker='', label=r'$M_{gz}$')

# Etykiety osi
plt.xlabel('l [mm]')
plt.ylabel(r'$M_g$ [Nm]')

# Tytuł i legenda
plt.title('Wykres momentów zastępczych Wału biernego')
plt.legend()

# Siatka
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
