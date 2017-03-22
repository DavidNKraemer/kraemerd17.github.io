# tools for numerical computation and basic plotting
import numpy as np
from scipy.stats import gaussian_kde 
import matplotlib.pyplot as plt

# seaborn is for improving the aesthetic of matplotlib's default 
# plotting it's also a pretty powerful statistical plotting 
# library, which we do not take advantage of here
import seaborn as sns
sns.set_style("white")
sns.set_palette("Blues_r")

# simulate a Brownian motion with N steps and variance T/N
def brownian_motion(T, N):
	dt = T/N
	return dt * np.cumsum(np.random.randn(N))

# plot one simulation
plt.plot(brownian_motion(10,1000))
plt.show()

# plot 100 simulations!
for i in range(100):
	plt.plot(brownian_motion(10,1000))
plt.show()

# plot 100 simulations and a histogram/KDE of the final 
# values of the sequences

# set up the figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10), sharey=True)

T, N = 1, 10000		# model parameters
time = np.linspace(0, T, N)
finals = [] # empty list, will store computed final values here
for i in range(100):
    bn = brownian_motion(T, N)
    ax1.plot(time, bn, linewidth=1)
    finals.append(bn[-1]) # append final value

# y-axis formatting 
lower, upper = ax1.get_ylim()
plot_padding = (upper - lower)/10
xc = np.linspace(lower - plot_padding, upper + plot_padding, 100)

# calculate the KDE
kde = gaussian_kde(finals)

# plot the histogram and the KDE
ax2.hist(finals, normed=True, bins=10, orientation='horizontal')
ax2.plot(kde(xc), xc, color="#ff0000", linewidth=5)
plt.show()