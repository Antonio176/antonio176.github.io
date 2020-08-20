# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:12:06 2016

@author: AntonioPeralta13
"""

import csv
import numpy as np
from bokeh.plotting import figure, output_file, show


rates2000 = []
rates2001 = []
rates2002 = []
rates2003 = []
rates2004 = []
rates2005 = []
rates2006 = []
rates2007 = []
rates2008 = []
rates2009 = []
rates2010 = []
rates2011 = []
rates2012 = []
rates2013 = []
rates2014 = []
with open('LocalAreaUnemployment.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        location = row[0]
        yrs = row[1]
        if location == 'New York State':
            if yrs == '2000':
                rates = row[6]
                rates2000.append(rates)
            elif yrs == '2001':
                rates = row[6]
                rates2001.append(rates)
            elif yrs == '2002':
                rates = row[6]
                rates2002.append(rates)
            elif yrs == '2003':
                rates = row[6]
                rates2003.append(rates)
            elif yrs == '2004':
                rates = row[6]
                rates2004.append(rates)
            elif yrs == '2005':
                rates = row[6]
                rates2005.append(rates)
            elif yrs == '2006':
                rates = row[6]
                rates2006.append(rates)
            elif yrs == '2007':
                rates = row[6]
                rates2007.append(rates)
            elif yrs == '2008':
                rates = row[6]
                rates2008.append(rates)
            elif yrs == '2009':
                rates = row[6]
                rates2009.append(rates)
            elif yrs == '2010':
                rates = row[6]
                rates2010.append(rates)
            elif yrs == '2011':
                rates = row[6]
                rates2011.append(rates)
            elif yrs == '2012':
                rates = row[6]
                rates2012.append(rates)
            elif yrs == '2013':
                rates = row[6]
                rates2013.append(rates)
            elif yrs == '2014':
                rates = row[6]
                rates2014.append(rates)
            
rates2000 = [s.strip('%') for s in rates2000] 
rates2000 = [float(i) for i in rates2000] 
rates2001 = [s.strip('%') for s in rates2001] 
rates2001 = [float(i) for i in rates2001] 
rates2002 = [s.strip('%') for s in rates2002] 
rates2002 = [float(i) for i in rates2002] 
rates2003 = [s.strip('%') for s in rates2003] 
rates2003 = [float(i) for i in rates2003] 
rates2004 = [s.strip('%') for s in rates2004] 
rates2004 = [float(i) for i in rates2004] 
rates2005 = [s.strip('%') for s in rates2005] 
rates2005 = [float(i) for i in rates2005] 
rates2006 = [s.strip('%') for s in rates2006] 
rates2006 = [float(i) for i in rates2006] 
rates2007 = [s.strip('%') for s in rates2007] 
rates2007 = [float(i) for i in rates2007] 
rates2008 = [s.strip('%') for s in rates2008] 
rates2008 = [float(i) for i in rates2008] 
rates2009 = [s.strip('%') for s in rates2009] 
rates2009 = [float(i) for i in rates2009] 
rates2010 = [s.strip('%') for s in rates2010] 
rates2010 = [float(i) for i in rates2010] 
rates2011 = [s.strip('%') for s in rates2011] 
rates2011 = [float(i) for i in rates2011] 
rates2012 = [s.strip('%') for s in rates2012] 
rates2012 = [float(i) for i in rates2012] 
rates2013 = [s.strip('%') for s in rates2013] 
rates2013 = [float(i) for i in rates2013] 
rates2014 = [s.strip('%') for s in rates2014] 
rates2014 = [float(i) for i in rates2014] 

average = 0
sum = 0    
for n in rates2000:
    sum = sum + n
average = sum / len(rates2000)
average1 = 0
sum = 0    
for n in rates2001:
    sum = sum + n
average1 = sum / len(rates2001)
average2 = 0
sum = 0    
for n in rates2002:
    sum = sum + n
average2 = sum / len(rates2002)
average3 = 0
sum = 0    
for n in rates2003:
    sum = sum + n
average3 = sum / len(rates2003)
average4 = 0
sum = 0    
for n in rates2004:
    sum = sum + n
average4 = sum / len(rates2004)
average5 = 0
sum = 0    
for n in rates2005:
    sum = sum + n
average5 = sum / len(rates2005)
average6 = 0
sum = 0    
for n in rates2006:
    sum = sum + n
average6 = sum / len(rates2006)
average7 = 0
sum = 0    
for n in rates2007:
    sum = sum + n
average7 = sum / len(rates2007)
average8 = 0
sum = 0    
for n in rates2008:
    sum = sum + n
average8 = sum / len(rates2008)
average9 = 0
sum = 0    
for n in rates2009:
    sum = sum + n
average9 = sum / len(rates2009)
average10 = 0
sum = 0    
for n in rates2010:
    sum = sum + n
average10 = sum / len(rates2010)
average11 = 0
sum = 0    
for n in rates2011:
    sum = sum + n
average11 = sum / len(rates2011)
average12 = 0
sum = 0    
for n in rates2012:
    sum = sum + n
average12 = sum / len(rates2012)
average13 = 0
sum = 0    
for n in rates2013:
    sum = sum + n
average13 = sum / len(rates2013)
average14 = 0
sum = 0    
for n in rates2014:
    sum = sum + n
average14 = sum / len(rates2014)

averageRates = [average,average1,average2,average3,average4,average5,average6,average7,average8,average9,average10,average11,average12,average13,average14]
years = [i for i in range(2000,2015)]




window_size = 30
window = np.ones(window_size)/float(window_size)

# output to static HTML file
output_file("unemployments.html", title="unemployments.py example")

# create a new plot with a a datetime axis type
p = figure(width=800, height=350)

p.circle(years, averageRates, size=5, color='green', alpha=0.9)
p.line(years, averageRates, color='green')

# setting attributes
p.title = "New York State Unemployment Rate(2000-2014)"
p.legend.location = "top_left"
p.grid.grid_line_alpha=1
p.xaxis.axis_label = 'years'
p.yaxis.axis_label = 'Unemployment Rate'
#p.ygrid.band_fill_color="blue"
#p.ygrid.band_fill_alpha = 0.8

# show the results
show(p)
