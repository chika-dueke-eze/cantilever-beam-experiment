# %% import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% Load and manipulate data
# Load data from Beam1.dat
beam_data = pd.read_table("Beam1.dat")

# copy data from each column into variables 
mass = beam_data.iloc[:, 0].copy()
disp = beam_data.iloc[:, 1].copy()

# convert mass to a force
force = mass * 9.81

# convert displacement to meters
disp = disp * 2.54 / 100

# %% Perform Calculation
# use polyfit to get coefficients
p = np.polyfit(force, disp, 1)
print(p)

# %%Generate predictions
# create 100 representational force values
force_model = np.linspace(force.min(), force.max(), 100)

# calculate displacement predictions
disp_model = np.polyval(p, force_model)

# %% Generate and save plots
# Create a figure and axis
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)

# Plot displacement 
ax.plot(force, disp, 'ko')

#plot the model values
ax.plot(force_model, disp_model, 'b-')

# Turn the grid on
ax.grid(True)

# Label and title the graph
ax.set(
    xlabel = "Force (Newtons )",
    ylabel = "Displacement (meters)",
    title = "Displacement vs. Force for Beam1.dat (cgd19 )",
) 

# Use tight layout
fig.tight_layout()

# Save the graph as EPS and PDF and PNG
fig.savefig('Beam2plot.eps')
fig.savefig('Beam2plot.pdf')
fig.savefig('Beam2plot.png')
