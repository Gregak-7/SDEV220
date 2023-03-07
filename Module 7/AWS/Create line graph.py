#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")
# create a new plot with a title and axis labels
p = figure(title="simple line example 2", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, line_width=2)

# show the results
show(p)


# In[7]:


from bokeh.io import show, output_notebook
from bokeh.models import CategoricalColorMapper, ColumnDataSource, FactorRange
from bokeh.plotting import figure, output_file
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

p = figure(x_range=fruits,  toolbar_location=None, title="Fruit Counts")
p.vbar(x=fruits, top=counts, width=0.9)
p.xgrid.grid_line_color = None
p.y_range.start = 0
output_notebook()
show(p)


# In[11]:


from bokeh.transform import factor_cmap

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']

data = {'fruits' : fruits,
          '2015'   : [2, 1, 4, 3, 2, 4],
          '2016'   : [5, 3, 3, 2, 4, 6],
          '2017'   : [3, 2, 4, 4, 5, 3]}

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (fruit, year) for fruit in fruits for year in years ]
counts = sum(zip(data['2015'], data['2016'], data['2017']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), toolbar_location=None, title="Fruit Counts by Year")
p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
         fill_color=factor_cmap('x', palette=["#c9d9d3", "#718dbf", "#e84d60"], factors=years, start=1, end=2))

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.major_label_orientation = 1
output_notebook()
show(p)


# In[ ]:




