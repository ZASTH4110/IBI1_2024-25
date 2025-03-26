# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# simulation parameters
N = 10000            # total population
beta = 0.3           # infection rate
gamma = 0.05         # recovery rate
time_steps = 1000    # simulation duration

# define vaccination rates from 0% to 100% in 10% steps
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # [0.0, 0.1, ..., 1.0]

# use high-contrast colormap
cmap = plt.get_cmap('tab10')  # 'tab10' is limited to 10 colors
colors = [cmap(i % 10) for i in range(len(vaccination_rates))]

# prepare figure
plt.figure(figsize=(10, 6))

# loop over vaccination rates
for idx, rate in enumerate(vaccination_rates):
    V = int(N * rate)     # vaccinated individuals
    I = 1                 # initial infected
    R = 0                 # initial recovered
    S = N - V - I         # initial susceptible

    S_array = [S]
    I_array = [I]
    R_array = [R]

    # simulation loop
    for _ in range(time_steps):
        if S > 0 and I > 0:
            infection_prob = beta * I / N
            infection_prob = min(max(infection_prob, 0), 1)
            new_infected = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
        else:
            new_infected = 0

        if I > 0:
            new_recovered = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        else:
            new_recovered = 0

        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered

        S_array.append(S)
        I_array.append(I)
        R_array.append(R)

    # plot infected curve
    plt.plot(I_array, label=f"{int(rate * 100)}%", color=colors[idx])

# finalize plot
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Individuals')
plt.title('Infection Curve under Different Vaccination Rates')
plt.legend(title='Vaccination Rate')
plt.tight_layout()
plt.savefig("SIR_vaccination_0_to_100_plot.png")
plt.show()
