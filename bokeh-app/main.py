# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:37:12 2019

@author: Bruno Che León B
"""

from bokeh.plotting import figure, output_file, show

output_file("test.html")
plot = figure()
plot.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
show(plot)