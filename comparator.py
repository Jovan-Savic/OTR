import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Parametri sistema
# ==========================
N = 50000        # broj bitova (smanjeno radi brzine simulacije)
U = 2.0          # amplituda polarnog signala
sigma = 1.0      # standardna devijacija šuma
nS_values = [1, 5, 20]  # različiti brojevi odbiraka po bitu

# ==========================
# Generisanje informacionog niza i polarnih odbiraka
# ==========================
bits = np.random.randint(0, 2, N)
polar_bits = np.where(bits == 0, -U, U)

# ==========================
# Range pragova za graf
# ==========================
thresholds = np.linspace(-U*nS_values[-1], U*nS_values[-1], 100)

plt.figure(figsize=(8,6))

for nS in nS_values:
    # Generisanje signala sa nS odbiraka po bitu
    signal_samples = np.repeat(polar_bits, nS)
    noise = np.random.normal(0, sigma, N*nS)
    r = signal_samples + noise
    
    # Integrator: sumiranje po bitu
    integrator_output = np.array([np.sum(r[i*nS:(i+1)*nS]) for i in range(N)])
    
    Pe_list = []
    for Th in thresholds:
        received_bits = np.where(integrator_output >= Th, 1, 0)
        errors = np.sum(bits != received_bits)
        Pe_list.append(errors / N)
    
    plt.plot(thresholds, Pe_list, label=f'nS = {nS}')

plt.xlabel("Prag odlučivanja")
plt.ylabel("Verovatnoća greške Pe")
plt.title("Pe vs Prag odlučivanja za različite nS")
plt.grid(True)
plt.legend()
plt.show()