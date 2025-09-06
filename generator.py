import numpy as np
import matplotlib.pyplot as plt

# Parametri
N = 10          # broj bitova (za primer)
nS = 5          # broj odbiraka po intervalu signalizacije
U = 1.0         # amplituda polarnog signala

# 1) Generisanje informacionog niza
bits = np.random.randint(0, 2, N)
print("Informacioni bitovi:", bits)

# 2) Generisanje polarnih odbiraka
# Kodiranje: 0 -> -U, 1 -> +U
polar_bits = np.where(bits == 0, -U, U)

# Svaki bit ponovimo nS puta da dobijemo niz odbiraka
signal_samples = np.repeat(polar_bits, nS)

print("Polarni signal (odbirci):", signal_samples)

# Opcionalno: prikaz signala
plt.stem(signal_samples, use_line_collection=True)
plt.title("Polarni signal po odbircima")
plt.xlabel("Odbirak")
plt.ylabel("Amplituda")
plt.grid(True)
plt.show()