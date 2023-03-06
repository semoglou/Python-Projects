import numpy as np
import matplotlib.pyplot as plt

grid_size = (50, 50) # size of the grid
grid = np.random.choice([0, 1], size=grid_size, p=[0.5, 0.5])   # initial state of the grid, randomly generated with a 50/50 chance of a cell being alive/dead

# rules of the game & update:
def update(grid, grid_size):
    new_grid = np.zeros(grid_size, dtype=int)   # create a new empty grid of the same size to update
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
              # Compute the number of live neighbors for each cell
            num_neighbors = np.sum(grid[max(0, i-1):min(i+2, grid_size[0]), max(0, j-1):min(j+2, grid_size[1])]) - grid[i, j]   # count the number of alive neighbors around the cell
            # Apply the rules of the game
            if grid[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 3):   # rule 1: if a live cell has fewer than 2 or more than 3 live neighbors, it dies
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and num_neighbors == 3:   # rule 2: if a dead cell has exactly 3 live neighbors, it becomes alive
                new_grid[i, j] = 1
            else:   # rule 3: otherwise, the cell state stays the same:
                new_grid[i, j] = grid[i, j]
      # Update the grid
    grid[:] = new_grid[:]   # update the old grid with the new one

# Set up the plot
plt.figure() 

def game(iter):
    for i in range(iter):                 # run the game for "iter" iterations
        update(grid, grid_size)           # update the grid for each iteration
        plt.imshow(grid, cmap='binary')   # display the grid using imshow
        plt.title(f"Generation {i}")      # set the title of the plot to indicate the current generation
        plt.axis('off')                   # remove the axis labels and ticks from the plot
        plt.pause(0.1)                    # pause for a short time between iterations to allow the plot to update

game(100)
