# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:12:14 2016

@author: AntonioPeralta13
"""

import csv
import numpy as np
from bokeh.plotting import figure, output_file, show

AvgEmployments = []
totalWages = []
AvgSalary = []
years = []
areas = []
allTitles =[]
    
with open('EmploymentAndWages.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next() 
    for row in reader:
        
        area = row[1]
        titles = row[3]
        
        areas.append(area)
        allTitles.append(titles)
        
        # get new york state data only
        if area == 'New York State':
            if titles == 'Total, All Industries':
                yrs = row[4]
                AvgEmps = row[6]
                tws = row[7]
                AvgSal = row[8]
                years.append(int(yrs))
                AvgEmployments.append(int(AvgEmps))
                totalWages.append(tws)
                AvgSalary.append(AvgSal)
 
while '' in totalWages:
    totalWages.remove('') 
while '' in AvgSalary:
    AvgSalary.remove('') 
totalWages = [s.strip('$') for s in totalWages] 
totalWages = [int(i) for i in totalWages]
AvgSalary = [s.strip('$') for s in AvgSalary] 
AvgSalary = [int(i) for i in AvgSalary]

years = [i for i in reversed(years)]
totalWages = [i for i in reversed(totalWages)]
AvgSalary = [i for i in reversed(AvgSalary)]
AvgEmployments = [i for i in reversed(AvgEmployments)]     

window_size = 30
window = np.ones(window_size)/float(window_size)

# output to static HTML file
output_file("employments.html", title="employments.py example")

# create a new plot with a a datetime axis type
p = figure(width=800, height=350)


p.circle(years, AvgEmployments, size=5, color='blue', alpha=0.5)
p.line(years, AvgEmployments, color='navy')

# customize setting attributes
p.title = "New York State Average Employment(2000-2014)"
p.legend.location = "top_left"
p.grid.grid_line_alpha=0
p.xaxis.axis_label = 'years'
p.yaxis.axis_label = 'Averages'
p.ygrid.band_fill_color="green"
p.ygrid.band_fill_alpha = 0.3

# show the results
show(p)




