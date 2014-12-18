prefig
======
Version 0.0.1

An awesome plotting object to make any plot poster or presentation ready in the colours of your choice! 

A class that can replace the 'plt.figure()' matplotlib python plotting command to create poster and presentaiton ready plots instantly out of your existing plotting code. Plots will be initialised with a transparent background. The font colour and axes colour must be specified - e.g. 'white' for a poster with a black background. Colours are inverted if 'white' is specified as the colour. Size of fonts changed appropriately according to figure size specified. 
        
        :axcol:
            The colour of the axes of the plot (optional). Default is 'black' or 'k'.
        
        :fontcol:
            The colour of the axes and tick labels of the plot (optional). Default is 'black' or 'k'.
        
        :figsize:
            tuple of integers (optional). (width, height) in inches. Default is (16,12), the size and aspect ratio of a presentation (PPT, keynote) slide
            
        :font: 
            font family (optional). Default from rc.font file. Can be specified within plot commands instead. 


Run the program test.py to see how the changing the class of the figure to Prefig() alters the simple error bar plot. 


