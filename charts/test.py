import matplotlib.pyplot as plt
import numpy as np

# Parametry i dane wejściowe
Raz = 236         # Reakcja w kierunku Z
Ray = 647.5       # Reakcja w kierunku Y
Kgo = 80000000    # Wytrzymałość zmęczeniowa [Pa]
Ms = 22           # Moment skręcający [Nm]

# Odcinki wału [mm]
zginanie = 0
zginanie_skrencanie = 48
skrencanie = 98
koniec_walu = 185

# Odcinki lokalne (każdy liczony od zera)
x_zginanie_local = np.linspace(0, zginanie_skrencanie - zginanie, 100)
x_zginanie_skrencanie_local = np.linspace(0, skrencanie - zginanie_skrencanie, 100)
x_skrencanie_local = np.linspace(0, koniec_walu - skrencanie, 100)

# Funkcja obliczająca średnicę bez momentu zastępczego
def daj_d_bez_zastepczego(x):
    Mgzx = Raz * x       # Moment zginający w płaszczyźnie Z
    Mgxy = Ray * x       # Moment zginający w płaszczyźnie Y
    Mgw = np.sqrt(Mgzx**2 + Mgxy**2)  # Moment gnący wypadkowy

    d_zginanie = np.cbrt((32 * Mgw) / (np.pi * Kgo))         # Zginanie
    d_skrecenie = np.cbrt((16 * Ms) / (np.pi * Kgo))         # Skręcanie (stałe)

    d_koncowe = np.maximum(d_zginanie, d_skrecenie)          # Wybierz większą średnicę
    return d_koncowe

# Oblicz średnice dla każdego odcinka
d1 = daj_d_bez_zastepczego(x_zginanie_local)
d2 = daj_d_bez_zastepczego(x_zginanie_skrencanie_local)
d3 = daj_d_bez_zastepczego(x_skrencanie_local)

# Sklejanie wykresu na wspólnej osi X
x_full = x_zginanie_local.tolist() + \
         (x_zginanie_skrencanie_local + zginanie_skrencanie).tolist() + \
         (x_skrencanie_local + skrencanie).tolist()

y_full = d1.tolist() + d2.tolist() + d3.tolist()

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(x_full, y_full, color='blue', label='Średnica wału [mm]')
plt.xlabel('Długość wału [mm]')
plt.ylabel('Średnica [mm]')
plt.title('Średnica wału bez użycia momentu zastępczego')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
