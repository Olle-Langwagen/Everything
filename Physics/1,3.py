import numpy as np
import matplotlib.pyplot as plt

# Define the constants
G = 6.67e-11
M = 5.97e24
R = 6.37e6

# Define the time
dt = 1
t_end = 100000
t = np.arange(0, t_end, dt)

# Define the initial conditions
v_0 = 0
h_0 = 0

# Define the arrays
v = np.zeros(len(t))
h = np.zeros(len(t))

# Set the initial conditions
v[0] = v_0
h[0] = h_0

# Calculate the velocity and height
for i in range(len(t)-1):
    v[i+1] = v[i] - G*M*h[i]**2/(R+h[i])**2*dt
    h[i+1] = h[i] + v[i+1]*dt

# Plot the results
plt.plot(t, h)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()