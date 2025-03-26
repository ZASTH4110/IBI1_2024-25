# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
N = 10000 # total population
I = 1 # initial number of infected individuals
R = 0 # initial number of recovered individuals
S = 9999 # initial number of susceptible individuals
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate

S_array = [S] # array to store the number of susceptible individuals
I_array = [I] # array to store the number of infected individuals
R_array = [R] # array to store the number of recovered individuals

# Using np.random.choice to randomly select individuals to be infected
# the rate of infection is determined as β*I/N
# the rate of recovery is determined as γ
# the model runs for 1000 time steps
# for i in range(1000):
# randomly choose new infected individuals and recovered individuals
# for choosing individuals, we value it as 1
# new_infected_individuals = np.random.choice([0,1],S,(1-β*I/N,β*I/N))
# new_recovered_individuals = np.random.choice([0,1],I,(1-γ,γ))
# update the number of susceptible, infected, and recovered individuals
# S = S - new_infected_individuals
# I = I + new_infected_individuals - new_recovered_individuals
# R = R + new_recovered_individuals
# append the updated values to the respective arrays
# S_array.append(S)
# I_array.append(I)
# R_array.append(R)
# Plot the number of susceptible, infected, and recovered individuals over time

for i in range(1000):
    if S > 0 and I > 0:
        infection_prob = beta * I / N
        infection_prob = min(max(infection_prob, 0), 1)  # Ensure it's between 0 and 1
        new_infected_individuals = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
    else:
        new_infected_individuals = 0
    if I > 0:
        new_recovered_individuals = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
    else:
        new_recovered_individuals = 0

    S = S - new_infected_individuals
    I = I + new_infected_individuals - new_recovered_individuals
    R = R + new_recovered_individuals

    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

    
plt.figure(figsize = (6,4) , dpi =150)
plt.plot(S_array, label = 'Susceptible', color = 'blue')
plt.plot(I_array, label = 'Infected', color = 'red')
plt.plot(R_array, label = 'Recovered', color = 'green')
plt.xlabel('Time Steps')
plt.ylabel('Number of Individuals')
plt.title('SIR Model')
plt.legend()
plt.savefig("SIR_plot.png")
plt.show()