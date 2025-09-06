import numpy as np

# Parametri sistema
U = 1.0          # amplituda polarnog signala
sigma = 0.5      # standardna devijacija Gausovog šuma
N = 100000       # broj simulanih bitova

# Generisanje nasumičnih bitova (0 ili 1)
bits = np.random.randint(0, 2, N)

# Kodiranje u polarni signal: 0 -> -U, 1 -> +U
s = np.where(bits == 0, -U, U)

# Generisanje Gausovog šuma
noise = np.random.normal(0, sigma, N)

# Signal na izlazu prijemnika (integrator je u ovom slučaju implicitno sumiranje)
r = s + noise

# Detekcija: threshold na 0
received_bits = np.where(r >= 0, 1, 0)

# Brojanje grešaka
errors = np.sum(bits != received_bits)

# Procena verovatnoće greške
Pe_sim = errors / N

print(f"Procena verovatnoće greške: Pe ≈ {Pe_sim:.5f}")