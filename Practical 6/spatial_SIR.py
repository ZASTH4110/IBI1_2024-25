# Firstly, create a 2D spatial 100x100 grid of susceptible individuals. 
    # population = np.zeros((100,100))
# Secondly, randomly choose a single individual to be infected
    # randomly choose two number as x and y to represent the position of the infected individual
    # outbreak = np.random.choice(range(100),2) 
    # position = [outbreak[0], outbreak[1]] let position = 1
# Thrid, set basic parameters
# Fourth, Construct the mechanism of neighborhood infection and recovery
    # For each infected cell (x, y) in the grid:
    #     For each of the 8 neighboring positions (dx, dy):
    #         Skip the current cell itself (when dx == 0 and dy == 0)
    #         Calculate the neighbor’s position (nx, ny) = (x + dx, y + dy)
    #         If the neighbor is inside the grid and is susceptible:
    #            With probability β, mark the neighbor for infection( = 1)
    # After checking neighbors:
    #     - With probability γ, the infected cell recovers (= 2)

# Fifth, plot the grid at plot_time 


import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 grid of susceptible individuals (status = 0)
population = np.zeros((100, 100))

# Randomly infect one individual
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # Mark as infected (status = 1)

# Define the time steps at which to capture snapshots
plot_point = [0, 10, 50, 100]
plots = {}  # Dictionary to store snapshots

# Infection and recovery probabilities
beta = 0.3
gamma = 0.05

# Save initial state before any infection spread
plots[0] = population.copy()

# Simulate from time step 1 to 100
for i in range(1, 101):
    infected_positions = np.where(population == 1)  # Get coordinates of infected cells
    new_infections = []

    for x, y in zip(infected_positions[0], infected_positions[1]):
        # Check 8 neighboring cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip self
                nx, ny = x + dx, y + dy
                if 0 <= nx < 100 and 0 <= ny < 100 and population[nx, ny] == 0:
                    if np.random.rand() < beta:
                        new_infections.append((nx, ny))
        # Recovery
        if np.random.rand() < gamma:
            population[x, y] = 2  # Recovered

    # Apply new infections
    for (nx, ny) in new_infections:
        population[nx, ny] = 1

    # Save snapshot if time matches
    if i in plot_point:
        plots[i] = population.copy()

# Plot results
fig, axes = plt.subplots(1, len(plot_point), figsize=(15, 4), dpi=150)

for idx, i in enumerate(plot_point):
    cmap = plt.get_cmap('viridis', 3)  # 0=susceptible, 1=infected, 2=recovered
    axes[idx].imshow(plots[i], cmap=cmap, interpolation='nearest')
    axes[idx].set_title(f"Time {i}")
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('spatial_SIR(2D).png')
plt.show()



