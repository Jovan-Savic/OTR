import numpy as np

# ==========================
# Parametri sistema
# ==========================
N = 10**5       # broj bitova
nS = 20         # broj odbiraka po intervalu signalizacije
U = 2.0         # amplituda polarnog signala
sigma = 1.0     # standardna devijacija Gausovog šuma

# ==========================
# 1) Generisanje informacionog niza i polarnih odbiraka
# ==========================
bits = np.random.randint(0, 2, N)                 # 0 ili 1 sa P(0)=P(1)
polar_bits = np.where(bits == 0, -U, U)           # 0 -> -U, 1 -> +U
signal_samples = np.repeat(polar_bits, nS)        # ukupno N*nS odbiraka

# ==========================
# 2) Generisanje Gausovog šuma
# ==========================
noise = np.random.normal(0, sigma, N*nS)          # šum sa standardnom devijacijom sigma

# ==========================
# a) Integrator sa rasterećenjem, prag 0 (optimalan)
# ==========================
r_a = signal_samples + noise
integrator_output_a = np.array([np.sum(r_a[i*nS:(i+1)*nS]) for i in range(N)])
received_bits_a = np.where(integrator_output_a >= 0, 1, 0)
errors_a = np.sum(bits != received_bits_a)
Pe_a = errors_a / N

# ==========================
# b) Odluka po jednom odbirku po bitu (nS=1)
# ==========================
# Koristimo prvi odbirak svakog bita za odluku
r_b = signal_samples[::nS] + noise[::nS]         # jedan odbirak po bitu
received_bits_b = np.where(r_b >= 0, 1, 0)
errors_b = np.sum(bits != received_bits_b)
Pe_b = errors_b / N

# ==========================
# c) Integrator sa rasterećenjem, prag Up = 2
# ==========================
Up = 2.0
r_c = r_a  # isti signal + šum kao u tački a
received_bits_c = np.where(integrator_output_a >= Up, 1, 0)
errors_c = np.sum(bits != received_bits_c)
Pe_c = errors_c / N

# ==========================
# Rezultati
# ==========================
print(f"a) Integrator sa rasterećenjem, prag 0: Pe ≈ {Pe_a:.6f}")
print(f"b) Jedan odbirak po bitu: Pe ≈ {Pe_b:.6f}")
print(f"c) Integrator sa rasterećenjem, prag Up=2: Pe ≈ {Pe_c:.6f}")

# Komentari
print("\nKomentar:")
print("- Tačka a) (optimalni prag) daje najmanju verovatnoću greške,")
print("  jer integracija smanjuje uticaj šuma (sabiranjem nS odbiraka).")
print("- Tačka b) koristi samo jedan odbirak po bitu, što povećava uticaj šuma,")
print("  pa je verovatnoća greške veća.")
print("- Tačka c) sa pragom Up=2 pomera granicu odlučivanja,")
print("  povećava šanse da pozitivni bitovi budu pogrešno detektovani,")
print("  pa je Pe veća od optimalnog praga.")