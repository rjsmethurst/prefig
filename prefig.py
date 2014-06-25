#github.com/rjsmethurst/prefig
"""
    An awesome plotting object to make any plot poster or presentation ready in the colour of your choice!
    
    R. J. Smethurst 
"""


import numpy as np
import matplotlib.pyplot as plt

class Prefig(plt.Figure):
    """
        A class that can replace the 'plt.figure' python plotting command to create poster and presentaiton ready plots instantly. Plots will be initialised with a transparent background. The font colour and axes colour must be specified - e.g. 'white' for a black background poster. Font sizes will be increased in proportion to the figure size specified. 
        
        :axcol:
            The colour of the axes of the plot (optional). Default is 'black' or 'k'.
        
        :fontcol:
            The colour of the axes labels and tick labels of the plot (optional). Default is 'black' or 'k'.
        
        :rot: 
            Rotation angle of axes tick labels of the plot (optional). Default is 45 degrees.
        
        :figsize:
            tuple of integers (optional). (width, height) in inches. Default is (10,10). 
        
        """
    def __init__(self, axcol, fontcol, rot, figsize):
        self.axcol = axcol
        self.fontcol = fontcol
        self.rot = rot
        self.figsize = figsize
        plt.rc('text', color=fontcol)
        plt.rc('axes', labelsize='x-large', edgecolor=axcol, labelcolor=fontcol, facecolor='none')




