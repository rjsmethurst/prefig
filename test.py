import numpy as np
import matplotlib.pyplot as plt
from prefig import Prefig

x = np.linspace(8,10,50)+ np.random.normal(0,0.5, 50)
m, c = 1.5, -3
y = m*x + c + np.random.normal(0,0.5,50)
yerr = np.random.normal(0,0.1,50)

Prefig(axcol='w', fontcol='w')
plt.errorbar(x,y, yerr, xerr=None, fmt=' ', ecolor='white', c='white', marker='D', mec='white')
plt.xlabel('measured')
plt.ylabel('observed')
plt.savefig('test.png')
