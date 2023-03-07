#!/usr/bin/env python
# coding: utf-8

# # Summary of taxi trips taken in January 2017

# In[1]:


import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

output_file('taxidata.html')
df = pd.read_csv('/home/ec2-user/yellow_tripdata_2017-01.csv')
sample = df.sample (50)
source = ColumnDataSource(sample)
p=figure()
p.circle(x='passenger_count', y='total_amount', source=source, size=10, color='green')
p.title.text = 'Taxi rides'
p.xaxis.axis_label = "Passengers"
p.yaxis.axis_label = "Amount paid"
show(p)


# In[ ]:




