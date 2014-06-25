import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(8,10,50)+ np.random.normal(0,0.5, 50)
m, c = 1.5, -3
y = m*x + c + np.random.normal(0,0.5,50)
yerr = N.random.normal(0,0.1,50)

P.figure()
P.errorbar(x,y, yerr, xerr=none, ecolor='white', c='white', marker='D')
P.xlabel('measured')
P.ylabel('observed')
P.savefig('test.png')
