import numpy as np

# ==========================
# Parametri sistema
# ==========================
N = 10000       # broj bitova
nS = 10         # broj odbiraka po intervalu signalizacije
U = 1.0         # amplituda polarnog signala
sigma = 0.5     # standardna devijacija Gausovog šuma

# ==========================
# 1) Generisanje informacionog niza
# ==========================
bits = np.random.randint(0, 2, N)                 # 0 ili 1 sa P(0)=P(1)
polar_bits = np.where(bits == 0, -U, U)           # 0 -> -U, 1 -> +U

# Generisanje niza odbiraka polarnog signala
signal_samples = np.repeat(polar_bits, nS)        # ukupno N*nS odbiraka

# ==========================
# 2) Generisanje Gausovog šuma
# ==========================
# Jedinična srednja snaga -> varijanca = 1
noise = np.random.normal(0, 1.0, N*nS)

# ==========================
# 3) Odbirci na ulazu prijemnika i izlaz integratora
# ==========================
r = signal_samples + sigma*noise                  # ulaz prijemnika: signal + šum

# Integracija u svakom intervalu signalizacije (sabiranje odbiraka po bitu)
integrator_output = np.array([np.sum(r[i*nS:(i+1)*nS]) for i in range(N)])

# Optimalni prag odlučivanja za polarni signal je 0
received_bits = np.where(integrator_output >= 0, 1, 0)

# ==========================
# 4) Procenjena informaciona sekvenca
# ==========================
# received_bits već predstavlja sekvencu po bitu nakon odlučivanja

# ==========================
# 5) Procena verovatnoće greške
# ==========================
errors = np.sum(bits != received_bits)
Pe_sim = errors / N

print(f"Broj bitnih grešaka: {errors} / {N}")
print(f"Procena verovatnoće greške po bitu: Pe ≈ {Pe_sim:.5f}")