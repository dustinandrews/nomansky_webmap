# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:55:58 2017

@author: dandrews
"""

"""
3d graphs
"""

import numpy as np
import plotly.graph_objs as go
import plotly

def get_scatter_trace(x,y,z,text,name,loc, color):
    trace = go.Scatter3d(
            name=name,
            hoverinfo='text',
            hovertext=[text],
            textposition='top center',
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker = dict(
                    size=4)
            )
    return trace


#np.random.seed(98019)
xdata = []
ydata = []
zdata = []
textdata = []
traces = []
color = 0

with open('coordinates.txt', 'r') as f:
    for line in f.readlines():
        name, loc = line.split(',')
        x,z,y,junk = loc.split(':')
        x = int(x,16)
        y = int(y,16)
        z = int(z,16)
        xdata.append(x)
        ydata.append(y)
        zdata.append(z)
        text = line.rstrip()
        textdata.append(text)
        trace = get_scatter_trace(x, y, z, text, name, loc, color)
        traces.append(trace)
        color+=1
        
colors = np.arange(len(zdata))
        
#%%

layout = dict(
    title='NMS Civilizations',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(250, 250, 250)',
            zerolinecolor='rgb(223, 230, 230)',
            range=[0,4095],
            showbackground=False,
            showaxeslabels=False,
            showticklabels=False 
        ),
        yaxis=dict(
            gridcolor='rgb(250, 250, 250)',
            zerolinecolor='rgb(223, 230, 230)',
            range=[0,4095],
            showbackground=False,
            showaxeslabels=False,
            showticklabels=False            
        ),
        zaxis=dict(
            gridcolor='rgb(250, 250, 250)',
            zerolinecolor='rgb(223, 230, 230)',
            range=[0,255],
            showbackground=False,
            showaxeslabels=False,
            showticklabels=False 
        ),
        aspectratio = dict( x=1, y=1, z=1 ),
        aspectmode = 'manual'        
    ),
    plot_bgcolor = 'black',
    paper_bgcolor = 'black',
)

data = traces
fig = dict(data=data,layout=layout)
plotly.offline.plot(fig, filename="nms-galaxy-map.html")
