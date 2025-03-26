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


# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# make array of all susceptible population
population = np.zeros((100,100))
# check number：population[line, column]
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1

plot_point = [0, 10, 50, 100]
plots = {}

beta = 0.3
gamma = 0.05
for i in range(101):
    infected_positions = np.where(population == 1)
    new_infections = []  # store the new infections
    for x, y in zip(infected_positions[0], infected_positions[1]):
             for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 100 and 0 <= ny < 100 and population[nx, ny] == 0:
                        if np.random.rand() < beta:
                            new_infections.append((nx, ny))
             if np.random.rand() < gamma:
                population[x, y] = 2
    for (nx, ny) in new_infections:
        population[nx, ny] = 1
    if i in plot_point:
        plots[i] = population.copy()

fig, axes = plt.subplots(1, len(plot_point), figsize=(15, 4), dpi=150)
for idx, i in enumerate(plot_point):
    axes[idx].imshow(plots[i], cmap= cm.get_cmap('viridis', 3), interpolation='nearest')
    axes[idx].set_title(f"Time {i}")
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('spatial_SIR(2D).png')
plt.show()


