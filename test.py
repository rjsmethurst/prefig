import numpy as np
import matplotlib.pyplot as plt
from prefig import Prefig

x = np.linspace(8,10,50)+ np.random.normal(0,0.5, 50)
m, c = 1.5, -3
y = m*x + c + np.random.normal(0,0.5,50)
yerr = np.random.normal(0,0.1,50)

Prefig()
plt.errorbar(x,y, yerr, xerr=None, fmt=' ', marker='D')
plt.plot(x, (m*x+c))
plt.xlabel('measured')
plt.ylabel('observed')
plt.savefig('test_prefig.png')

#plt.figure()
#plt.errorbar(x,y, yerr, xerr=None, fmt=' ', marker='D')
#plt.plot(x, (m*x+c))
#plt.xlabel('measured')
#plt.ylabel('observed')
#plt.savefig('test_orig.png')


