# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:32:48 2020

@author: Adam
"""

import matplotlib.pyplot as plt

import matplotlib 


colorFn = plt.get_cmap("rainbow")

minPages = 3
maxPages = 50

# calculation would be something like
pages = 20
rgb = colorFn((pages-minPages)/(maxPages-minPages))[:3]
print(matplotlib.colors.rgb2hex(rgb))





