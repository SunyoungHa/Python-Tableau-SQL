#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas
 
from bokeh.plotting import figure, output_file, show
 
df=pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx",sheet_name=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
 
i=figure(plot_width=500,plot_height=400,tools='pan')
 
i.title.text="Temperature and Air Pressure"
i.title.text_color="Gray"
i.title.text_font="arial"
i.title.text_font_style="bold"
i.xaxis.minor_tick_line_color=None
i.yaxis.minor_tick_line_color=None
i.xaxis.axis_label="Temperature (°C)"
i.yaxis.axis_label="Pressure (hPa)"    
 
i.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("Weather.html")
show(i)


# In[36]:



p = figure(plot_width=500, plot_height=400, tools = 'pan, reset')
p.title.text = "Earthquakes"
p.title.text_color = "Orange"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.yaxis.minor_tick_line_color = "Yellow"
p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"
p.circle([1,2,3,4,5], [5,6,5,5,3], size = [i*2 for i in [8,12,14,15,20]], color="red", alpha=0.5)
output_file("Scatter_plotting.html")
show(p)


# In[39]:


df=pandas.read_csv("adbe.csv", parse_dates=["Date"])

p = figure(plot_width=500, plot_height=500, x_axis_type="datetime")

p.line(df["Date"], df["Close"],color="Green", alpha=0.5)
output_file("Time_series.html")
show(p)

